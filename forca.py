def forca():
    exit = False
    while not exit:

        print('Seja bem-vindo ao jogo da forca')
        print('1. Iniciar')
        print('2. Sair')
        choice = int(input('Escolha uma das opções: '))

        word = 'etrom'
        lifes = [1, 2, 3, 4, 5, 6]

        # Função de contar quantas vidas restam

        def lifes_left():
            del lifes[-1]
            if len(lifes) > 0:
                print(f'Você possui {lifes[-1]} tentativas restantes')
        
        ##### Função quando o jogador perde

        def lose():
            choice_lose = int(input('Se deseja tentar novamente digite 1, se deseja voltar para o menu principal digite 2: '))
            if choice_lose == 1:
                forca()
            elif choice_lose == 2:
                exit = True
            else: 
                print('Opção inexistente, tente novamente')
                lose()

        # Função de adivinhar as letras das palavras
        def attempt():
            attempt_value = input('Adivinhe uma letra da palavra: ').lower()
            if attempt_value in word:
                word.index(attempt_value)
                print('Letra encontrada')
                next()
            else:
                print('Letra não encontrada')
                next()
        
        ##### Função validadora, que determina se o usuário terá mais uma vida ou se perdeu o jogo
        def next():
            if len(lifes) > 1:
                lifes_left()
                attempt()
            elif len(lifes) <= 1:
                print('Você perdeu!')
                lose()

        # Opção de sair do jogo
        if choice == 1:
            attempt()
        elif choice == 2:
            exit = True
            print('Até a próxima!')


forca()
