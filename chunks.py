from gptabla import split_text_with_overlap, gpt_tabla, gpt_union_tablas
from tbsamples import tabla_incompleta_ac_otros
import os
from concurrent.futures import ThreadPoolExecutor

# lista de nombres de los archivos en la carpeta cv/mx
list_dir = os.listdir('cv/mx')

# lista de los archivos que terminan en .txt
list_txt = [i for i in list_dir]
print(list_txt)

indice = 0 # indice para la lista de los textos

# Texto a dividir
with open(f'cv/mx/{list_txt[indice]}', 'r') as file:
    text = file.read()
print(len(text))

# Obtener los pedazos
split_text = split_text_with_overlap(text, chunk_size=45000, overlap=300)
print(len(split_text))


# Obtener las tablas con gpt
list_res = []

def get_gpt_table(i):
    return gpt_tabla(tabla_incompleta_ac_otros, split_text[i], list_txt[indice] + str(i))

with ThreadPoolExecutor() as executor:
    list_res = list(executor.map(get_gpt_table, range(len(split_text))))


# unir las tablas con gpt
tabla_final = gpt_union_tablas(list_res, list_txt[indice])