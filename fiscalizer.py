import pandas as pd
import os


# Lectura del directorio actual y creación de carpetas
def get_csv_files_in_directory():
    """
    Obtiene una lista de archivos CSV en el directorio actual.

    Retorna:
    list: Una lista de nombres de archivos CSV en el directorio actual.
    """
    current_directory = os.getcwd()
    files = [f for f in os.listdir(current_directory) if f.endswith('.csv')]
    return files

def create_directory_for_a_file(file):
    """
    Crea un directorio basado en el nombre del archivo (sin la extensión).

    Parámetros:
    file (str): El nombre del archivo.
    """
    file_name_without_extension = os.path.splitext(file)[0] 
    if not os.path.exists(file_name_without_extension):
        os.makedirs(file_name_without_extension)
    return file_name_without_extension

# Lectura del archivo CSV y catalogación de transacciones por tipo

def read_csv_data(ruta):
    """
    Lee un archivo CSV que contiene datos históricos y devuelve un DataFrame de pandas.

    Parámetros:
    ruta (str): La ruta al archivo CSV.

    Retorna:
    pd.DataFrame: Un DataFrame que contiene los datos del archivo CSV.
    """
    try:
        df = pd.read_csv(ruta)
        return df
    except Exception as e:
        print(f"Error al leer el archivo {ruta}: {e}")
        return None

def get_transactions_by_type(file, type):
    """
    Muestra todas las transacciones de un DataFrame que coinciden con un valor específico en la columna 'Type'.
    """
    return file[file['Type'] == type]

def export_by_type(file, type):
    """
    Exporta las transacciones de un tipo específico a un archivo CSV.
    
    Parámetros:
    file (pd.DataFrame): El DataFrame
    type (str): El tipo de transacción a exportar.
    """
    df_type = get_transactions_by_type(file, type)
    if not df_type.empty:
        df_type.to_csv(f'Nexo_{type.replace(" ","_")}.csv', index=False)
    return len(df_type)

def delete_from_dataframe(file, type):
    """
    Elimina todas las filas de un DataFrame que coinciden con un valor específico en la columna 'Type'.
    """
    return file[file['Type'] != type]

def extract_type(file):
    """
    Extrae el primer valor único de la columna 'Type' en un DataFrame.
    """
    return file.loc[0,'Type']

def process_transactions(file):
    """
    Pocesa todas las transacciones en un DataFrame, exportándolas por tipo y eliminándolas del DataFrame original.

    Parámetros:
    file (pd.DataFrame): El DataFrame
    """
    total_count = 0
    while len(file) > 0:
        tipo = extract_type(file)
        total_count += len(file[file['Type'] == tipo])
        export_by_type(file, tipo)
        file = delete_from_dataframe(file, tipo).reset_index(drop=True)
    print(f'Total transactions processed: {total_count}')


def main():
    """
    Procesa los archivos CSV en el directorio actual, creando un directorio para cada archivo
    y exportando las transacciones por tipo dentro de cada directorio.
    """
    for f in get_csv_files_in_directory():
        print(f'Processing file: {f}')
        print('-' * 40)

        dir_name = create_directory_for_a_file(f)
        file  = read_csv_data(f)
        os.chdir(dir_name)
        process_transactions(file)
        os.chdir('..')

main()