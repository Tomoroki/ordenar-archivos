import os
import shutil
import sys

# Obtener la ruta del directorio a organizar desde los argumentos de línea de comandos
if len(sys.argv) > 1:
    directorio = sys.argv[1]
else:
    directorio = input("Ingrese la ruta del directorio a organizar: ")

# Verificar si la ruta del directorio es válida
if not os.path.isdir(directorio):
    print("La ruta del directorio no es válida.")
    sys.exit(1)

# Crear las carpetas principales si no existen
carpetas_principales = ["Documentos", "Imagenes", "Musica", "Videos", "Comprimidos", "Programas"]
for carpeta_principal in carpetas_principales:
    ruta_carpeta_principal = os.path.join(directorio, carpeta_principal)
    if not os.path.exists(ruta_carpeta_principal):
        os.makedirs(ruta_carpeta_principal)

# Crear un diccionario para almacenar las extensiones y las carpetas correspondientes
extensiones_carpetas = {
    ".7z": "Comprimidos/7z",
    ".apk": "Programas",
    ".avif": "Videos/avif",
    ".c": "Documentos/C",
    ".cpp": "Documentos/C++",
    ".csv": "Documentos/CSV",
    ".docx": "Documentos/Words",
    ".drawio": "Documentos/Drawio",
    ".exe": "Programas",
    ".gif": "Imagenes/gif",
    ".gz": "Comprimidos/gz",
    ".html": "Documentos/HTML",
    ".jpeg": "Imagenes/jpg",
    ".jpg": "Imagenes/jpg",
    ".json": "Documentos/JSON",
    ".m4a": "Musica/m4a",
    ".mp3": "Musica/mp3",
    ".mp4": "Videos/mp4",
    ".pdf": "Documentos/PDFs",
    ".png": "Imagenes/png",
    ".pptx": "Documentos/PowerPoint",
    ".rar": "Comprimidos/rar",
    ".svg": "Imagenes/svg",
    ".torrent": "Documentos/Torrents",
    ".txt": "Documentos/txt",
    ".webm": "Videos/webm",
    ".webp": "Imagenes/webp",
    ".xlsx": "Documentos/Excel",
    ".xml": "Documentos/XML",
    ".zip": "Comprimidos/zip"
}

# Crear las subcarpetas correspondientes si no existen
for carpeta in extensiones_carpetas.values():
    ruta_carpeta = os.path.join(directorio, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Mover archivos a las carpetas correspondientes
archivos = os.listdir(directorio)

for archivo in archivos:
    ruta_archivo = os.path.join(directorio, archivo)
    if os.path.isfile(ruta_archivo):
        extension = os.path.splitext(archivo)[1].lower()
        if extension in extensiones_carpetas:
            carpeta_destino = os.path.join(directorio, extensiones_carpetas[extension])
            shutil.move(ruta_archivo, carpeta_destino)
