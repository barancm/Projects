def girilen_bilgiler(lise_ogrenci_say, lise_ogrenci_ort,sinif_ortalama,sinif_ogr_sayi):#burada 3 tane parametre alıp işlemleri gerçekleştirdim
    ogrenci_var_mi = "e"   
    while (ogrenci_var_mi == "e" or ogrenci_var_mi == "E"):#e harfine bastığı sürece bu while içine girmeye devam edecek
    
        ogrenci_sinif = int(input("ogrencinin sinifini giriniz:"))
        while(ogrenci_sinif > 5 or ogrenci_sinif < 1):#öğrencinin sınıfı 1 ile 4 arasında olmadığı sürece sormaya devam edecek
            ogrenci_sinif = int(input("hatali giris tekrar giriniz:"))
        ogrenci_not_ortalamasi = int(input("ogrenci not ortalamasini giriniz:"))
        while(ogrenci_not_ortalamasi > 101 or ogrenci_not_ortalamasi <= 0):#öğrencinin not ortalaması 0 ile 100 arasında olmadığı sürece sormaya devam edecek
            ogrenci_not_ortalamasi = int(input("hatali giris tekrar giriniz:"))
        ogrenci_mezun_lise_adi = input("ogrenci lisesini giriniz:")

        if ogrenci_mezun_lise_adi in lise_ogrenci_say:
            lise_ogrenci_say[ogrenci_mezun_lise_adi]+=1#sözlük içinde o lise adından önce girilmişse onu bir arttırıyorum tekrardan
        else:
            lise_ogrenci_say[ogrenci_mezun_lise_adi]=1#sözlük içinde eğer o lise adından yoksa oluşturup 1 atıyorum.

        if ogrenci_mezun_lise_adi in lise_ogrenci_ort:
            lise_ogrenci_ort[ogrenci_mezun_lise_adi]+=ogrenci_not_ortalamasi#diğer sözlükte ise yine o liseden var ise o lisenin olduğu key'e genel not ortalamasını atıyorum ve hepsini girdikçe topluyorum
        else:
            lise_ogrenci_ort[ogrenci_mezun_lise_adi]=ogrenci_not_ortalamasi#burada yine eğer o liseden ilk defa giriliyorsa tanımlıyorum ve o girilen öğrenci not ortalamasını atıyorum.

        ogrenci_var_mi = input("baska ogrenci var mi?(e, h)")  

        for o in range(1,5):#burada sözlüğümüz 4 tane sınıf olduğu için 4 kere dönecek
            if ogrenci_sinif == o:
                o = str(o)
                sinif_ortalama[o][10]+=1#burada hangi sınıftan kaç tane öğrenci olduğunu tutuyorum
                sinif_ortalama["tum_siniflar"][10]+=1#burada toplam öğrenci sayısını tutuyorum.
                if ogrenci_not_ortalamasi>=0 and ogrenci_not_ortalamasi<=10:#burada ortalaması 0 ile 10 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][0]+=ogrenci_not_ortalamasi#listelerin ilk indislerinde not ortalamaları 0 ile 10 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][0]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=11 and ogrenci_not_ortalamasi<=20:#burada ortalaması 11 ile 20 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][1]+=ogrenci_not_ortalamasi#listelerin ikinci indislerinde not ortalamaları 11 ile 20 olan öğrencilerin not ortalamalarını tuttum 
                    sinif_ortalama["tum_siniflar"][1]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=21 and ogrenci_not_ortalamasi<=30:#burada ortalaması 21 ile 30 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][2]+=ogrenci_not_ortalamasi#listelerin üçüncü indislerinde not ortalamaları 21 ile 30 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][2]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=31 and ogrenci_not_ortalamasi<=40:#burada ortalaması 31 ile 40 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][3]+=ogrenci_not_ortalamasi#listelerin dördüncü indislerinde not ortalamaları 31 ile 40 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][3]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=41 and ogrenci_not_ortalamasi<=50:#burada ortalaması 41 ile 50 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][4]+=ogrenci_not_ortalamasi#listelerin beşinci indislerinde not ortalamaları 41 ile 50 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][4]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=51 and ogrenci_not_ortalamasi<=60:#burada ortalaması 51 ile 60 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][5]+=ogrenci_not_ortalamasi#listelerin altıncı indislerinde not ortalamaları 51 ile 60 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][5]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=61 and ogrenci_not_ortalamasi<=70:#burada ortalaması 61 ile 70 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][6]+=ogrenci_not_ortalamasi#listelerin yedinci indislerinde not ortalamaları 61 ile 70 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][6]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=71 and ogrenci_not_ortalamasi<=80:#burada ortalaması 71 ile 80 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][7]+=ogrenci_not_ortalamasi#listelerin sekizinci indislerinde not ortalamaları 71 ile 80 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][7]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=81 and ogrenci_not_ortalamasi<=90:#burada ortalaması 81 ile 90 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][8]+=ogrenci_not_ortalamasi#listelerin dokuzuncu indislerinde not ortalamaları 81 ile 90 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][8]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=91 and ogrenci_not_ortalamasi<=100:#burada ortalaması 91 ile 100 arasında olan öğrencilerin girmesini sağladım
                    sinif_ortalama[o][9]+=ogrenci_not_ortalamasi#listelerin onuncu indislerinde not ortalamaları 91 ile 100 olan öğrencilerin not ortalamalarını tuttum
                    sinif_ortalama["tum_siniflar"][9]+=ogrenci_not_ortalamasi#buralarda ise tüm sınıfların hepsini tutabilmek için ayrı bir listede tüm bölümdekileri bir listede tuttum.

        for o in range(1,5):#bu for'da ise ortalamalarını bulmak için bir sozluk olusturdum ve ortalamalarını tuttum
            if ogrenci_sinif == o:
                o = str(o)
                if ogrenci_not_ortalamasi>=0 and ogrenci_not_ortalamasi<=10:
                    sinif_ogr_sayi[o][0]+=1
                    sinif_ogr_sayi["tum_siniflar"][0]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=11 and ogrenci_not_ortalamasi<=20:
                    sinif_ogr_sayi[o][1]+=1
                    sinif_ogr_sayi["tum_siniflar"][1]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=21 and ogrenci_not_ortalamasi<=30:
                    sinif_ogr_sayi[o][2]+=1
                    sinif_ogr_sayi["tum_siniflar"][2]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=31 and ogrenci_not_ortalamasi<=40:
                    sinif_ogr_sayi[o][3]+=1
                    sinif_ogr_sayi["tum_siniflar"][3]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=41 and ogrenci_not_ortalamasi<=50:
                    sinif_ogr_sayi[o][4]+=1
                    sinif_ogr_sayi["tum_siniflar"][4]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=51 and ogrenci_not_ortalamasi<=60:
                    sinif_ogr_sayi[o][5]+=1
                    sinif_ogr_sayi["tum_siniflar"][5]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=61 and ogrenci_not_ortalamasi<=70:
                    sinif_ogr_sayi[o][6]+=1
                    sinif_ogr_sayi["tum_siniflar"][6]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=71 and ogrenci_not_ortalamasi<=80:
                    sinif_ogr_sayi[o][7]+=1
                    sinif_ogr_sayi["tum_siniflar"][7]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=81 and ogrenci_not_ortalamasi<=90:
                    sinif_ogr_sayi[o][8]+=1
                    sinif_ogr_sayi["tum_siniflar"][8]+=ogrenci_not_ortalamasi
                elif ogrenci_not_ortalamasi>=91 and ogrenci_not_ortalamasi<=100:
                    sinif_ogr_sayi[o][9]+=1
                    sinif_ogr_sayi["tum_siniflar"][9]+=ogrenci_not_ortalamasi  

def yazdir(lise_ogrenci_say,lise_ogrenci_ort,sinif_ortalama,sinif_ogr_sayi):#bu fonksiyonda ise istenilen bütün printleri yazdırdım
    print("Mezun Olunan Lise Adı                  Bölümdeki Öğrenci Say                     Not Ortalamaları")
    print("--------------------------------       ---------------------                     ----------------")

    for lise_adi in lise_ogrenci_say:
        print(lise_adi,((47-len(lise_adi))*" "),lise_ogrenci_say[lise_adi],(36*" "),lise_ogrenci_ort[lise_adi]/lise_ogrenci_say[lise_adi])
        
    print("Bolumumuzdeki her siniftaki ogrencilerin sayilari ve 10 puanlik genel not ortalamasi araliklarina gore dagilimlari:")

    print("Sınıflar      0-10%      11-20%      21-30%      31-40%      41-50%      51-60%      61-70%      71-80%      81-90%      91-100%      Öğrenci Say")
    print("--------      -----      ------      ------      ------      ------      ------      ------      ------      ------      -------      -----------")

    for j in sinif_ortalama:

        if j == "tum_siniflar":
            print(j,"   ", end="")
        else:
            print(j,".Sınıf        ", end="")

        for k in range(0,len(sinif_ortalama[j])):
            if k == 10:
                print(sinif_ortalama[j][k], end="")
                print("           ", end="")

            else:
                try:
                    print(sinif_ortalama[j][k] / sinif_ogr_sayi[j][k], end="")
                    print("           ", end="")
                except ZeroDivisionError:
                    print("0", end="")
                    print("           ", end="")
                      
        print("")

def main():
    sinif_ortalama = {'1': [0,0,0,0,0,0,0,0,0,0,0], '2': [0,0,0,0,0,0,0,0,0,0,0],'3': [0,0,0,0,0,0,0,0,0,0,0],'4': [0,0,0,0,0,0,0,0,0,0,0], 'tum_siniflar': [0,0,0,0,0,0,0,0,0,0,0]}
    sinif_ogr_sayi = {'1': [0,0,0,0,0,0,0,0,0,0], '2': [0,0,0,0,0,0,0,0,0,0],'3': [0,0,0,0,0,0,0,0,0,0],'4': [0,0,0,0,0,0,0,0,0,0], 'tum_siniflar': [0,0,0,0,0,0,0,0,0,0]}

    lise_ogrenci_say={}
    lise_ogrenci_ort={}
    girilen_bilgiler(lise_ogrenci_say,lise_ogrenci_ort, sinif_ortalama,sinif_ogr_sayi)
    yazdir(lise_ogrenci_say,lise_ogrenci_ort, sinif_ortalama,sinif_ogr_sayi)
    
main()