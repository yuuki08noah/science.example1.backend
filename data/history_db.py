from data import get_db
from model.HistoryDeleteRequest import HistoryDeleteRequest
from model.HistoryRequest import HistoryRequest

conn, cur = get_db()

def get_history_by_id(history_id):
    sql = f"select * from history where history_id = {history_id}"
    cur.execute(sql)
    return cur.fetchone()

def get_histories():
    sql = "select * from history order by seen_at desc"
    cur.execute(sql)
    res = cur.fetchall()
    return res

def get_history_by_isotope_number(isotope_number):
    sql = f"select * from history where isotope_number = {isotope_number}"
    cur.execute(sql)
    return cur.fetchone()

def save(history: HistoryRequest):
    sql = f"insert into history(isotope_number) values({history.isotope_number})"
    cur.execute(sql)
    conn.commit()

def update(history: HistoryRequest):
    sql = f"update history set seen_at = now() where isotope_number = {history.isotope_number}"
    cur.execute(sql)
    conn.commit()

def delete(history: HistoryDeleteRequest):
    sql = f"delete from history where history_id = {history.history_id}"
    cur.execute(sql)
    conn.commit()