# IMC => PESO (KG) / ALTURA (M)²

def numero_quadrado(numero):
  quadrado = numero * numero 
  return quadrado 

def calcular_imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada

  return meu_imc

def classificar_imc(meu_imc):
  if imc < 18.5:
    print('Magreza')
  elif imc >= 18.5 and imc < 25:
    print('Normal')
  elif imc >= 25 and imc < 30:
    print('Sobrepeso')
  elif imc >= 30 and imc < 40:
    print('Obesidade')
  else:
    print('Obesidade Grave')

imc = calcular_imc(66, 1.75)

print('Seu IMC é:', imc)

print('Sua classificação é:')
classificar_imc(imc)