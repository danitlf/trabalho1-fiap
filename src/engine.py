import math
import json

LOAD_FILENAME = "storage.json"


def save_json(obj):
    """Saves a Python object as a JSON file."""
    try:
        with open(LOAD_FILENAME, 'w', encoding='utf-8') as file:
            json.dump(obj, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


def load_json():
    """Loads a JSON file into a Python object."""
    try:
        with open(LOAD_FILENAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {LOAD_FILENAME} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {LOAD_FILENAME}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def calcular_area(cultura, dimensoes):
    if cultura == "soja":
        return dimensoes[0] * dimensoes[1]  # Retângulo (base * altura)
    elif cultura == "milho":
        return math.pi * (dimensoes[0] ** 2)  # Círculo (pi * raio^2)
    else:
        return None


def calcular_insumos(quantidade_por_metro, total_metros):
    return quantidade_por_metro * total_metros


def get_form_plantio():
    cultura = input("Informe a cultura (soja/milho): ").lower()
    if cultura not in ["soja", "milho"]:
        print("Cultura inválida!")
        return get_form_plantio()
    if cultura == "soja":
        largura = float(
            input("Informe a largura da área em metros: "))
        comprimento = float(
            input("Informe o comprimento da área em metros: "))
        dimensoes = (largura, comprimento)
    else:
        raio = float(input("Informe o raio da área em metros: "))
        dimensoes = (raio,)

    area = calcular_area(cultura, dimensoes)
    produto = input("Informe o produto para manejo: ")
    quantidade_por_metro = float(input("Quantidade em ml por m²: "))
    insumos = calcular_insumos(
        cultura, produto, quantidade_por_metro, area)

    plantio_obj = {"cultura": cultura, "area": area,
                   "produto": produto, "insumos": insumos}
    return plantio_obj
