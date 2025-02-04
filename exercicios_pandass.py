import pandas as pd
import matplotlib.pyplot as plt

# importando arquivos

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

# retirar colunas
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)


# 1 - Folha Salarial

funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print(sum(funcionarios_df['Salario Total']))
print(f'Total da folha Salarial Mensal é de R$ {funcionarios_df['Salario Total'].sum():.2f}')


# 2 - Faturamento da Empresa

faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']
print(f'Total do faturamento mensal foi de R$ {faturamentos_df["Faturamento Total"].sum()}')


# 3 - % Funcionarios Fecharam Contrato

qtde_funcionario_contrato = len(servicos_df['ID Funcionário'].unique())
qtde_funcionario_total = len(funcionarios_df['ID Funcionário'])
print(f'A porcentagem de funcionarios que fecharam contratos foi de {qtde_funcionario_contrato / qtde_funcionario_total:.2%}')


# 4 - Qtde Contratos por Area

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
contratos_area_qtde = contratos_area_df['Area'].value_counts()
print(contratos_area_qtde)


# 5 - Qtde Funcionarios por Area

funcionarios_area = funcionarios_df['Area'].value_counts()
print(funcionarios_area)
funcionarios_area.plot(kind='bar')
plt.show(block=True)  # comando para mostrar graficos no pycharm. Obrigatorio usar depois do plot para mostrar o grafico


# 6 - Ticket Medio Mensal

def formatar(valor):
    return f'${valor:,.2f}'


ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
clientes_df = clientes_df['Valor Contrato Mensal'].map(formatar)
print(f'Ticket medio mensal foi de R$ {ticket_medio:,.2f}')
