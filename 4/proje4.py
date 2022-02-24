import string
import math
def inputal_ve_isle(LNo,yarismacilar): 
    yarismaci = list()
    oyuncuyok = False
    while(oyuncuyok == False):
        lisans = int(input("oyuncunun lisans numarasını giriniz(bitirmek için 0 ya da negatif sayı giriniz):"))
        alindi = False
        while (lisans > 0 and alindi == False):
            if lisans not in LNo:
                LNo.append(lisans)
                yarismaci.append(lisans)
                alindi = True
            else:
                lisans = int(input("oyuncunun lisans numarasını giriniz(bitirmek için 0 ya da negatif sayı giriniz):"))
        if lisans <= 0:
            oyuncuyok = True
        if oyuncuyok == False:
            ad_soyad = input("oyuncunun adını soyadını giriniz:")
            adsoyad = ""
            for i in ad_soyad:
                if i == "i":
                    i = "İ"
                else:
                    i = i.upper()
                adsoyad+=i
            yarismaci.append(adsoyad)
            elo = int(input("oyunucunun ELO'sunu giriniz(en az 1000, yoksa 0):"))
            while(elo < 1000 and elo != 0):
                elo = int(input("oyunucunun ELO'sunu giriniz(en az 1000, yoksa 0):"))
            yarismaci.append(elo)
            ukd = int(input("oyuncunun UKD'sini giriniz(en az 1000, yoksa 0):"))
            while(ukd < 1000 and ukd != 0):
                ukd = int(input("oyuncunun UKD'sini giriniz(en az 1000, yoksa 0):"))
            yarismaci.append(ukd)
            yarismaci.append(0)
            listekopya = yarismaci.copy()
            yarismacilar.append(listekopya)
            yarismaci.clear()
    return yarismacilar
    
def siralama(yarismacilar):
    yarismacilar.sort(key=lambda yarismaci:yarismaci[0], reverse = False)
    yarismacilar.sort(key=alfabe, reverse = False)
    yarismacilar.sort(key=lambda yarismaci:yarismaci[3], reverse = True)
    yarismacilar.sort(key=lambda yarismaci:yarismaci[2], reverse = True)
    yarismacilar.sort(key=lambda yarismaci:yarismaci[4], reverse = True)
    

    return yarismacilar

def listeleri_olustur(rakipleri,renk,oynanmayan,yarismacilar,maclar,LNo):
    for i in range(len(yarismacilar)):
        yarismacilar[i].append(i+1)
    for i in range(len(yarismacilar)):
        oyuncurenk = [0,0,0,0,0,"yok",yarismacilar[i][0]]
        renk.append(oyuncurenk)
        oynanmamıs = list()
        rakipler = list()
        rakipleri.append(rakipler)
        oynanmayan.append(oynanmamıs)
        mac = list()
        maclar.append(mac)
        LNo[i] = yarismacilar[i][0]


def liste_siralama(yarismacilar,renk,oynanmayan,maclar,rakipleri,LNo):
    for i in range(len(yarismacilar)):
        for j in range(len(yarismacilar)):
            if(yarismacilar[i][0] == renk[j][6]):
                lno_tut = renk[i]
                renk[i] = renk[j]
                renk[j] = lno_tut

                lno_tut = maclar[i]
                maclar[i] = maclar[j]
                maclar[j] = lno_tut

                lno_tut = oynanmayan[i]
                oynanmayan[i] = oynanmayan[j]
                oynanmayan[j] = lno_tut

                lno_tut = rakipleri[i]
                rakipleri[i] = rakipleri[j]
                rakipleri[j] = lno_tut

                lno_tut = LNo[i]
                LNo[i] = LNo[j]
                LNo[j] = lno_tut
                

def sonuclar(tursayisi,masa,maclar,oynanmayan,yarismacilar,renk,LNo):
    for i in range(len(yarismacilar)//2):
        sonuc = int(input("{0}.turda {1}.masada oynanan macin sonucunu giriniz (0-5): ".format(tursayisi,i+1)))
        while(sonuc < 0 or sonuc > 5):
            sonuc = int(input("{0}.turda {1}.masada oynanan macin sonucunu giriniz (0-5): ".format(tursayisi,i+1)))

        beyaz = LNo.index(masa[i][1])
        siyah = LNo.index(masa[i][4])
    
        if(sonuc == 0):
            yarismacilar[beyaz][4]+=0.5
            yarismacilar[siyah][4]+=0.5
            maclar[beyaz].append([yarismacilar[siyah][5],renk[beyaz][5],sonuc,yarismacilar[siyah][0]])
            maclar[siyah].append([yarismacilar[beyaz][5],renk[siyah][5],sonuc,yarismacilar[beyaz][0]])
        elif(sonuc == 1):
            yarismacilar[beyaz][4]+=1
            yarismacilar[siyah][4]+=0
            maclar[beyaz].append([yarismacilar[siyah][5],renk[beyaz][5],sonuc,yarismacilar[siyah][0]])
            maclar[siyah].append([yarismacilar[beyaz][5],renk[siyah][5],sonuc,yarismacilar[beyaz][0]])
        elif(sonuc == 2):
            yarismacilar[beyaz][4]+=0
            yarismacilar[siyah][4]+=1
            maclar[beyaz].append([yarismacilar[siyah][5],renk[beyaz][5],sonuc,yarismacilar[siyah][0]])
            maclar[siyah].append([yarismacilar[beyaz][5],renk[siyah][5],sonuc,yarismacilar[beyaz][0]])
        elif(sonuc == 3):
            oynanmayan[beyaz].append([tursayisi,yarismacilar[beyaz][4],renk[beyaz][5],sonuc])
            oynanmayan[siyah].append([tursayisi,yarismacilar[siyah][4],renk[siyah][5],sonuc])
            yarismacilar[beyaz][4]+=1
            renk[beyaz][4] = 1
            yarismacilar[siyah][4]+=0
            maclar[beyaz].append([yarismacilar[siyah][5],renk[beyaz][5],sonuc,yarismacilar[siyah][0]])
            maclar[siyah].append([yarismacilar[beyaz][5],renk[siyah][5],sonuc,yarismacilar[beyaz][0]])
        elif(sonuc == 4):
            oynanmayan[beyaz].append([tursayisi,yarismacilar[beyaz][4],renk[beyaz][5],sonuc])
            oynanmayan[siyah].append([tursayisi,yarismacilar[siyah][4],renk[siyah][5],sonuc])
            yarismacilar[beyaz][4]+=0
            renk[siyah][4] = 1
            yarismacilar[siyah][4]+=1
            maclar[beyaz].append([yarismacilar[siyah][5],renk[beyaz][5],sonuc,yarismacilar[siyah][0]])
            maclar[siyah].append([yarismacilar[beyaz][5],renk[siyah][5],sonuc,yarismacilar[beyaz][0]])
        else:#sonuc 5 ise
            oynanmayan[beyaz].append([tursayisi,yarismacilar[beyaz][4],renk[beyaz][5],sonuc])
            oynanmayan[siyah].append([tursayisi,yarismacilar[siyah][4],renk[siyah][5],sonuc])
            yarismacilar[beyaz][4]+=0
            yarismacilar[siyah][4]+=0
            maclar[beyaz].append([yarismacilar[siyah][5],renk[beyaz][5],sonuc,yarismacilar[siyah][0]])
            maclar[siyah].append([yarismacilar[beyaz][5],renk[siyah][5],sonuc,yarismacilar[beyaz][0]])
   
    if(len(yarismacilar) %2 == 1):
        bay = LNo.index(masa[len(yarismacilar)//2][1])
        oynanmayan[bay].append([tursayisi,yarismacilar[bay][4],"yok",6])#6 bay demek       
        yarismacilar[bay][4]+=1 
        maclar[bay].append([-1,"-",6,-1])#-1 bsno ve lno yok çünkü bay 
       
               
def alfabe(yarismacilar):
    harfler = ' aAbBcCçÇdDeEfFgGğĞhHıIiİjJkKlLmMnNoOöÖpPrRsSşŞtTuUüÜvVyYzZ'
    cevrim = dict()
    for i in harfler:
        indis = harfler.index(i)
        cevrim[i] = indis
        
    return [cevrim.get(yarismacilar[1][i]) for i in range(len(yarismacilar[1]))]


def baslangic_yazdir(yarismacilar):
    print("BSNo   LNo     Ad-Soyad  ELO  UKD")
    print("---- ----- ------------ ---- ----")
    for i in range(len(yarismacilar)):
        print(format(yarismacilar[i][5],'4d'),end=" ")
        print(format(yarismacilar[i][0],'5d'),end=" ")
        print(format(yarismacilar[i][1],'12s'),end=" ")
        print(format(yarismacilar[i][2],'4d'),end=" ")
        print(format(yarismacilar[i][3],'4d'),end="\n")    

def bay(yarismacilar,renk):
    baygecen = 0
    baygecenbsno = 0  
    bay = list()
    bulundu = False
    azaltıcı = len(yarismacilar) - 1
    while(azaltıcı >= 0 and bulundu == False):
        if renk[azaltıcı][4] != 1:
            baygecen = yarismacilar[azaltıcı][0]
            baygecenbsno = yarismacilar[azaltıcı][5]
            renk[azaltıcı][4] = 1
            bulundu = True
            bay.append(baygecen)
            bay.append(baygecenbsno)
            bay.append(yarismacilar[azaltıcı][4])
        else:
            azaltıcı-=1
    return bay

def bh1_2_hesaplama(yarismacilar,LNo,maclar,oynanmayan,sayitur):
    for i in range(len(LNo)):
        puans = list()
        var = False
        for j in range(len(maclar[i])):
            if(maclar[i][j][2] == 0 or maclar[i][j][2] == 1 or maclar[i][j][2] == 2):
                index = LNo.index(maclar[i][j][3])
                puans.append(yarismacilar[index][4])
            else:
                var = True     

        if(var == True):
            for k in range(len(oynanmayan[i])):
                puan = (sayitur - oynanmayan[i][k][0])*0.5+ oynanmayan[i][k][1]
                puans.append(puan)
        enkucuk = len(yarismacilar)*1 #bütün oyuncularla oynayıp kazanması imkansız en fazla oyuncu sayısı -1 kadar maç olabilir.
        for a in range(len(puans)):
            if(enkucuk > puans[a]):
                enkucuk = puans[a]
        toplam = sum(puans)-enkucuk
        yarismacilar[i].append(toplam) 
       
        puans.remove(enkucuk)

        enkucuk2 = len(yarismacilar)*1 #bütün oyuncularla oynayıp kazanması imkansız en fazla oyuncu sayısı -1 kadar maç olabilir.
        for a in range(len(puans)):
            if(enkucuk2 > puans[a]):
                enkucuk2 = puans[a]

        toplam2 = sum(puans)-enkucuk2
        yarismacilar[i].append(toplam2)

def sb_hesaplama(yarismacilar,LNo,maclar,oynanmayan,sayitur):
    for i in range(len(LNo)):
        puans = list()
        var = False
        for j in range(len(maclar[i])):
            if(maclar[i][j][2] == 0):
                index = LNo.index(maclar[i][j][3])
                puans.append(yarismacilar[index][4] / 2)
            elif(maclar[i][j][2] == 1 and maclar[i][j][1] == "b"):
                index = LNo.index(maclar[i][j][3])
                puans.append(yarismacilar[index][4])
            elif(maclar[i][j][2] == 2 and maclar[i][j][1] == "s"):
                index = LNo.index(maclar[i][j][3])
                puans.append(yarismacilar[index][4])
            else:
                var = True
        if(var == True):
            for k in range(len(oynanmayan[i])):
                if(oynanmayan[i][k][3] == 3 and oynanmayan[i][k][2] == "b"):
                    puan = (sayitur - oynanmayan[i][k][0])*0.5+ oynanmayan[i][k][1]
                    puans.append(puan)
                elif(oynanmayan[i][k][3] == 4 and oynanmayan[i][k][2] == "s"):
                    puan = (sayitur - oynanmayan[i][k][0])*0.5+ oynanmayan[i][k][1]
                    puans.append(puan)
                elif(oynanmayan[i][k][3] == 6 ):
                    puan = (sayitur - oynanmayan[i][k][0])*0.5+ oynanmayan[i][k][1]
                    puans.append(puan)
                
        yarismacilar[i].append(sum(puans)) 

def galibiyet_sayisi(yarismacilar,LNo,maclar,oynanmayan,sayitur):
    for i in range(len(LNo)):
        galibiyet = 0
        for j in range(len(maclar[i])):
            if(maclar[i][j][2] == 1 and maclar[i][j][1] == "b"):
                galibiyet+=1
            elif(maclar[i][j][2] == 2 and maclar[i][j][1] == "s"):
                galibiyet+=1
            elif(maclar[i][j][2] == 3 and maclar[i][j][1] == "b"):
                galibiyet+=1
            elif(maclar[i][j][2] == 4 and maclar[i][j][1] == "s"):
                galibiyet+=1
        yarismacilar[i].append(galibiyet)

def nihaisiralama(yarismacilar):
    yarismacilar.sort(key=lambda yarismaci:yarismaci[9], reverse = True)
    yarismacilar.sort(key=lambda yarismaci:yarismaci[8], reverse = True)
    yarismacilar.sort(key=lambda yarismaci:yarismaci[7], reverse = True)
    yarismacilar.sort(key=lambda yarismaci:yarismaci[6], reverse = True)
    yarismacilar.sort(key=lambda yarismaci:yarismaci[4], reverse = True)

    for i in range(len(yarismacilar)):
        yarismacilar[i].append(i+1)

def nihaiyazdirma(yarismacilar):
    print("Nihai Sıralama Listesi:")
    print("SNo BSNo   LNo Ad-Soyad      ELO  UKD Puan  BH-1  BH-2    SB GS")
    print("--- ---- ----- ------------ ---- ---- ---- ----- ----- ----- --")

    for i in range(len(yarismacilar)):
        print(format(yarismacilar[i][10],"3d"),end=" ")
        print(format(yarismacilar[i][5],"4d"),end=" ")
        print(format(yarismacilar[i][0],"5d"),end=" ")
        print(format(yarismacilar[i][1],"12s"),end=" ")
        print(format(yarismacilar[i][2],"4d"),end=" ")
        print(format(yarismacilar[i][3],"4d"),end=" ")
        print(format(yarismacilar[i][4],"4.2f"),end=" ")
        print(format(yarismacilar[i][6],"5.2f"),end=" ")
        print(format(yarismacilar[i][7],"5.2f"),end=" ")
        print(format(yarismacilar[i][8],"5.2f"),end=" ")
        print(format(yarismacilar[i][9],"2d"),end="\n")


def capraztablo(yarismacilar,maclar,renk,oynanmayan,rakipleri,LNo):
    yarismacilar.sort(key=lambda x : x[5], reverse = False)
    
    liste_siralama(yarismacilar,renk,oynanmayan,maclar,rakipleri,LNo)

    print("Çapraz Tablo:")
    print("BSNo SNo LNo       Ad-Soyad ELO  UKD",end="  ")
    for i in range(len(maclar[0])):
        print("{}. tur".format(i+1),end="  ")
    
    print("Puan  BH-1  BH-2    SB GS")
    print("---- --- ----- ------------ ---- ----",end=" ")
    for j in range(len(maclar[0])):
        print("-------",end=" ")
    print("---- ----- ----- ----- --")

    for k in range(len(yarismacilar)):
        print(format(yarismacilar[k][5],"4d"),end=" ")
        print(format(yarismacilar[k][10],"3d"),end=" ")
        print(format(yarismacilar[k][0],"5d"),end=" ")
        print(format(yarismacilar[k][1],"12s"),end=" ")
        print(format(yarismacilar[k][2],"4d"),end=" ")
        print(format(yarismacilar[k][3],"4d"),end=" ")
        for i in range(len(maclar[k])):
            if(maclar[k][i][2] == 0):
                rakipbsno = str(maclar[k][i][0])
                sonuc = "½"
            elif(maclar[k][i][2] == 1):
                if(maclar[k][i][1] == "b"):
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "1"
                else:
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "0"
            elif(maclar[k][i][2] == 2):
                if(maclar[k][i][1] == "b"):
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "0"
                else:
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "1"
            elif(maclar[k][i][2] == 3):
                if(maclar[k][i][1] == "b"):
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "+"
                else:
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "-"
            elif(maclar[k][i][2] == 4):
                if(maclar[k][i][1] == "b"):
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "-"
                else:
                    rakipbsno = str(maclar[k][i][0])
                    sonuc = "+"
            elif(maclar[k][i][2] == 5):   
                rakipbsno = str(maclar[k][i][0])
                sonuc = "-"
            elif(maclar[k][i][2] == 6):
                rakipbsno = "-"
                sonuc = "1"
            print(end="  ")
            print(rakipbsno,end=" ")
            print(maclar[k][i][1],end=" ")
            print(sonuc,end=" ")
        print(format(yarismacilar[k][4],"4.2f"),end=" ")
        print(format(yarismacilar[k][6],"5.2f"),end=" ")
        print(format(yarismacilar[k][7],"5.2f"),end=" ")
        print(format(yarismacilar[k][8],"5.2f"),end=" ")
        print(format(yarismacilar[k][9],"2d"),end="\n")


def eslestirme(yarismacilar,renk,maclar,oynanmayan,tursayisi,renkler,rakipleri):
    rakibivar = list()
    masalar = list()
    if(len(yarismacilar) %2 == 1):
        gecenbay = bay(yarismacilar,renk)
    rakiparanan = 0
    bitir = False
    while(rakiparanan < len(yarismacilar) and bitir == False):
        sayac = rakiparanan
        bulundu = False
        esitpuanli = 0 
        asilrakiparanan = rakiparanan
        while(sayac < len(yarismacilar) and bulundu == False and yarismacilar[asilrakiparanan][0] not in rakibivar and yarismacilar[asilrakiparanan][0] != gecenbay[0]):
            if(yarismacilar[rakiparanan][4] == yarismacilar[sayac][4]):
                esitpuanli+=1
                sayac+=1
                if(sayac == len(yarismacilar)):
                    bulundu = True
            elif(esitpuanli == 1):
                rakiparanan +=1              
                esitpuanli = 0
            else:
                bulundu = True
            if(bulundu == True):
                eslestirilmek = renk_koyma(sayac,yarismacilar,asilrakiparanan,esitpuanli,renk,renkler,tursayisi,rakibivar,gecenbay[0],rakipleri)
                if(eslestirilmek[0] == False):
                    rakiparanan = sayac
                    esitpuanli = 0
                    bulundu = False
                    
                else:
                    masa = list()
                    if(renk[asilrakiparanan][5] == "s"):
                        masa.append(yarismacilar[eslestirilmek[1]][5])
                        masa.append(yarismacilar[eslestirilmek[1]][0])
                        masa.append(yarismacilar[eslestirilmek[1]][4])
                        masa.append(yarismacilar[asilrakiparanan][4])
                        masa.append(yarismacilar[asilrakiparanan][0])
                        masa.append(yarismacilar[asilrakiparanan][5])
                    else:
                        masa.append(yarismacilar[asilrakiparanan][5])
                        masa.append(yarismacilar[asilrakiparanan][0])
                        masa.append(yarismacilar[asilrakiparanan][4])
                        masa.append(yarismacilar[eslestirilmek[1]][4])
                        masa.append(yarismacilar[eslestirilmek[1]][0])
                        masa.append(yarismacilar[eslestirilmek[1]][5])
                    masalar.append(masa)
                    if(len(yarismacilar) %2 == 1 and len(yarismacilar)//2 == len(masalar)):
                        masa = list()
                        masa.append(gecenbay[1])
                        masa.append(gecenbay[0])
                        masa.append(gecenbay[2])
                        bitir = True
                        masalar.append(masa)
                    elif(len(yarismacilar) %2 == 0 and len(yarismacilar)//2 == len(masalar)):
                        bitir = True
        rakiparanan = asilrakiparanan                
        rakiparanan += 1
    return masalar

                                                  
def renk_koyma(sayac,yarismacilar,rakiparanan,esitpuanli,renk,renkler,tursayisi,rakibivar,gecenbay,rakipleri):
    
    if(renkler == "b"):
        digerrenk = "s"
    else:
        digerrenk = "b"      
    
    enkücükbeyaz = len(yarismacilar)#hiçbir yarışmacı oyuncu sayısı kadar taş alamaz.
    enkücüksiyah = len(yarismacilar)

    for i in range(len(yarismacilar)):
        if(enkücükbeyaz > renk[i][2]):
            enkücükbeyaz = renk[i][2]

    for i in range(len(yarismacilar)):
        if(enkücüksiyah > renk[i][3]):
            enkücüksiyah = renk[i][3]   

    if(renk[rakiparanan][5] == "b" and renk[rakiparanan][3]-enkücüksiyah <= 2):
        renk[rakiparanan][5] = "s"
        renk[rakiparanan][3]+=1
        beyazsaklama = renk[rakiparanan][0]
        siyahsaklama = renk[rakiparanan][1]
        renk[rakiparanan][0] = 0
        renk[rakiparanan][1] += 1

    elif(renk[rakiparanan][5] == "s" and renk[rakiparanan][2]-enkücükbeyaz <= 2):
        renk[rakiparanan][5] = "b"
        renk[rakiparanan][2]+=1
        siyahsaklama = renk[rakiparanan][1]
        beyazsaklama = renk[rakiparanan][0]
        renk[rakiparanan][1] = 0
        renk[rakiparanan][0] += 1


    elif(renk[rakiparanan][5] == "yok" ):
        if(yarismacilar[rakiparanan][5] %2 == 1 ):
            renk[rakiparanan][5] = renkler
            if(renkler == "b"):
                renk[rakiparanan][0]+=1
                renk[rakiparanan][2]+=1
                renk[rakiparanan][1]=0               
                
            else:
                renk[rakiparanan][1]+=1
                renk[rakiparanan][3]+=1
                renk[rakiparanan][0]=0
        else:
            renk[rakiparanan][5] = digerrenk
            if(digerrenk == "b"):
                renk[rakiparanan][0]+=1
                renk[rakiparanan][2]+=1
                renk[rakiparanan][1]=0 
            else:
                renk[rakiparanan][1]+=1
                renk[rakiparanan][3]+=1
                renk[rakiparanan][0]=0

    indisler = sayac


    rakip = rakiparanan + 1
    bulundu = False
    while(rakip < indisler and bulundu == False):
        if(yarismacilar[rakip][0] not in rakibivar and yarismacilar[rakip][0] != gecenbay and yarismacilar[rakip][0] not in rakipleri[rakiparanan]):
            if(renk[rakip][5] == renk[rakiparanan][5] or renk[rakip][5] == "yok"):
                if(renk[rakiparanan][5] == "b" and renk[rakip][3]-enkücüksiyah <= 2):
                    renk[rakip][5] = "s"
                    renk[rakip][3]+=1
                    renk[rakip][1]+=1
                    renk[rakip][0] = 0
                    bulundu = True
                elif(renk[rakiparanan][5] == "s" and renk[rakip][2]-enkücükbeyaz <= 2):
                    renk[rakip][5] = "b"
                    renk[rakip][2]+=1
                    renk[rakip][0]+=1                   
                    renk[rakip][1] = 0
                    bulundu = True
        if(bulundu == False):
            rakip+=1
                                       

    if(bulundu == False):
        rakip = rakiparanan + 1
    while(rakip < indisler and bulundu == False):
        if(yarismacilar[rakip][0] not in rakibivar and yarismacilar[rakip][0] != gecenbay and yarismacilar[rakip][0] not in rakipleri[rakiparanan]):
            if(renk[rakip][5] != renk[rakiparanan][5]):
                if(renk[rakiparanan][5] == "s" and renk[rakip][2]-enkücükbeyaz <= 2 and renk[rakip][0] < 2):
                    renk[rakip][5] = "b"
                    renk[rakip][2]+=1                   
                    renk[rakip][1] = 0
                    renk[rakip][0]+=1
                    bulundu = True
                    
                elif(renk[rakiparanan][5] == "b" and renk[rakip][3]-enkücüksiyah <= 2 and renk[rakip][1] < 2 ):
                    renk[rakip][5] = "s"
                    renk[rakip][3]+=1
                    renk[rakip][0] = 0
                    renk[rakip][1]+=1
                    
                    bulundu = True
                
        if(bulundu == False):
            rakip+=1

    if(bulundu == False):
        if(renk[rakiparanan][5] == "s"):
            renk[rakiparanan][5] = "b"  
            renk[rakiparanan][1] = 0
            renk[rakiparanan][3]-=1
            renk[rakiparanan][0] = beyazsaklama+1
            renk[rakiparanan][2] += 1

        elif(renk[rakiparanan][5] == "b"):
            renk[rakiparanan][5] = "s"
            renk[rakiparanan][1] = siyahsaklama + 1
            renk[rakiparanan][3]+=1
            renk[rakiparanan][0] = 0
            renk[rakiparanan][2] -= 1

        rakip = rakiparanan + 1 

        while(rakip < indisler and bulundu == False):
            if(yarismacilar[rakip][0] not in rakibivar and yarismacilar[rakip][0] != gecenbay and yarismacilar[rakip][0] not in rakipleri[rakiparanan]):
                if(renk[rakip][5] == renk[rakiparanan][5] or renk[rakip][5] == "yok"):
                    if(renk[rakiparanan][5] == "b" and renk[rakip][3]-enkücüksiyah <= 2):
                        renk[rakip][5] = "s"
                        renk[rakip][3]+=1
                        renk[rakip][1]+=1
                        renk[rakip][0] = 0
                        bulundu = True
                    elif(renk[rakiparanan][5] == "s" and renk[rakip][2]-enkücükbeyaz <= 2):
                        renk[rakip][5] = "b"
                        renk[rakip][2]+=1
                        renk[rakip][0]+=1                   
                        renk[rakip][1] = 0
                        bulundu = True
            if(bulundu == False):
                rakip+=1
                
                if(renk[rakiparanan][5] == "b"):
                    renk[rakiparanan][1] = siyahsaklama
                    renk[rakiparanan][2]-=1
                    renk[rakiparanan][0] = beyazsaklama
                else:
                    renk[rakiparanan][1] = siyahsaklama
                    renk[rakiparanan][3]-=1
                    renk[rakiparanan][0] = beyazsaklama


    bilgi = list()
    if(bulundu == True):       
        rakibivar.append(yarismacilar[rakip][0])
        rakibivar.append(yarismacilar[rakiparanan][0])
        rakipleri[rakip].append(yarismacilar[rakiparanan][0])
        rakipleri[rakiparanan].append(yarismacilar[rakip][0])
        bilgi.append(bulundu)
        bilgi.append(rakip)
    else:
        bilgi.append(bulundu)


    return bilgi

def yazdir_masa(tur,masalar,yarismacilar):
    print("{}. tur eşleştirme listesi:".format(tur))
    print("       Beyazlar       Siyahlar")
    print("MNo BSNo LNo   Puan - Puan LNo BSNo")
    print("--- ---- ----- ----   ---- ----- ----")

    for i in range(len(masalar)):
        print(format(i+1,"3d"),end=" ")
        print(format(masalar[i][0],"4d"),end=" ")
        print(format(masalar[i][1],"5d"),end=" ")
        print(format(masalar[i][2],"4.2f"),end=" ")
        print("-",end=" ")
        if(len(yarismacilar)%2 == 1 and i == len(masalar)-1):
            print("bye")
        else:
            print(format(masalar[i][3],"4.2f"),end=" ")
            print(format(masalar[i][4],"5d"),end=" ")
            print(format(masalar[i][5],"4d"),end="\n")


def tur(yarismacilar):
    oyuncusayi = len(yarismacilar)
    EN_AZ = math.ceil(math.log2(oyuncusayi))
    tursayi = int(input("tur sayisini giriniz:"))
    while tursayi < EN_AZ or tursayi > oyuncusayi-1:
        tursayi = int(input("tur sayisini giriniz:"))

    return tursayi
  
def renk_al():
    renk = input("tas rengini giriniz(b/s):")
    while(renk != "b" and renk != "s"):
        renk = input("tas rengini giriniz(b/s):")

    return renk
         
def main():   
    LNo = list()
    yarismacilar = list()
    renk = list()
    maclar = list()
    oynanmayan = list()
    rakipleri = list()
    yarismacilar = inputal_ve_isle(LNo,yarismacilar)
    yarismacilar = siralama(yarismacilar)
    listeleri_olustur(rakipleri,renk,oynanmayan,yarismacilar,maclar,LNo)
    baslangic_yazdir(yarismacilar)
    sayitur = tur(yarismacilar)
    renkler = renk_al()

    for i in range(sayitur):
        liste_siralama(yarismacilar,renk,oynanmayan,maclar,rakipleri,LNo)
        masalar = eslestirme(yarismacilar,renk,maclar,oynanmayan,i,renkler,rakipleri)
        yazdir_masa(i+1,masalar,yarismacilar)
        sonuclar(i+1,masalar,maclar,oynanmayan,yarismacilar,renk,LNo)
        if(i != sayitur - 1):
            yarismacilar = siralama(yarismacilar)

    bh1_2_hesaplama(yarismacilar,LNo,maclar,oynanmayan,sayitur)
    sb_hesaplama(yarismacilar,LNo,maclar,oynanmayan,sayitur)
    galibiyet_sayisi(yarismacilar,LNo,maclar,oynanmayan,sayitur)
    nihaisiralama(yarismacilar)
    liste_siralama(yarismacilar,renk,oynanmayan,maclar,rakipleri,LNo)
    nihaiyazdirma(yarismacilar)
    capraztablo(yarismacilar,maclar,renk,oynanmayan,rakipleri,LNo)

   
main()




















