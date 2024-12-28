# senai-python-basico-ed
Curso Senai de Python Básico

## Observações e apoio
Caso o virtualenv não funcione, aplique o comando abaixo
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Treino de digitação: site <a href="https://monkeytype.com/"> monkey type </a>

## Aula 01
- O que é linguagem de programação?
- Tipos de lp: Alto Nivel x Baixo Nivel (Linguagem de máquina)
- Formato de execução: Interpretado x Compilado
- O que é python? (Globo Reporter do Python: o que comem, como vivem...)
- Primeiro código no interpretador do python
- Segundo código no IDE do python
- Terceiro código no VSCode
    - Executando o código no VSCode
    - Limpando terminais
- Praticando emissão de mensagens (print)
    - Usando "\n" para quebra de linhas
    - Utilização de escapes "\" para tratamentos especiais.
    - Alternando entre aspas e apostrofes
    - Concatenadores (+ ou ,)
    - Categorias de valores
        - string: texto simples
        - integer: números sem decimais
        - float: números com decimais
        - boolean: verdadeiro (true) / falso (false)
    - Operadores
        - Matemáticos: +, -, * , /, //, % e **
        - Comparação: ==, !=, >, >=, <, <=
    - funções
        - sep
        - end
- Praticando os Operadores Matemáticos
- Variáveis
    - Boas Praticas: Não criar variáveis baseados em palavras reservadas
        - evitar: nomes baseados em tipos de dados ou nomes de funções, bibliotecas ou nome do arquivo python.
        - Pode ocasionar erro no interpretador. Ou invalidar metodos, por exemplo print.
    - Boas Praticas: Use padrões de nomenclatura, como camelcase. ex: nomeDaVariavel
- Solicitando dados do usuario (input)
    - Input sempre coleta dados em formato texto
- Colocando tudo junto: Usando format para criar mensagens combinadas: f"{Variavel} restante do texto"
- Conversão de tipos
    - int(): Convertendo para valor numérico inteiro
    - float(): Convertendo para valor numérico decimal
- Programinha de desafio da aula: Calculo da média.     



## Aula 02
- Revisão dos pontos da aula 1.
     ```python
    print('[Mensagem que será apresentada na tela]')
    var = input('[Mensagem para orientar o usuário sobre o valor esperado]')
    ```
- Condicionais (if - elif - else)
    - Operadores de comparação (revisão)
    ```python
    if [condição]:
        {Comandos que devem ser executados, se a condição é atendida}
    elif [condicao alternativa]:
        {Comandos que devem ser executados, se a condição ALTERNATIVA é atendida}
    else:
        {Comandos que devem ser executados, se a NENHUMA condição é atendida}        
    ```
- Função round()    
- Exercicio: Calculo do IMC
- Função type() - Identificando o tipo do valor
- Uso de comentários
    ```python
    # Comentário de linha (Use hash '#' para comentario em linha)
    '''
    Hoje o dia está lindo
    E sai para passear
    sai pelo mundo sem rumo
    (Use aspas triplas para comentario de blocos)
    '''
    # Voltando para o comentario em linha
    ```
    - Dica VSCode 1: CTRL + ';', comenta o bloco selecionado
    - Dica VSCode 2: F2 para selecionar e renomear a mesma variavel em vários lugares. Dê enter após editar o nome e aplicar em todos os lugares.
    - Dica VSCode 3: CTRL + SHIFT + 'L'. Mesmo que a dica 2. Porém, mais interativo.
- Operadores lógicos (AND / OR / NOT)

