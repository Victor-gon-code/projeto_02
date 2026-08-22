import os
from pathlib import Path
import csv
import random
import time

os.system('cls')

class Cliente:
    def __init__(self, dados):
        self.dados = dados

class Registro_clientes:
    def __init__(self):
        self.lista_clientes = []
        
    def adicionar_clientes(self, cliente):
            self.lista_clientes.append(cliente)

    def mostrar_clientes(self):
        for c in self.lista_clientes:
            print(c.dados)

class Bot_whatsapp:
    
    def __init__(self):
        self.mensagens_enviadas = []

    def criar_texto(self,nome_cliente, dia_cliente):
        texto = (f'olá {nome_cliente}, consta em meu sistema que o senhor(a)'
                           f'tem aula conosco dia {dia_cliente}, por favor só confirme sua presença digitando 1')
        return texto
        
    def enviar_mensagem(self, cliente_alvo):
        nome = cliente_alvo.dados['nome']
        dia = cliente_alvo.dados['dia']
        texto_pronto = self.criar_texto(nome, dia)
        self.mensagens_enviadas.append(texto_pronto)
        print("Mensagem disparada com sucesso:\n")
        print(f"=> {texto_pronto}")

caminho_csv = Path(__file__).parent/'clientes.csv'

# ==========================================
# EXECUTANDO A OPERAÇÃO EM MASSA
# ==========================================
registro = Registro_clientes()
with open(caminho_csv, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for c in leitor:
        pegar_cliente = Cliente(c)
        registro.adicionar_clientes(pegar_cliente)

registro.mostrar_clientes()

# 3. Ligamos o Bot
bot = Bot_whatsapp()

print("Iniciando operação de disparos...\n")

# 4. O Loop de Disparo (A varredura)
for cliente_atual in registro.lista_clientes:
    numero_random = random.randrange(4,7)
    bot.enviar_mensagem(cliente_atual)
    print("-" * 40)
    print(f'aguardando {numero_random}s de intervalo')
    time.sleep(numero_random)
    
