hasta_maske = input("COVID-19 hastasinda tıbbi maske takilmis olup olmadigini giriniz(e/h):")
endikasyon = input("N95 endikasyonu olup olmadigini giriniz:")
calisan_maske = input("Saglik calisaninin maske kullanim durumunu giriniz(t: tıbbi, n: n95, h: hicbiri): ")
goz_koruyucu = input("Saglik calisaninin göz koruyucu kullanip kullanmadigini giriniz(e/h): ")
eldiven = input("Saglik calisaninin eldiven&onluk kullanip kullanmadigini giriniz(e/h): ")

#risk kategorilerinin her birini ayrı değişkenlere atadım.
yuksek = "\n Saglik calisani yüksek riskli kategoridedir.\n Semptom gelismezse 7.günde PCR testi yapilmasi gereklidir.\n O güne kadar calisamaz."
orta = "\n Saglik calisani orta riskli kategoridedir. \n Semptom gelismezse 7.günde PCR testi yapilmasi gereklidir. \n O güne kadar calisabilir."
dusuk = "\n Saglik calisani dusuk riskli kategoridedir. \n Semptom gelismezse 7.günde PCR testi yapilmasi gerekli degildir. \n O güne kadar calisabilir."
risksiz = "\n Saglik calisani risksiz kategoridedir."


if(hasta_maske == "h"):#hasta eğer maske takmamış ise bu if'e girecek
    if(endikasyon == "h" and calisan_maske == "h"):#çalışan maske takmıyor ve n95 endikasyonu yok ise buraya girecek
        print(yuksek)
    if(endikasyon == "h" and (calisan_maske == "n" or calisan_maske == "t")):#çalışanın n95 endikasyonu yoksa ve herhangi bir maske takıyor ise buraya girecek
        if (goz_koruyucu == "h" and eldiven == "h"):#çalışan gözlük, eldiven ve önlük takmamış ise bu if'e girecek
            print(orta)
        if (goz_koruyucu == "e" and eldiven == "h"):#çalışan sadece gözlük takmış ise bu if'e girecek
            print(dusuk)
        if (goz_koruyucu == "h" and eldiven == "e"):#çalışan sadece gözlük takmamış ise bu if'e girecek
            print(orta)
        if (goz_koruyucu == "e" and eldiven == "e"):#çalışan hem gözlük takmış hem eldiven ile önlüğü giymiş ise bu if'e girecek
            print(risksiz)
    if(endikasyon == "e" and calisan_maske == "t"):#çalışanın n95 endikasyonu var ve tıbbi maske takıyor ise buraya girecek.
        print(orta)
    if(endikasyon == "e" and calisan_maske == "n"):#çalışanın n95 endiksayonu var ve n95 maskesini takıyor ise buraya girecek.
        if(goz_koruyucu == "h" and eldiven == "h"):#çalışan gözlük, eldiven ve önlük takmamış ise bu if'e girecek.
            print(orta)
        if(goz_koruyucu == "e" and eldiven == "h"):#çalışan sadece gözlük takmış ise bu if'e girecek.
            print(dusuk)
        if(goz_koruyucu == "h" and eldiven == "e"):#çalışan sadece gözlük takmamış ise bu if'e girecek.
            print(orta)
        if(goz_koruyucu == "e" and eldiven == "e"):# çalışan tüm kke'yi düzgün şekilde kullanmış ise buraya girecek.
            print(risksiz)

if(hasta_maske == "e"):#hasta eğer maske takmış ise bu if'e girecek
    #ilk olarak çalışanın n95 endikasyonu var ve tıbbi maske takıyor ise alttaki if'e girecek.
    #ikinci olarak çalışanın n95 endikasyonu yok ve maske takmıyor ise yine alttaki if'e girecek.
    if(((endikasyon == "e" and calisan_maske == "t") or calisan_maske == "h") or (endikasyon == "h" and calisan_maske == "h") ):
        print(orta)
    if(endikasyon == "e" and calisan_maske == "n"):#çalışanın n95 endikasyonu var ve aynı zamanda n95 maskesini takıyor ise bu if'e girecek.
        if(goz_koruyucu == "h" or eldiven == "h"):#çalışanın gözlüğü, eldiveni ve önlüğü yok ise bu if'e girecek.
            print(dusuk)
        else:#bir üstteki if'ten kalan diğer seçeneklerde ise bu if'e girecek.
            print(risksiz)

    if(endikasyon == "h" and (calisan_maske == "n" or calisan_maske == "t")):#çalışanın n95 endikasyonu yok ve herhangi bir maske takmış ise bu if'e girecek.
        if (goz_koruyucu == "h" or eldiven == "h"):#çalışanın herhangi bir ekipmanı yok ise bu if'e girecek
            print(dusuk)
        else:# bir üstteki if'ten kalan diğer seçeneklerde ise bu if'e girecek.
            print(risksiz)

input()




