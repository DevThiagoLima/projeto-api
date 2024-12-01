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

# CONTROLE DE SAIDA DO PROGRAMA E DA FUNÇÃO

fimPrograma = 'Não'
continuar = ['Sim', 'sim', 'S', 's']
way_conselhos = 'pasta_conselhos/conselhos.txt'
conselhos_temporarios = []


if __name__ == '__main__':
    
    while fimPrograma == 'Não':

        print(f'Seja Bem-vindo Ao Nosso Programa de Conselhos!!')
        print()

        print(f'\nO Que Voce Deseja Fazer?')
        print()

        print(f'1. Ouvir Conselhos Arretados')
        print(f'2. Mostrar Os Conselhos Já Salvos')
        print(f'3. Sair')
        print(f'4. Guardar os conselhos')
        print()

        opcao = int(input('>> '))

        # PRIMEIRA OPÇÃO DO MENU - BUSCAR CONSELHOS E SALVAR COM ID, CONSELHO E
        if opcao == 1:
            numConselhos = int(input('Digite a quantidade de conselhos que deseja receber: '))
            print()

            for i in range(numConselhos):
                consulta = requests.get(URL)

                id = consulta.json()['slip']['id']
                advice = consulta.json()['slip']['advice']
                traducao = GoogleTranslator(source='english', target='portuguese').translate(advice)

                sleep(1)
                print(f'{traducao}\n')
                print('-='*110 + '\n')

        # SEGUNDA OPÇÃO DO MENU - MOSTRAR OS CONSELHOS SALVOS
        elif opcao == 2:

            with open(way_conselhos, 'r', encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                
            print(conteudo)
                
        # TERCEIRA OPÇÃO DO MENU - SAIR DO PROGRAMA
        elif opcao == 3:

            print('Saindo do Programa')
            sleep(1)
            print('Fim do Programa!')
            fimPrograma = 'Sim'

        elif opcao == 4:
            with open(f'conselhos.txt', 'a', encoding='UTF-8') as arquivo:
                arquivo.write(f'{id} | {advice} | {traducao}\n')