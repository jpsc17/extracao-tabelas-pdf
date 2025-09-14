# TUTORIAIS
#intalar tabula-py
#intalar java jdk
#importar a biblioteca tabula
#extrair tabelas de um pdf e salvar em excel

import tabula
#ler a tabela do pdf
tabela = tabula.read_pdf("tabela_exemplo.pdf", pages='all', encoding='latin-1')

print(tabela)

#transformar a tabela em um dataframe
df = tabela[0]
#salvar o dataframe em excel
df.to_excel("tabela_extraida.xlsx", index=False)