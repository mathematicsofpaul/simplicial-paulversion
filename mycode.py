import torch 

tsr = torch.Tensor(3,5)

print(tsr)

#requires_grad is contaginous
a = torch.randn((3,3), requires_grad = True)

w1 = torch.randn((3,3), requires_grad = True)
w2 = torch.randn((3,3), requires_grad = True)
w3 = torch.randn((3,3), requires_grad = True)
w4 = torch.randn((3,3), requires_grad = True)

b = w1*a 
c = w2*a

d = w3*b + w4*c 

L = 10 - d

print("The grad fn for a is", a.grad_fn)
print("The grad for d is", d.grad)