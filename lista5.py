#1
class fila:
   def __init__(self):
      self.fila = []


   def adicionar_documento(self, documento):
      self.fila.append(documento)
      print(f"Documento {documento} adicionado à fila")

   def imprimir_documento(self):
      if self.fila:
         doc = self.fila.pop(0)
         print(f"Imprimindo documento {doc}")

   def primeiro_documento(self):
      if self.fila:
         return self.fila[0]
      else:
         return "A fila de impressão está vazia"

   def ultimo_documento(self):
      if self.fila:
         return self.fila[-1]
      else:
         return "A fila de impressão está vazia"

   def total_na_fila(self):
      return len(self.fila)


fila1 = fila()

fila1.adicionar_documento("doc1.pdf")
fila1.adicionar_documento("doc2.pdf")
fila1.adicionar_documento("doc3.pdf")
fila1.adicionar_documento("doc4.pdf")


print(f"Primeiro na fila {fila1.primeiro_documento()}")

print(f"Ultimo documento da fila {fila1.ultimo_documento()}")

print(f"Total de documentos na fila {fila1.total_na_fila()}")

fila1.imprimir_documento()
fila1.imprimir_documento()

print(f"Primeiro na fila {fila1.primeiro_documento()}")

print(f"Total de documentos na fila {fila1.total_na_fila()}")

////////////////////////////

#2
class fila_atendimento:
   def __init__(self):
      self.fila = []


   def adicionar_cliente(self,cliente):
      self.fila.append(cliente)
      print(f"Cliente {cliente} entrou na fila")

   def atender_cliente(self):
      if self.fila:
         cliente = self.fila.pop(0)
         print(f"Atendendo cliente {cliente}")
      else:
         return "A fila está vazia"

   def primeiro_cliente(self):
      if self.fila:
         return self.fila[0]
      else:
         return "Fila vazia"

   def ultimo_cliente(self):
      if self.fila:
         return self.fila[-1]
      else:
         return "Fila vazia"

   def total_na_fila(self):
      if self.fila:
         return len(self.fila)
      else:
         return "Fila vazia"


fila = fila_atendimento()

fila.adicionar_cliente("joao")
fila.adicionar_cliente("pedro")
fila.adicionar_cliente("gabriel")

print(f"Primeiro da fila {fila.primeiro_cliente()}")
print(f"último da fila {fila.ultimo_cliente()}")
print(f"Total de clientes na fila {fila.total_na_fila()}")

fila.atender_cliente()
fila.atender_cliente()

print(f"Primeiro da fila {fila.primeiro_cliente()}")
print(f"Total na fila {fila.total_na_fila()}")

//////////////////////////////////

#3
class FilaDePedidos:
    def __init__(self):
        self.fila = []

    def adicionar_pedido(self, pedido):
        self.fila.append(pedido)
        print(f"Pedido '{pedido}' adicionado à fila de pedidos.")

    def processar_pedido(self):
        if self.fila:
            pedido = self.fila.pop(0)
            print(f"Processando pedido: {pedido}")
        else:
            print("A fila de pedidos está vazia!")

    def primeiro_pedido(self):
        if self.fila:
            return self.fila[0]
        else:
            return "A fila de pedidos está vazia!"

    def ultimo_pedido(self):
        if self.fila:
            return self.fila[-1]
        else:
            return "A fila de pedidos está vazia!"

    def total_na_fila(self):
        return len(self.fila)

fila = FilaDePedidos()

fila.adicionar_pedido("Pedido1: Pizza Margherita")
fila.adicionar_pedido("Pedido2: Hambúrguer com Batata Frita")
fila.adicionar_pedido("Pedido3: Salada Caesar")

print(f"Primeiro na fila: {fila.primeiro_pedido()}")
print(f"Último na fila: {fila.ultimo_pedido()}")
print(f"Total de pedidos na fila: {fila.total_na_fila()}")

fila.processar_pedido()
fila.processar_pedido()

print(f"Primeiro na fila: {fila.primeiro_pedido()}")
print(f"Total de pedidos na fila: {fila.total_na_fila()}")

/////////////////////////////////

#4
class ListaDeTarefas:
    def __init__(self):
        self.fila = []

    def adicionar_tarefa(self, tarefa):
        self.fila.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à lista de tarefas.")

    def concluir_tarefa(self):
        if self.fila:
            tarefa = self.fila.pop(0)
            print(f"Tarefa '{tarefa}' conclida")
        else:
            print("A lista de tarefas esta vazia")

    def primeira_tarefa(self):
        if self.fila:
            return self.fila[0]
        else:
            return "A lista de tarefas esta vazia!"

    def ultima_tarefa(self):
        if self.fila:
            return self.fila[-1]
        else:
            return "A lista de tarefas est vazia!"

    def total_de_tarefas(self):
        return len(self.fila)


lista = ListaDeTarefas()

lista.adicionar_tarefa("Estudar Python")
lista.adicionar_tarefa("Fazer exercícios de matemática")
lista.adicionar_tarefa("Ir ao mercado")

print(f"Primeira tarefa: {lista.primeira_tarefa()}")
print(f"Última tarefa: {lista.ultima_tarefa()}")
print(f"Total de tarefas: {lista.total_de_tarefas()}")

lista.concluir_tarefa()
lista.concluir_tarefa()

print(f"Primeira tarefa: {lista.primeira_tarefa()}")
print(f"Total de tarefas: {lista.total_de_tarefas()}")

////////////////////////////////

#5
class FilaDePedidosOnline:
    def __init__(self):
        self.fila = []

    def adicionar_pedido(self, pedido):
        self.fila.append(pedido)
        print(f"Pedido '{pedido}' adicionado à fila de pedidos online.")

    def processar_pedido(self):
        if self.fila:
            pedido = self.fila.pop(0)
            print(f"Processando pedido: {pedido}")
        else:
            print("A fila de pedidos online está vazia!")

    def primeiro_pedido(self):
        if self.fila:
            return self.fila[0]
        else:
            return "A fila de pedidos online está vazia!"

    def ultimo_pedido(self):
        if self.fila:
            return self.fila[-1]
        else:
            return "A fila de pedidos online está vazia!"

    def total_de_pedidos(self):
        return len(self.fila)


fila_pedidos = FilaDePedidosOnline()

fila_pedidos.adicionar_pedido("Pedido #001: Smartphone")
fila_pedidos.adicionar_pedido("Pedido #002: Notebook")
fila_pedidos.adicionar_pedido("Pedido #003: Fone de Ouvido")

print(f"Primeiro pedido na fila: {fila_pedidos.primeiro_pedido()}")
print(f"Último pedido na fila: {fila_pedidos.ultimo_pedido()}")
print(f"Total de pedidos na fila: {fila_pedidos.total_de_pedidos()}")

fila_pedidos.processar_pedido()
fila_pedidos.processar_pedido()

print(f"Primeiro pedido na fila: {fila_pedidos.primeiro_pedido()}")
print(f"Total de pedidos na fila: {fila_pedidos.total_de_pedidos()}")

/////////////////////////////////

#6
class navegador_web:
   def __init__(self):
      self.historico = []
      self.futuro = []
      self.pagina_atual = None

   def visitar_pagina(self,url):
      if self.pagina_atual:
         self.historico.append(self.pagina_atual)
      self.pagina_atual = url
      self.futuro.clear()
      print(f"Visitando página {self.pagina_atual}")

   def voltar(self):
      if self.historico:
         self.futuro.append(self.pagina_atual)
         self.pagina_atual = self.historico.pop()
         print(f"Voltando para página {self.pagina_atual}")

   def avancar(self):
      if self.futuro:
         self.historico.append(self.pagina_atual)
         self.pagina_atual = self.futuro.pop()
         print(f"Avancando para página {self.pagina_atual}")
      else:
         print(f"Não há páginas para avancar")


chrome = navegador_web()

chrome.visitar_pagina("www.site1.com")
chrome.visitar_pagina("www.site2.com")
chrome.visitar_pagina("www.site3.com")
chrome.visitar_pagina("www.site4.com")


chrome.voltar()
chrome.voltar()
chrome.avancar()

///////////////////////////////

#7
class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def avaliar(self, expressao):
        for token in expressao.split():
            if token.isdigit():
                self.pilha.append(int(token))
            else:
                self.operar(token)

        return self.pilha.pop() if self.pilha else None

    def operar(self, operador):
        if len(self.pilha) < 2:
            raise ValueError("Expressão inválida: não há operandos suficientes.")

        b = self.pilha.pop()
        a = self.pilha.pop()

        if operador == '+':
            self.pilha.append(a + b)
        elif operador == '-':
            self.pilha.append(a - b)
        elif operador == '*':
            self.pilha.append(a * b)
        elif operador == '/':
            if b == 0:
                raise ZeroDivisionError("Divisão por zero.")
            self.pilha.append(a / b)
        else:
            raise ValueError(f"Operador desconhecido: {operador}")

calculadora = CalculadoraRPN()

expressao = "3 4 + 2 * 7 /"
resultado = calculadora.avaliar(expressao)
print(f"Resultado da expressão '{expressao}': {resultado}")

expressao2 = "5 1 2 + 4 * + 3 -"
resultado2 = calculadora.avaliar(expressao2)
print(f"Resultado da expressão '{expressao2}': {resultado2}")

/////////////////////////////////

#8
class editor_texto():
   def __init__(self):
      self.pilha_desfazer = []
      self.pilha_refazer = []
      self.texto = ""

   def adicionar_texto(self, texto_adicionado):
      self.pilha_desfazer.append(self.texto)
      self.texto += texto_adicionado
      self.pilha_refazer.clear()
      print(f"Texto atual: {self.texto}")

   def desfazer(self):
      if self.pilha_desfazer:
         self.pilha_refazer.append(self.texto)
         self.texto = self.pilha_desfazer.pop()
         print(f"Desfeito! texto atual: {self.texto}")
      else:
         print("nenhuma acao a ser desfeita")


   def refazer(self):
      if self.pilha_refazer:
         self.pilha_desfazer.append(self.texto)
         self.texto = self.pilha_refazer.pop()
         print(f"Refeito! texto atual {self.texto}")
      else:
         print("nenhuma acao a ser refeita")


editor = editor_texto()
editor.adicionar_texto("Olá, ")
editor.adicionar_texto("mundo!")
editor.desfazer()
editor.refazer()
editor.desfazer()
editor.desfazer()
editor.refazer()

////////////////////////////////

#9
class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.estah_vazia():
            return self.itens.pop()
        return None

    def estah_vazia(self):
        return len(self.itens) == 0

def verificar_palindromo(texto):
    pilha = Pilha()
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")  # Normaliza o texto

    for char in texto:
        pilha.empilhar(char)

    texto_invertido = ''
    while not pilha.estah_vazia():
        texto_invertido += pilha.desempilhar()

    return texto == texto_invertido


entrada = input("Digite uma palavra ou frase: ")
if verificar_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" não é um palíndromo.')

    ///////////////////////////////////

#10
class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.estah_vazia():
            return self.itens.pop()
        return None

    def estah_vazia(self):
        return len(self.itens) == 0

def verificar_palindromo(texto):
    pilha = Pilha()
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")  # Normaliza o texto

    for char in texto:
        pilha.empilhar(char)

    texto_invertido = ''
    while not pilha.estah_vazia():
        texto_invertido += pilha.desempilhar()

    return texto == texto_invertido


entrada = input("Digite uma palavra ou frase: ")
if verificar_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" não é um palíndromo.')
