import mysql.connector as MS
from flask import request

connection = MS.connect(user='dantoine', password='michel',
host='127.0.0.1', buffered=True, database="epytodo")
cursor = connection.cursor()

def bdd_login(username, password):
    req_connection_client = "SELECT * FROM user where username = %s AND password = %s "
    cursor.execute(req_connection_client, (username, password))
    resultat_connection_client = cursor.fetchall()
    return resultat_connection_client

def bdd_info(username):
    request_id_client = "SELECT user_id FROM user WHERE username = '%s'"
    cursor.execute(request_id_client % username)
    user_id = cursor.fetchone()
    requete_information_client = "SELECT user.user_id, user.username FROM user WHERE user.user_id = %s AND user.username = %s "
    cursor.execute(requete_information_client , (user_id[0], username))
    resultat_requete_information_client = cursor.fetchall()
    username = request.args.get('username')
    return resultat_requete_information_client

def bdd_register(username, password):
    try:
        sql = "INSERT INTO user (`username`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        connection.commit()
    finally:
        connection.close()
