'''


'''

lazy from pathlib import Path
lazy import shutil, os, sys, time, builtins

try:
    
    
    _print_original = builtins.print

    def print_centered(*args, **kwargs):
        
        width = shutil.get_terminal_size().columns
        text = ' '.join(str(a) for a in args)
        
        for line in text.splitlines() or ['']:
                
            _print_original(line.center(width), **kwargs)
        
    def input_centered(prompt = ''):
            
        print('\n')
        
        width = shutil.get_terminal_size().columns
        # Moves the prompt to the horizontal center of the terminal
        space = (width - len(prompt)) // 2
        return input(' ' * max(space, 0) + prompt)

    def loading_bar(total = 30, atraso = 0.2):
            
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
        
    print_centered('\n------------------------------')
    print_centered('FolderOrganizer')
    print_centered('------------------------------\n')
        
    loading_bar()
            
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def main(op = 0):
    
        print_centered('\n------------------------------')
        print_centered('FolderOrganizer')
        print_centered('------------------------------')
        print_centered('1 - Organizar')
        print_centered('2 - Sair')
        print_centered('------------------------------\n')
        
        option = input('\nOpção (Somente números): ')
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if (option != '1') and (option != '2'):

            print('\n[AVISO] Opção inválida, digite novamente\n')
            input('Clique qualquer tecla para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')
            main(op = 0)
        
        match option:
            
            case '1':
                
                folder_path = input('Caminho da pasta: ')
                os.system('cls' if os.name == 'nt' else 'clear')
                
                destination_folder = Path.home() / f'{folder_path}'
                
                folders = {
                    
                    'Imagens': ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.tiff', '.tif', '.bmp', '.raw', '.svg', '.ai', '.eps', '.cdr', '.ico'],
                    
                    'Documentos': ['.pdf', '.txt', '.doc', '.docx', '.odt', '.rtf', '.xlsx', '.xls', '.pptx', '.htm', '.html', 'dotx', '.docm', '.dotm'],
                    
                    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.webm', '.avchd', '.wmv', '.flv', '.ogg', '.mpg'],
                    
                    'Audio': ['.wav', '.aiff', '.pcm', '.flac', '.m4a', '.alac', '.mp3', '.aac', '.wma'],
                    
                    'Executaveis': ['.exe', '.com', '.bat', '.cmd', '.msi', '.sh', '.app', '.dmg'],
                    
                }
                
                for name in folders:
                    
                    ()
                
            case '2':
                
                print_centered('\nSaindo...\n')
                loading_bar()
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.exit()
        
    main(op = 0)
    
except Exception as error:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_centered('\nOps! Ocorreu um erro inesperado ao processar sua solicitação.\n')
    print_centered('Entre em contato com o suporte técnico, informando nome do erro.')
    print_centered(f'\nErro: {error} ({type(error).__name__})\n')

    input_centered('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')