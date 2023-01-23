# import modul sys untuk mendapatkan jenis pengecualian
import sys
newList = ['n', "p", 6]
for data in newList:
    try:
        print("Hasilnya :", data)
        x = int(data)*int(data)
        break
    except:
        print("Maaf!", sys.exc_info()[0])
        print("Data selanjutnya.")
        print()
print("Pangkat 2 dari ", data, "adalah", x)
