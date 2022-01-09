print("kayıt olma sistemi (@Mrpirate) ")
isim=input("isiminizi giriniz : ")
kullanıcı=input("kullanıcı adınızı oluşturunuz : ")
şifre=input("şifrenizi oluşturunuz : ")
print("kaydınız başarıyla oluşturuldu ")
a=input("giriş işlemi için 1 e basınız : ") 
if a=="1" :
    print("Giriş Yapınız ")
    kullan=input("kullanıcı adınızı giriniz : ")
    kullan=(str(kullan))
    şifreni=input("şifrenizi giriniz : ")
    if kullan==kullanıcı and şifreni==şifre :
        print("hoş geldin ",isim,)
        print("başarıyla giriş yapıldı ")
    elif kullan!=kullanıcı and şifreni!=şifre :
        print("Kullanıcı veya şifreniz yanlış ")
        print("ip adresiniz kopyalanmıştır :)")