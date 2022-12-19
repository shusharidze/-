import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\GR21\Students1.accdb;'
    conn = pyodbc.connect(con_string)
    #print("Connected To Database")

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Студ')

    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error in Connection&quot", e)
