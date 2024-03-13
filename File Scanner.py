import os

def scan_file(file_path):
    if os.path.exists(file_path):
        # Realizar un análisis de seguridad aquí (esto es simplificado).
        # Puedes utilizar bibliotecas como ClamAV o implementar tu propio análisis.

        # Aquí, simplemente consideramos que el archivo es seguro.
        print(f"El archivo {file_path} es seguro.")
    else:
        print(f"El archivo {file_path} no existe.")

if __name__ == "__main__":
    file_to_scan = input("Ingrese la ruta del archivo a escanear: ")
    scan_file(file_to_scan)
