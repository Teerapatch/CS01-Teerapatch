import numpy as np
Lenght = []
Row = []
M = int(input("Enter Your Row For Matrix : "))
N = int(input("Enter Your Lenght For Matrix : "))
print("Enter Number For First Array")

for i in range(M * N) : 
    Lenght += [int(input(""))]

print("Enter Number For Second Arrey")
for l in range(M * N) :
    Row += [int(input(""))]

NRow = np.asarray(Row)
NLenght = np.asarray(Lenght)

Rowprint = NLenght.reshape(int(M),N)
print(Rowprint)
Lenghtprint = NRow.reshape(int(N),M)
print(Lenghtprint)

print(np.add(Rowprint, Lenghtprint))