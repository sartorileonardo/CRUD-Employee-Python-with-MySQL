#!/usr/bin/python3

import pymysql

############# INICIO DAS FUNÇÕES ######################

#Function create Table for initialize system of step zero!
def createTable():
    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    
    # Create table as per requirement
    sqlCreateTable = """CREATE TABLE EMPLOYEE (
    ID INT NOT NULL AUTO_INCREMENT,
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,  
    SEX CHAR(1),
    INCOME FLOAT,
    PRIMARY KEY(ID))"""

    # Execute the SQL command
    cursor.execute(sqlCreateTable)
    # Commit your changes in the database
    db.commit()
    return "Tabela Employee criada com sucesso!\n"

#Function insert record
def insert():
    fname = input("Digite o nome:\n")
    lname = input("Digite o sobrenome:\n")
    age = input("Digite a idade:\n")
    age = int(age)
    sex = input("Digite o sexo (M/F):\n")
    income = input("Digite a renda:\n")
    income = float(income)

    if validation(fname, lname, age, sex, income):
        # Prepare SQL query to INSERT a record into the database.
        sqlInsert = """INSERT INTO EMPLOYEE(FIRST_NAME,
        LAST_NAME, AGE, SEX, INCOME)
        VALUES ('%s','%s', '%d', '%c', '%.2d')""" % (fname, lname, age, sex, income)

        # Execute the SQL command
        cursor.execute(sqlInsert)
        # Commit your changes in the database
        db.commit()

        return print("Salvo com sucesso!\n")
    else:
        print("Você digitou dados inválidos!")
        opc = 0

#Function list all records of employee
def selectAll():
    sqlSelectAll = "SELECT ID, FIRST_NAME, LAST_NAME, AGE, SEX, INCOME FROM EMPLOYEE"

    # Execute the SQL command
    cursor.execute(sqlSelectAll)

    print("Lista de empregados cadastrados:\n")

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
      id = row[0]
      fname = row[1]
      lname = row[2]
      age = row[3]
      sex = row[4]
      income = row[5]
      # Now print fetched result
      print ("id = %d,fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
             (id, fname, lname, age, sex, income ))

def selectById(id):
    # Prepare SQL query to SELECT all records of EMPLOYEE table when ID = ?.
    selectById = "SELECT * FROM EMPLOYEE WHERE id = '%d'" % (id)

    # Execute the SQL command
    cursor.execute(selectById)

    # Fetch all the rows in a list of lists.
    results = cursor.fetcone()

    if results == null:
        print("Não há ninguém cadastrado com esse ID!")
    
    for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      return print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % 
             (fname, lname, age, sex, income ))

#Function change an record
def update():
    id = input("Digite o id do usuário para alterar o cadastro:\n")
    id = int(id)

    fname = input("Digite o nome:\n")
    lname = input("Digite o sobrenome:\n")
    age = input("Digite a idade:\n")
    age = int(age)
    sex = input("Digite o sexo (M/F):\n")
    income = input("Digite a renda:\n")
    income = float(income)

    if validation(fname, lname, age, sex, income):
        # Prepare SQL query to UPDATE a record into the database.
        sqlInsert = """UPDATE EMPLOYEE SET FIRST_NAME = '%s',
        LAST_NAME = '%s', AGE = '%d', SEX = '%c', INCOME = '%.2d'
        WHERE ID = '%d'""" % (fname, lname, age, sex, income, id)

        # Execute the SQL command
        cursor.execute(sqlInsert)
        # Commit your changes in the database
        db.commit()

        return print("Alterado com sucesso!\n")
    else:
        print("Você digitou dados inválidos!")
        opc = 0

#Function remove record
def delete():
    id = input("Digite o id do usuário para remove-lo do sistema:\n")
    id = int(id)
    
    # Prepare SQL query to DELETE a record when ID = ?
    sqlDelete = """DELETE FROM EMPLOYEE WHERE ID = '%d'""" % (id)

    # Execute the SQL command
    cursor.execute(sqlDelete)
    # Commit your changes in the database
    db.commit()

    return print("Removido com sucesso!")

#Function validate entry of data
def validation(fname, lname, age, sex, income):

    if not fname | len(fname) == 0 | fname in ('0,1,2,3,4,5,6,7,8,9'):
        print("O campo [nome] está vazio ou possui valores núméricos/invlálidos!")
        return False
    elif not lname | len(lname) == 0 | lname in ('0,1,2,3,4,5,6,7,8,9'):
        print("O campo [sobrenome] está vazio ou possui valores núméricos/invlálidos!")
        return False
    elif not age | age <= 0 | age < 150:
        print("O campo [idade] está vazio ou com valor inválido!")
        return False
    elif not sex:
        print("O campo [sexo] é obrigatório!")
    elif sex != 'M' | sex != 'F':
        print("Valor inválido no campo sexo, o campo só aceita M ou F!")
        return False
    elif sex in ('0,1,2,3,4,5,6,7,8,9'):
        print("Valor inválido no campo sexo, o campo só aceita M ou F!")
        return False
    elif not income:
        print("O campo [renda] é obrigatório!")
        return False
    elif income <= 0:
        print("O campo [renda] só permite valores maiores do que 0!")
        return False
    else:
        return True
    

#Function to continue or stop
def proceed(confirm):
    if confirm == "y":
        opc = 0
    else:
        opc = 5

############# FIM DAS FUNÇÕES ######################

# Open database connection
db = pymysql.connect("localhost","root","root","EMPLOYEE_DB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


print("\n------------- Menu do Sistema de Controle de Funcionários ------------\n");
opc = int(0)

try:

    #Function create Table
    #Function for initialize system of step zero!
    #createTable()

    while opc != 5:
        opc = input("Escolha apenas 1 das opções:\n1-Cadastro de novo funcionário \n2-Listar funcionários cadastrados \n3-Alterar um funcionário cadastrado \n4-Remover um funcionario cadastrado \n5-Sair do sistema\n")
        opc = int(opc)
        
        if opc == 1:
            #Function insert record
            insert()

        elif opc == 2:
            #Function list all records of employee
            selectAll()

        elif opc == 3:
            #Function change an record
            update()
            selectAll()
        
        elif opc == 4:
            #Function remove record
            delete()
            selectAll()
                
        elif opc == 5:
            print("Você saiu do sistema...")

        else:
            print("\nOpção inválida!\n")
        
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
