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

    query = "SELECT * FROM tb_integrasi"
    cur_bank.execute(query)
    integrasi = cur_bank.fetchall()

    # update
    if (transaksi != integrasi):
        for data_transaksi in transaksi:
            for data_integrasi in integrasi:
                if (data_transaksi[0] == data_integrasi[0]):
                    if (data_transaksi != data_integrasi):
                        if (data_transaksi[0] == data_integrasi[0]):
                            print("Update id %s" % (data_transaksi[0]))
                            
                            data = (data_transaksi[6], data_transaksi[1])
                            data_kode = (data_transaksi[6], data_transaksi[1], data_transaksi[2])

                            query = "UPDATE tb_integrasi SET status = %s where id_transaksi = %s AND kode_toko = %s"
                            cur_bank.execute(query, data_kode)
                            
                            if (data_transaksi[2] == config.KODE_TOKO):
                                query = helper.query_update_toko_builder('tb_integrasi')
                                cur_toko.execute(query, data)
                                
                                query = helper.query_update_toko_builder('tb_transaksi')
                                cur_toko.execute(query, data)

    conn_toko.commit()
    conn_bank.commit()

    time.sleep(config.DELAY2)