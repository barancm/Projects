def oylar(partiler,file):
    oy = [0] * partiler#parti sayısı kadar değişken tutan bir liste oluşturdum
    for j in range(partiler):#partiler kadar dönen bi for döngüsü kurdum
        oy[j] = int(file.readline())#main'in içinde sırası geldiğinde oyları teker teker text dosyasından alıp listeye ekledim.
    return oy

def tum_oylar(oy):
    tum_oylar = 0#tüm oyları tutacağım bir değişken oluşturdum.
    for k in range(len(oy)):#oyların içindeki sayı kadar dönecek bi for kurdum.
        tum_oylar += oy[k]#her bir indisteki oyları toplayıp tum_oylar değişkenine attım
    return tum_oylar

def milletvekilleri(oylar_listesi,katilan_parti,mvkontenjani):
    mv_oy_listesi = oylar_listesi.copy()#kaybetmemek için oylar_listesindeki sayıları kopyaladım
    mv_sayilari = [0]*katilan_parti#parti sayısı kadar yeri olan bir mv_sayilari listesi oluşturdum
    while(mvkontenjani != 0):#milletvekili kontenjanı sıfır olmadığı sürece buraya girmesi için while döngüsü kurdum.
        max_oy = max(mv_oy_listesi)#bu listedeki maksimum olan değeri bi değişkenle tuttum.
        max_index = mv_oy_listesi.index(max_oy)#bu maksimum değerin hangi indexte olduğunu bir diğer değişkenle tuttum
        mv_oy_listesi[max_index] = max_oy // 2#maksimum oy sayısını ikiye böldüm ve bulunduğu indexe yolladım
        mv_sayilari[max_index]+=1#millettvekili sayısının bulunduğu indexi bir arttırdım
        mvkontenjani-=1#kontenjan dolduğunda çıkabilmesi için her döndüğünde kontenjanı bir azalttım
    return mv_sayilari



def main():
    file = open("secim.txt","r")#dosyayı açtım
    file_boyutu = len(file.readlines())#dosyanın uzunluğunu öğrendim ve bir değişkene atadım
    file.seek(0)#tekrardan imleci en başa yolladım
    katilan_parti = int(file.readline())#katılan parti sayısını text dosyasından çektim
    oylar_listesi = [0]*katilan_parti#katılan parti sayısı kadar indexi olan bir oylar listesi listesi oluşturdum
    plaka = [0] * katilan_parti#katılan parti sayısı kadar indexi olan bir plaka listesi oluşturdum
    il_sayisi = int((file_boyutu-1)/(katilan_parti+1+1))#girilen il sayısını hesapladım
    mvkontenjan = [0]*il_sayisi#milletvekili kontenjanını tutabilecek bir liste tanımladım
    sifir_milletvekili = [0]*katilan_parti#hiç milletvekili alamayanları tutabilmek için bir liste tanımladım
    toplam_mv_kontenjan = 0#tüm milletvekilleri kontenjanlarını tutacak bir değişken tanımladım
    toplam_gecerli_oy = 0#geçerli sayılan oyları tutan bir değişken tanımladım
    genel_oy_listesi = [0]*katilan_parti#
    toplam_mv_sayilari = [0]*katilan_parti
    for i in range(il_sayisi):#bu döngünün il sayısı kadar dönmesini sağladım
        plaka[i] = int(file.readline())#plakayı text dosyasından aldım
        mvkontenjan[i] = int(file.readline())#milletvekili kontenjanını text dosyasından çektim
        toplam_mv_kontenjan += mvkontenjan[i]# her döndüğünde döngü milletvekili kontenjanlarının tümümü tutabilmek için bir değişkene atadım
        oylar_listesi = oylar(katilan_parti,file)#oyları bir listeye atadım
        gecerli_oy = tum_oylar(oylar_listesi)#tüm oyları geçerli oy değişkenine atadım
        toplam_gecerli_oy += gecerli_oy#tüm gecerli oyları toplayarak bir değişkene atadım
        mv_sayilari_listesi = milletvekilleri(oylar_listesi,katilan_parti,mvkontenjan[i])
        for t in range(katilan_parti):
            genel_oy_listesi[t] += oylar_listesi[t]#oylar listesinide tüm ülke genelinde tutabilmek için her bir döngüde gene oy listesinde attım
            toplam_mv_sayilari[t] += mv_sayilari_listesi[t]#tüm ülke genelinde milletvekili sayılarını tutabilmek için bir değişkene toplayıp attım
            if mv_sayilari_listesi[t] == 0:#milletvekili sayısı sıfır olduğunda buraya girmesini sağladım
                sifir_milletvekili[t]+=1#sıfır olan partinin indisinin 1 artmasını sağladım



        print("Il Plaka Kodu:",plaka[i])
        print("Milletvekili Kontenjani:",mvkontenjan[i])
        print("Gecerli Oy Sayisi:",gecerli_oy)
        print("Pusula Sira   Oy Say   Oy Yuzde   MV Say")
        print("-----------   ------   --------   ------")#gerekli printleri yazdırdım
        for j in range(katilan_parti):#8 parti olduğu için olan parti kadar bir for döngüsü kurdum
            print(format(j+1,"11d"),end="   ")
            print(format(oylar_listesi[j],"6d"),end="   ")
            print(format(oylar_listesi[j]*100/gecerli_oy,'8.2f'),end="   ")
            print(format(mv_sayilari_listesi[j],"6d"),end="  \n")

    print("Turkiye Geneli")
    print("Milletvekili Kontenjani:",toplam_mv_kontenjan)
    print("Gecerli Oy Sayisi:",toplam_gecerli_oy)
    print("Pusula Sira   Oy Say   Oy Yuzde   MV Say   MV Yuzde   0 MV Il Say")
    print("-----------   ------   --------   ------   --------   -----------")#tüm ülke için gerekli printleri yazdırdım
    for h in range(katilan_parti):#olan parti sayısı kadar for'da döndürüp gerekli printleri yazdırdım
        print(format(h+1,"11d"),end="   ")
        print(format(genel_oy_listesi[h],"6d"),end="   ")
        print(format(genel_oy_listesi[h]*100/toplam_gecerli_oy,'8.2f'),end="   ")
        print(format(toplam_mv_sayilari[h],"6d"),end="   ")
        print(format(toplam_mv_sayilari[h]*100/toplam_mv_kontenjan,'8.2f'),end="   ")
        print(format(sifir_milletvekili[h],"11d"),end="  \n")



main()
        
   



    


    
    



