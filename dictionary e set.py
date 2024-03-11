anos = {
    #chave #valor
    1945   :45,
    1947   :47,
    1949   :49,
}
print(anos.get(1945))
#          ou       a diferença do get pro padrão é q se passar uma chave inexistente n dará erro
# print(anos[1945])
#print(anos.get[1948,1945]) passa o valor pós a vírgula caso o valor antes da vírgula seja inexistente
# print(len(anos))


#dictionary é uma coleção de chave e valor
#set e dictionary são chamados por meio de {} e pode armazenar qualquer valor
#set e dictionary liberam os valores inseridos neles de forma desordenada
#no set n é possível modificar valores dentro dele, sendo possível apenas adicionar ou remover
#set e dictionary n aceitam valores repetidos