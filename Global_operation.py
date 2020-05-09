import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plot(arr):

    fig, ax = plt.subplots(figsize=(10,10))
    im = ax.imshow(arr,cmap='Blues_r')

    # Rotate the tick labels and set their alignment.
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
    
source = np.zeros([10,10], dtype=int)
#point1
source[1][9] = 1
#point2
source[8][4] = 1

plot(source)


for i in range(len(source)):
    for j in range(len(source[i])):
        
        cy=i*10
        cx=j*10
        #distance of each cell from point1
        dist1=np.sqrt(((90-cx)**2+(10-cy)**2))
        #distance of each cell from point2
        dist2=np.sqrt(((40-cx)**2+(80-cy)**2))
        if dist1 < dist2:
            source[i][j] = dist1
        else:
            source[i][j] = dist2
plot(source)

