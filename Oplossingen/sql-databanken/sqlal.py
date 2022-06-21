# sqlite database - bewerken: https://sqlitebrowser.org/

# via sqlalchemy (een ORM-oplossing die als generieke DB-connector kan gebruikt worden)
# https://www.sqlalchemy.org/
# Kijk eens hier: het sql-alchemy standaardwerk open en bloot op het internet ;-) https://github.com/princox/my-book-library/blob/master/Essential%2BSQLAlchemy%2C%2B2nd%2BEdition.pdf 
import sqlalchemy as sa
import time

conn = sa.create_engine('sqlite:///sqlalchemy.db')
# id, event, user_id, timestamp
insert_sql = "INSERT INTO logging (event, user_id, timestamp) VALUES (?, ?, ?)"
return_curs = conn.execute(insert_sql, "IP-adressen gescand", 1, time.time())
print(return_curs.lastrowid)

# alle records opvragen
select_sql = "SELECT * from logging"
return_curs = conn.execute(select_sql)
for row in return_curs:
    print(row)

# één record opvragen
select_sql = "SELECT * from logging where id = ?"
return_curs = conn.execute(select_sql, 30).one_or_none()
print(f"Record met id=30: {return_curs}")