# Aula 03

## Laços - Introdução
Laços são utilizados para repetir um bloco de comandos.
Uma repetição, também pode ser chamado de "I"teração.
Essa repetição, por ser normalmente controlada de forma numérica, também pode ser chamado de "I"ndice

Consequentemente e curiosamente, todo laço ao ser controlado por uma variavel, utiliza a variavel nomeada como "i"
Onde esse "i" representa o indice ou iteração atual do laço.

## Laços - Comandos
- For: Utilizado com laços controlados por quantidade de iterações / indices.
```python
for i in range(10):
    print(i)
```

- While: Utilizado com laços controlados por condicionais
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