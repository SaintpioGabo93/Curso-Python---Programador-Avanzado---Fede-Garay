import torch

X = torch.tensor([[25,2],[5,26],[3,7]])
dimension = X.shape
seleccion_fila = X[1,:]

# Operaciones:
transposicion = X.T
mult = X*2
sum_mat = X+2
mult_sum = X*2+2
mult_sum_metodo = torch.add(torch.mul(X,2),2)
# Impresiones:

print(X)
print(dimension)
print(seleccion_fila)

# Impresiones de Operaciones:

print(transposicion)
print(mult)
print(sum_mat)
print(mult_sum)
print(mult_sum_metodo)