from datetime import date
atual = date.today().year
maior = []
menor = []
for anos in range(1,8):
  ano = int(input('digite o ano de nascimento: '))
  idade = atual - ano
  if idade >= 18:
      maior.append(ano)
  else:
      menor.append(ano)
print('existe {} pessoas maior de idade e {} pessoas menor de idade'.format(len(maior), len(menor)))
