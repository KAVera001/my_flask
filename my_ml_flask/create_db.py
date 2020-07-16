from sqlalchemy import create_engine
import pandas as pd


product_df = pd.read_csv('product.csv')


engine = create_engine('sqlite:////Users/Vera/Documents/my_ml_flask/appdata.sqlite')
engine.execute('DROP TABLE IF EXISTS session_views;')

engine.execute('DROP TABLE IF EXISTS categories;')

engine.execute('''
CREATE TABLE session_views (
    session_id  TEXT NOT NULL ,
    sequence_order INTEGER NOT NULL,
    category_a TEXT NOT NULL ,
    category_b TEXT NOT NULL ,
    category_c TEXT NOT NULL ,
    category_d TEXT NOT NULL 
    
); ''')
for row in product_df.values:
    engine.execute(''' INSERT OR IGNORE INTO session_views(session_id , sequence_order,
       category_a, category_b, category_c, category_d) VALUES ( ?,?,?,?,?,? )''', tuple(row))


engine.execute('''
    CREATE TABLE categories AS   
SELECT session_id 
,COUNT(distinct category_a) AS category_A 
,COUNT(distinct category_b) AS category_B 
,COUNT(distinct category_c) AS category_C 
,COUNT(distinct category_d) AS category_D 
FROM session_views 
GROUP BY session_id;
''')
    


    

