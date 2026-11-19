# Registro del Experimento: PCA10_A

## Configuración Principal
- Neuronas:              [64, 32, 16, 8]
- Activaciones:          ['relu', 'relu', 'relu', 'softmax']
- Activación salida:     scaled_sigmoid
- Dropouts:              [0.3, 0.2, 0.1, 0.05]                      
- Estandarizacion:       Standar
- Nombre del Modelo:     PCA10_A
- Loss:                  mae
- Metrics                ['mae']
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 10)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 450
- Bach_size:             512
- Save_best_only         False
- Optimizador:           adam 
- Learn_rate:            0.001
- Features:              10
- PCA:                   True
