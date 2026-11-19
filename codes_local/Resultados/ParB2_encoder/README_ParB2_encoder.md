# Registro del Experimento: ParB2_encoder

## Configuración Principal
- Neuronas:              [96, 64, 32, 16]
- Activaciones:          ['relu', 'relu', 'relu', 'relu']
- Activación salida:     scaled_sigmoid
- Dropouts:              [0.35, 0.25, 0.2, 0.1]
- Estandarizacion:       Robust
- Nombre del Modelo:     ParB2_encoder
- Loss:                  mse
- Metrics                ['mae']
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 21)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 300
- Bach_size:             256
- Save_best_only         False
- Optimizador:           adam 
- Learn_rate:            0.0014
- Features:              ['decErr', 'dered_u', 'dered_g', 'dered_r', 'dered_i', 'dered_z', 'psfMag_u', 'psfMag_g', 'psfMag_r', 'psfMag_i', 'psfMag_z', 'fiberMag_u', 'fiberMag_g', 'fiberMag_r', 'fiberMag_i', 'fiberMag_z', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'modelMag_i', 'modelMag_z', 'z']
