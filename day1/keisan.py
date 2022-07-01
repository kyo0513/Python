a=10
b=3

answer=a+b
print(a,'+',b,'=',answer)

answer=a-b
print(a,'-',b,'=',answer)

answer=a*b
print(a,'*',b,'=',answer)

answer=a/b
print(a,'/',b,'=',answer)

answer=a//b
print(a,'//',b,'=',answer)

answer=a%b
print(a,'%',b,'=',answer)

str='hello' *3
print(str)

x=10
if x>0:
    print('正の値です')
else:
    print('正の値ではありません')


"""
コメント化 if文はインデント必須
"""
# 1行コメントは#を使う

score=64
if score>80:
    print('優')
elif score>60:
    print('良')
elif score>40:
    print('可')
else:
    print('不可')


n=0
while n<10:
    print(n)
    n=n+1
print('終了')

for i in range(5):  #0,1,2,3,4
    print(i)

#range(3,5) = 3,4
#range(1,10,3) = 1,4,7

for i in range(1,11):
    print(i,end=' ')
print()

print()

for i in range(1,4):
    for j in range(1,11):
        print(i*j,end=' ')
    print()

"""
height=int(input('何段の階段を作る?>'))
for i in range(height):
    for j in range(i+1):
        print('*',end='')
    print()
"""

name ='A'
age  =24
height=170.5
print('私の名前は{}で年齢は{}歳で身長は{}cmです'
        .format(name,age,height))
print(f'私の名前は{name}で、年齢は{age}歳で、身長は{height}cmです')

"""
a='a'
x=10
y=(type(a)(x))*3
print(y)
"""

z='ac'
print(type(z) is str)
print(type('Abc') is int)

x=10
print(isinstance(x,int))
