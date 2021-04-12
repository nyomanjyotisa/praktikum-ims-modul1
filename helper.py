import pymysql

def connect_db(db_config):
    return pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['pass'],
        db=db_config['db_name']
    )

def query_insert_bank_builder(tb_name):
    sql = "INSERT INTO " + tb_name
    sql += " (id_transaksi, kode_toko, rekening, tanggal, total, status) values(%s,%s,%s,%s,%s,%s)"
    return sql

def query_insert_toko_builder(tb_name):
    sql = "INSERT INTO " + tb_name
    sql += " (id_transaksi, rekening, tanggal, total, status) values(%s,%s,%s,%s,%s)"
    return sql

def query_delete_builder(tb_name):
    sql = "DELETE FROM " + tb_name
    sql += " WHERE id_transaksi = %s AND kode_toko = %s"
    return sql

def query_delete_toko_builder(tb_name):
    sql = "DELETE FROM " + tb_name
    sql += " WHERE id_transaksi = %s"
    return sql

def query_update_bank_builder(tb_name):
    sql = "UPDATE " + tb_name
    sql += " SET rekening = %s, tanggal = %s, total = %s where id_transaksi = %s AND kode_toko = %s"
    return sql

def query_update_toko_builder(tb_name):
    sql = "UPDATE " + tb_name
    sql += " SET status = %s where id_transaksi = %s"
    return sql