import random

display_messages = [
    'Seja Feliz :)',
    'Fique tranquilo, tudo vai acabar bem!',
    'ola mundo! estou aqui!'
]

while True:
    resposta = input('Deseja Receber um Conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
