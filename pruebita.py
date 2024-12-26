def calculadora():
    a = int(input('coloque el primer numero: '))
    b = int(input('coloque el segundo numero: '))
    decision = input('escoga la operacion que deszea realizar con los siguiente simbolos: +,-,*,/: ')
    if decision == '+':
        print(a+b)
    elif decision == '-':
        print(a-b)
    elif decision == '*':
        print(a*b)
    elif decision == '/':
        print(a/b)



calculadora()


