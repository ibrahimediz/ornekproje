import psycopg2
conn = psycopg2.connect(
    database="yemeksepeti",
    user="postgres",
    password="123456", 
    host="localhost",
    port="5432")
cur = conn.cursor()