print("************* Conversão de moeda **********")
NDM = input(" Entre com o nome da moeda : ")
#Nome da moeda
moeda = eval(input(" Entre com o valor da moeda em real :"))
if(NDM == "Dolar"):
    moeda = moeda * 5.78
    print(" O valor em dolar é :",moeda)
elif(NDM == "Euro"):
    moeda = moeda * 6.74
    print(" O valor em Euro é :",moeda)
elif(NDM == "Libra esterlina"):
    moeda = moeda * 7.45
    print(" O valor em Libra Esterlina é :",moeda)
elif(NDM == "Dolar canadense"):
    moeda = moeda * 4.32
    print(" O valor em Dolar canadense é : ",moeda)
elif(NDM == "Dolar australiano"):
    moeda = moeda * 4.05
    print (" O valor em Dolar Australiano é : ",moeda)
elif(NDM == "Franco Suiço"):
    moeda = moeda * 6.30
    print("O valor em Franco Suiço é : ",moeda)
elif(NDM =="Iene"):
    moeda = moeda * 0.55
    print("O valor em Iene é :",moeda)
elif(NDM == "Peso Argentino"):
    moeda = moeda * 0.74
    print("O valor em Peso Argentino é :",moeda)
elif(NDM =="Renminbi"):
    moeda = moeda * 0.86
    print("o valor em Corona Moeda é : ",moeda)
elif(NDM == "Lira Turca"):
    moeda = moeda * 0.70
    print("o valor en Lira Turca é :",moeda)
else:
    print("Nome da Moeda esta incorreto : ")



