
salario=int(input("Digite o seu salário:   "))
base = salario 
imposto = 0
if base >3000:
  imposto = imposto +((base-3000)*0.35)
  base = 3000
if base >1000:
  imposto += (base - 1000) * 0.20
  print("Salário: R${} imposto a pagar: R${}".format(salario, imposto))
