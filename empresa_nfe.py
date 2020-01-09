''' fazer tambem faturamento por mes
como no documento do banco do brasil
select sum(valor) FROM NFe where datahora like '%2012%'
SELECT *, valor * .06 AS imposto FROM NFe WHERE datahora > datetime("2013-02-01")

'''

import glob
import csv
import sqlite3
import re

imposto = 0.06

conn = sqlite3.connect('nfe.sqlite')
c = conn.cursor()

def drop():
    c.execute('''DROP TABLE IF EXISTS NFe'''); #file # IF EXISTS nfe.NFe
def init():    
    c.execute('''CREATE TABLE IF NOT EXISTS NFe (id INTEGER NOT NULL UNIQUE, datahora DATETIME, valor INTEGER, razao TEXT, cnpj TEXT)''')
def gather():
    dir = 'NFe'
    lista = glob.glob(dir+'/*.txt')
    contagem = 0
    for a in lista:
        #print a
        data = csv.reader(open(a, "rb"), delimiter='\t')
        fields = data.next()
        if contagem >0:
            for row in data:
                items = zip(fields, row)
                item = {}
                numero = row[1] #numero
                datahora = row[2] #hora e data
                if datahora:
                
                    data = row[2].split(' ')[0].split('/');
                    novadata = data[2]+'-'+data[1]+'-'+data[0]
                    hora = row[2].split(' ')[1]
                    datahora = novadata + ' ' + hora

                
                #formato certo
                #("YYYY-MM-DD HH:MM:SS.SSS").
                
                #formato atual
                #25/07/2011 14:19:34
                valor = re.sub("[^0-9]", "", row[26][:-3].strip("\."))
                #print fields
                #print row[37].decode('iso-8859-1').encode('utf-8')
                razao = row[37].decode('iso-8859-1').encode('utf-8') #razao social
                cnpj = row[34]
            
                sql = "INSERT OR IGNORE INTO NFe VALUES ('" + \
                str(numero)  + "','" + \
                str(datahora)  + "','" + \
                str(valor)  + "','" + \
                str(razao)  + "','" + \
                str(cnpj)  + "')"

                if row[0] != 'Total':
                    c.execute(sql)
        contagem +=1
def process():
    sql = 'SELECT SUM(valor) as soma, count(*) as vezes, razao, cnpj FROM NFe GROUP BY cnpj ORDER BY soma DESC'
    c.execute(sql)
    for row in c:
        print row
        
def process2():
    #sql = "SELECT * FROM NFe WHERE datahora LIKE '%/2011%'"
    sql = "SELECT * FROM NFe WHERE datahora LIKE '%/2012%'"
    c.execute(sql)
    soma = 0

    for row in c:
        print 'x'
        soma += row[2]
        print row[2]  
    #print soma * .935 - 7464
    print soma, 'xx'


def process3():
    print 'impostos devidos desde fev de 2013'
    sql = 'SELECT * FROM NFe WHERE datahora > datetime("2013-02-01")'
    c.execute(sql)
    soma = 0
    for row in c:
        soma += row[2]
        print row[2], row[2]* imposto,  row[3]
    print soma * imposto

def process3b():
    print 'impostos devidos desde fev de 2013 sem multa'
    sql = 'SELECT sum(valor) FROM NFe WHERE datahora > datetime("2013-02-01")'
    c.execute(sql)
    soma = 0
    for row in c:
        print row[0] * imposto

def somaano(ano):
    print 'soma do faturamento do ano: ' + str(ano);
    sql = "select sum(valor) FROM NFe where datahora like '"+ str(ano)+"%'"
    c.execute(sql)
    for row in c:
        print row[0];
        
def somaanosemimposto(ano):
    print 'soma do faturamento do ano sem imposto: ' + str(ano)
    sql = "select sum(valor) FROM NFe where datahora like '"+ str(ano)+"%'"
    c.execute(sql)
    for row in c:
#        print row[0] * 0.945;
        print row[0] * (1.0 - imposto);

def impostoano(ano):
    print 'imposto relativo ao ano: ' + str(ano)
    sql = "select sum(valor) FROM NFe where datahora like '"+ str(ano)+"%'"
    c.execute(sql)
    for row in c:
#    	print row
        print row[0] * imposto;

def process4b(mesano):
    #print 'faturamento do ano ' + mesano;
    sql = "select sum(valor) FROM NFe where datahora like '%"+(mesano)+"%'"
    #print sql;
    c.execute(sql)
    for row in c:
        print mesano, row[0];

def last():
    print 
    print 'ultima nota:'
    sql = 'SELECT * FROM NFe ORDER BY id DESC LIMIT 1'
    c.execute(sql)
    for row in c:
        print row


if 2==2:
    drop()
    init()
    gather()
    impostoano(2012)

#somaano(2014)
#somaanosemimposto(2014)

#impostoano(2012)
#process3b()
    
#process()
#process4(2014)

if 2==3:
    for mes in range (1, 13):
        process4b('2014-' + str(mes).zfill(2))

#process4b('2013-08')
#last()

conn.commit()
c.close()