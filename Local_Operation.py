import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plot(arr):

    fig, ax = plt.subplots(figsize=(10,10))
    im = ax.imshow(arr,cmap='Blues_r')

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    ax.axis('image')    

    # Loop over data dimensions and create text annotations.
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            text = ax.text(j,i , arr[i, j],
                           ha="center", va="center", color="r")

    ax.set_title('Raster')
    plt.show()

#create raster
raster = np.array([i for i in range(1,101)])
raster = raster.reshape([10,10])
longterm =raster * 3 * 106/100
plot(longterm)
