menu = """

[X] - Sair
[D] - Depositar
[S] - Sacar
[E] - Extrato

=> """

saldo = 0 
extrato = ""
numero_de_saques = 0
limite_saques = 3
limite = 500

while True: 
    opcao = input(menu)
    
    if opcao == "X":
        print("Até uma próxima!")
        break
    
    elif opcao == "D":
        print("DEPÓSITO")
        
        valor = float(input("Qual o valor deseja depositar?"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" 
            
        else:
            print("Operação inválida! Valor não existente")
            
    elif opcao == "S":
        print("SAQUE")
        if numero_de_saques <=1:
            print(f"Valor disponível: {saldo}")
            valor_saque = float(input("Qual valor deseja sacar?"))
            
            if valor_saque > saldo or valor_saque > 500:
                print("impossível realizar saque.")
            
            else:
                saldo -= valor_saque
                extrato += f"SAQUE: R$ {valor:.2f}\n" 
        else:
            print("Limite diário atingido!")
    
    elif opcao == "E":
        print("EXTRATO")  
        extrato += f"SAQUE: R$ {valor:.2f}\n" 
        
    else:
        print("Digite alguma opção válida")