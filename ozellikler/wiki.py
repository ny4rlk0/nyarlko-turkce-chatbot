import wikipedia as w
w.set_lang("tr")

def ara(konu):
    if konu.startswith("wiki"):
        try:
            veri=konu.split("wiki ")
            ozet=w.summary(veri[1])
            ozet=str(ozet)
        except:return f"Üzgünüm, [{konu}] Wikipedia içerisinde bulamadım!"
        else:return ozet