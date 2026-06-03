### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 50
preco = -30

if quantidade > 0 and preco > 0:
    print('Dados válidos')
else:
    print('Dados inválidos')


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = int(input('Digite o dado coletado pelo sensor: '))

if temperatura >= 100:
    print('Alta')
elif temperatura >= 40:
    print('Normal')
else:
    print('Baixa')


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

for registro in log.values():
    if registro == 'ERROR':
        print('Houve um erro')
    else:
        pass


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

email_usuario = input('Digite o email do usuário: ')
idade_usuario = int(input('Digite a idade do usuário: '))
verificar_email = email_usuario.split('@')   

if idade_usuario < 18:
    print('Erro: Idade deve ser maior ou igual a 18 anos.')
elif idade_usuario > 65:
    print('Erro: Idade deve ser menor ou igual a 65 anos.')
elif len(verificar_email) == 2 and verificar_email[1].count('.') > 0:
    print('Dados de usuário válidos')
else:
    print('Erro: dados inválidos.')

    

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 1200, 'hora': 10}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print('Transação suspeita')
else:
    print('Transação normal')  




### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "dados dados análise análise ciência ciência ciência"
quebra_texto = texto.split()
contagem_palavras = {}

for palavra in quebra_texto:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.



### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numero = (4,6,2,7,8,2,8,446,646,689,563,578,34)
numero_par = []

for par in numero:
    if par % 2 == 0:
        numero_par.append(par)  
    else:
        pass

print(numero_par)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    entrada = input('Digite uma palavra (ou "sair" para encerrar): ')
    if entrada.strip().lower() == 'sair':
        print('Programa encerrado.')
        break

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True:
    if True:
        numero = int(input('Digite um número entre 1 e 10: '))
        if 1 <= numero <= 10:
            print(f'Número {numero} é válido.')
            break
        else:
            print('Número inválido. Tente novamente.')
    

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parada = int(input('Digite um número para indicar a parada (entre 1 e 10):'))

while True:
    for i in lista:
        if parada == i:
            print('Você selecionou o número da parada!')
            exit()