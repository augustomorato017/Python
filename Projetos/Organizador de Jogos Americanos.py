from pathlib import Path
import shutil
pasta = Path(r'D:\ROMS\Mega Drive')
pasta_usa = Path(r'D:\ROMS\Mega Drive\Usa')

for arquivo in pasta.iterdir():
    if arquivo.is_file():
        if '(USA)' in arquivo.name or '(World)' in arquivo.name:
            destino = pasta_usa / arquivo.name
            shutil.move(str(arquivo), str(destino))
            print(f'Movido {arquivo.name}')
print('Concluído!')