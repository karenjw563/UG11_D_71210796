w = input("Masukkan kata : ")
kata = len(w) 

def cetakHuruf():
    if len(w) % 2 == 0:
        print(f"Huruf paling ujung pada kata {kata} adalah",kata[-3:])
    else:
        print(f"Huruf paling ujung pada kata {kata} adalah",kata[:3])

cetakHuruf()
