import pymysql
import time
import socket
import urllib.request

while True:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while sock.connect_ex(('localhost', 3306)) != 0:
		print('Tidak dapat dilakukan koneksi ke database 1...')
		time.sleep(5)
	sock.close()

	try:
		urllib.request.urlopen('http://google.com')
		cek_internet = True
	except:
		cek_internet = False

	if cek_internet == True:
		db_bank = pymysql.connect(host="database1.c1bxfqu7h4ww.us-east-1.rds.amazonaws.com", user="admin", passwd="gungkrisna", db="db_sinkron1") 
		cursor_bank = db_bank.cursor() 

		db_belanja = pymysql.connect(host="database-2.cwnltbc7h1y5.ap-southeast-1.rds.amazonaws.com", user="admin", passwd="gungkrisna", db="db_sinkron2") 
		cursor_belanja = db_belanja.cursor() 

		select_belanja = """SELECT * FROM invoice;"""
		count_belanja = cursor_belanja.execute(select_belanja)

		select_bank = """SELECT * FROM invoice;"""
		count_bank = cursor_bank.execute(select_bank)

		result = cursor_belanja.fetchall()
		for row in result:
			Id = row[0]
			namaBarang = row[1]
			harga = row[2]
			jumlah = row[3]
			cek_bank = """SELECT * FROM invoice WHERE id = {}""".format(Id)
			count_existence = cursor_bank.execute(cek_bank)
			if(count_existence == 0):
				insert_invoice = """INSERT INTO invoice(id, nama_barang, harga, jumlah, pembayaran) VALUES({}, '{}', {}, {}, 'not paid')""".format(Id, namaBarang, harga, jumlah)
				cursor_bank.execute(insert_invoice)
				db_bank.commit()
				print("Insert new data to Bank")
			else:
				update_invoice = """UPDATE invoice SET nama_barang = '{}', harga = {}, jumlah = {} WHERE id = {}""".format(namaBarang, harga, jumlah, Id)
				cursor_bank.execute(update_invoice)
				db_bank.commit()

		cursor_bank.execute(select_bank)
		result_from_bank = cursor_bank.fetchall()
		for bar in result_from_bank:
			Id_from_bank = bar[0]
			namaBarang_from_bank = bar[1]
			harga_from_bank = bar[2]
			jumlah_from_bank = bar[3]
			pembayaran_from_bank = bar[4]
			cek_belanja = """SELECT * FROM invoice WHERE id = {}""".format(Id_from_bank)
			count_existence_in_belanja = cursor_belanja.execute(cek_belanja)
			if(count_existence_in_belanja == 0):
				delete_invoice = """DELETE FROM invoice WHERE id = {}""".format(Id_from_bank)
				cursor_bank.execute(delete_invoice)
				db_bank.commit()
				print("Delete data in Bank")
			else:
				cek_pembayaran_query = """SELECT pembayaran FROM invoice WHERE id = {}""".format(Id_from_bank)
				cursor_bank.execute(cek_pembayaran_query)
				result_pembayaran = cursor_bank.fetchall()
				for row_pembayaran in result_pembayaran:
					cek_pembayaran = row_pembayaran[0]
				if(cek_pembayaran == 'paid'):
					cek_pembayaran_in_belanja_query = """SELECT pembayaran FROM invoice WHERE id = {}""".format(Id_from_bank)
					cursor_belanja.execute(cek_pembayaran_in_belanja_query)
					result_pembayaran_in_belanja = cursor_belanja.fetchall()
					for row_pembayaran_in_belanja in result_pembayaran_in_belanja:
						cek_pembayaran_in_belanja = row_pembayaran_in_belanja[0]
					if(cek_pembayaran_in_belanja == 'not paid'):
						update_belanja_invoice = """UPDATE invoice SET pembayaran = 'paid' WHERE id = {}""".format(Id_from_bank)
						cursor_belanja.execute(update_belanja_invoice)
						db_belanja.commit()
						print("update pembayaran in Belanja")
				if(cek_pembayaran == 'not paid'):
					update_belanja_invoice = """UPDATE invoice SET pembayaran = 'not paid' WHERE id = {}""".format(Id_from_bank)
					cursor_belanja.execute(update_belanja_invoice)
					db_belanja.commit()

		print("Listening...")
		time.sleep(5)
	else:
		print('Tidak dapat dilakukan koneksi ke database 2...')
		time.sleep(5)
