name = input('あなたの名前を教えてください')
print('{}さん、こんにちは'.format(name))
food = input('{}さんの好きな食べものをおしえてください>>'.format(name))
#if 'カレー' not in food:  否定版  
if 'カレー' in food:
    print('素敵です。カレーは最高ですね')
else:
    print('私も{}が好きですよ'.format(food))
