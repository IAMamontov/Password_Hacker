s = input()
n = int(input())
slide = (n).to_bytes(2, byteorder="little")[0] + (n).to_bytes(2, byteorder="little")[1]
for i in s:
    print(chr(ord(i) + slide), end="")