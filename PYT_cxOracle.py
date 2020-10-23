import pandas as pd
import cx_Oracle

######################################################
# variables
host = 'db-ip-address'
port = 8888 # your db port
server = 'db-sid'
user = 'db-username'
password = 'db-pwd'
######################################################
# funtion : change pandas Dataframe to list
def df_to_lst(DF):
    DF = pd.DataFrame(DF)
    return DF.values.tolist()
######################################################

# oracle encoding problem "hangeul(korean)"
# if utf-8, use ".AL32UTF8"
# if CP949, use ".KO16MSWIN949"
os.environ["NLS_LANG"] = ".AL32UTF8"


# cx_Oracle connect
dsn = cx_Oracle.makedsn(host, port, sid)
conn = cx_Oracle.connect(user, password, dsn)
cur = conn.cursor()

# select query
query = 'SELECT * FROM Table'
DF_SRC = pd.read_sql(sql=query,con=conn)

# delete query
query = 'DELETE * FROM Table'
cur.execute(query)
conn.commit()

# insert query
query = 'INSERT * INTO Table'
RST_LST = df_to_lst(DF_RST)
cur.executemany(query, RST_LST)
conn.commit()

# disconnect
conn.close()
######################################################
