import os
from time import sleep
from PIL import Image

main_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(main_path, "arquivos")

def format_sizes(size):
    if size < 1024:
        return f"{size:.3f} KB" 
    else:    
        return f"{size/1024:.2f} MB"

def reduce_img(size, quality=10):
    print(f"Arquivo:{filename} | Tamanho original: {format_sizes(size)}")
    sleep(1)
    file_path = os.path.join(output_path, filename)
    img = Image.open(file_path)
    img.save(file_path,quality=quality)
    size = os.path.getsize(output_path+"\\"+filename)
    print(f"Arquivo reduzido com sucesso!\nTamanho final: {format_sizes(size)}")

print("Procurando arquivos para compressão...")
sleep(1)
for filename in os.listdir(output_path):
    file_size = os.path.getsize(output_path+"\\"+filename)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        size = file_size / 1024
        if size > 2500:
            reduce_img(size)