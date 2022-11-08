
def principal():                    #FUNÇÃO PRINCIPAL
    submit=0
    frase = input('Seu email').strip().lower()
    proibidas = []


    while submit == 0:
        if frase == '':
            inputEmail = input('Digite um email: ')                 #CRIANDO LOOP
            frase = inputEmail

        print('')
        print('Digite "comandos" para mostrar os comandos disponiveis.')
        print('')

        command = input('=> ')

        if command == 'comandos':
            print('')
            print('add - Adiciona uma nova palavra para censurar.')
            print('submit - Executa a censura das palavras selecionadas.')
            print('')

        if command == 'add':
            word = input('|_ Digite uma nova palavra/frase: ')
            proibidas.append(word)                                                  #LISTA IF'S DE OPÇÕES PARA SELECIONAR
            for word in proibidas:
                frase = frase.replace(word, "*" * len(word))
                print('-' * 30)
                print(proibidas)

        if command == 'submit':
            for word in proibidas:
                frase = frase.replace(word, "*" * len(word))
            print('TEXTO ORIGINAL:')
            print(frase)
            print(' ')
            print('\033[1;30;41mPALAVRAS PROIBIDAS:\033[m')

            print(proibidas)

#chamando função
principal()                    #CHAMANDO FUNÇÃO














