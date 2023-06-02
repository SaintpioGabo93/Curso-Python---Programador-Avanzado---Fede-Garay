import torch

X = torch.tensor([[0,1,2],[3,4,5],[6,7,8]])
Y = torch.tensor([-1,1,-2])# Para este vector no se necesita transponer
Z = torch.tensor([[-1,1,-2],[0,1,2]]).T #Para esta matríz si se necestia transponer
matriz_ejemplo =torch.tensor([[4,2.],[-5,-3.]])
mult_mat_reg = torch.matmul(X,Y)
mult_mat_reg_2 = torch.matmul(X,Z)
inverso = torch.inverse(matriz_ejemplo)
comprobacion = torch.matmul(matriz_ejemplo,inverso)
resultados = torch.tensor([4,-7.])
solucion = torch.matmul(resultados,inverso)
print(mult_mat_reg)
print(mult_mat_reg_2)
print(matriz_ejemplo)
print(inverso)
print(comprobacion)
print(solucion)