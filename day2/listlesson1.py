members=['工藤','松田','浅木']
print(members)

scores=[89,90,95]

total=sum(scores)
print(f'合計{total}') 

#sumを定義した場合上書きされてしまう

print(len(scores))
avg=sum(scores)/len(scores)
print(avg)

members.append('菅原')
members.append('湊')
members.append('朝香')
print(members)

del members[2]
print(members)


a=[10,20,30,40,50]
b=a[1:3]
print(b)
c=a[2:]
d=a[:3]
print(c)
print(d)

e=a[:]  #配列のコピー メモリも新しく作られるので完全新規

print(a[-1]) #50　一番後ろの要素がでる

f=a[0:100] #スライスの場合は範囲外という概念はない
print(f)

g=a[::-1] #配列逆順コピー
print(g)




