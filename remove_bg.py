from rembg import remove
from PIL import Image

# Caminhos dos arquivos
input_path = r"C:\Users\SeuUsuario\Caminho\Para\Sua\Imagem.jpg"
output_path = "sem_fundo.png"

try:
    # Abrir a imagem original
    with Image.open(input_path) as img:
        # Remover o fundo
        img_sem_fundo = remove(img)
    # Redimensionar para manter tamanho original
    img_sem_fundo = img_sem_fundo.resize(img.size, Image.LANCZOS)
    # Salvar imagem sem fundo
    img_sem_fundo.save(output_path, "PNG", optimize=True, quality=100)
    print("Imagem processada e salva como", output_path)
except Exception as e:
    print("Ocorreu um erro:", e)
