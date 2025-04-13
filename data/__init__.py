import pymysql

conn = pymysql.connect(host="localhost", port=7777, user="root", password="1234",
                        db='isotope', charset="utf8", cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

create_db = '''
create table if not exists history (
    history_id int primary key auto_increment,
    isotope_number int not null,
    seen_at datetime default now()
)
'''

cur.execute(create_db)
conn.commit()

def get_db():
    return conn, cur