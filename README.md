# FolderOrganizer 🗂️

Organizador de arquivos para terminal, escrito em Python. Ele varre uma pasta e move cada arquivo para uma subpasta de acordo com a extensão, deixando seus downloads e diretórios bagunçados em ordem em poucos segundos.

✨ Funcionalidades
Interface de terminal centralizada, com menu interativo e barra de carregamento animada
Organização automática por tipo de arquivo
Criação automática das subpastas necessárias
Proteção contra sobrescrita: se já existir um arquivo com o mesmo nome no destino, ele é ignorado
Tratamento de erros com mensagem amigável
Compatível com Windows, Linux e macOS (limpeza de tela via cls/clear)
📁 Categorias
Pasta	Extensões
Imagens	.jpg, .jpeg, .png, .webp, .gif, .tiff, .bmp, .raw, .svg, .ai, .eps, .cdr, .ico
Documentos	.pdf, .txt, .doc, .docx, .odt, .rtf, .xls, .xlsx, .pptx, .html, entre outras
Videos	.mp4, .mov, .avi, .mkv, .webm, .wmv, .flv, .mpg, entre outras
Audio	.mp3, .wav, .flac, .m4a, .aac, .wma, entre outras
Executaveis	.exe, .msi, .bat, .cmd, .sh, .app, .dmg, entre outras
Pastas_ZIP	.zip
ISO	.iso, .torrent, .vbo-extpack
🚀 Como usar
Requisitos
Python 3.14 ou superior, pois o código usa lazy imports (lazy import, PEP 810) e match/case
Execução
bash
git clone https://github.com/seu-usuario/FolderOrganizer.git
cd FolderOrganizer
python folder_organizer.py
Passo a passo
No menu, digite 1 para organizar ou 2 para sair.
Informe o caminho da pasta relativo à sua pasta de usuário (por exemplo, Downloads ou Documents/Projetos).
Aguarde a barra de carregamento. Os arquivos serão movidos para as subpastas correspondentes.
⚙️ Como funciona
Define um dicionário que associa cada categoria às suas extensões.
Cria as subpastas no diretório escolhido (mkdir(exist_ok=True)).
Percorre os itens da pasta com Path.iterdir() e compara a extensão (em minúsculas) de cada arquivo com as categorias.
Move o arquivo com shutil.move, caso não exista outro com o mesmo nome no destino.
🛠️ Tecnologias
Python 3
Bibliotecas padrão: pathlib, shutil, os, sys, time, builtins
⚠️ Observações
Arquivos com extensões não listadas permanecem na pasta original.
Subpastas existentes não são tocadas, apenas arquivos soltos na raiz da pasta escolhida.
O caminho é sempre resolvido a partir de Path.home().
Recomenda-se testar primeiro em uma pasta de teste, pois a operação move os arquivos.
🔮 Ideias para o futuro
Suporte a mais extensões (.7z, .rar, .csv, .json, etc.)
Opção de desfazer a organização
Modo de pré-visualização (dry run)
Aceitar caminhos absolutos
Renomear arquivos duplicados em vez de ignorá-los