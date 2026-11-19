# Registro del Experimento: St_A2

## Configuración Principal
- Neuronas:              [50, 36, 24, 16]
- Activaciones:          ['relu', 'tanh', 'tanh', 'relu']
- Activación salida:     scaled_sigmoid
- Dropouts:              [0.2, 0.15, 0.15, 0.05]                      
- Estandarizacion:       Standar
- Nombre del Modelo:     St_A2
- Loss:                  mse
- Metrics                ['mae']
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (112486, 28)
- Split (train% - val%): (0.75-0.1)
- Epoch:                 400
- Bach_size:             200
- Save_best_only         True
- Optimizador:           adam 
- Learn_rate:            0.002
- Features:              ['ra', 'dec', 'decErr', 'dered_u', 'dered_g', 'dered_r', 'dered_i', 'dered_z', 'psfMag_u', 'psfMag_g', 'psfMag_r', 'psfMag_i', 'psfMag_z', 'fiberMag_u', 'fiberMag_g', 'fiberMag_r', 'fiberMag_i', 'fiberMag_z', 'psfMagErr_u', 'psfMagErr_g', 'psfMagErr_r', 'psfMagErr_i', 'psfMagErr_z', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'modelMag_i', 'modelMag_z', 'z']
- PCA:                   False
