# Remoção de Fundo de Imagem com Python 🖼️✨

Este projeto é um script simples em Python que **remove o fundo de uma imagem** automaticamente, utilizando as bibliotecas `rembg` e `Pillow (PIL)`.

## Funcionalidades 🚀
- Remove o fundo de uma imagem `.jpg` ou `.png`
- Salva a nova imagem com fundo transparente
- Mantém a qualidade e tamanho original da imagem

## Pré-requisitos 🛠️
Antes de rodar o script, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Como usar 📂
1. Coloque sua imagem original no caminho indicado.
2. No script `remove_bg.py`, ajuste o caminho da imagem:

```python
input_path = r"C:\Users\SeuUsuario\Caminho\Para\Sua\Imagem.jpg"
```

3. Execute o script:

```bash
python remove_bg.py
```

4. A imagem sem fundo será salva como `sem_fundo.png` na mesma pasta.

## Exemplo 🖼️
| Imagem Original | Imagem Processada |
|----------------|-------------------|
| ![Original](exemplo/original.jpg) | ![Sem Fundo](exemplo/sem_fundo.png) |

*(Substitua os arquivos em `/exemplo/` com as suas imagens para demonstrar)*

## Licença 📄
Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e compartilhar!
