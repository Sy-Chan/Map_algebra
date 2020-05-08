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

#create raster
raster = np.array([i for i in range(1,101)],dtype = float)
raster = raster.reshape([10,10])

#zone1
set1 = np.array([])
for i in range(0,5):
    for j in range(0,5):
        set1 = np.append(set1, raster[i][j])
mean1=round(np.mean(set1),1)

#zone2
x = 6
arr = []
for j in range(5,len(raster[i])):
    for i in range(0,x):
        arr.append(raster[i][j])
    x+=1
arr.sort()
set2=np.array(arr)
mean2=round(np.mean(set2),1)

#zone3
set3 = np.array([])
x = 6
for i in range(5,len(raster)):
    for j in range(0,x):
        set3 = np.append(set3,raster[i][j])
    x+=1
mean3=round(np.mean(set3),1)
    
reset=raster.copy()
for i in range(len(raster)):
    for j in range(len(raster[i])):
        if raster[i][j] in set1:
            reset[i][j] = mean1
        elif raster[i][j] in set2:
            reset[i][j] = mean2
        elif raster[i][j] in set3:
            reset[i][j] = mean3
        
            
plot(reset)
