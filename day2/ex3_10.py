print('すべての質問にyまたはnで答えてください')
okane_aruka = input('お金に余裕はありますか?>>')
if okane_aruka =='y':
    onaka_suiteruka = input('お腹がすごくすいてますか?>>')
    nomitai_kibunka = input('ビールを飲みたいですか?>>')
    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('焼肉')
    elif onaka_suiteruka =='y':
        print('カレー')
    elif nomitai_kibunka =='y':
        print('焼き鳥')
    else:
        print('パスタ')
    yashoku_iruka = input('夜食は必要ですか?>>')
    if yashoku_iruka == 'y':
        print('コンビニのチキン')
else:
    print('家で食べましょう')
