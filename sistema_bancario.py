class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f'Saque: R$ {valor:.2f}')
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Saque inválido. Verifique o valor ou saldo disponível.')

    def extrato(self):
        print(f'Saldo atual: R$ {self.saldo:.2f}')
        print('Histórico de transações:')
        for transacao in self.historico:
            print(transacao)

def menu():
    banco = Banco()
    
    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor a depositar: "))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a sacar: "))
            banco.sacar(valor)
        elif opcao == '3':
            banco.extrato()
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
