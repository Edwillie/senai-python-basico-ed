import sqlite3 as sql

localbd = sql.connect('bd_teste.db')
lcursor = localbd.cursor()