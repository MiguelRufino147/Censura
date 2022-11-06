#Processo para pegar o e-mail#

email=input('Insira o E-mail desejado').strip().split(" ")
if email =='':
    print('Nenhum email inserido')

#lista palavras#
palavras=input('Palavras Restritas').strip().split(" ") #Coloque todas palavras a serem restrita


for p in palavras:
    nmrpalavras=len(p)    #Usado para ver quantas letras possui a palavra restrita


#localizar palavras específicas#

def localizar(x):
        if x in palavras:
            emailsbs = x.replace(x, "*" * nmrpalavras)   #função para substituir palavras para *
            return emailsbs

        else:
            return x

def retornar(x):
    if x in palavras:                                #Retorna palavras censuradas sem o *
        return x
    else:
        return ''


#texto final

l=''
l2=''
for words in email:
    l+=localizar(words)+' '
    l2+=retornar(words)+ ' '
print('Texto substituido:')                                   #Pega as palavras e joga nas funções
print('-' * 30)
print(l)
print('-' * 30)
print(f'\033[1;30;41mPALAVRAS RESTRITAS ENCONTRADAS:\033[m')
print(l2)



