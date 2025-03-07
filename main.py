import math

def calcular_area(cultura, dimensoes):
    if cultura == "soja":
        return dimensoes[0] * dimensoes[1]  # Retângulo (base * altura)
    elif cultura == "milho":
        return math.pi * (dimensoes[0] ** 2)  # Círculo (pi * raio^2)
    else:
        return None

def calcular_insumos(cultura, produto, quantidade_por_metro, total_metros):
    return quantidade_por_metro * total_metros

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar dados de plantio")
    print("2. Exibir dados de plantio")
    print("3. Atualizar dados de plantio")
    print("4. Deletar dados de plantio")
    print("5. Sair")

dados_plantio = []

def run_project():

    while True:
        exibir_menu()
        try:

            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                cultura = input("Informe a cultura (soja/milho): ").lower()
                if cultura not in ["soja", "milho"]:
                    print("Cultura inválida!")
                    continue
                
                if cultura == "soja":
                    largura = float(input("Informe a largura da área em metros: "))
                    comprimento = float(input("Informe o comprimento da área em metros: "))
                    dimensoes = (largura, comprimento)
                else:
                    raio = float(input("Informe o raio da área em metros: "))
                    dimensoes = (raio,)
                
                area = calcular_area(cultura, dimensoes)
                produto = input("Informe o produto para manejo: ")
                quantidade_por_metro = float(input("Quantidade por metro: "))
                total_metros = float(input("Total de metros a serem tratados: "))
                insumos = calcular_insumos(cultura, produto, quantidade_por_metro, total_metros)
                
                dados_plantio.append({"cultura": cultura, "area": area, "produto": produto, "insumos": insumos})
                print("Dados adicionados com sucesso!")
            
            elif opcao == "2":
                for i, dado in enumerate(dados_plantio):
                    print(f"{i}: Cultura: {dado['cultura']}, Área: {dado['area']:.2f} m², Produto: {dado['produto']}, Insumos necessários: {dado['insumos']:.2f}")
            
            elif opcao == "3":
                indice = int(input("Informe o índice do dado a atualizar: "))
                if 0 <= indice < len(dados_plantio):
                    novo_produto = input("Novo produto: ")
                    nova_quantidade = float(input("Nova quantidade de insumo: "))
                    dados_plantio[indice]["produto"] = novo_produto
                    dados_plantio[indice]["insumos"] = nova_quantidade
                    print("Dados atualizados com sucesso!")
                else:
                    print("Índice inválido!")
            
            elif opcao == "4":
                indice = int(input("Informe o índice do dado a excluir: "))
                if 0 <= indice < len(dados_plantio):
                    dados_plantio.pop(indice)
                    print("Dado removido com sucesso!")
                else:
                    print("Índice inválido!")
            
            elif opcao == "5":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida!")
        except:
            print("Opção inválida!")
            pass


if __name__ == "__main__":
    run_project()
