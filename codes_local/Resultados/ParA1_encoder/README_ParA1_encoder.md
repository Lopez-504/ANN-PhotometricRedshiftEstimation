# Registro del Experimento: ParA1_encoder

## Configuración Principal
- Neuronas:              [32, 16, 8, 4]
- Activaciones:          ['relu', 'tanh', 'tanh', 'relu']
- Dropouts:              [0.3, 0.2, 0.1, 0.05]                      
- Estandarizacion:       Standar
- Nombre del Modelo:     ParA1_encoder
- Loss:                  mse
- Semilla global:        42
- Data entrada:          cleanA_150k.csv
- Dimensión de Entrada:  (97488, 66)
- Split (train% - val%): (0.65-0.2)
- Epoch:                 450
- Bach_size:             164
- Optimizador:           adam 
- Learn_rate:            0.0017
- Features:              ['dered_u', 'dered_g', 'dered_r', 'dered_i', 'dered_z', 'psfMag_u', 'psfMag_g', 'psfMag_r', 'psfMag_i', 'psfMag_z', 'fiberMag_u', 'fiberMag_g', 'fiberMag_r', 'fiberMag_i', 'fiberMag_z', 'modelMag_u', 'modelMag_g', 'modelMag_r', 'modelMag_i', 'modelMag_z', 'expRad_g', 'expRad_i', 'expRad_r', 'expRad_z', 'deVRad_g', 'deVRad_i', 'deVRad_r', 'deVRad_z', 'expPhi_u', 'expPhi_g', 'expPhi_r', 'expPhi_i', 'expPhi_z', 'petroRad_r', 'z']
