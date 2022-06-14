import pyodbc

server = 'tcp:gamesucht.database.windows.net,1433'
database = 'gamesucht'
username = 'slr'
password = '#h:!~8maB;)@H#[*'
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:gamesucht.database.windows.net,1433;Database=gamesucht;Uid=slr;Pwd={#h:!~8maB;)@H#[*};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

def getUmfrage(Name):
    cursor.execute("Select * from Umfragen;")
    row = cursor.fetchone()
    return(row[2])