initial ='k'
if initial == 'k':
    print('ok')


point = 100
if 80<= point <256:
    print('ok')


bmi = 30
if bmi < 20 or bmi >25:
    print('ng')


year = 2024
if year % 4 ==0:
    print('ok')

day = 1
if day not in [28,30,31]:
    print('ok')



month=int(input('今何月ですか?'))

if month in [1,3,5,7,8,10,12]:
    print('31日まであります')
else:
    if month !=2:
        print('30日までですね')
    else:
        print('1年で一番寒い月ですね')
    print('年が明けてから')
print('{}箇所がすぎました'.format(montht))
