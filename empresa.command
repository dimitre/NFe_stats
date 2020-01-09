## Direto da linha de comando:

sqlite3 ./nfe_tudo.sqlite "SELECT count(*) as NUM, cnpj, razao  FROM NFe GROUP BY cnpj ORDER BY NUM DESC;"

sqlite3 ./nfe_tudo.sqlite "SELECT count(*) as NUM, cnpj, razao  FROM NFe GROUP BY cnpj ORDER BY NUM DESC;" -separator $'\t'

#sqlite3 ./nfe_tudo.sqlite "select strftime('%m-%Y',datahora) as 'month-year', SUM(valor) * 0.06 as total  from NFe WHERE datahora LIKE '%2016%' group by strftime('%m-%Y',datahora);"

#sqlite3 ./nfe_tudo.sqlite "select strftime('%m-%Y',datahora) as 'month-year', SUM(valor) * 0.06 as total  from NFe WHERE datahora LIKE '%2015%' group by strftime('%m-%Y',datahora);"

#sqlite3 ./nfe_tudo.sqlite "select strftime('%m-%Y',datahora) as 'month-year', SUM(valor) * 0.06 as total  from NFe WHERE datahora LIKE '%2014%' group by strftime('%m-%Y',datahora);"

#sqlite3 ./nfe_tudo.sqlite "select strftime('%m-%Y',datahora) as 'month-year', SUM(valor) * 0.055 as total  from NFe WHERE datahora LIKE '%2007%' group by strftime('%m-%Y',datahora);"

#sqlite3 ./nfe_tudo.sqlite "select strftime('%m-%Y',datahora) as 'month-year', SUM(valor) * 0.055 as total  from NFe WHERE datahora LIKE '%2006%' group by strftime('%m-%Y',datahora);"

#sqlite3 ./nfe_tudo.sqlite "select strftime('%m-%Y',datahora) as 'month-year', SUM(valor) * 0.055 as total  from NFe WHERE datahora LIKE '%2005%' group by strftime('%m-%Y',datahora);"