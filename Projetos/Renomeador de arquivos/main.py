from pathlib import Path

diretorio = Path(r'C:\Users\José Augusto\Documents\Scripts\Curso - Python\Teste')

for pasta in diretorio.iterdir():
    if pasta.is_dir():  # Garante que é uma pasta antes de entrar nela
        for arquivo in pasta.iterdir():
            if arquivo.is_file():
                # 1. Guarda o nome antigo para o print antes de renomear
                nome_antigo = arquivo.name 
                
                # 2. Define o novo caminho na MESMA pasta original do arquivo
                novo_caminho = arquivo.parent / 'main.py'
                
                # 3. Renomeia o arquivo fisicamente
                arquivo.rename(novo_caminho)
                
                print(f'Arquivo {nome_antigo} renomeado para {novo_caminho.name}')