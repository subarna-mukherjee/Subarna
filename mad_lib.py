
#roses are (red), (violets) are blue,i love (you)
def mad_lib(color,object,celebrity):
    print('Roses are ',color)
    print(object,' are blue')
    print('I love ',celebrity)
    print('\nLets go again\n')
n=int(input('So how many times you want it to be? '))
count=0
while count!=n:
    c=input('Enter any color ')
    o=input('Enter any object(pural) ')
    c1=input('Enter the name of your favorite celebrity ')
    print()
    mad_lib(c,o,c1)
    count+=1