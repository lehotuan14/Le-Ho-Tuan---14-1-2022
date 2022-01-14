a=input("tên đầy đủ:")
print(a)
n=int(input("n="))
str1=str(n);
str2=str1[::-1]
if(str1==str2):
    print(n ,"là số thuận nghịch")
else:
    print(n,"không là số thuận nghịch")
