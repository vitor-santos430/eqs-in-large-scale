def listTostr(li):
    resp_str = str(li).strip('[]')
    resp_str = resp_str.replace('\'','')
    resp_str = resp_str.replace(',','')
    return resp_str

def resolve(eqs,num_eqs):
    respostas = open('./resolvidas_pgrau.txt','a')
    num_eqs = str(num_eqs) + ')'
    respostas.write(num_eqs)
    respostas.write('\n')
    respostas.write(listTostr(eqs))
    respostas.write('\n')
    eqs[1] = int(eqs[1]) * -1
    if int(eqs[1]) > 0:
        eqs[1] = '+'+str(eqs[1])
    eqs = [eqs[0],eqs[2],eqs[3],eqs[1]]
    respostas.write(listTostr(eqs))
    respostas.write('\n')

    if list(eqs[0].replace('x','')) != []:
        if eqs[0].replace('x','') == '-':
            eqs[0] = '-1'
        eqs = [eqs[0],eqs[1],eqs[3],]
        respostas.write(listTostr(eqs))
        respostas.write('\n')
        eqs[0] = int(eqs[0].replace('x','')) * -1
        eqs = ['x',eqs[1],eqs[2],'/',eqs[0]]
        respostas.write(listTostr(eqs))
        respostas.write('\n')
        x_igual = int(eqs[2]) / int(eqs[4])
        x_igual *= -1
        respostas.write('x = {0:.3f}\n\n'.format(x_igual).replace('.',','))
    else:
        x_igual = int(eqs[2]) +0+ int(eqs[3])
        respostas.write('x = {0:.3f}\n\n'.format(x_igual).replace('.',','))
    respostas.close()

file = str(input("Digite o nome do arquivo => "))
cont = 1
with open(file,'r') as arquivo:
    for conteudo in arquivo:
        #print(conteudo.replace('\n','').split(' '))
        eqs = conteudo.replace('\n','').split(' ')
        resolve(eqs,cont)
        cont += 1