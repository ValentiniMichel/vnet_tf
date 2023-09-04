import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

test_load = nib.load('./hippocampus_001.nii').get_fdata()
test_load.shape

print(test_load.shape)


#test = test_load[:,:,1]
# plt.imshow(test)
# plt.show()


for i in range(20):
    plt.subplot(5, 5,i + 1)
    plt.imshow(test_load[:,:,1 + i])
    plt.gcf().set_size_inches(10, 10)
plt.show()