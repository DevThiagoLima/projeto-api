# O sistema precisar ter um menu com as opções abaixo. Organize o menu como ficar mais fácil para o usuário.

# Ouvir o Seu Zé: Perguntar quantos conselhos ele quer receber.

# Mostrar os Conselhos: Exibir os conselhos mágicos da API na tela. >> a.Consumir a API.

# Guardar a Sabedoria: Dar a opção de salvar os conselhos em um arquivo de texto, junto com o ID do conselho.

# Mostrar os Conselhos guardados no arquivo de texto;

# Traduzir para o "Gringo": Se o Seu Zé quiser alcançar clientes internacionais, traduzir os conselhos do inglês para português usando a API deep_translator com o GoogleTranslator.

# Relembrar as Dicas: Permitir que o Seu Zé acesse os conselhos salvos e, se precisar, traduzi-los.
# A. Opção de apenas traduzir o conselho da API;
# B. Opção de traduzir o que estiver salvo no arquivo de texto;

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

from loguru import logger
import requests
from deep_translator import GoogleTranslator
from time import sleep

URL = 'https://api.adviceslip.com/advice'
way_conselhos = 'conselhos.txt'
conselhos_temporarios = []

if __name__ == '__main__':
    fimPrograma = 'Não'

    while fimPrograma == 'Não':
        print("\nSeja Bem-vindo Ao Nosso Programa de Conselhos!!\n")
        print("1. Ouvir Conselhos Arretados")
        print("2. Mostrar Os Conselhos Já Salvos")
        print("3. Guardar os Conselhos")
        print("4. Traduzir para o Gringo")
        print("5. Sair\n")

        try:
            opcao = int(input('>> '))
        except ValueError:
            print("Opção inválida! Digite um número entre 1 e 5.")
            continue

        match opcao:
            case 1:
                numConselhos = int(input('Digite a quantidade de conselhos que deseja receber: \n'))
                for i in range(numConselhos):
                    consulta = requests.get(URL).json()
                    id = consulta['slip']['id']
                    advice = consulta['slip']['advice']
                    traducao_br = GoogleTranslator(source='english', target='portuguese').translate(advice)
                    conselhos_temporarios.append((id, advice, traducao_br))
                    print(f'Conselho {i + 1}: {traducao_br}', '-' * 120)
                    sleep(1)

            case 2:
                try:
                    with open(way_conselhos, 'r', encoding="utf-8") as arquivo:
                        print(arquivo.read())
                except FileNotFoundError:
                    print("Nenhum conselho foi salvo ainda.")

            case 3:
                if conselhos_temporarios:
                    with open(way_conselhos, 'a', encoding='utf-8') as arquivo:
                        for id, advice, traducao_br in conselhos_temporarios:
                            arquivo.write(f'{id} - {traducao_br}\n')
                    print("Conselhos salvos com sucesso!")
                    conselhos_temporarios.clear()
                else:
                    print("Nenhum conselho para salvar.")

            case 4:
                try:
                    with open(way_conselhos, "r", encoding="utf-8") as arquivo:
                        conselhos_traduzidos = [
                            GoogleTranslator(source='portuguese', target='english').translate(linha.strip())
                            for linha in arquivo.readlines()
                        ]
                    print("\nConselhos traduzidos para o inglês:\n")
                    for i, traducao in enumerate(conselhos_traduzidos, start=1):
                        print(f"Conselho {i}: {traducao}")
                except FileNotFoundError:
                    print("Nenhum conselho foi salvo ainda. O arquivo não existe.")

            case 5:
                print('Saindo do Programa...')
                sleep(1)
                fimPrograma = 'Sim'

            case _:
                print("Opção inválida. Digite um número entre 1 e 5.")
