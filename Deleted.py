import pyodbc

try:

    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\GR21\Students1.accdb;'
    conn = pyodbc.connect(con_string)
    #print("Connected To Database")
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Студ WHERE код = ?', (13))
    conn.commit()
    print("Data Deleted")

except pyodbc.Error as e:
    print("Error in Connection&quot", e)
