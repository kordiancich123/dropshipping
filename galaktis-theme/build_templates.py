"""Generuje templates/*.json motywu GALAKTIS. Treści edytujesz tutaj albo w edytorze motywu."""
import json

img = lambda n: f"shopify://shop_images/{n}"

def blocks(kind, items):
    b = {f"{kind}{i+1}": {"type": kind, "settings": s} for i, s in enumerate(items)}
    return {"blocks": b, "block_order": list(b)}

hero = {"type": "gx-hero", "settings": {"image": img("GALAKTIS_HERO_01.png"), "video": "shopify://files/videos/GALAKTIS_VIDEO_HERO_01.mp4"}}
proof = {"type": "gx-proof", "settings": {}, **blocks("photo", [
    {"image": img("nn-opinia-es.jpg"), "alt": "Zdjęcie klienta: księżyc na suficie"},
    {"image": img("nn-opinia-sa.jpg"), "alt": "Zdjęcie klienta: projekcja księżyca"},
    {"image": img("nn-opinia-nl.jpg"), "alt": "Zdjęcie klienta: projektor i slajdy"},
])}
ba = {"type": "gx-before-after", "settings": {"before": img("GALAKTIS_BEFORE_02.png"), "after": img("GALAKTIS_AFTER_02.png"), "before_alt": "Sypialnia wieczorem ze zwykłą żółtą lampką", "after_alt": "Ta sama sypialnia z projekcją księżyca i gwiazd na suficie", "before_list": "Zwykły pokój\nŻółte światło lampki\nBrak klimatu"}}
why = {"type": "gx-why", "settings": {}, **blocks("card", [
    {"icon": "galaxy", "title": "Kosmos nad głową", "text": "Księżyc, planety, mgławice i galaktyki z 12 wymiennych slajdów."},
    {"icon": "sparkle", "title": "Efekt wow", "text": "Zwykły sufit zamienia się w okno na nocne niebo."},
    {"icon": "moon", "title": "Wieczorny relaks", "text": "Miękkie światło na koniec dnia. Działa też jako lampka nocna."},
    {"icon": "gift", "title": "Prezent, który zostaje", "text": "Dla dziecka, partnera albo fana kosmosu. W pakiecie taniej."},
    {"icon": "gamepad", "title": "Granie i seanse", "text": "Klimat podczas grania i oglądania filmów, bez rozpraszania."},
    {"icon": "bolt", "title": "Prosta obsługa", "text": "Port USB, slajd, dotyk przycisku. Bez aplikacji i bez baterii."},
])}
prod_home = {"type": "gx-product", "settings": {"product": "projektor-gwiazd"}}
prod_page = {"type": "gx-product", "settings": {}}
bundles_home = {"type": "gx-bundles", "settings": {"product": "projektor-gwiazd"}}
bundles_page = {"type": "gx-bundles", "settings": {}}
steps = {"type": "gx-steps", "settings": {}, **blocks("step", [
    {"image": img("nn-krok1b.png"), "ph": "WTYK USB WKŁADANY DO ŁADOWARKI, 1:1", "title": "Podłącz GALAKTIS", "text": "Wtyk USB do ładowarki, powerbanku albo laptopa."},
    {"image": img("GALAKTIS_UGC_01.png"), "ph": "SLAJD WSUWANY DO PROJEKTORA, 1:1", "title": "Wybierz projekcję", "text": "Wsuń jeden z 12 slajdów i włącz tryb gwiazd albo lampki."},
    {"image": img("nn-krok3b.png"), "ph": "PROJEKCJA NA SUFICIE W CIEMNYM POKOJU, 1:1", "title": "Ciesz się galaktyką", "text": "Zgaś światło, wygnij szyjkę w stronę sufitu i ustaw ostrość."},
])}
proj = {"type": "gx-tiles", "settings": {
    "anchor": "projekcje", "alt": True, "square": True, "eyebrow": "Projekcje",
    "heading": "Jeden projektor.\nNiezliczone klimaty.",
    "lead": "Każdy slajd to inny wieczór. Zmieniasz go w kilka sekund.",
    "note": "Przykładowe motywy. Projektor wyświetla jeden okrągły obraz naraz, najwyraźniejszy w ciemnym pokoju.",
}, **blocks("tile", [
    {"image": img("gx-proj-galaktyka.jpg"), "alt": "Projekcja galaktyki", "title": "Galaktyka", "ph": "PROJEKCJA GALAKTYKI, 1:1"},
    {"image": img("gx-proj-ksiezyc.jpg"), "alt": "Projekcja księżyca", "title": "Księżyc", "ph": "PROJEKCJA KSIĘŻYCA, 1:1"},
    {"image": img("gx-proj-mglawica.png"), "alt": "Projekcja mgławicy", "title": "Mgławica", "ph": "PROJEKCJA MGŁAWICY, 1:1"},
    {"image": img("gx-proj-zorza.png"), "alt": "Projekcja zorzy polarnej", "title": "Zorza", "ph": "PROJEKCJA ZORZY, 1:1"},
    {"image": img("gx-proj-planeta.png"), "alt": "Projekcja planety", "title": "Planety", "ph": "PROJEKCJA PLANETY, 1:1"},
])}
uses = {"type": "gx-tiles", "settings": {
    "eyebrow": "Zastosowania", "heading": "Gdzie możesz używać GALAKTIS?",
    "lead": "Wszędzie tam, gdzie jest gniazdo USB i odrobina ciemności.",
}, **blocks("tile", [
    {"image": img("GALAKTIS_BEDROOM_01.png"), "alt": "Kobieta na łóżku patrzy na księżyc na suficie", "title": "Sypialnia", "text": "Wieczór dla siebie po całym dniu", "ph": "SYPIALNIA Z PROJEKCJĄ, 4:5"},
    {"image": img("nn-hero.png"), "alt": "Dziecko w łóżku patrzy na księżyc na suficie", "title": "Pokój dziecięcy", "text": "Wieczorny rytuał zamiast ekranu", "ph": "POKÓJ DZIECIĘCY Z PROJEKCJĄ, 4:5"},
    {"image": img("gx-gaming.png"), "alt": "Gaming room z galaktyką nad monitorem", "title": "Gaming room", "text": "Klimat, który nie rozprasza", "ph": "GAMING ROOM Z PROJEKCJĄ, 4:5"},
    {"image": img("gx-salon.png"), "alt": "Para na kanapie pod księżycem na suficie", "title": "Salon i kino domowe", "text": "Seans pod gwiazdami", "ph": "SALON, WIECZÓR FILMOWY, 4:5"},
    {"image": img("GALAKTIS_GIFT_01.png"), "alt": "Projektor i slajdy w pudełku prezentowym", "title": "Prezent", "text": "Dla dziecka, partnera, fana kosmosu", "ph": "PROJEKTOR JAKO PREZENT, 4:5"},
])}
emo = {"type": "gx-emotion", "settings": {}}
reviews = {"type": "gx-reviews", "settings": {}, **blocks("review", [
    {"image": img("nn-opinia-es.jpg"), "alt": "Zdjęcie klienta: księżyc na suficie", "stars": 5, "text": "Świetny i piękny, najbardziej podobają mi się czarno-białe obrazy. Ostrość da się regulować, a projektor działa też jako lampka nocna z przyciskiem dotykowym. Minus: każdy slajd trzeba zmieniać ręcznie. Daję 9 na 10.", "name": "Kupujący z Hiszpanii"},
    {"image": img("nn-opinia-sa.jpg"), "alt": "Zdjęcie klienta: projekcja księżyca", "stars": 4, "text": "Za tę cenę dobry produkt. Kilka slajdów jest mniej wyraźnych, ale da się z tym żyć. Córka jest zadowolona.", "name": "Kupujący z Arabii Saudyjskiej"},
    {"image": img("nn-opinia-nl.jpg"), "alt": "Zdjęcie klienta: projektor i slajdy", "stars": 5, "text": "Bardzo ładny efekt.", "name": "Kupujący z Holandii"},
])}
faq = {"type": "gx-faq", "settings": {}, **blocks("qa", [
    {"q": "Czy GALAKTIS jest łatwy w obsłudze?", "a": "<p>Tak. Podłączasz wtyk USB do ładowarki, powerbanku albo laptopa, wsuwasz slajd i dotykasz przycisku. Szyjkę wyginasz w stronę sufitu lub ściany, a ostrość ustawiasz ręcznie.</p>"},
    {"q": "Na jakiej powierzchni najlepiej działa?", "a": "<p>Na gładkim, jasnym i matowym suficie albo ścianie, w ciemnym pokoju. Projektor wyświetla jeden okrągły obraz naraz. Im ciemniej, tym wyraźniejszy obraz; przy zapalonym świetle prawie go nie widać.</p>"},
    {"q": "Czy można używać go w sypialni?", "a": "<p>Tak, to jego główne zastosowanie. Oprócz projekcji ma tryb delikatnej lampki nocnej, a przytrzymanie przycisku zmienia jasność.</p>"},
    {"q": "Czy nadaje się do pokoju dziecięcego?", "a": "<p>Tak, jako wieczorny rytuał przed snem. Zasilanie z USB, bez baterii. To nie jest zabawka: projektor podłącza i obsługuje dorosły, a ładowarkę i kabel trzymaj poza zasięgiem małych dzieci.</p>"},
    {"q": "Jakie projekcje są dostępne?", "a": "<p>W zestawie jest 12 wymiennych slajdów z motywami kosmicznymi. Projekcje pokazane na stronie to przykładowe motywy.</p>"},
    {"q": "Czy projektor można zostawić włączony przez dłuższy czas?", "a": "<p>Odradzamy zostawianie go na całą noc. Slajdy to cienka folia, która przy wielogodzinnym świeceniu może się odkształcić. Włącz go na wieczór i wyłącz, gdy zasypiasz.</p>"},
    {"q": "Co znajduje się w zestawie?", "a": "<p>Projektor na giętkiej szyjce z wtykiem USB i 12 wymiennych slajdów. Do zasilania wystarczy dowolny port USB, na przykład ładowarka do telefonu.</p>"},
    {"q": "Jak długo trwa dostawa?", "a": "<p>7 do 12 dni roboczych. Wysyłamy z magazynu dostawcy za granicą, dlatego nie obiecujemy dostawy na jutro. Dostawa kosztuje 14,99 zł, od 200 zł jest darmowa. Cło i podatki są w cenie.</p>"},
    {"q": "Jak wygląda zwrot?", "a": "<p>Masz 30 dni na zwrot bez podawania przyczyny. Odsyłasz na polski adres, pieniądze wracają w ciągu 14 dni. Jeśli produkt jest uszkodzony, odesłanie jest na nasz koszt. <a href=\"/pages/zwroty\">Szczegóły zwrotów</a></p>"},
    {"q": "Czy otrzymam numer śledzenia przesyłki?", "a": "<p>Tak. Wysyłamy go mailem, gdy tylko paczka zostanie nadana.</p>"},
])}
guar = {"type": "gx-guarantee", "settings": {"lead": "Przyszedł uszkodzony albo nie działa? Wymienimy go albo oddamy pieniądze. Odesłanie na nasz koszt."}, **blocks("item", [
    {"icon": "lock", "title": "Bezpieczna płatność", "text": "Szyfrowana kasa Shopify"},
    {"icon": "truck", "title": "Śledzona przesyłka", "text": "Numer śledzenia mailem"},
    {"icon": "return", "title": "30 dni na zwrot", "text": "Bez podawania przyczyny"},
    {"icon": "chat", "title": "Obsługa klienta", "text": "Odpowiadamy w 1 dzień roboczy"},
])}
final = {"type": "gx-final", "settings": {"image": img("GALAKTIS_BEDROOM_01.png")}}

def template(order):
    secs = {k: v for k, v in order}
    return {"layout": "galaktis", "sections": secs, "order": [k for k, _ in order]}

index = template([("hero", hero), ("proof", proof), ("ba", ba), ("why", why), ("product", prod_home),
                  ("bundles", bundles_home), ("steps", steps), ("proj", proj), ("uses", uses), ("emo", emo),
                  ("reviews", reviews), ("faq", faq), ("guar", guar), ("final", final)])
product = template([("product", prod_page), ("proof", proof), ("why", why), ("bundles", bundles_page),
                    ("steps", steps), ("proj", proj), ("uses", uses), ("reviews", reviews), ("faq", faq),
                    ("guar", guar), ("final", final)])
page = template([("main", {"type": "gx-page", "settings": {}})])

for name, t in [("index.json", index), ("product.galaktis.json", product), ("product.nocne-niebo.json", product), ("page.galaktis.json", page)]:
    with open("templates/" + name, "w", encoding="utf-8") as f:
        json.dump(t, f, ensure_ascii=False, indent=1)
print("ok")
