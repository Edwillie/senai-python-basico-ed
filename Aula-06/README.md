# Aula 06

## Dicionários (Continuação)
Como visto anteriormente, um elemento do dicionário é composto por:
* Chave (Key)
* Valor (Value)

Um dicionário pode armazenar varios elementos. Assim como em uma lista, sendo conhecido como item.

Sendo, contudo, mais simples de operar do que uma lista. Pois pode ser acessado diretamente por sua chave:

```python
MyGroup = {
    'Arroz':5.37,
    'Feijão':4.83,
    'Açúcar': 6.76
    }

print(MyGroup['Feijão']) --Imprime na tela o valor 4,83 referente ao valor do item Feijão.    
```

### Trabalhando com dicionários
use o operador "_*in*_" para atuar sobre os elementos:
* key
* value
* items

Exemplo:
```python
MyGroup = {
    'Arroz':5.37,
    'Feijão':4.83,
    'Açúcar': 6.76
    }

valor_busca = 'Açúcar'

if valor_busca in MyGroup.keys():
    print(f'encontrado com o valor {MyGroup[valor_busca]}')
else:
    print(f'Desculpa, não encontrei {valor_busca} no dicionário')

# iterando entre os elementos do meu dicionário
for minha_chave, meu_valor in MyGroup.items():
    print(f'{minha_chave} = {meu_valor}')

```

## Controle de Erros (Exceptions)

Permite que você identifique que ocorreu um erro em um código.
Seu tratamento deve ser do mais específico para o mais genérico.

Exemplo:
```Python
valor = int(input('Digite um valor inteiro'))
```

No caso acima, caso seja informado um valor com decimais ou um texto, seu programa será encerrado com erro. Para controlar isso, podemos fazer:

Exemplo:
```Python
try:
    valor = int(input('Digite um valor inteiro'))
except:
    print('Não foi possivel converter o valor informado para um número inteiro')
```

Dentro do Try, você pode colocar um conjunto de códigos e qualquer problema poderá ser tratado.

Exemplo:
```Python
try:
    valor = int(input('Digite um valor inteiro'))
    valor2 = int(input('Digite outro valor inteiro'))
    valor3 = valor / valor2
    print(valor3)
except:
    print('Não foi possivel converter o valor informado para um número inteiro')
```
Ou seja, no exemplo acima, o usuario pode colocar um valor invalido para valor, valor2. E com isso, a mensagem será informada (e com uma mensagem coerente).

Agora, caso o usuario informe 3 em valor e 0 (zero) no valor2, receberemos a mesma mensagem. mas, o erro efetivamente foi outro.

Para evitar, podemos colocar excessões mais especificas. E devemos deixar o mais genérico (except) por ultimo.

Exemplo:
```Python
try:
    valor = int(input('Digite um valor inteiro'))
    valor2 = int(input('Digite outro valor inteiro'))
    valor3 = valor / valor2
    print(valor3)
except ValueError:    
    print('Não foi possivel converter o valor informado para um número inteiro')
except ZeroDivisionError:    
    print('Não foi possivel efetuar uma divisão por zero')    
except:
    print('Aconteceu um erro qualquer.')    
```
