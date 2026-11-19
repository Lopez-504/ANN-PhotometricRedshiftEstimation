import os
import sys
import pandas as pd
import numpy as np
import tensorflow as tf
#import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam, Adagrad, RMSprop

from data_utils import gen_rand_split              # script local

################################################################

# --- 1. LOAD DATA ---
path_to_data = 'cleanA_150k.csv'
df_raw = pd.read_csv(path_to_data)

# --- 2. SEED SETTING FOR REPRODUCIBILITY ---
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

print(f"Data loaded from {path_to_data}\nSeed set to {SEED}")

########################################################################

# train/val/test split
val_p, test_p = 0.2, 0.15  
X_train, X_val, X_test, y_train, y_val, y_test = gen_rand_split(df_raw, val_p, test_p, SEED=42)

# Ajustar en X_train, luego trainformar los demás
scaler_name = 'Robust'

if scaler_name=='Standar':
    scaler = StandardScaler()
elif scaler_name=='MinMax':
    scaler = MinMaxScaler() 
elif scaler_name=='Robust':
    scaler=RobustScaler()

# Aplicar scaler
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

print(f"Data split: Train ({len(X_train)}), Validation ({len(X_val)}), Test ({len(X_test)}) samples.")
print(f"Data standardized using {scaler_name}Scaler")

#####################################################################

def build_fnn_model(input_shape, units_hl, rates_dl, activation, output_activation='linear',
                                 optimizer_name='adam', learning_rate=1e-3, loss_function='mse'):
    """
    Builds a Fully Connected FF NN with explicit Dropout layers.
    input_shape: shape of the input data (tuple)
    units_hl: list with neurons for each hidden layer (list)
    rates_dl: list with droput rate for dropout layers (list)
    activation: list with activation functions for each hidden layer (list)
    output_activation: activation function for the output layer    
    """
    model = Sequential()
    
    # Input Layer (Input shape defined here)
    model.add(Input(shape=(input_shape,)))
    
    # Loop through the hidden layers
    for i in range(len(units_hl)):
    # 1. Add the Dense (Hidden) Layer
        model.add(Dense(units=units_hl[i], 
                        activation=activation[i], 
                        name=f'Hidden_{i+1}'))
    
    # 2. Conditionally Add the Dropout Layer
    # Only add the layer if the rate is > 0
    if rates_dl[i] > 0.0:
        model.add(Dropout(rate=rates_dl[i], 
                          name=f'Dropout_{i+1}'))

    # Output Layer (1 unit for scalar target/regression)
    model.add(Dense(1, activation=output_activation, name='Output_Layer'))

    # Define optimizer
    if optimizer_name=='adam':
        optimizer = Adam(learning_rate=learning_rate)
    elif optimizer_name=='adagrad':
        optimizer = Adagrad(learning_rate=learning_rate)
    elif optimizer_name=='rmsprop':
        optimizer = RMSprop(learning_rate=learning_rate)            

    # Compile the model
    model.compile(optimizer=optimizer, loss=loss_function, metrics=['mae'])
    return model

########################################################################


# Hiperparameters
HP_INPUT_SHAPE = X_train_scaled.shape[1]
HP_UNITS_HL = [144, 64, 32, 8]                      # Units for each layer
HP_RATES_DL = [0.2, 0.15, 0.1, 0.05]                       # Dropout Rates
HP_ACTIVATION = ['relu', 'tanh', 'tanh', 'relu']            # Activation functions
HP_ACTIVATION_OUTPUT = 'linear'
HP_LOSS = 'mse'                                 # Loss function
HP_OPTIMIZER = 'adam'                           # Optimizer
HP_LR = 1.2e-3                                    # Learning rate
HP_EPOCHS = 450                                 # Epochs
HP_BATCH_SIZE = 96                               # Batch size

# Build the model
model = build_fnn_model(
    input_shape=HP_INPUT_SHAPE,
    units_hl=HP_UNITS_HL,
    rates_dl=HP_RATES_DL,
    activation=HP_ACTIVATION,
    output_activation=HP_ACTIVATION_OUTPUT,
    optimizer_name=HP_OPTIMIZER,
    learning_rate=HP_LR,
    loss_function=HP_LOSS
)

# Change name and print summary, it's saved later folder
#model.name = 'TA4_encoder_test'            # Conflicto entre tensorflow y keras
model_name = sys.argv[1]
model.summary()


###############################################################


print("\nStarting model training...")

# Definir checkpoint para guardar el mejor modelo (i.e., el que presente mejor métrica [metrics])
cp = ModelCheckpoint(model_name+'.keras', save_best_only=True)

history = model.fit(
    X_train_scaled, y_train,
    epochs=HP_EPOCHS,
    batch_size=HP_BATCH_SIZE,
    validation_data=(X_val_scaled, y_val),
    verbose=0,
    callbacks=[cp]
)

print("Training finished.")


###################################################################


# Evaluar validación usando las mismas métricas del modelo
loss_val_final, mae_val_final = model.evaluate(X_val_scaled, y_val, verbose=0)
y_pred = model.predict(X_val_scaled)
R2_val = r2_score(y_val, y_pred)

# Guardar función de pérdida en entrenamiento y validación
train_losses = history.history['loss'] 
val_losses = history.history['val_loss']

print(f"Val Loss (MSE): {loss_val_final:.4f}\nVal MAE: {mae_val_final:.4f}\nVal R2: {R2_val:.4f}")


######################################################################


# Solicitar el nombre del directorio de salida
# model_name = model.name               # Conflicto entre tensorflow y keras
#folder_name = input("Output folder name: ")             # Double check
folder_name = model_name

# Definir la ruta base: Resultados/NOMBRE_DEL_MODELO
BASE_PATH = os.path.join('Resultados', folder_name)
os.makedirs(BASE_PATH, exist_ok=False)      # para evitar sobreescribir 

print(f"\nGuardando resultados críticos en: '{BASE_PATH}'")

# 1. Archivo de Descripción (README)
readme_content = f"""# Registro del Experimento: {model_name}

## Configuración Principal
- Neuronas:              {HP_UNITS_HL}
- Activaciones:          {HP_ACTIVATION}
- Dropouts:              {HP_RATES_DL}                      
- Estandarizacion:       {scaler_name}
- Nombre del Modelo:     {model_name}
- Loss:                  {HP_LOSS}
- Semilla global:        {SEED}
- Data entrada:          {path_to_data}
- Dimensión de Entrada:  {X_train_scaled.shape}
- Split (train% - val%): ({1-val_p-test_p}-{val_p})
- Epoch:                 {HP_EPOCHS}
- Bach_size:             {HP_BATCH_SIZE}
- Optimizador:           {HP_OPTIMIZER} 
- Learn_rate:            {HP_LR}
"""

# Guardar README en la carpeta del modelo
with open(os.path.join(BASE_PATH, 'README.md'), 'w') as f:
    f.write(readme_content)
print("- README.md (Descripción) guardado.")

# Guardar summary 
def write_summary_to_file(s):
    with open(os.path.join(BASE_PATH, 'model_summary.txt'), 'a') as f:  
        f.write(s + '\n')

model.summary(print_fn=write_summary_to_file)        

# Resultados (Métricas) sobre el grupo de validación
results_data = {
    'Metric': ['RMSE', 'MSE', 'MAE', 'R2'],
    'Value': [np.sqrt(loss_val_final), loss_val_final, mae_val_final, R2_val]          
}
results_df = pd.DataFrame(results_data)

# Guardar CSV de métricas en la carpeta del modelo
results_df.to_csv(os.path.join(BASE_PATH, 'metrics.csv'), index=False)
print("Métricas guardadas en metrics.csv")

# Momentos sobre grupo de validación
y_pred = pd.Series(y_pred.flatten())        # Para poder aplicar momentos
moments_val = [y_val.mean(),y_val.var(),y_val.skew(),y_val.kurt()]
moments_pred = [y_pred.mean(),y_pred.var(),y_pred.skew(),y_pred.kurt()]

## Crer dataframe con los momentos
moments_df = pd.DataFrame([moments_val, moments_pred], 
                          columns=['Mean', 'Variance', 'Skewness', 'Kurtosis'], 
                          index=['TrueVal z', 'PredVal z'])

moments_df.to_csv(os.path.join(BASE_PATH, 'moments.csv'), index=False)
print("Momentos de PredVal y TrueVal guardados en moments.csv")

##### GRÁFICAS ####
fs = 13                       # fontsize

#####
## Gráfica de Entrenamiento (Train/Val Loss)
plt.figure(figsize=(10, 6))
plt.plot(train_losses, label='Train Loss')
plt.plot(val_losses, label='Validation Loss')
plt.title('Pérdida de Entrenamiento y Validación por Época', fontsize=fs)
plt.xlabel('Época', fontsize=fs)
plt.ylabel(f'Pérdida {HP_LOSS}', fontsize=fs)
plt.legend()
plt.grid(linestyle='--')
plt.savefig(os.path.join(BASE_PATH, 'train_val_loss.png'), dpi=300)
plt.close()
print("Gráfica de Pérdida guardada en train_val_loss.png")


#####
## Gráfica de dispersión True vs Pred sobre el grupo de validación
fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(y_val, y_pred, alpha=.2)         
ax.plot([0,7], [0, 7],linestyle='--', color='k')
ax.set_xlabel('TrueVal z', fontsize=fs)
ax.set_ylabel('PredVal z', fontsize=fs)
ax.set_title(model_name, fontsize=fs)

ax.text(1.9, 6.5, f'MSE_test= {round(loss_val_final,4)}\nMAE_test= {round(mae_val_final,4)}\nR2_test=  {round(R2_val,4)}',
        horizontalalignment='center',
        verticalalignment='center',
        bbox=dict(facecolor='yellow', alpha=0.5, boxstyle='round,pad=0.5'))

plt.grid(linestyle='--')
plt.savefig(os.path.join(BASE_PATH, 'ValScatter.png'), dpi=300)
plt.close()
print("Gráfica TrueVal vs PredVal guardada en ValScatter.png")


#####
## Gráfica de Distribución de Residuos (Histograma/KDE)
residuals = y_pred-y_val

plt.figure(figsize=(8, 5))
#sns.kdeplot(residuals, color='purple',fill=True, alpha=0.5)
plt.hist()
plt.title('KDE residuos sobre ValidationSet', fontsize=fs)
plt.xlabel('Residuos (pred-true)', fontsize=fs)
plt.ylabel('KDE', fontsize=fs)
plt.axvline(x=0, color='k', linestyle='--')
plt.grid(linestyle='--')
plt.savefig(os.path.join(BASE_PATH, 'KDE_residuos.png'), dpi=300)
plt.close()
print("Gráfica KDE de residuos guardada en KDE_residuos.png")

print("\nProceso finalizado.")
     
# Quizás agregar algún violin or box plot

