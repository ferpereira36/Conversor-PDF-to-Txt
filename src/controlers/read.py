import platform
from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
import os

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# import mygetDir

# localpoppler = (mygetDir.getlocalpp)+"\poppler-0.68.0\\bin"
# print("\n")
# print(localpoppler)
# print("\n")


PDF_file = "seu_arquivo.pdf" #Identificando o arquivo pdf
  
if platform.system() == "Windows": #identificando o Sistema Operacional
 
    pytesseract.pytesseract.tesseract_cmd = (r"Tesseract-OCR\tesseract.exe") #Localizando a instalação do tesseract

    # path_to_poppler_exe = Path(str(localpoppler))
    # path_to_poppler_exe = Path(r"C:\Program Files (x86)\poppler-0.68.0\bin") #Poppler foi ajustado nas variaveis de ambiente do windows


paginas = convert_from_path(PDF_file, 500) #Converte pdf para imagem
contador = 1

for page in paginas:

    nomearquivo = "page_"+str(contador)+".jpg"
      
    
    page.save(nomearquivo, 'JPEG')
  
    
    contador = contador + 1
  
    
limitearquivo = contador-1
textosaida = "texto_saida.txt"

with open(textosaida, "a") as f:
    for i in range(1, limitearquivo + 1): 

        nomearquivo = "page_"+str(i)+".jpg"
            
        
        text = str(((pytesseract.image_to_string(Image.open(nomearquivo))))) 

        text = text.replace('-\n', '')
        
        f.write(text) #Escrevendo no arquivo texto
    f.close() #Fechando o arquivo texto