import sqlite3
import _sqlite3


# connect() will try to open the specified file if not it will create a new file of that name
databasefile = sqlite3.connect("calculator.sqlite")
cur = databasefile.cursor()
# Creating a table named ModuloCalculator to store the values of x, a , p and the calculated result as columns
cur.execute('CREATE TABLE ModuloCalculator (xValue VARCHAR, aValue VARCHAR, pValue VARCHAR, AnswerValue VARCHAR )')

# Commit command saves the changes
databasefile.commit()
databasefile.close()
