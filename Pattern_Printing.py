''' If n = 4

    For True:   *
                **
                ***
                ****

    For False:  ****
                ***
                **
                *
'''

n = int(input('Enter the number of rows: '))
boolean_value = bool(int(input('Enter 0 for \'False\' and another integer for \'True\': ')))

if boolean_value == True:
    for i in range(1,n+1):
        print('*'*i)

else:
    for i in range(n,0,-1):
        print('*'*i)
