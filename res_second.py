from math import sqrt

def listTostr(li):
    resp_str = str(li).strip('[]')
    resp_str = resp_str.replace('\'','')
    resp_str = resp_str.replace(',','')
    return resp_str

def resEq(eqs):
    eqs[0] = eqs[0].replace('Â','')
    print(listTostr(eqs))

    if eqs[0] == 'x²':
        eqs[0] = 1
    elif eqs[0] == '-x²':
        eqs[0] = -1
    else:
        eqs[0] = eqs[0].replace('x','')
        eqs[0] = eqs[0].replace('²','')

    eqs[1] = eqs[1].replace('x','') 

    a = int(eqs[0])
    b = int(eqs[1])
    c = int(eqs[2])

    delta = (b**2) - 4 * a * c

    if delta > 0:
        print('delta = ', delta)
        x1 = (-b + sqrt(delta)) /(2 * a)
        x2 = (-b - sqrt(delta)) /(2 * a)

        print('x1 = %d' %(x1))
        print('x2 = %d' %(x2))
    else:
        print("Raízes inexistentes")

    print('\n')

arq = str(input("Digite o nome do arquivo => "))
with open(arq,'r') as arquivo:
    for conteudo in arquivo:
        resEq(conteudo.replace('\n','').split(' '))
