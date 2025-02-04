# Análise Financeira e Operacional da Empresa

## Descrição
Este script utiliza `pandas` e `matplotlib` para analisar dados financeiros e operacionais da empresa. Ele realiza cálculos sobre folha salarial, faturamento, contratos fechados e distribuição de funcionários, gerando também gráficos informativos.

## Como Utilizar
### Pré-requisitos
Antes de executar o script, instale as dependências necessárias:
```bash
pip install pandas matplotlib openpyxl
```

Certifique-se de que os arquivos necessários (`CadastroFuncionarios.csv`, `CadastroClientes.csv`, `BaseServiçosPrestados.xlsx`) estão disponíveis no mesmo diretório do script.

### Executando o Script
1. Execute o script Python:
   ```bash
   python nome_do_script.py
   ```
2. O script realizará as seguintes operações:
   - Cálculo da folha salarial total.
   - Determinação do faturamento total da empresa.
   - Percentual de funcionários que fecharam contratos.
   - Quantidade de contratos fechados por área.
   - Quantidade de funcionários por área (exibindo um gráfico).
   - Cálculo do ticket médio mensal dos clientes.

### Observações
- O script presume que os arquivos de entrada estejam corretamente formatados com os campos necessários.
- Caso os gráficos não apareçam, verifique se a execução do script permite exibição visual (`plt.show()`).
- Modifique a função `formatar()` caso deseje alterar a formatação dos valores monetários.

## Contribuindo para o Projeto
Caso queira contribuir com melhorias ou correções para este projeto, siga os seguintes passos:
1. Faça um fork do repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Faça commit das suas alterações (`git commit -m 'Melhoria na análise financeira'`).
4. Faça push para a branch (`git push origin minha-modificacao`).
5. Abra um Pull Request para análise.

Sinta-se à vontade para sugerir melhorias!
