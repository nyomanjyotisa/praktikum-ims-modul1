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
    cur_toko.execute(query)
    transaksi = cur_toko.fetchall()

    query = "SELECT * FROM tb_history"
    cur_toko.execute(query)
    integrasi = cur_toko.fetchall()

    query = "SELECT * FROM tb_integrasi"
    cur_toko.execute(query)
    integrasi2 = cur_toko.fetchall()

    # insert
    for data_transaksi in transaksi:
        is_sync = 0
        for data_integrasi in integrasi:
            if (data_transaksi[0] == data_integrasi[1]):
                is_sync = 1
        if (is_sync == 0):
            print("Insert id %s to history" % (data_transaksi[0]))
            
            data = (data_transaksi[0], config.KODE_TOKO, data_transaksi[1], data_transaksi[2], data_transaksi[3], data_transaksi[4])

            query = "INSERT INTO tb_history (`id_transaksi`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,'insert', NOW())"
            cur_toko.execute(query, data_transaksi)

            query = "INSERT INTO tb_history (`id_transaksi`, `kode_toko`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,%s,'insert', NOW())"
            cur_bank.execute(query, data)

    # delete
    for data_integrasi in integrasi:
        is_sync = 0
        for data_transaksi in transaksi:
            if (data_integrasi[1] == data_transaksi[0]):
                is_sync = 1

        query = "SELECT id_transaksi, action FROM tb_history WHERE id_transaksi = %s"
        cur_toko.execute(query, data_integrasi[1])
        actions = cur_toko.fetchall()
        
        for action in actions:
            if (action[1] == 'delete'):
                is_sync = 1
        
        if (is_sync == 0):
            print("Delete id %s  to history" % (data_integrasi[1]))

            data = (data_transaksi[0], config.KODE_TOKO, data_transaksi[1], data_transaksi[2], data_transaksi[3], data_transaksi[4])

            query = "INSERT INTO tb_history (`id_transaksi`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,'delete', NOW())"
            cur_toko.execute(query, data_transaksi)

            query = "INSERT INTO tb_history (`id_transaksi`, `kode_toko`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,%s,'delete', NOW())"
            cur_bank.execute(query, data)

    # update
    for data_transaksi in transaksi:
        query = "SELECT * FROM tb_history WHERE id_transaksi = %s ORDER BY id_history DESC LIMIT 1"
        cur_toko.execute(query, data_transaksi[0])
        history = cur_toko.fetchall()
        for data_history in history:
            if ((data_transaksi[1] != data_history[2]) or (data_transaksi[2] != data_history[3]) or (data_transaksi[3] != data_history[4])):
                print("Update id %s  to history" % (data_transaksi[0]))

                data = (data_transaksi[0], config.KODE_TOKO, data_transaksi[1], data_transaksi[2], data_transaksi[3], data_transaksi[4])
                
                query = "INSERT INTO tb_history (`id_transaksi`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,'update', NOW())"
                cur_toko.execute(query, data_transaksi)

                query = "INSERT INTO tb_history (`id_transaksi`, `kode_toko`, `rekening`, `tanggal`, `total`, `status`, `action`, `created_at`) VALUES (%s,%s,%s,%s,%s,%s,'update', NOW())"
                cur_bank.execute(query, data)
    
    for data_integrasi in reversed(integrasi):
        print(data_integrasi[0])
        if (data_integrasi[6] == 'update'):
            is_sync = 0
            for data_transaksi in transaksi:
                if ((data_integrasi[1] == data_transaksi[0]) and (data_integrasi[5] == data_transaksi[4])):
                    is_sync = 1
        
            if (is_sync == 0):
                print("update id %s" % (data_integrasi[1]))
                data = (data_integrasi[5], data_integrasi[1])
                query = "UPDATE tb_transaksi SET status = %s where id_transaksi = %s"
                cur_toko.execute(query, data)

    conn_toko.commit()
    conn_bank.commit()

    time.sleep(config.DELAY1)