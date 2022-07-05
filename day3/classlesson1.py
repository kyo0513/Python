class Hero:
    name='松田'
    hp = 100
    def sleep(self,hours):
        print('{}は{}時間寝た'.format(self.name,hours))
        self.hp += hours

print('題材')
h = Hero()
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name,h.hp))

scores1=[80,40,50]
scores2=[80,40,50]

print('scores1のidentity:{}'.format(id(scores1)))
print('scores2のidentity:{}'.format(id(scores2)))


if scores1 == scores2:
    print('同じ内容')
else:
    print('違う内容')

if id(scores1) == id(scores2):
    print('同じ存在')
else:
    print('違う存在')

names=list()
print('前:{}'.format(id(names)))
names.append('松田')
print('前:{}'.format(id(names)))

name=name+'さん'
print('後:{}'.format(id(names)))


























