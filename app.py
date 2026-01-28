import os
import pymysql
from flask import Flask, jsonify, Response

app = Flask(__name__)

def get_conn():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST", "mysql.luzbipolar.com.br"),
        user=os.getenv("MYSQL_USER", "luzbipolar"),
        password=os.getenv("MYSQL_PASSWORD", "Ahps161951"),
        database=os.getenv("MYSQL_DATABASE", "luzbipolar"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=10,
        read_timeout=30,
        write_timeout=30,
    )

@app.get("/")
def health():
    return "OK - car api"

@app.get("/makes")
def get_all_makes():
    sql = "SELECT make_name FROM car_make ORDER BY make_name ASC"
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return Response(
            f"ERRO_DB: {type(e).__name__}",
            status=500,
            mimetype="text/plain; charset=utf-8"
        )
