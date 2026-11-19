# Registro del Experimento: St_A1

## Configuración Principal
- Neuronas:              [64, 32, 32, 32]
- Activaciones:          ['relu', 'tanh', 'tanh', 'relu']
- Activación salida:     scaled_sigmoid
- Dropouts:              [0.2, 0.1, 0.1, 0.05]                      
- Estandarizacion:       Standar
- Nombre del Modelo:     St_A1
- Loss:                  mse
- Metrics                ['mae']
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 28)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 400
- Bach_size:             164
- Save_best_only         True
- Optimizador:           adam 
- Learn_rate:            0.0028
- Features:              ['ra', 'dec', 'decErr', 'dered_u', 'dered_g', 'dered_r', 'dered_i', 'dered_z', 'psfMag_u', 'psfMag_g', 'psfMag_r', 'psfMag_i', 'psfMag_z', 'fiberMag_u', 'fiberMag_g', 'fiberMag_r', 'fiberMag_i', 'fiberMag_z', 'psfMagErr_u', 'psfMagErr_g', 'psfMagErr_r', 'psfMagErr_i', 'psfMagErr_z', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'modelMag_i', 'modelMag_z', 'z']
- PCA:                   False
