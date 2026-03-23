# BinaryTest/test02.py

a = 0b1100
b = 0b1010

# a 와 b 비트 AND 연산( 자리수 별로 모두가 1일때 결과가 1이 된다)
print( a & b)
print(bin(a&b))

info = 0b1111_1111_1111_0000
print(info)
data1 = 0b11100_0011_1010_1001
data2 = 0b11100_0011_1010_0010
data3 = 0b11100_0011_1010_1011
data4 = 0b11100_0011_1010_1100

print(bin(info&data1))
print(bin(info&data2))
print(bin(info&data3))
print(bin(info&data4))