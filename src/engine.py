import math
import json

LOAD_FILENAME = "storage.json"
LARGURA_RUA = 1

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

def calcular_ruas(cultura, dimensoes):
    quantidade_ruas = 0
    if cultura == "soja":
        maior_dimensao = dimensoes[0]
        menor_dimensao = dimensoes[1]
        if dimensoes[1] > dimensoes[0]:
            maior_dimensao = dimensoes[1]
            menor_dimensao = dimensoes[0]

        quantidade_ruas = menor_dimensao / 5
        return quantidade_ruas, (quantidade_ruas * maior_dimensao * LARGURA_RUA)  # Retângulo (base * altura)
    elif cultura == "milho":
        quantidade_ruas = 2
        return quantidade_ruas, (dimensoes[0] * quantidade_ruas * LARGURA_RUA)
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

    area_total = calcular_area(cultura, dimensoes)
    quantidade_ruas, area_rua = calcular_ruas(cultura, dimensoes)
    produto = input("Informe o produto para manejo: ")
    quantidade_por_metro = float(input("Quantidade em ml por m²: "))
    area_util = area_total - area_rua
    insumos = calcular_insumos(convert_ml_to_l(quantidade_por_metro), (area_total - area_rua ))

    plantio_obj = {"cultura": cultura, "area_total": area_total,
                   "produto": produto, "insumos": insumos,
                   "quantidade_ruas": quantidade_ruas, "area_rua": area_rua,
                   "area_util": area_util}
    return plantio_obj

def convert_ml_to_l(ml):
    return ml/1000