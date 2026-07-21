#integer
yas=20
ögrenciSayisi=5500
sicaklik=29
print(yas)
print(ögrenciSayisi)
print(sicaklik)

a=10
b=20
toplam=a+b
print(toplam)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#ürün sayısı var ve her ürünün fiyatı var. toplam fiyatı hesaplayın
ürünSayisi=8
birimFiyat=15
toplamFiyat=ürünSayisi*birimFiyat
print(toplamFiyat)

#zam uygulaması yapalım. 
birimFiyat=1500
yuzde=int(input("Zam yüzdesini giriniz: "))
print("Zam yüzdesi: ", yuzde)
zamMiktari=birimFiyat*yuzde/100
print("Zam miktarı: ", zamMiktari)

#float
pi=3.14
sicaklik=29.5
urunFiyati=15.99
print(pi)
print(sicaklik)
print(urunFiyati)


#matematiksel işlemler
a=10.5
b=20.5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#ondalık hassasiyet
print(2.0 + 6.0)

#yuvarlama işlemleri(round )
sonuc=1.0+2.5
print(sonuc)
yuvarlanmisSonuc=round(sonuc,2)
print(yuvarlanmisSonuc)

#GELEN FİYAT ÜZERİNDEN KDV HESAPLAMA(%20)
fiyat=float(input("Fiyatı giriniz: "))
print("Fiyat: ", fiyat)
kdvliFiyat=fiyat+20*fiyat/100
print("KDVli Fiyat: ", kdvliFiyat)

#string 
ad="Ahmet"
soyad="Yılmaz"
tamAd=ad+" "+soyad
print(tamAd)
bilgi="Benim adım Gülsüm,soyadım KURTOĞULLARI ve yaşım 20"
print(bilgi)
bilgi2="Benim adım "+ad+",soyadım "+soyad+" ve yaşım 20"
print(bilgi2)
##string ve sayısal değerleri birleştirme
yas=35
int_to_str=str(yas)
bilgi3=ad+" "+ "YAŞI: "+int_to_str
print(bilgi3)
uyeSayisi=7
bilgi4="Benim adım Gülsüm ailemde toplam "+ str(uyeSayisi)+" kişi var"
print(bilgi4)
print (f"Benim adım {ad} ailemde toplam {uyeSayisi} kişi var")

accuracy=95
print(f"Karar AğacıAccuracy: %{accuracy}")

#string indeksleme
kelime="python"
print(kelime[0])
print(kelime[5])
    
#string metodları
metin="PythoN Programlama Dili"
metinKucukHarf=metin.lower() #hepsini küçük yazar
print(metinKucukHarf)

metinBuyukHarf=metin.upper() #hepsini büyük yazar.
print(metinBuyukHarf)

metinIlkHarfBuyuk=metin.capitalize() #ilk harfi büyük yazar
print(metinIlkHarfBuyuk)

metinHerIlkHarfBuyuk=metin.title() #her kelimenin ilk harfi büyük yazar
print(metinHerIlkHarfBuyuk)

metinBuyukKucuk=metin.swapcase()#büyük harfleri küçük, küçük harfleri büyük yazar
print(metinBuyukKucuk)

metinHarfDegisimi=metin.replace("m","M")#istediğimiz harfi değiştirebiliriz
print(metinHarfDegisimi)

metinUzunluk=len(metin)#METİN UZUNLUĞUNU VERİR
print(metinUzunluk)

metinboslukDegisimi=metin.replace("P","p").replace("D","*").replace("N","n").replace(" ","-")#istediğimiz harfi değiştirebiliriz
print(metinboslukDegisimi)

