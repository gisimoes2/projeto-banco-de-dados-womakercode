import sqlite3
conexao = sqlite3.connect('banco') #conexão do arquivo python com o banco de dados o nome do arquivo e depois 
cursor = conexao.cursor()
# Questão 1 
cursor.execute('CREATE TABLE aluno(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(10));')
# Questão 2
cursor.execute('INSERT INTO aluno(id,nome,idade,curso) VALUES(1,"Giovanna",23,"Sistema de informação");')
cursor.execute('INSERT INTO aluno(id,nome,idade,curso) VALUES(2,"Gabriella",18,"medicina");')
cursor.execute('INSERT INTO aluno(id,nome,idade,curso) VALUES(3,"Anna julia",56,"engenharia");')
cursor.execute('INSERT INTO aluno(id,nome,idade,curso) VALUES(4,"Severino",65,"economia");')
cursor.execute('INSERT INTO aluno(id,nome,idade,curso) VALUES(5,"Paulo",22,"ed.fisica");')
# Questão 3, a)
dados = cursor.execute('SELECT * FROM alunos')
for alunos in dados: 
    print(alunos)
    
# Questão 3, b)
dados1= cursor.execute('SELECT nome,idade FROM alunos WHERE idade>20 ')
for alunos in dados1:
    print(alunos)
    
# Questão 3, c)
# dados2= cursor.execute('SELECT curso = 'Engenharia' FROM alunos ORDER BY nome')

# Questão 3, d)
dados3 = cursor.execute('SELECT id FROM alunos')
for alunos in dados3:
    print(alunos)
    
#Questão 4 
cursor.execute('UPDATE aluno SET idade = 22 WHERE nome = "Giovanna"')
#Questão 4, b) 
cursor.execute('DELETE FROM alunos where id=1')

#Questão 5 
cursor.execute('CREATE TABLE clientes(id (PRIMARY KEY), nome VARCHAR(100), idade INT, saldo FLOAT);')

cursor.execute('INSERT INTO  clientes(id,nome,idade,saldo) VALUES(1,"Giovanna",23, 5000000);')
cursor.execute('INSERT INTO  clientes(id,nome,idade,saldo) VALUES(2,"Gabriella",18, 100000);')
cursor.execute('INSERT INTO  clientes(id,nome,idade,saldo) VALUES(3,"Severino",65, 1000000);')
cursor.execute('INSERT INTO  clientes(id,nome,idade,saldo) VALUES(4,"Anna Julia",55, 1000000);')
cursor.execute('INSERT INTO  clientes(id,nome,idade,saldo) VALUES(5,"Paulo",22, 10000000);')
#Questão 6, a)
cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30 ')
quantid =cursor.execute('SELECT id FROM clientes')
for clientes in quantid: 
    print(clientes)
dados4= cursor.execute('SELECT nome,saldo FROM clientes')


#Questão 7, a)
cursor.execute('UPDATE clientes SET saldo= 10000000000 WHERE id= 2')
#Questão 7, b) 
cursor.execute('DELETE FROM clientes WHERE saldo id=1')



#Questão 8 
#trabalhar com informações agrupadas de duas tabales 
#Crie uma segunda tabela chamada "compras" com os campos: id
# (chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). Insira algumas
# compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra
cursor.execute('CREATE TABLE compras(id PK, cliente_id FK, produto VARCHAR(100), valor CURRENCY);')
cursor.execute('INSERT INTO  compras(id,cliente_id,produto,valor) VALUES(1,3,"arroz", 6);')

dados5 = cursor.execute(' SELECT nome,produto FROM clientes INNER JOIN compras ON id.clientes = cliente_id.compras ') #retornas apenas as linhas que tem correspondencias em todas as tabelas 



conexao.commit()
conexao.close