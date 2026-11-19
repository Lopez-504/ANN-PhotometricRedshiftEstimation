# Registro del Experimento: MM_B

## Configuración Principal
- Neuronas:              [96, 96, 96, 64]
- Activaciones:          ['relu', 'tanh', 'tanh', 'relu']
- Activación salida:     scaled_sigmoid
- Dropouts:              [0.3, 0.25, 0.2, 0.05]                      
- Estandarizacion:       MinMax
- Nombre del Modelo:     MM_B
- Loss:                  mse
- Metrics                ['mae']
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 38)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 800
- Bach_size:             512
- Save_best_only         False
- Optimizador:           adam 
- Learn_rate:            0.0015
- Features:              ['ra', 'dec', 'decErr', 'dered_u', 'dered_g', 'dered_r', 'dered_i', 'dered_z', 'psfMag_u', 'psfMag_g', 'psfMag_r', 'psfMag_i', 'psfMag_z', 'psfMagErr_u', 'psfMagErr_g', 'psfMagErr_r', 'psfMagErr_i', 'psfMagErr_z', 'fiberMag_u', 'fiberMag_g', 'fiberMag_r', 'fiberMag_i', 'fiberMag_z', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'modelMag_i', 'modelMag_z', 'expRad_g', 'expRad_i', 'expRad_r', 'expRad_z', 'expPhi_u', 'expPhi_g', 'expPhi_r', 'expPhi_i', 'expPhi_z', 'petroRad_r', 'z']
- PCA:                   False
