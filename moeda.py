import requests
import json
CoinAPI = requests.get(" https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
List = CoinAPI.json()

commandList = {
    'comandos': ['ajuda (a)', 'verificar moeda (v)', 'lista de moedas (l)'],
    'users': ['karlão', 'tayná', 'alana', 'gabigol', 'gabriel anão', 'cidalhão']
}

#commandList = ['ajuda (a)', 'comandos (c)', '']



def init():

    print('''bem vindo ao coinPicker, essa é uma aplicação que foi desenvolvida utilizando a api: https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL digite comandos ou (c) para ver a lista de comandos''')

    while True:
        def VerifyCoinPrice():
            global coin, List, code
            code = input("digite o código da moeda que deseja verificar: ")
            coin = List[f'{code}']['name']
            print(F"o preço da moeda: {coin} hoje é: ",List[f'{code}']['bid'])

        def PrintCoinList():
            print(List)
        escolha = input('''comand: ''')

        if escolha == "ajuda" or escolha == "a":
            print(commandList['ajuda'])

        elif escolha == 'comandos' or escolha == 'c':
            print(commandList['comandos'])

        elif escolha == "verificar moeda" or escolha == "v":
            VerifyCoinPrice()

        elif escolha == "lista de moedas" or escolha == "l":
            PrintCoinList()

        elif escolha == "sair" or escolha == "s":
            print("terminando execução...")
            break
        elif escolha == "usuários":
            print(commandList['users'])