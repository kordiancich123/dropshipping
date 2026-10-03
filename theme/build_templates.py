import json
img = lambda n: f"shopify://shop_images/{n}"
settings = {
 "product": "projektor-gwiazd",
 "delivery_days": "7 do 12",
 "img_hero": img("nn-hero.png"),
 "headline": "Wieczór bez walki o zgaszenie światła",
 "subheadline": "Gwiazdy i księżyc na suficie pokoju dziecka. Podłączasz do USB, gasisz światło i jest na co patrzeć zamiast na ekran.",
 "problem": "Znasz to: „jeszcze pięć minut”, trzecia szklanka wody i światło, którego nie da się zgasić.",
 "problem_2": "Projektor nie uśpi dziecka za Ciebie. Daje mu za to powód, żeby położyć się do łóżka i patrzeć w górę, a Tobie kilka minut spokoju na koniec dnia.",
 "img_step1": img("nn-krok1.png"), "step1_title": "Podłącz do USB",
 "step1_text": " Ładowarka do telefonu, powerbank, laptop albo gniazdo USB w aucie. Bez baterii.",
 "img_step2": img("nn-krok2.png"), "step2_title": "Włóż slajd",
 "step2_text": " Wybierz jedną z 12 projekcji i wsuń slajd do projektora.",
 "img_step3": img("nn-krok3.png"), "step3_title": "Zgaś światło",
 "step3_text": " Skieruj projektor na sufit. Im ciemniej w pokoju, tym wyraźniejsze gwiazdy.",
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
 "q1": "Czy będzie wyglądać jak na zdjęciach?",
 "a1": "Zdjęcia na tej stronie są wizualizacjami. Projekcja jest najwyraźniejsza w całkowicie ciemnym pokoju. Przy zapalonym świetle gwiazd prawie nie widać, a w jasnym pokoju efekt jest delikatniejszy niż na zdjęciach.",
 "q2": "Czym go zasilam?",
 "a2": "Dowolnym gniazdem USB: ładowarką do telefonu, powerbankiem, laptopem albo gniazdem USB w aucie. Nie ma baterii do wymiany.",
 "q3": "Ile jest projekcji?",
 "a3": "W zestawie jest 12 wymiennych slajdów. Projekcję zmieniasz, wkładając inny slajd.",
 "q4": "Kiedy dotrze paczka?",
 "a4": "W 7 do 12 dni roboczych od zamówienia. Numer śledzenia dostajesz mailem. Jeśli paczka nie dotrze w 20 dni roboczych, wyślemy nową albo oddamy pieniądze.",
 "q5": "Co, jeśli dziecku się nie spodoba?",
 "a5": "Masz 30 dni na zwrot bez podawania przyczyny. Odsyłasz na polski adres, pieniądze wracają w ciągu 14 dni.",
 "q6": "Ile kosztuje dostawa?",
 "a6": "14,99 zł. Od 200 zł, czyli na przykład przy zestawie 2 projektorów, dostawa jest darmowa."
}
for name in ["index.json", "product.nocne-niebo.json"]:
    t = {"layout": "nocne-niebo", "sections": {"main": {"type": "nn-landing", "blocks": {}, "block_order": [], "settings": dict(settings)}}, "order": ["main"]}
    if name.startswith("product"):
        t["sections"]["main"]["settings"]["product"] = ""
        del t["sections"]["main"]["settings"]["product"]
    json.dump(t, open("templates/" + name, "w"), ensure_ascii=False, indent=1)
print("ok")
