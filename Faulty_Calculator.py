# A program on the basis of 'If Else', 'Elif'.
# The program must return following faulty values:-
# 56+9=77; 45*3=555 and 56/6=4

a=int(input('Enter a number:'))
b=int(input('Enter another number:'))
print(
    '''
    Operations:
      --> +
      --> -
      --> *
      --> /
      '''
     )

c=input('Select your choice:')

if a==56  and b==9  and c=='+':
    print(77)
elif a==45  and b==3  and c=='*':
    print(555)
elif a==56  and b==6  and c=='/':
    print(4)
elif c=='+' and a!=56 and b!=9:
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*' and a!=45 and b!=3:
    print(a*b)
elif c=='/' and a!=56 and b!=6:
    print(a/b)
else:
    print('Invalid Choice.')





