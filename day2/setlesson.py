#SETは種類を管理する（信号の色　とか）

scores={70,80,55,80}  #同じ値は無視される
scores.add(80)
print(scores)
print(len(scores))
print(sum(scores))

scores={'network':60,'database':80,'security':60}
members={'松田','浅木','工藤'}
print(tuple(members))
print(list(scores))
print(set(scores.values())) #80と60の2種類だけ表示になる

matsuda_scores={'network':60,'database':80,'security':50}
asagi_scores={'network':80,'database':75,'security':92}

member_scores={
        '松田':matsuda_scores,
        '浅木':asagi_scores,
        }

print(member_scores['松田']['network'])  #60

member_hobbies={
        '松田':{'sns','麻雀','自転車'},
        '浅木':{'麻雀','食べ歩き','数学','数学','数学'}
        }

print(member_hobbies)
print(member_hobbies['松田'])
print(member_hobbies['浅木'])

common_hobbies=member_hobbies['松田']&member_hobbies['浅木']
print(common_hobbies)
        

a=[1,2,3]
b=[4,5,6]
c=[a,b]

print(c)        #[1,2,3][4,5,6]
print(c[0])     #[1,2,3]
print(c[1][2])  #6

A={1,2,3,4}
B={2,3,4,5}
print(A|B)
print(A&B)
print(A-B)
print(A^B)


