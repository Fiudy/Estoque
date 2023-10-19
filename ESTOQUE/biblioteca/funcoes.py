import sqlite3 as sql

def incluir():
    conn = sql.connect("manutencao.db")
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE equipa IF NOT EXISTS (
                        codigo INTEGER  PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        categoria INTEGER
                    )
                """)

def excluir():
    pass


def alterar():
    pass


def relGeral():
    pass


def relEsp():
    pass

