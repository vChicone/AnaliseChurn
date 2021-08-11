import pandas as pd
import plotly.express as px
from IPython.display import display

#Importar tabela
tabela = pd.read_csv("telecom_users.csv")

#Descobrir erros
pd.set_option('display.max_columns', None)
display(tabela)
tabela = tabela.drop("Unnamed: 0", axis=1) #0=linha, 1=coluna
tabela = tabela.drop("IDCliente", axis=1)

#Tratamento de dados
print(tabela.info())
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
#Colunas vazias
tabela = tabela.dropna(how="all", axis=1) #all=colunas completaments vazios, any=tem pelo menos um valor vazio
#Linhas vazias
tabela = tabela.dropna(how="any", axis=0)

#Análise dos dados
display(tabela["Churn"].value_counts())
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Identificar os motivos
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, pattern_shape="Churn")
    grafico.show()

#Clientes com familias maiores (casados e filhos) tendem a cancelar menos
#MesesComoCliente baixo tem MUITO mais chance de cancelar
#Clientes de Fibra tem uma taxa de cancelamento alto
#Quanto mais serviços, menor a chance de cancelar
#Maioria do cancelamento no contrato mensal
#Boleto Eletronico maior taxa de cancelamento
