print("**************Calculo Geral ******************")
print("Digite um numero de acordo a função desejada :")
print("**********************************************")
print("1) IMC : ")
print("2) Calculo de media :")
print("3) Calulo de juros")
qfuncao = eval(input("Digite o numero desejado :"))
if qfuncao == 1:
     print("**********************Você digitou o calculo de IMC**********")
     altura = eval(input("Digite sua altura : "))
     peso = eval(input("Digite seu peso :"))
     altura2 = altura * altura
     IMC = peso/altura2
     if IMC < 18:
          print("Abaixo do Peso")
     elif IMC < 25:
          print("Peso Normal")
     elif IMC < 30:
          print("SobrePreso")
     elif IMC < 35:
          print("obesidade grau I")
     elif IMC < 40:
          print("Obesidade grau II")
     else:
          print("Obedidade Morbida III")
else:
     if qfuncao == 2:
          print("**********************Calculo de media **********")
          materia = input("Qual o nome da matéria:")
          mediaestipulada = eval(input("Digite a media da matéria : "))
          nota1 = eval(input("Digite a primeira nota :"))
          print("************************************************")
          while nota1 > 10 or nota1 < 0:
               print("Digite novamente! favor digitar um valor entre zero e dez**:")
               nota1 = eval(input("Digite novamente o valor da primeira nota:"))
               print("************************************************")
          nota2 = eval(input("Digite a segunda nota :"))
          print("************************************************")
          while nota2 > 10 or nota2 < 0:
               print("Digite novamente! favor digitar um valor entre zero e dez**:")
               nota2 = eval(input("Digite novamente o valor da segunda nota:"))
          print("************************************************")
          nota3 = eval(input("Digite a terceira nota:"))
          print("************************************************")
          while nota3 > 10 or nota3 < 0:
               print("Digite novamente! favor digitar um valor entre zero e dez**:")
               nota3 = eval(input("Digite novamente o valor da terceira nota:"))
          print("************************************************")
          nota4 = eval(input("Digite a quarta nota:"))
          print("************************************************")
          while nota4 > 10 or nota4 < 0:
               print("Digite novamente! favor digitar um valor entre zero e dez**:")
               nota4 = eval(input("Digite novamente o valor da quarta nota : "))
               print("************************************************")
          media = (nota1 + nota2 + nota3 + nota4) / 4
          if media >= mediaestipulada:
               print(" Sua media na matéria de ",materia," é : ",media, " Parabens! Aluno aprovado !!")
               print("************************************************")
          else:
               print("Sua Media na matéria de ",materia," é : ",media," Ixi a casa caiu!!")
               print("************************************************")
     else:
          if qfuncao == 3:
               print("calculo de juros simples e composto:")
               capital = eval(input("Entre com o valor do capital  :"))
               taxa = int(input("Entre com o valor da taixa (estipulado ao mês) : "))
               tempo = eval(input("Entre com o tempo estipulado em meses :"))
               taxa = taxa/100
               print(taxa)
               juros = taxa * capital * tempo
               print("O valor do seu juros simples é de : ",juros)
               print("*************** Programa Encerrado*************")
print("*************** Programa Encerrado*************")


