# def soma(a,b):
#     return a+b
# def subtração(a,b):
#     return a-b
# def multiplicacao(a,b):
#     return a*b
# def divisão(a,b):
#     if b == 0 :
#         print('zero não pode')
#     return a/b
# def cumprimento():
#     nome= input ('digite um nome')
#     idade= input ('digite uma idade')
#     print(f'O nome do usuario é {nome} a idade é {idade}')
# def calculadora():
#     n1= int(input('numero 1: '))
#     escolha= input(f'função: ')
#     n2=int(input('numero 2: '))
#     soma= n1+n2
#     subtração= n1-n2
#     multiplicação= n1*n2
#     divisão= n1/n2

    
#     if escolha == '+':
#         print(f'{n1} + {n2} = {soma}')
#     elif escolha == '-':
#         print(f'{n1} - {n2} = {subtração}')
#     elif escolha == '*'or escolha == 'x':
#         print (f'{n1} X {n2} = {multiplicação}')
#     elif escolha == '/':
#         print(f'{n1} / {n2} = {divisão}')
#     else:
#         print('ERROR')

# calculadora()

def atendimento():
    resposta= input('Olá, se o Sr(a) quiser comer digite 1, se quiser beber digite 2')
    if resposta== 1:
        print('O que desejas comer?')
    elif resposta == 2:
        print('O que queres beber?')

def comida():
    print('qual vai ser a boa de hoje?')
    pratos=input('1.salada, 2.churrasco, 3.massas, 4.sopa, 5.pizza ')
    if pratos == '1':
        print('Ja esta a caminho')
    elif pratos == '2':
        print('ta fresquinho, acabamos de matar')
    elif pratos == '3':
        print('Macarrão, nhoque ou outro?')
    elif pratos== '4':
        print('Quem vem num restaurante pra tomar sopa?')
    elif pratos== '5':
        print('Mamma Mia')


def bebida():
    print('Vai beber o que?')
    bebidas= input('1.Agua, 2.Refri, 3.Breja, 4.Vinho')
    if bebidas == '1':
        print('Boa escolha')
    elif bebidas == '2':
        a=input('Qual')
        if a == 'coca' or a== 'fanta' or a== 'sprite':
            print('É pra ja')
        else:
            print('Não temos esse')
    elif bebidas == '3':
        print('Credo!!')
    elif bebidas =='4':
        b=input('1.Tinto, 2.seco, 3.suave, 4.branco?')
        if b == '1' or b=='2' or b== '4':
            print('Ja traremos')
        elif b== '3':
            print('Acabou o estoque.')


atendimento_cliente = atendimento
escolha_comida= comida
escolha_bebida= bebida

if atendimento_cliente == '1':
    comida ()
elif atendimento_cliente== '2':
    bebida()
    
        