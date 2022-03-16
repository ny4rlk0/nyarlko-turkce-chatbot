import datetime as suan

def al(text):
    try:
        zaman=suan.datetime.now()
        saat=zaman.strftime("%H")
        dakika=zaman.strftime("%M")
        saniye=zaman.strftime("%S")
        gun=zaman.strftime("%A")
        ay=zaman.strftime("%B")
        yil=zaman.strftime("%Y")
        if gun=="Monday":
            gun="Pazartesi"
        elif gun=="Tuesday":
            gun="Salı"
        elif gun=="Wednesday":
            gun="Çarşamba"
        elif gun=="Thursday":
            gun="Perşembe"
        elif gun=="Friday":
            gun="Cuma"
        elif gun=="Saturday":
            gun="Cumartesi"
        elif gun=="Sunday":
            gun="Pazar"
        if ay=="January":
            ay="Ocak"
        elif ay=="February":
            ay="Şubat"
        elif ay=="March":
            ay="Mart"
        elif ay=="April":
            ay="Nisan"
        elif ay=="May":
            ay="Mayıs"
        elif ay=="June":
            ay="Haziran"
        elif ay=="July":
            ay="Temmuz"
        elif ay=="August":
            ay="Ağustos"
        elif ay=="September":
            ay="Eylül"
        elif ay=="October":
            ay="Ekim"
        elif ay=="November":
            ay="Kasım"
        elif ay=="December":
            ay="Aralık"
    except: return "Tarih, saati alırken hata ile karşılaştım."
    else:
        if text.startswith("saat") or text.startswith("dakika") or text.startswith("saniye"):
            return saat+":"+dakika+":"+saniye
        elif text.startswith("tarih"):
            return gun+"/"+ay+"/"+yil+" "+saat+":"+dakika+":"+saniye
        elif text.startswith("gün") or text.startswith("gun"):
            return gun
        elif text.startswith("ay"):
            return ay
        elif text.startswith("yıl") or text.startswith("yil"):
            return yil