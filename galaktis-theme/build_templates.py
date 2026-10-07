"""Generuje templates/*.json motywu GALAKTIS. Treści edytujesz tutaj albo w edytorze motywu."""
import json

img = lambda n: f"shopify://shop_images/{n}"

def blocks(kind, items):
    b = {f"{kind}{i+1}": {"type": kind, "settings": s} for i, s in enumerate(items)}
    return {"blocks": b, "block_order": list(b)}

hero = {"type": "gx-hero", "settings": {"image": img("GALAKTIS_HERO_01.png"), "video": "shopify://files/videos/GALAKTIS_VIDEO_HERO_01.mp4"}}
proof = {"type": "gx-proof", "settings": {"text": "12 slajdów w zestawie · zasilanie z USB · 30 dni na zwrot"}}
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
    {"image": img("GALAKTIS_STEP_01_CONNECT.jpg"), "ph": "WTYK USB WKŁADANY DO ŁADOWARKI, 1:1", "title": "Podłącz GALAKTIS", "text": "Wtyk USB do ładowarki, powerbanku albo laptopa."},
    {"image": img("GALAKTIS_STEP_02_CHOOSE.jpg"), "ph": "SLAJD WSUWANY DO PROJEKTORA, 1:1", "title": "Wybierz projekcję", "text": "Wsuń jeden z 12 slajdów i włącz tryb gwiazd albo lampki."},
    {"image": img("GALAKTIS_STEP_03_ENJOY.jpg"), "ph": "PROJEKCJA NA SUFICIE W CIEMNYM POKOJU, 1:1", "title": "Ciesz się galaktyką", "text": "Zgaś światło, wygnij szyjkę w stronę sufitu i ustaw ostrość."},
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
def mixed(*groups):
    b, order = {}, []
    for kind, items in groups:
        for i, st in enumerate(items):
            k = f"{kind}{i+1}"; b[k] = {"type": kind, "settings": st}; order.append(k)
    return {"blocks": b, "block_order": order}

# ─────────────────────────────────────────────────────────────────────────────
# OPINIE: jedno miejsce do podmiany.
# sampleReview=True  → treść przykładowa do projektu, widoczna TYLKO w edytorze motywu.
# sampleReview=False → prawdziwa opinia, widoczna w sklepie.
# verified=True tylko przy potwierdzonym zamówieniu w sklepie GALAKTIS.
# featured=True → pierwsza widoczna taka opinia trafia do dużej karty.
# ─────────────────────────────────────────────────────────────────────────────
SRC = "Opinia o tym samym modelu z platformy producenta, przetłumaczona. Nie jest to zamówienie w sklepie GALAKTIS."
REVIEWS = [
    # przykładowe (tylko edytor)
    {"sampleReview": True, "featured": True, "rating": 5, "topic": "Efekt wow", "name": "Natalia S.", "date": "12.09.2026",
     "text": "Pierwszy raz włączyłam go przy zapalonym świetle i pomyślałam: no, takie sobie. Potem zgasiłam lampę i zrozumiałam, o co chodzi. Siedziałam chyba kwadrans i tylko patrzyłam w sufit."},
    {"sampleReview": True, "rating": 5, "topic": "Atmosfera", "name": "Ola K.", "date": "03.09.2026", "image": "GALAKTIS_SP_BEDROOM.jpg",
     "text": "Mój pokój wieczorem wyglądał jak poczekalnia. Teraz zamiast górnego światła włączam księżyc na suficie i od razu inaczej się tu siedzi."},
    {"sampleReview": True, "rating": 5, "topic": "Prezent", "name": "Marcin W.", "date": "28.08.2026",
     "text": "Kupiłem bratu na szesnastkę. Myślałem, że to gadżet na tydzień, a stoi u niego przy łóżku od dwóch miesięcy."},
    {"sampleReview": True, "rating": 4, "topic": "Sypialnia", "name": "Karolina M.", "date": "21.08.2026",
     "text": "Włączam go zamiast scrollowania przed snem. Jasność da się zmniejszyć przytrzymaniem przycisku, co było dla mnie ważne. Gwiazdka mniej, bo slajdy zmienia się ręcznie."},
    {"sampleReview": True, "rating": 5, "topic": "Gaming", "name": "Kuba", "date": "14.08.2026", "image": "GALAKTIS_SP_GAMING.jpg",
     "text": "Podpięty do USB w monitorze. W trakcie gry nie przeszkadza, a znajomi pytają o niego jako pierwsze."},
    {"sampleReview": True, "rating": 5, "topic": "Pokój dziecięcy", "name": "Ania P.", "date": "09.08.2026",
     "text": "Syn (6 lat) sam wybiera slajd na wieczór. Wygrywa Saturn. Wyłączamy, kiedy zaśnie."},
    {"sampleReview": True, "rating": 4, "topic": "Jakość", "name": "Tomek R.", "date": "30.07.2026",
     "text": "Obudowa matowa, nie wygląda tanio, szyjka trzyma pozycję. Dwa slajdy na dwanaście są mniej ostre, reszta wygląda dobrze."},
    {"sampleReview": True, "rating": 5, "topic": "Prosta obsługa", "name": "Ewa", "date": "22.07.2026", "image": "GALAKTIS_SP_IN_HAND.jpg",
     "text": "Wtyczka do ładowarki, slajd, dotknięcie przycisku. Tyle."},
    # prawdziwe opinie (widoczne w sklepie): kupujący ten sam model u producenta
    {"sampleReview": False, "featured": True, "rating": 5, "topic": "Jakość", "name": "Kupujący z Hiszpanii", "source": SRC,
     "text": "Świetny i piękny, najbardziej podobają mi się czarno-białe obrazy. Ostrość da się regulować, a projektor działa też jako lampka nocna z przyciskiem dotykowym. Minus: każdy slajd trzeba zmieniać ręcznie. Daję 9 na 10."},
    {"sampleReview": False, "rating": 4, "topic": "Pokój dziecięcy", "name": "Kupujący z Arabii Saudyjskiej", "source": SRC,
     "text": "Za tę cenę dobry produkt. Kilka slajdów jest mniej wyraźnych, ale da się z tym żyć. Córka jest zadowolona."},
    {"sampleReview": False, "rating": 5, "topic": "Atmosfera", "name": "Kupujący z Holandii", "source": SRC,
     "text": "Bardzo ładny efekt."},
]

def review_block(r):
    st = {"sample_review": r["sampleReview"], "featured": r.get("featured", False), "rating": r["rating"],
          "topic": r["topic"], "text": r["text"], "name": r["name"], "date": r.get("date", ""),
          "verified": r.get("verified", False), "source": r.get("source", "")}
    if r.get("image"): st["image"] = img(r["image"])
    return st

GALLERY = [
    ("GALAKTIS_HERO_01.png", "Sypialnia nocą"),
    ("GALAKTIS_SP_CLOSEUP.jpg", "Na stoliku nocnym"),
    ("GALAKTIS_SP_BEDROOM.jpg", "Projekcja na suficie"),
    ("nn-hero.png", "Pokój dziecięcy"),
    ("GALAKTIS_SP_GAMING.jpg", "Pokój do grania"),
    ("GALAKTIS_SP_IN_HAND.jpg", "W dłoni, ze slajdem"),
]

reviews = {"type": "gx-reviews", "settings": {
    "announcement": "Opinie",
    "heading": "Zobacz, co mówią o GALAKTIS",
    "lead": "Prawdziwe wrażenia z wieczorów w różnych pokojach. Bez upiększania, razem z minusami.",
    "feat_image": img("GALAKTIS_SP_FEATURED_EXPERIENCE.jpg"),
    "feat_alt": "Osoba leży w łóżku i patrzy na projekcję na suficie, obok projektor GALAKTIS",
    "feat_image_label": "Wizualizacja",
    "gallery_heading": "GALAKTIS w różnych przestrzeniach",
    "gallery_note": "Wizualizacje produktu",
    "grid_heading": "Doświadczenia",
    "note": "Opinie widoczne w sklepie pochodzą od osób, które kupiły ten sam model projektora u producenta. Przetłumaczyliśmy je bez zmian w treści. Opinie klientów GALAKTIS pojawią się tu po pierwszych zamówieniach.",
    "cta_heading": "Teraz czas na Twoją galaktykę.",
    "cta_text": "Zobacz, co GALAKTIS może zmienić w Twoim pokoju.",
    "cta_label": "Odkryj GALAKTIS", "cta_link": "#produkt",
}, **mixed(
    ("review", [review_block(r) for r in REVIEWS]),
)}
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
                  ("bundles", bundles_home), ("proj", proj), ("emo", emo),
                  ("reviews", reviews), ("faq", faq), ("guar", guar), ("final", final)])
product = template([("product", prod_page), ("proof", proof), ("why", why), ("bundles", bundles_page),
                    ("proj", proj), ("reviews", reviews), ("faq", faq),
                    ("guar", guar), ("final", final)])
page = template([("main", {"type": "gx-page", "settings": {}})])

for name, t in [("index.json", index), ("product.galaktis.json", product), ("product.nocne-niebo.json", product), ("page.galaktis.json", page)]:
    with open("templates/" + name, "w", encoding="utf-8") as f:
        json.dump(t, f, ensure_ascii=False, indent=1)
print("ok")
