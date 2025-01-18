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