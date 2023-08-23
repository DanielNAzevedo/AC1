Ano = float(input("Informe o ano:"))

Ano % 4 == 0
Ano % 100 == 0
Ano % 400 ==0

print(Ano % 4 == 0 or Ano %100 != 0 and Ano % 4 ==0)