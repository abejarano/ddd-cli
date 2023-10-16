#!/usr/bin/env python3
import argparse
import os

def create_module_structure(module_name):
    current_directory = os.getcwd()  # Obten la carpeta actual
    module_path = os.path.join(current_directory, module_name)

    if os.path.exists(module_path):
        print(f"El módulo '{module_name}' ya existe en la carpeta actual.")
        return

    os.mkdir(module_path)

    subfolders = ['domain', 'usecase', 'infrastructure']

    for subfolder in subfolders:
        subfolder_path = os.path.join(module_path, subfolder)
        os.mkdir(subfolder_path)

        if subfolder == 'infrastructure':
            infrastructure_subfolders = ['http', 'persistence']
            for infrastructure_subfolder in infrastructure_subfolders:
                infrastructure_subfolder_path = os.path.join(subfolder_path, infrastructure_subfolder)
                os.mkdir(infrastructure_subfolder_path)

                if infrastructure_subfolder == 'http':
                    http_subfolders = ['controllers', 'validators']
                    for http_subfolder in http_subfolders:
                        http_subfolder_path = os.path.join(infrastructure_subfolder_path, http_subfolder)
                        os.mkdir(http_subfolder_path)

    print(f"Estructura de carpetas creada para el módulo '{module_name}' en {module_path}.")

def main():
    parser = argparse.ArgumentParser(description="Crea la estructura de carpetas para un módulo de backend.")
    parser.add_argument("module_name", help="Nombre del módulo")

    args = parser.parse_args()
    create_module_structure(args.module_name)

if __name__ == "__main__":
    main()
