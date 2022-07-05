def hello():
    print('こんにちは')

hello()

def hello(name):
    print('こんにちは{}です'.format(name))

hello('松田')

def profile(name,age,hobby):   #intやstringといった指定もない
    print('私の名前は{}です'.format(name))
    print('年齢は{}です'.format(age))
    print('趣味は{}です'.format(hobby))

profile('名前',20,'読書')

def plus(x,y):
    answer = x + y
    return answer

answer=plus(100,50)
print(answer)

def plus_and_minus(a,b):
    return a+b , a-b

next,prev = plus_and_minus(1978,1)

print(next)
print(prev)

"""
def eat(breakfast,lunch,dinner='カレー'): #デフォルト引数の後ろに無しは定義できない
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))

eat('トースト','おにぎり')
eat('サンドウィッチ','そば','焼肉')

def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))


eat(breakfast='納豆',dinner='うどん')
eat('おにぎり',dinner='うどん')

def eat(breakfast,lunch='ラーメン',dinner='カレー',dessert=()):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('晩は{}を食べました'.format(dinner))
    for d in dessert:
        print('おやつに{}を食べました'.format(d))
        
#eat('トースト','昼','晩',('アイス','パフェ'))
eat('おにぎり','昼',('おやつ','おやつ2'))
"""

def eat(**kwargs):
    for key in kwargs:
        print('{}に{}を食べました'.format(key,kwargs[key]))

eat(朝食='納豆',遅めの昼食='パスタ',夕方のおやつ='カレーパン')



