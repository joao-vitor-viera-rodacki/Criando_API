import sqlite3 as sq



def cadastraUsuatio(nome, idade, email):
    
    banco = sq.connect('database.db')
    cursor = banco.cursor()
    cursor.execute(f'INSERT INTO pessoas VALUES("{nome}","{idade}","{email}")')

    banco.commit() 
    print(cursor.fetchall())
    return {'id' : 1,'nome': nome,'idade': idade,'email' : email}

'''
def criar_database():

    banco = sq.connect('database.db')
    cursor = banco.cursor()
    cursor.execute('CREATE TABLE pessoas (nome text , idade integer , email text)')
'''

banco = sq.connect('database.db')
cursor = banco.cursor()
cursor.execute('SELECT * FROM pessoas')
print(cursor.fetchall())