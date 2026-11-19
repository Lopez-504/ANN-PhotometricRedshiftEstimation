# Registro del Experimento: ParB1_encoder

## Configuración Principal
- Neuronas:              [32, 16, 8, 4]
- Activaciones:          ['relu', 'relu', 'relu', 'relu']
- Activación salida:     linear
- Dropouts:              [0.35, 0.25, 0.2, 0.1]
- Estandarizacion:       MinMax
- Nombre del Modelo:     ParB1_encoder
- Loss:                  mse
- Metrics                mae
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 6)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 300
- Bach_size:             144
- Save_best_only         False
- Optimizador:           adam 
- Learn_rate:            0.0016
- Features:              ['dered_g', 'dered_r', 'psfMag_g', 'psfMag_r', 'expPhi_g', 'expPhi_r', 'z']
