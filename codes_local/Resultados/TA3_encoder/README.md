# Registro del Experimento: TA3_encoder

## Configuración Principal
- Neuronas:              [64, 32, 16, 8]
- Activaciones:          ['relu', 'tanh', 'relu', 'relu']
- Dropouts:              [0.3, 0.2, 0.1, 0.05] 
- Estandarizacion:       Robust
- Nombre del Modelo:     TA3_encoder
- Loss:                  mse
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 66)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 350
- Bach_size:             144
- Optimizador:           adam 
- Learn_rate:            0.0015
