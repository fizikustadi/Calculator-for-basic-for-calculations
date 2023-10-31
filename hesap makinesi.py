def toplama(list):
    toplam = 0
    for num in list:
        toplam += int(num)
    print(toplam)

def cikarma(list):
    if len(list) == 2:
        sonuc = int(list[0]) - int(list[1])
        print(sonuc)
    else:
        print("Lütfen iki sayı girin.")

def carpma(list):
    carpim = 1
    for num in list:
        carpim *= int(num)
    print(carpim)

def bolme(list):
    if len(list) == 2 and int(list[1]) != 0:
        sonuc = int(list[0]) / int(list[1])
        print(sonuc)
    else:
        print("Lütfen iki sayı girin ve ikinci sayının 0 olmadığından emin olun.")

def islem():
    try:
        islemadi = int(input("Lütfen yapmak istediğiniz işlemi seçiniz\n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\nYapmak istediğiniz işlemin numarasını giriniz:"))
        if islemadi == 1:
            islemsayilari = []
            while True:
                islemsayisi = input("Lütfen işlem yapmak istediğiniz sayıları giriniz (Çıkmak istediğinizde q veya Q yazınız):")
                if islemsayisi.lower() == 'q':
                    break
                else:
                    islemsayilari.append(islemsayisi)
            if len(islemsayilari) >= 2:
                toplama(islemsayilari)
            else:
                print("Lütfen en az iki sayı girin.")
        elif islemadi == 2:
            islemsayilari = []
            for i in range(2):
                islemsayisi = input("Lütfen işlem yapmak istediğiniz sayıları giriniz :")
                if islemsayisi.lower() == 'q':
                    break
                else:
                    islemsayilari.append(islemsayisi)
            if len(islemsayilari) == 2:
                cikarma(islemsayilari)
            else:
                print("Lütfen iki sayı girin.")
        elif islemadi == 3:
            islemsayilari = []
            while True:
                islemsayisi = input("Lütfen işlem yapmak istediğiniz sayıları giriniz (Çıkmak istediğinizde q veya Q yazınız):")
                if islemsayisi.lower() == 'q':
                    break
                else:
                    islemsayilari.append(islemsayisi)
            if len(islemsayilari) >= 2:
                carpma(islemsayilari)
            else:
                print("Lütfen en az iki sayı girin.")
        elif islemadi == 4:
            islemsayilari = []
            for i in range(2):
                islemsayisi = input("Lütfen işlem yapmak istediğiniz sayıları giriniz :")
                if islemsayisi.lower() == 'q':
                    break
                else:
                    islemsayilari.append(islemsayisi)
            if int(islemsayilari[1]) != 0:
                bolme(islemsayilari)
            else:
                print("İkinci sayının 0 olmadığından emin olun.")
        else:
            print("Geçersiz işlem talebi")
    except ValueError:
        print("Lütfen sayı girişi yapınız")

while True:
    islem()
