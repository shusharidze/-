import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\GR21\Students1.accdb;'
    conn = pyodbc.connect(con_string)
    #print("Connected To Database")

    cursor = conn.cursor()
    Студ = (

        (12, 'Шушарин', 'Сергей', 'Алексеевич',),
        (13, 'Сушков', 'Константин', 'Олегович'),
        (14, 'Антонов', 'Олег', 'Владимирович')
    )

    cursor.executemany('INSERT INTO Студ  VALUES (?,?,?,?)', Студ)
    conn.commit()
    print('Data Inserted')


except pyodbc.Error as e:
    print("Error in Connection&quot", e)
