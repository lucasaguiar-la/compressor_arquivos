import os
from time import sleep
from PIL import Image

main_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(main_path, "arquivos")

def reduce_img(quality=10):
    print(f"Arquivo:{filename} | Tamanho original: {size}")
    sleep(1)
    file_path = os.path.join(output_path, filename)
    img = Image.open(file_path)
    img.save(file_path,quality=quality)
    print(f"Arquivo:{filename} | Tamanho final: {size}")

print("Procurando arquivos para compressão...")
sleep(1)
for filename in os.listdir(output_path):
    file_size = os.path.getsize(output_path+"\\"+filename)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        size = file_size / 1024
        if size > 2500:
            reduce_img()