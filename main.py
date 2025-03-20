from src.menu import exibir_menu
import subprocess
from src.engine import get_form_plantio, save_json, load_json, convert_ml_to_l

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
                        f"{i}\n Cultura: {dado['cultura']}\n",
                            f"Área: {dado['area_total']:.2f} m²\n",
                            f"Produto: {dado['produto']}\n",
                            f"Insumos necessários: {dado['insumos']:.2f} Litros\n",
                            f"Número de Ruas: {int(dado['quantidade_ruas'])}\n",
                            f"Área das Ruas: {dado['area_rua']}\n",
                            f"Área Útil: {dado['area_util']}\n"
                        )

            elif opcao == "3":
                indice = int(input("Informe o índice do dado a atualizar: "))
                if 0 <= indice < len(dados_plantio):
                    plantio_obj = get_form_plantio()
                    dados_plantio[indice]["area_total"] = plantio_obj["area_total"]
                    dados_plantio[indice]["quantidade_ruas"] = plantio_obj["quantidade_ruas"]
                    dados_plantio[indice]["area_rua"] = plantio_obj["area_rua"]
                    dados_plantio[indice]["area_util"] = plantio_obj["area_util"]
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
                    save_json(dados_plantio)
                    print("Dado removido com sucesso!")
                else:
                    print("Índice inválido!")

            elif opcao == "5":
                resultado = subprocess.run(["Rscript", "projeto_r/main.R"], capture_output=True, text=True)
                print("Executando programa em R para estatísticas")
                print(resultado.stdout)  # Exibe a saída

            
            elif opcao == "6":
                cidade = input("Informe a cidade: ")
                resultado = subprocess.run(["Rscript", "projeto_r/services/weatherLocationService.R", cidade], capture_output=True, text=True)
                print("Executando programa em R para dados climáticos")
                print(resultado.stdout)  # Exibe a saída

                
            elif opcao == "7":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida!")
        except Exception as e:
            print("Opção inválida!")
            print(e)
            pass


if __name__ == "__main__":
    try:
        loaded_data = load_json()
        if loaded_data:
            dados_plantio = loaded_data
    except:
        print("falha ao carregar dados")

    run_project()
