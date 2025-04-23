def calculator():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")
    
    while True:
        try:
            escolha = input("\nEscolha a operação (1-5): ")
            
            if escolha == '5':
                print("Obrigado por usar a calculadora!")
                break
                
            if escolha not in ['1', '2', '3', '4']:
                print("Opção inválida! Por favor, escolha entre 1 e 5.")
                continue
                
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                resultado = num1 + num2
                print(f"\n{num1} + {num2} = {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"\n{num1} - {num2} = {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"\n{num1} * {num2} = {resultado}")
            elif escolha == '4':
                if num2 == 0:
                    print("\nErro: Divisão por zero não é permitida!")
                else:
                    resultado = num1 / num2
                    print(f"\n{num1} / {num2} = {resultado}")
                    
        except ValueError:
            print("Erro: Por favor, digite apenas números!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            
if __name__ == "__main__":
    calculator() 