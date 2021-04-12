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

    query = "SELECT * FROM tb_integrasi"
    cur_toko.execute(query)
    integrasi = cur_toko.fetchall()

    # insert
    for data_transaksi in transaksi:
        is_sync = 0
        for data_integrasi in integrasi:
            if (data_transaksi[0] == data_integrasi[0]):
                is_sync = 1
        if (is_sync == 0):
            print("Insert id %s" % (data_transaksi[0]))
            
            data = (data_transaksi)

            query = helper.query_insert_builder('tb_integrasi')
            cur_toko.execute(query, data)

            query = helper.query_insert_builder('tb_integrasi')
            cur_bank.execute(query, data)

            query = helper.query_insert_builder('tb_transaksi')
            cur_bank.execute(query, data)

    # delete
    for data_integrasi in integrasi:
        is_sync = 0
        for data_transaksi in transaksi:
            if (data_integrasi[0] == data_transaksi[0]):
                is_sync = 1
        if (is_sync == 0):
            print("Delete id %s" % (data_integrasi[0]))

            query = helper.query_delete_builder('tb_integrasi')
            cur_toko.execute(query, data_integrasi[0])

            query = helper.query_delete_builder('tb_integrasi')
            cur_bank.execute(query, data_integrasi[0])

            query = helper.query_delete_builder('tb_transaksi')
            cur_bank.execute(query, data_integrasi[0])

    # update
    if (transaksi != integrasi):
        for data_transaksi in transaksi:
            for data_integrasi in integrasi:
                if (data_transaksi[0] == data_integrasi[0]):
                    if (data_transaksi != data_integrasi):
                        print("Update id %s" % (data_transaksi[0]))
                        
                        data = (data_transaksi[1], data_transaksi[2], data_transaksi[3], data_transaksi[0])
                    
                        query = helper.query_update_bank_builder('tb_integrasi')
                        cur_toko.execute(query, data)

                        query = helper.query_update_bank_builder('tb_integrasi')
                        cur_bank.execute(query, data)
                        
                        query = helper.query_update_bank_builder('tb_transaksi')
                        cur_bank.execute(query, data)

    conn_toko.commit()
    conn_bank.commit()

    time.sleep(config.DELAY1)