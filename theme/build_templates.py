import json
img = lambda n: f"shopify://shop_images/{n}"
settings = {
 "product": "projektor-gwiazd",
 "delivery_days": "7 do 12",
 "announcement": "Darmowa dostawa od 200 zł · 30 dni na zwrot",
 "bullet1": "Księżyc, planety i gwiazdy na suficie",
 "bullet2": "12 wymiennych slajdów w zestawie",
 "bullet3": "Projektor i lampka nocna w jednym",
 "img_hero": img("nn-hero.png"),
 "headline": "Wieczór bez walki o zgaszenie światła",
 "subheadline": "Gwiazdy i księżyc na suficie pokoju dziecka. Podłączasz do USB, gasisz światło i jest na co patrzeć zamiast na ekran.",
 "problem": "Znasz to: „jeszcze pięć minut”, trzecia szklanka wody i światło, którego nie da się zgasić.",
 "problem_2": "Projektor nie uśpi dziecka za Ciebie. Daje mu za to powód, żeby położyć się do łóżka i patrzeć w górę, a Tobie kilka minut spokoju na koniec dnia.",
 "img_step1": img("nn-krok1b.png"), "step1_title": "Podłącz do USB",
 "step1_text": " Wtyk na końcu giętkiej szyjki wkładasz do ładowarki do telefonu, powerbanku, laptopa albo gniazda USB w aucie. Bez baterii.",
 "img_step2": img("nn-krok2.png"), "step2_title": "Włóż slajd",
 "step2_text": " Wybierz jedną z 12 projekcji i wsuń wkładkę ze slajdem do projektora.",
 "img_step3": img("nn-krok3b.png"), "step3_title": "Zgaś światło",
 "step3_text": " Wygnij szyjkę w stronę sufitu i ustaw ostrość. Obraz jest wyraźny tylko w ciemnym pokoju.",
 "img_before": img("nn-przed.png"), "img_after": img("nn-hero.png"),
 "ba_note": "Zdjęcia są wizualizacjami. Projekcja jest najwyraźniejsza w całkowicie ciemnym pokoju.",
 "who1_title": "Rodzic przedszkolaka",
 "who1_text": "Codziennie o 20:00 zaczyna się ta sama negocjacja o zgaszenie światła, a Ty po całym dniu nie masz już siły na kolejną rundę.",
 "who2_title": "Ktoś, kto urządza swój pokój",
 "who2_text": "Wracasz wieczorem do pokoju, który wygląda jak każdy inny, i siedzisz w nim przy białym świetle sufitówki.",
 "who3_title": "Szukasz prezentu",
 "who3_text": "Masz prezent do kupienia za mniej niż 200 zł i nie chcesz po raz kolejny dawać kosmetyków ani skarpetek.",
 "img_box": img("nn-zestaw.png"),
 "delivery_text": "Projektor wysyłamy z magazynu dostawcy za granicą. Nie obiecujemy dostawy na jutro, podajemy realny czas. Cło i podatki są wliczone w cenę.",
 "guarantee": "Przyszedł uszkodzony albo nie działa? Wyślij nam zdjęcie lub krótki film, a wyślemy nowy albo oddamy pieniądze. Koszt odesłania pokrywamy my. Paczka nie dotarła w 20 dni roboczych? Tak samo.",
 "q1": "Jak duży i jasny jest obraz?",
 "a1": "Projektor wyświetla jeden okrągły obraz naraz, na przykład księżyc z gwiazdami albo planetę, tak jak na zdjęciach kupujących wyżej. Nie wypełnia całego sufitu. Obraz jest wyraźny tylko w ciemnym pokoju i z niewielkiej odległości, przy zapalonym świetle prawie go nie widać. Grafiki na górze strony są wizualizacjami.",
 "q2": "Czy obraz będzie ostry?",
 "a2": "Ostrość ustawiasz ręcznie. Część kupujących pisze, że niektóre slajdy wychodzą mniej wyraźnie niż inne. Jeśli żaden slajd nie daje ostrego obrazu, to wada: wymienimy projektor albo oddamy pieniądze.",
 "q3": "Jak go włączam i czym zasilam?",
 "a3": "Dotykowym przyciskiem na obudowie: tryb lampki nocnej, tryb gwiazd, wyłączenie. Przytrzymanie przycisku zmienia jasność. Zasilanie z dowolnego gniazda USB: ładowarka do telefonu, powerbank, laptop albo gniazdo w aucie. Nie ma baterii.",
 "q4": "Czy mogę zostawić go włączonego na całą noc?",
 "a4": "Lepiej nie. Slajdy to cienka folia i jeden z kupujących pisze, że po wielu godzinach świecenia slajd się zniszczył. Włącz go na czas zasypiania i wyłącz, gdy dziecko zaśnie.",
 "q5": "Kiedy dotrze paczka i ile kosztuje dostawa?",
 "a5": "W 7 do 12 dni roboczych od zamówienia, z numerem śledzenia. Dostawa kosztuje 14,99 zł, od 200 zł jest darmowa. Jeśli paczka nie dotrze w 20 dni roboczych, wyślemy nową albo oddamy pieniądze.",
 "q6": "Co, jeśli dziecku się nie spodoba?",
 "a6": "Masz 30 dni na zwrot bez podawania przyczyny. Odsyłasz na polski adres, pieniądze wracają w ciągu 14 dni."
}
blocks = {
 "rev_sa": {"type": "review", "settings": {"image": img("nn-opinia-sa.jpg"), "stars": 4, "text": "Za tę cenę dobry produkt. Kilka slajdów jest mniej wyraźnych, ale da się z tym żyć. Córka jest zadowolona.", "name": "Kupujący z Arabii Saudyjskiej"}},
 "rev_es": {"type": "review", "settings": {"image": img("nn-opinia-es.jpg"), "stars": 5, "text": "Świetny i piękny, najbardziej podobają mi się czarno-białe obrazy. Ostrość da się regulować, a projektor działa też jako lampka nocna z przyciskiem dotykowym. Minus: każdy slajd trzeba zmieniać ręcznie. Daję 9 na 10.", "name": "Kupujący z Hiszpanii"}},
 "rev_nl": {"type": "review", "settings": {"image": img("nn-opinia-nl.jpg"), "stars": 5, "text": "Bardzo ładny efekt.", "name": "Kupujący z Holandii"}}
}
for name in ["index.json", "product.nocne-niebo.json"]:
    t = {"layout": "nocne-niebo", "sections": {"main": {"type": "nn-landing", "blocks": blocks, "block_order": list(blocks), "settings": dict(settings)}}, "order": ["main"]}
    if name.startswith("product"):
        t["sections"]["main"]["settings"]["product"] = ""
        del t["sections"]["main"]["settings"]["product"]
    json.dump(t, open("templates/" + name, "w"), ensure_ascii=False, indent=1)
print("ok")
