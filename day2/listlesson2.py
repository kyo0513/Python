import pprint

"""
data=[1,2,3],[4,5,6]
print(data[1][2])   #6

data2=[
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
#print(data2)

data2=list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
        data2.append(temp)
print(data2)

pprint.pprint(data2)

data3=[1,2,3]+[4,5]
data4=[1,2,3]*3
print(data4)

data=[None]*10
for i in range(10):
    data[i]=[0]*10
pprint.pprint(data)


data=[[0]*10]*10    #これは0が10個の列を１０コピーしているが
                    #メモリの参照先も同じになってしまう
pprint.pprint(data)

#内包表記
data=[[0]*10 for i in range(10)]
pprint.pprint(data)
"""

data=[[i]*10 for i in range(10)]
pprint.pprint(data)

data=[ i for i in range(1,11)]
print(data)




