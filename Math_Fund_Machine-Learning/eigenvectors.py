import torch
import  matplotlib.pyplot as plt
v = torch.tensor([[3,1]])
E = torch.tensor([[2,0],[0,-1]])

def graf_vectores(vectores, colores):
    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')
    for i in range(len(vectores)):
        x= torch.concat([torch.tensor([0,0]),vectores[i]])
        plt.quiver([x[0]],[x[1]],[x[2]],[x[3]], angles ='xy',scale_units='xy',scale=1, color=colores[i])

graf_vectores(v,'b')
plt.xlim(-1,20)
_=plt.ylim(-1,20)
plt.show()