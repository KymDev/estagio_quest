faturamento = {
'SP' : 67836.43, 
'RJ' : 36678.66, 
'MG' : 29229.88 ,
'ES' : 27165.48 ,
'Outros' : 19849.53
}

valor_tot = sum(faturamento.values())

print("O Valor total foi:")
print(f'{valor_tot:.2f}')

print("Percentual de representação por estado:")
for estado, valor in faturamento.items():
    percentual = (valor/valor_tot)*100
    print(f'{estado}: {percentual:.2f}%')