# Aula 03

## Laços - Introdução
Laços são utilizados para repetir um bloco de comandos.
Uma repetição, também pode ser chamado de "I"teração.
Essa repetição, por ser normalmente controlada de forma numérica, também pode ser chamado de "I"ndice

Consequentemente e curiosamente, todo laço ao ser controlado por uma variavel, utiliza a variavel nomeada como "i"
Onde esse "i" representa o indice ou iteração atual do laço.

## Laços - Comandos
- **For**: Utilizado com laços controlados por quantidade de iterações / indices.
```python
for i in range(10):
    print(i)
```

- **While**: Utilizado com laços controlados por condicionais
```python
condicao = True
contador = 0

while condicao: #Executa enquanto a condição for verdadeira!
    print(f'Contador em {contador}')

    resp = input('Continuo contando (Sim / Não)? ')
    if resp.upper() == 'S' or resp.upper() == 'SIM':
        contador += 1
    else:
        condicao = False    
```

O fato do while ser basedo em condicional, ele pode usar um cenário alternativo

```python
condicao = True
contador = 0

while condicao: #Executa enquanto a condição for verdadeira!
    print(f'Contador em {contador}')

    resp = input('Continuo contando (Sim / Não)? ')
    if resp.upper() == 'S' or resp.upper() == 'SIM':
        contador += 1
    else:
        condicao = False 

else: #Note que este else é do WHILE!
    print(f'Seu último contador foi {contador}')          
```

- **break**: comando usado para interromper um laço. Podendo ser usado com FOR ou WHILE

>  _**OBS**: O uso de break, não executa o bloco de else do While._
```python
contador = 0

while True: #Executa enquanto a condição for verdadeira!
    print(f'Contador em {contador}')

    resp = input('Continuo contando (Sim / Não)? ')
    if resp.upper() == 'S' or resp.upper() == 'SIM':
        contador += 1
    else:
        break
```

## Bibliotecas
Você pode utilizar bibliotecas para "turbinar" o código.

Para isso, devemos usar o comando import. E com ele, indicar a biblioteca que queremos.
Depois de importada a biblioteca, podemos trabalhar com suas funções!

```python
import os       #biblioteca de interatividade com o sistema operacional
import time     #biblioteca com funções para trabalhar com tempo
import random   #biblioteca com funções para trabalhar com dados aleatórios
```

> _Recomenda-se que as importações de bibliotecas sejam feitas no inicio do programa._

> _**OBS** Não crie variaveis com os nomes das funções ou das bibliotecas. O programa pode travar_

```python
import os       #biblioteca de interatividade com o sistema operacional
import time     #biblioteca com funções para trabalhar com tempo
import random   #biblioteca com funções para trabalhar com dados aleatórios

os.system('cls')    #limpa a tela
time.sleep(5)       #faz o programa pausar por 5 segundos
valor = random.randint(1,10) #gera um numero aleatório entre 1 e 10
```