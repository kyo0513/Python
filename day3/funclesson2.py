name='松田'


def hello():
    global name  #=山田のように1行で書けない
    name='山田'
    print('こんにちは' + name +'さん')
    #name=''   グローバル変数を中で定義してるとエラーになる

hello()       #山田
print(name)   #松田 global指定すると山田へ
