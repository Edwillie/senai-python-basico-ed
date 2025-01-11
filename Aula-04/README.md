# Aula 04

## Listas
Listas, é um tipo de variável que podem armazenar varios valores. São criadas por valores cercados pelos caracteres "[]".

Ex:
```python
nomes = ['José', 'Joaquim', 'Manoel']   #Lista de valores em string (texto)
idades = [25, 42, 36]                   #Lista de valores numéricos

combinadas = [['José', 'Joaquim', 'Manoel'], [25, 42, 36]] #Lista de Listas
```

Como visto na última linha do código acima, podemos ter uma lista de listas (combinado). Pelo fato da lista ser um tipo.

Agora que conhecemos um pouco sobre listas, podemos também concluir que o tipo string (texto) é uma lista de caracteres. Sendo assim:

```python
Palavra = "Ayrton Senna" #string com 12 caracteres. Pode contar ai!

print(Palavra[7:1]) #Lembre que as contagens começam de zero. Aqui vamos imprimir a letra "S"
```

### Funções importantes - Entendendo o conteúdo de uma lista

Para contar quantos elementos temos dentro de uma lista, podemos usar a função **_len()_**

```python
nomes = ['José', 'Joaquim', 'Manoel']   #Lista de valores em string (texto)
print(len(nomes))                       #Imprime 3 na tela. Referente a quantidade de elementos que temos na lista nomes.
```

Para saber qual indice (ou posição) está um valor na lista, usamos a função **_index()_**

```python
nomes = ['José', 'Joaquim', 'Manoel']   #Lista de valores em string (texto)
print(nomes.index('Manoel'))            #Imprime 2 na tela. Referente a posição da palavra Manoel está na sua lista.
```

Para saber quantas vezes um valor aparece na lista, usamos a função **_count()_**
```python
nomes = ['José', 'Joaquim', 'Manoel', 'Joaquim', 'Maria', 'Abreu']   #Lista de valores em string (texto)
print(nomes.count('Joaquim'))  #Imprime 2 na tela. Referente a quantidade de vezes que "Joaquim" está na lista
```

### Funções importantes - Inserindo valores em uma lista
Para incluir um valor na lista (mesmo que esteja vazia), usamos a função **_append()_**

```python
nomes = []   #Lista vazia!
print(nomes)  #Não imprime nada, porque a lista está vazia

nomes.append('Juca')
nomes.append('Senai')
print(nomes)  #Imprime as palavras Juca e Senai
```

Para inserir em uma posição especifica da lista, use a função **_insert()_**
> **OBS** Os demais elementos, serão movidos para a proxima posição na lista.

```python
nomes = ["Matheus", "Lucas", "Joaquim"]   
print(nomes)  #Imprime os nomes na lista
print(nomes.len()) #Mostra que temos 3 nomes

nomes.insert(2, 'Juca')
print(nomes)  #Imprime os nomes na lista. Agora com Juca, sendo ele, antes de Joaquim.
print(nomes.len()) #Mostra que temos 4 nomes
```

Para estender lista, com base em outras listas, use a função **_extend()_** ou até mesmo "some" as listas, usando o operador "+"

```python
nomes = ["Matheus", "Lucas", "Joaquim"] 
outrosNomes = ["Fulano", "Beltrano", "Deltrano"]   
print(nomes)  #Imprime os nomes na lista
print(nomes.len()) #Mostra que temos 3 nomes

print(outrosNomes)  #Imprime os nomes na lista
print(outrosNomes.len()) #Mostra que temos 3 nomes


nomes.extend(outrosNomes)
print(nomes)  #Imprime os nomes na lista e seus novos valores ao final
print(nomes.len()) #Mostra que temos 6 nomes

print(outrosNomes)  #Imprime os nomes na lista
print(outrosNomes.len()) #Mostra que ainda temos 3 nomes
```
### Funções importantes - Removendo Valores de uma lista

### Funções importantes - Outras formas de trabalhar uma lista