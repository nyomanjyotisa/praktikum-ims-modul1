import time
import helper
import config

print("Start Engine")
while (1):
    conn_toko = helper.connect_db(config.DB_TOKO)
    conn_bank = helper.connect_db(config.DB_BANK)
    cur_toko = conn_toko.cursor()
    cur_bank = conn_bank.cursor()

    query = "SELECT * FROM tb_transaksi"
    cur_bank.execute(query)
    transaksi = cur_bank.fetchall()

    query = "SELECT * FROM tb_history"
    cur_bank.execute(query)
    integrasi = cur_bank.fetchall()

    for data_transaksi in transaksi:
        query = "SELECT * FROM tb_history WHERE id_transaksi = %s ORDER BY id_history DESC LIMIT 1"
        cur_bank.execute(query, data_transaksi[1])
        history = cur_bank.fetchall()

        for data_history in history:
            if (data_transaksi[6] != data_history[6]):
                print("Update id %s" % (data_transaksi[0]))
                
                data = (data_transaksi[1], data_transaksi[3], data_transaksi[4], data_transaksi[5], data_transaksi[6])
                data_kode = (data_transaksi[1], data_transaksi[2], data_transaksi[3], data_transaksi[4], data_transaksi[5], data_transaksi[6])
                
                query = "INSERT INTO tb_history (`id_transaksi`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,'update', NOW())"
                cur_toko.execute(query, data)

                query = "INSERT INTO tb_history (`id_transaksi`, `kode_toko`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,%s,'update', NOW())"
                cur_bank.execute(query, data_kode)
    
    for data_integrasi in integrasi:
        if ((data_integrasi[7] == 'insert') and (data_integrasi[2] == config.KODE_TOKO)):
            is_sync = 0

            data_check = (data_integrasi[1], config.KODE_TOKO)
            query = "SELECT * FROM tb_history WHERE id_transaksi = %s AND kode_toko = %s AND action = 'delete'"
            cur_bank.execute(query, data_check)
            check = cur_bank.fetchall()

            if check:
                is_sync = 1

            for data_transaksi in transaksi:
                if ((data_integrasi[1] == data_transaksi[1]) and (data_integrasi[2] == data_transaksi[2])):
                    is_sync = 1
        
            if (is_sync == 0):
                print("Insert id %s toko %s" % (data_integrasi[1], config.KODE_TOKO))
                data = (data_integrasi[1], data_integrasi[2], data_integrasi[3], data_integrasi[4], data_integrasi[5], data_integrasi[6])
                query = "INSERT INTO tb_transaksi (id_transaksi, kode_toko, rekening, tanggal, total, status) values(%s,%s,%s,%s,%s,%s)"
                cur_bank.execute(query, data)
        
        elif ((data_integrasi[7] == 'delete') and (data_integrasi[2] == config.KODE_TOKO)):
            for data_transaksi in transaksi:
                if (data_integrasi[1] == data_transaksi[1]):
                    print("Delete id %s toko %s" % (data_integrasi[1], config.KODE_TOKO))
                    data = (data_integrasi[1], data_integrasi[2])
                    query = "DELETE FROM tb_transaksi WHERE id_transaksi = %s AND kode_toko = %s"
                    cur_bank.execute(query, data)


    conn_toko.commit()
    conn_bank.commit()

    time.sleep(config.DELAY2)