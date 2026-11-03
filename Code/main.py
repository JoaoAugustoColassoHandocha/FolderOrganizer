'''


'''

lazy from pathlib import Path
lazy import shutil, os, sys, time, builtins

try:
    
    
    _print_original = builtins.print

    def print_centralizado(*args, **kwargs):
        
        largura = shutil.get_terminal_size().columns
        texto = ' '.join(str(a) for a in args)
        
        for linha in texto.splitlines() or ['']:
                
            _print_original(linha.center(largura), **kwargs)
        
    def input_centralizado(prompt = ''):
            
        print('\n')
        
        largura = shutil.get_terminal_size().columns
        # Move o prompt para o centro horizontal do terminal
        espaco = (largura - len(prompt)) // 2
        return input(' ' * max(espaco, 0) + prompt)

    def barra_carregamento(total=30, atraso=0.2):
            
        print('\n')
            
        for i in range(total + 1):
            porcentagem = int((i / total) * 100)
            barra = '█' * i + '-' * (total - i)
            texto = f'Carregando: |{barra}| {porcentagem}%'
            largura = shutil.get_terminal_size().columns
            sys.stdout.write('\r' + texto.center(largura - 1))
            sys.stdout.flush()
            time.sleep(atraso)
            
    os.system('cls' if os.name == 'nt' else 'clear')
        
    print_centralizado('\n------------------------------')
    print_centralizado('FolderOrganizer')
    print_centralizado('------------------------------\n')
        
    barra_carregamento()
            
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def main(op = 0):
    
        print_centralizado('\n------------------------------')
        print_centralizado('FolderOrganizer')
        print_centralizado('------------------------------\n')
        
        print_centralizado('1 - Organizar')
        print_centralizado('2 - Sair')
        
        opcao = input('Opção (Somente números): ')
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if (opcao != '1') or (opcao != '2'):

            print('\n[AVISO] Opção inválida, digite novamente\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            main(op = 0)
        
        match opcao:
            
            case '1':
                
                ...
                
            case '2':
                
                ...
        
    main(op = 0)
    
except Exception as error:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_centralizado('\nOps! Ocorreu um erro inesperado ao processar sua solicitação.\n')
    print_centralizado('Entre em contato com o suporte técnico, informando nome do erro.')
    print_centralizado(f'\nErro: {error} ({type(error).__name__})\n')

    input_centralizado('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')