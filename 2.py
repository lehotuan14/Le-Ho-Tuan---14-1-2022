a=input("tên đệm của tôi là:")
print(a)
n= int(input("nhập số nguyên n:"))
x=n
tong=0
while (x>0):
    tong= tong+x%10
    x=int(x/10)
print("tổng các chữ số của", n ,"là:", tong)
