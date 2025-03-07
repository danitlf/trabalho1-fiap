from src.menu import exibir_menu
from src.engine import get_form_plantio, save_json, load_json

dados_plantio = []


def run_project():

    while True:
        exibir_menu()
        try:

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                
                dados_plantio.append(get_form_plantio())
                save_json(dados_plantio)
                print("Dados adicionados com sucesso!")

            elif opcao == "2":
                if not dados_plantio:
                    print("Por favor, volte e preencha os dados na opção 1.")
                for i, dado in enumerate(dados_plantio):
                    print(
                        f"{i}: Cultura: {dado['cultura']}, Área: {dado['area']:.2f} m², Produto: {dado['produto']}, Insumos necessários: {dado['insumos']:.2f}")

            elif opcao == "3":
                indice = int(input("Informe o índice do dado a atualizar: "))
                if 0 <= indice < len(dados_plantio):
                    plantio_obj = get_form_plantio()
                    dados_plantio[indice]["area"] = plantio_obj["area"]
                    dados_plantio[indice]["cultura"] = plantio_obj["cultura"]
                    dados_plantio[indice]["produto"] = plantio_obj["produto"]
                    dados_plantio[indice]["insumos"] = plantio_obj["insumos"]
                    save_json(dados_plantio)
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
    try:
        loaded_data = load_json()
        if loaded_data:
            dados_plantio = loaded_data
    except:
        print("falha ao carregar dados")

    run_project()
