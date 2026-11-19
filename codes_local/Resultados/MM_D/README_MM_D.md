# Registro del Experimento: MM_D

## Configuración Principal
- Neuronas:              [16, 8, 8, 8]
- Activaciones:          ['relu', 'tanh', 'relu', 'relu']
- Activación salida:     scaled_sigmoid
- Dropouts:              [0.3, 0.25, 0.25, 0.1]                      
- Estandarizacion:       MinMax
- Nombre del Modelo:     MM_D
- Loss:                  mae
- Metrics                ['mae']
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 38)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 400
- Bach_size:             512
- Save_best_only         False
- Optimizador:           adam 
- Learn_rate:            0.0011
- Features:              ['ra', 'dec', 'decErr', 'dered_u', 'dered_g', 'dered_r', 'dered_i', 'dered_z', 'psfMag_u', 'psfMag_g', 'psfMag_r', 'psfMag_i', 'psfMag_z', 'psfMagErr_u', 'psfMagErr_g', 'psfMagErr_r', 'psfMagErr_i', 'psfMagErr_z', 'fiberMag_u', 'fiberMag_g', 'fiberMag_r', 'fiberMag_i', 'fiberMag_z', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'modelMag_i', 'modelMag_z', 'expRad_g', 'expRad_i', 'expRad_r', 'expRad_z', 'expPhi_u', 'expPhi_g', 'expPhi_r', 'expPhi_i', 'expPhi_z', 'petroRad_r', 'z']
- PCA:                   False
