import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plot(arr):

    fig, ax = plt.subplots(figsize=(10,10))
    im = ax.imshow(arr,cmap='Blues_r')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")
    ax.axis('scaled')

    # Loop over data dimensions and create text annotations.
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            text = ax.text(j,i , arr[i, j],
                           ha="center", va="center", color="r")

    ax.set_title('Raster')
    plt.show()

    
##create raster array
raster2 = np.array([
    [29.0, 79.0, 41.0, 88.0, 94.0,  6.0, 53.0, 89.0, 56.0, 46.0],
    [96.0, 46.0, 68.0, 58.0, 11.0, 90.0, 25.0,  5.0, 33.0, 95.0],
    [89.0, 70.0, 64.0, 99.0, 66.0, 71.0, 55.0, 60.0, 30.0, 16.0],
    [96.0, 90.0, 69.0, 80.0,  3.0, 48.0, 76.0, 22.0, 32.0, 24.0],
    [15.0, 42.0, 42.0, 38.0, 16.0, 15.0, 24.0, 47.0, 27.0, 86.0],
    [ 6.0, 45.0, 80.0, 13.0, 57.0, 21.0, 14.0, 76.0, 90.0, 38.0],
    [67.0, 10.0, 39.0, 28.0, 82.0, 45.0, 81.0, 81.0, 80.0, 45.0],
    [76.0, 63.0, 71.0,  1.0, 48.0, 23.0, 39.0, 62.0, 36.0, 12.0],
    [25.0, 67.0, 42.0, 79.0, 11.0, 44.0, 99.0, 89.0, 89.0, 18.0],
    [14.0, 66.0, 35.0, 66.0, 33.0, 20.0, 78.0, 10.0, 47.0, 52.0]])
arr=[]
for i in range(1,len(raster2)-1):
    row = []
    for j in range(1, len(raster2[i])-1):
        A = raster2[i][j]#center data
        B = raster2[i][j + 1]
        C = raster2[i + 1][j + 1]
        D = raster2[i + 1][j]
        E = raster2[i + 1][j - 1]
        F = raster2[i][j - 1]
        G = raster2[i - 1][j - 1]
        H = raster2[i - 1][j]
        I = raster2[i - 1][j + 1]
        newA = np.mean([A,B,C,D,E,F,G,H,I])
        row.append(round(newA,1))
    arr.append(row)
    
array = np.array(arr)
plot(raster2)
plot(array)
