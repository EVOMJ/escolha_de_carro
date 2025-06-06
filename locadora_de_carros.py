
def trancos( ):
     print('-' * 50)

trancos()
print (" aluguel  de carros com a maior frota do brasil| localiza ")
trancos()



trancos()
print("oi qual o  seu  nome ?")
trancos()

trancos()
nome=input("digite seu nome ")
trancos()

trancos()
print(f"Ola {nome}! estou felizes em  tê-lo conosco")
trancos()

print("selecione o carro que  deseja alugar :")

def mostra_opcoes():
     print("1 - BMW")
     print("2 - MUSTANG")
     print("3 - BH20")
     print("4 - FUSCA")
     print("5 - CIVIC")
     print("0 - SAIR")

mostra_opcoes()

trancos()



este_carro =int(input("digite o carro que desejar alugar:"))

match  este_carro:
     case 1:
      print(f' BMW,boa ideia {nome} ele é 1.6 thp  - R$ 3M')
     case 2:
      print(f'MUSTANG,boa ideia {nome}  ele é 1.6 ecoboost  - R$ 6M')
     case 3:
      print(f' BH20,boa ideia {nome} ele é 1.6 thp  - R$ 200k')
     case 4:
      print(f'FUSCA,boa ideia {nome}  ele é 1.6 ecoboost  - R$ 12k')
     case 5:
      print(f'CIVIC,boa ideia {nome} ele é 1.6 ecoboost - R$ 500k')
     case 0:
      print("saindo do programa...")
     case _:
         print("codigo invalido.por favor, selecione um código do menu.")


trancos()


