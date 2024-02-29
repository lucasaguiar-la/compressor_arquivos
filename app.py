import os
from time import sleep
from PIL import Image

main_path = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(main_path, "arquivos")
pdf_program_path = os.path.join(f"{main_path}\\pdf_reduce\\")

def reduce_pdf(file):
    path = (f"{pdf_program_path}pdfsizeopt")
    print(f"{path} --use-pngout=no {file} {file}")
    os.system(f"{path} --use-pngout=no {file} {file}")

def reduce_img(size, quality=10):
    print(f"\nArquivo:{filename} | Tamanho original: {size / 1024:.2f} MB")
    file_path = os.path.join(output_path, filename)
    img = Image.open(file_path)
    img.save(file_path,quality=quality)
    size = os.path.getsize(output_path+"\\"+filename)
    print(f"Arquivo reduzido com sucesso!\nTamanho final: {size / 1024:.2f} KB")
    sleep(1)

print("Procurando arquivos para compressão...")
sleep(1)
for filename in os.listdir(output_path):
    file_size = os.path.getsize(output_path+"\\"+filename)
    size = file_size / 1024
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        if size > 2500:
            reduce_img(size)
    elif filename.endswith(".pdf"):
        if size > 1500:
            reduce_pdf(filename)