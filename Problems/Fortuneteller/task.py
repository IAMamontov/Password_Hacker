# put your code here
s = input()
digits = (int(i) for i in s)
z = 0
for n in digits:
    z += n
print(z)