# Aula 08 - Banco de dados

Para exemplificar o uso de banco de dados com o python, usaremos o software SQLite. O qual usaremos a biblioteca sqlite3.

De forma complementar e de apoio visual, usaremos o SQLite Studio, facilitando a visualização e manipulação do banco de dados.

Para criar uma tabela usamos um comando como o abaixo
```SQL
CREATE TABLE tb_clientes (
    Nome      TEXT (255),
    Telefone  TEXT (14),
    Documento TEXT (14)  PRIMARY KEY
                         UNIQUE
);
```
Um banco de dados é composto por comandos classificados como:
* DDL - Para Criar / Excluir / Modificar tabelas
* DML - Para Criar / Excluir / Modificar dados nas tabelas existentes