import pandas as pd
import pymssql

######################################################
# variables
server = 'server-address'
database = 'server-sid'
user = 'db-username'
password = 'db-pwd'
######################################################
# funtion : change pandas Dataframe to list
def df_to_lst(DF):
    DF = pd.DataFrame(DF)
    return DF.values.tolist()
######################################################

# encoding problem "hangeul(korean)"
# if utf-8, use ".AL32UTF8"
# if CP949, use ".KO16MSWIN949"
os.environ["NLS_LANG"] = ".AL32UTF8"

# mssql connect
cnn =  pymssql.connect(server, username, password, database)
cursor = cnn.cursor()

# select query
query = 'SELECT * FROM Table'
DF_SRC = pd.read_sql(sql=query,con=cnn)

# delete query
query = 'DELETE * FROM Table'
cur.execute(query)
cnn.commit()

# insert query
query = 'INSERT * INTO Table'
RST_LST = df_to_lst(DF_RST)
cur.executemany(query, RST_LST)
cnn.commit()

# disconnect
conn.close()
######################################################
