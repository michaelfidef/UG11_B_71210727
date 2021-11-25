def kata_sisip(kalimat_awal,kalimat_sisipan,index):
    proses = kalimat_awal[:index-1] + kalimat_sisipan + kalimat_awal[index-1:]
    print(proses)

kalimat_awal = input("Masukkan kalimat awal : ")
kalimat_sisipan = input("Masukkan kata untuk disisipkan : ")
index = int(input("Masukkan index : "))
kata_sisip(kalimat_awal,kalimat_sisipan,index)
