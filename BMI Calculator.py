def header():
  print("=============================================================================================")
  print("1 - Português\n2 - English\n")
  return input("Escolha sua linguagem/Choose your language: ")

menu = header()

if menu == "1":
  print ("\nBEM VINDO À CALCULADORA DE ÍNDICE DE IMC")
  height = input("Escreva sua altura em Metros: ")
  weight = input("Escreva seu peso em Kilos: ")

  float_Height = float(height)
  float_Weight = float(weight)
  result = int(float_Weight / float_Height ** 2)

  if result < 18.5:
    bmi = "'abaixo do peso'"
  elif result >= 18.5 and result < 25:
    bmi = "'peso normal'"
  elif result >= 25 and result < 30:
    bmi = "'acima do peso'"
  else:
    bmi = "'obesidade'"

  print("\nSeu índice de IMC é", result, "e isso significa que você se encaixa na categoria", bmi, "!")
  print("=============================================================================================")
  
elif menu == "2":
  print("\nWELCOME TO THIS BMI CALCULATOR")
  height = input("Enter your height in Meters: ")
  weight = input("Enter your weight in Kilos: ")

  float_Height = float(height)
  float_Weight = float(weight)
  result = int(float_Weight / float_Height ** 2)

  if result < 18.5:
    bmi = "'underweight'"
  elif result >= 18.5 and result < 25:
    bmi = "'normal weight'"
  elif result >= 25 and result < 30:
    bmi = "'overweight'"
  else:
    bmi = "'obesity'"

  print("\nYour BMI is", result, "and that means you are under the", bmi, "category!")
  print("=============================================================================================")
  
else:
  print("\n\nOPÇÃO INVÁLIDA/INVALID OPTION\n\n")
  header()