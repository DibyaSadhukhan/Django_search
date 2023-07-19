import sqlite3
import pandas as pd
df=pd.read_csv('resturant_details.csv')
df1=pd.read_csv('Menu_details.csv')
df2=pd.read_csv('Menu_items.csv')
connection=sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
# cursor.execute("SELECT * from search_menu_resturant_details Limit 10")
# res=cursor.fetchall()
# print(res)
# print([desc[0] for desc in cursor.description])
df.to_sql('search_menu_resturant_details',connection,if_exists='replace')
df1.to_sql('search_menu_menu_details',connection,if_exists='replace')
df2.to_sql('search_menu_menu_items',connection,if_exists='replace')
connection.close()
