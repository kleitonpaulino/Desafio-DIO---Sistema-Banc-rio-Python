import datetime

# Função para obter a data atual e formatá-la
def get_data():
    data = datetime.datetime.now()
    data = data.strftime("%Y-%m-%d %H:%M:%S")
    return data

# Função para gerenciar as entradas ao extrato da conta
def extrato_conta_vazio(string):
    global extrato_conta
    if extrato_conta == "": # Verifica se o extrato está vazio
        # Se estiver vazio, adiciona o cabeçalho e a string fornecida
        extrato_conta = f"\n{separador}\nExtrato da Conta:\n{separador}\n"
        extrato_conta += string
    else:
        # Caso contrário, somente a string fornecida na linha seguinte
        extrato_conta += "\n" + string

# Função para testar se a entrada fornecida pelo usuário é um número
def testar_numero(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Função para testar se a entrada fornecida pelo usuário é um número válido (não negativo)
def verificar_validade_numero(numero):
    if testar_numero(numero):
        if float(numero) >= 0:
            return True
        else:
            print("Número menor que 0")
            return False
    else:
        print("Número inválido")
        return False

# Função para realizar um depósito
def deposito():
    entrada = input("Digite o valor a ser depositado: ")
    if verificar_validade_numero(entrada):
        global saldo
        print("Saldo anterior R$ {:.2f}".format(saldo))
        global extrato_conta
        extrato_conta_vazio(f"Depósito às {get_data()}" + " no valor de R$ {:.2f}".format(float(entrada)))
        saldo += float(entrada)
        print("Valor depositado R$ {:.2f}".format(float(entrada)))
        print("Saldo atual R$ {:.2f}".format(saldo))

# Função para realizar um saque
def saque():
    global limite_saque
    # Verificar se o limite de saques diários foi alcançado
    if limite_saque == 0:
        print("Limite de saques diários alcançados!")
    else:
        entrada = input("Digite o valor do saque: ")
        # Verificar se a entrada fornecida pelo usuário é valida
        if verificar_validade_numero(entrada):
            global limite
            # Verificar se o valor fornecido é menor ou igual ao valor limite de saque individual
            if float(entrada) <= limite:
                global saldo
                # Verificar se o valor do saque é coberto pelo saldo da conta
                if saldo >= float(entrada):
                    saldo -= float(entrada)
                    print("Saque de R$ {:.2f}".format(float(entrada)) + " realizado com sucesso!")
                    print("Saldo atual de R$ {:.2f}".format(float(saldo)))
                    limite_saque -= 1
                    global extrato_conta
                    extrato_conta_vazio(f"Saque    às {get_data()}" + " no valor de R$ {:.2f}".format(float(entrada)))
                else:
                    print("Saldo insuficiente para o saque!")
            else:
                print("Valor inválido! O limite por saque é de R$ 500.00")

# Função para exibir o extrato da conta
def extrato():
    global extrato_conta
    if extrato_conta == "Extrato da Conta:":
        print(extrato_conta + "\nNenhuma movimentação realizada")
        print(separador)
    else:
        global saldo
        print(extrato_conta)
        print(separador)
        print("Saldo em conta de R$ {:.2f}".format(saldo))
        print(separador)

# Menu de operações
menu = """
Escolha uma operação:
    [d] Depósito
    [s] Sacar
    [e] Extrato
    [q] Sair
==> """
separador = "-----------------------------------------------------"

# Variáveis de estado
saldo = float(0)
limite = 500
limite_saque = 3
extrato_conta = ""

# Loop principal do programa
while True:
    opcao = input(menu)

    if opcao == "d":
        deposito()
    elif opcao == "s":
        saque()
    elif opcao == "e":
        extrato()
    elif opcao == "q":
        print("Saindo")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")