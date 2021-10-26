import random
from .messages import display_messages

while True:
    resposta = input('Deseja Receber um Conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
