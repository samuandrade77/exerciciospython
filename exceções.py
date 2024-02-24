try:
    ola = int(input("digite o valor:"))
    print(ola)
except ZeroDivisionError: 
     print('divisão por zero não existe, volte pra escola')
except ValueError:
     print ("tem que digitar um número inteiro, animal")
except:
     print("bugou foi tudo")
finally: 
     print("a bebir")
     
