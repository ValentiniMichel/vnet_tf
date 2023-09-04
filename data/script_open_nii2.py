import gzip
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt



# # Specifica il percorso del tuo file NIfTI .gz
# nifti_gz_file_path = './Task05_Prostate/imagesTr/prostate_00.nii.gz'
# # Apri il file NIfTI .gz e leggilo usando nibabel
# with gzip.open(nifti_gz_file_path, 'rb') as f:
#     test_load = nib.load(f).get_fdata()

# Specifica il percorso del tuo file NIfTI .nii.gz
nifti_gz_file_path = './Task05_Prostate/labelsTr/prostate_00.nii.gz'

# Carica il file NIfTI .nii.gz
nifti_image = nib.load(nifti_gz_file_path)

# Ottieni i dati dall'immagine
test_load = nifti_image.get_fdata()

#test_load = nib.load('./hippocampus_001.nii').get_fdata()
test_load.shape

print(test_load.shape)


#test = test_load[:,:,1]
# plt.imshow(test)
# plt.show()


for i in range(10):
    plt.subplot(5, 5,i + 1)
    plt.imshow(test_load[:,:,1 + i])
    plt.gcf().set_size_inches(10, 10)
plt.show()


# # Itera attraverso le due immagini e visualizzale
# for i in range(1):
#     plt.subplot(1, 2, i + 1)
#     plt.imshow(test_load[:, :, 1, i], cmap='gray')  # Usa 'gray' per immagini in scala di grigi
#     plt.title(f'Immagine {i + 1}')
#     plt.axis('off')  # Rimuovi gli assi
#     plt.gcf().set_size_inches(10, 5)

# plt.show()