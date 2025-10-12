# Registro del Experimento: Ro2_enc_65REP

## Configuración Principal
- Neuronas:              [64, 32, 16, 8]
- Activaciones:          ['relu', 'tanh', 'tanh', 'softmax']
- Activación salida:     linear
- Dropouts:              [0.3, 0.2, 0.1, 0.05]                      
- Estandarizacion:       Robust
- Nombre del Modelo:     Ro2_enc_65REP
- Loss:                  mse
- Metrics                ['mae']
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 65)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 450
- Bach_size:             512
- Save_best_only         False
- Optimizador:           rmsprop 
- Learn_rate:            0.003
- Features:              ['dec', 'decErr', 'dered_g', 'dered_i', 'dered_r', 'dered_u', 'dered_z', 'deVRad_g', 'deVRad_i', 'deVRad_r', 'deVRad_z', 'deVRadErr_g', 'deVRadErr_i', 'deVRadErr_r', 'deVRadErr_z', 'expPhi_g', 'expPhi_i', 'expPhi_r', 'expPhi_u', 'expPhi_z', 'expRad_g', 'expRad_i', 'expRad_r', 'expRad_z', 'expRadErr_g', 'expRadErr_i', 'expRadErr_r', 'expRadErr_z', 'extinction_g', 'extinction_i', 'extinction_r', 'extinction_u', 'extinction_z', 'fiberMag_g', 'fiberMag_i', 'fiberMag_r', 'fiberMag_u', 'fiberMag_z', 'fiberMagErr_g', 'fiberMagErr_i', 'fiberMagErr_r', 'fiberMagErr_u', 'fiberMagErr_z', 'modelMag_g', 'modelMag_i', 'modelMag_r', 'modelMag_u', 'modelMag_z', 'modelMagErr_g', 'modelMagErr_i', 'modelMagErr_r', 'modelMagErr_u', 'modelMagErr_z', 'petroRad_r', 'psfMag_g', 'psfMag_i', 'psfMag_r', 'psfMag_u', 'psfMag_z', 'psfMagErr_g', 'psfMagErr_i', 'psfMagErr_r', 'psfMagErr_u', 'psfMagErr_z', 'ra']
- PCA:                   False
