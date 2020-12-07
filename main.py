import matplotlib.pyplot as plt
import psycopg2 as ps

con = ps.connect(
  database="postgres",
  user="postgres",
  password="1029384756Qq",
  host="db-education.craxflbg8nli.us-east-1.rds.amazonaws.com",
  port="5432"
)
cur = con.cursor()
cur.execute("SELECT transaction_num, timecode from logs")
rows = cur.fetchall()
array_x = []
array_y = []
for row in rows:
    array_x.append(row[0])
    array_y.append(row[1])
plt.title("output analyze")
plt.xlabel("transaction number")
plt.ylabel("milliseconds")
plt.scatter(array_x, array_y)
plt.show()
