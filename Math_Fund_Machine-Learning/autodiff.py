import torch

x = torch.tensor(5.0)
print(x)
x.requires_grad_()
print(x)
y = x**2
print(y)
y.backward()
print(y)
grad = x.grad
print(grad)