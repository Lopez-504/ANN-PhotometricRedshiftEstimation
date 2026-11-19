# Registro del Experimento: MSt1_encoder

## Configuración Principal
- Neuronas:              [16, 8, 4, 2]
- Activaciones:          ['relu', 'tanh', 'tanh', 'tanh']
- Dropouts:              [0.3, 0.2, 0.1, 0.05]                      
- Estandarizacion:       Standar
- Nombre del Modelo:     MSt1_encoder
- Loss:                  mse
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 66)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 500
- Bach_size:             300
- Optimizador:           adam 
- Learn_rate:            0.001
