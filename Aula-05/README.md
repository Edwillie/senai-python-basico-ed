# Aula 05

## Trabalhando com funções
Funções ou métodos, permitem que um trecho de código possa ser reaproveitado. Para chamadas recorrentes.

Esta segmentação do código, é uma boa pratica para deixar o código mais enxuto e de facil manutenção.

As funções podem ser dos tipos:
- Embutidas: Do próprio núcleo do Python. 
- Módulos: Importadas de outros produtores.
- Autoria Própria: Criadas internamente no código local, com o apoio do comamndo **_def_**

> As funções devem ser estar declaradas (criadas) antes de serem chamadas!

> Assim como as variaveis, evite as palavras reservadas. Como funções já existentes ou comandos.

Exemplo
```python
#Iniciando o programa
# ****** Declarando a função *****
def meuprint(texto):
    print(texto)

# ***** Rotina principal ****
minhamensagem = input('Qual mensagem você quer apresentar? ')
meuprint(minhamensagem)  # Chamando a função criada internamente.
```

## Dicionários e Tuplas
Dicionário é um tipo de dado composto no python. Composto por 2 elementos:
- Chave: Identificação (nomeação) de um valor
- Valor: Informação carregada.

Podemos dizer que um dicionário é um conjunto de variáveis.

Exemplo:
```python
# Antes de conhecermos dicionário:
Nome_Pessoa1 = 'José'
Idade_Pessoa1 = 25

Nome_Pessoa2 = 'Abreu'
Idade_Pessoa2 = 30

Nome_Pessoa3 = 'Carlos'
Idade_Pessoa3 = 17

# Depois de conhecermos dicionário:
Pessoa1 = {'Nome':'José', 'Idade': 25}
Pessoa2 = {'Nome':'Abreu', 'Idade': 30}
Pessoa3 = {'Nome':'Carlos', 'Idade': 17}
```