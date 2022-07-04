scores={'newwork':60,'database':80,'security':50}
print(scores)
print(scores['database']) #80　のみ出る

scores['programing']=65
scores['security']=55
print(scores)

del scores['programing']
print(scores)

#scores['security']=55,60  #複数ももてる？？？
#print(scores)

total=sum(scores.values())  #上を消したらできた
print(total)

#total =sum(scores.security)
#print(total)

scores2=(70,80,55)
print(scores2)
print(scores2[0])
print(len(scores2))
print(sum(scores2))

members=('松田',)
print(type(members))

members2=tuple('松田')
print(type(members2))


