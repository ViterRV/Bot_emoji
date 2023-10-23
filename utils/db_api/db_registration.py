import sqlite3 as sq

db = sq.connect('db.db')
cur = db.cursor()

async def register_db():
    cur.execute('''CREATE TABLE if not EXISTS registration(
    id INTEGER PRIMARY KEY,
    first_name text,
    last_name text,
    user_id INTEGER)
    ''')

async def create_profile_registration(state,user_id):
    async with state.proxy() as register:
        cur.execute("INSERT INTO registration (first_name,last_name,user_id) VALUES(?,?,?)",
                    (register['first_name'],register['last_name'],user_id))
        db.commit()

async def read_db_registration(user_id):
    cur.execute(
        "SELECT * FROM registration WHERE user_id = ?", (user_id,)
    )
    data = cur.fetchall()
    if data:
        return True
    else:
        return False