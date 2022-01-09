import psycopg2
from config import config

import psycopg2
from config import config

def insert_account():

    sql = f"""INSERT INTO public.accounts(
	id,username, password, email)
	VALUES (%s, %s, %s, %s) RETURNING id;"""
    
    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(1, 'admin', 'admin', ''))
        result = cur.fetchone()[0]
        print(result)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_account()