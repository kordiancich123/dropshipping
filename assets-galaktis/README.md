# GALAKTIS: biblioteka materiałów wizualnych

## 1. Research (co zostało przeanalizowane)

* **TikTok @thegalix_:** 232 filmy, przeanalizowane klatki 5 najpopularniejszych (6 do 64 mln wyświetleń). Pobrane tylko lokalnie do analizy, nieużyte w materiałach.
* **Sklep thegalix.com:** struktura i teksty (analiza w `docs/01-analiza-i-uklad.md`).
* **Prawdziwe zdjęcia klientów** naszego dostawcy (projekcja na suficie): użyte jako wzorzec realizmu projekcji.

### Najważniejsze wnioski

1. **Galix sprzedaje dokładnie ten sam projektor** (biała kapsuła na giętkiej szyjce, slajdy we wkładkach). Ich materiały pokazują więc realny wygląd naszego produktu.
2. **Dlaczego ich filmy wyglądają prawdziwie:** bo są prawdziwe. Telefon w ręce, żarówkowe ciepłe światło, projektor wpięty w ładowarkę przy łóżku, ręka z prawdziwymi paznokciami, bałagan na stoliku, nierówny kadr.
3. **Powtarzalna struktura wiralowego filmu (14 do 22 s):**
   1. zbliżenie projektora w świetle pokoju,
   2. ręka wybiera slajd ze stosu i wsuwa go,
   3. pstryk wyłącznika, ciemność,
   4. ujęcie sufitu z bliska, kamera powoli płynie po księżycu.
4. **Hook zawsze tekstem na górze kadru**, emocjonalny i o konkretnej osobie („If you're afraid of the dark…”, „Every boy mom needs this”), bez lektora.
5. **Projekcja wygląda na ogromną, bo kamera jest blisko sufitu.** W szerokim kadrze to jeden okrągły obraz. Nasze materiały pokazują go uczciwie.

## 2. Kierunek wizualny GALAKTIS

* **Styl:** dobry współczesny smartfon, nie studio. Szum ISO, lekko krzywy kadr, światło lampki, monitora albo samego projektora.
* **Wnętrza:** zwykłe mieszkania (szklanka wody, książka, ładowarka, pognieciona pościel). Bez „Pinterest bedroom”.
* **Produkt:** zawsze ten sam. Referencje: `GALAKTIS_PRODUCT_01` (packshot) i zdjęcia dostawcy. Wkładki slajdów mają kształt małej kłódki z okrągłym okienkiem.
* **Projekcja:** jeden okrągły obraz z miękkimi krawędziami, jasność spada w ciemność. Nigdy galaktyka na cały pokój.
* **Kolory marki:** granat i czerń, biel, delikatny fiolet i niebieski. Ciepłe światło pokoju jako kontrast.

## 3. Mastery i pochodne

| Asset | Plik | Gdzie użyty |
|---|---|---|
| GALAKTIS_HERO_01 | masters/GALAKTIS_HERO_01.png | hero strony, końcowe CTA, reklamy |
| GALAKTIS_BEDROOM_01 | masters/GALAKTIS_BEDROOM_01.png | zastosowania: sypialnia, reklamy young adult |
| GALAKTIS_PRODUCT_CLOSEUP_01 | masters/GALAKTIS_PRODUCT_CLOSEUP_01.png | galeria produktu, „dlaczego” |
| GALAKTIS_UGC_01 | masters/GALAKTIS_UGC_01.png | krok 2 „jak to działa”, reklamy UGC |
| GALAKTIS_GIFT_01 | masters/GALAKTIS_GIFT_01.png | zastosowania: prezent, reklamy prezentowe |
| GALAKTIS_GAMING_01 | wcześniejszy gaming room | zastosowania: gaming |
| GALAKTIS_BEFORE_02 | masters/GALAKTIS_BEFORE_02.png | sekcja „Przed i po”: sypialnia przy żółtej lampce, projektor wyłączony |
| GALAKTIS_AFTER_02 | masters/GALAKTIS_AFTER_02.png | sekcja „Przed i po”: ten sam kadr, lampka zgaszona, jedna okrągła projekcja na suficie |
| GALAKTIS_KIDS_01 / BEFORE_01 | wcześniejsze kadry pokoju dziecka | pokój dziecięcy |

Formaty (16:9, 1:1, 4:5, 9:16) to przycięcia mastera w `crops/`, nie nowe generacje.

### Zdjęcia „Jak to działa” (jedna sesja, ta sama sypialnia)

| Asset | Plik | Gdzie użyty |
|---|---|---|
| GALAKTIS_STEP_01_CONNECT | masters/…_STEP_01_CONNECT.png (2k, 16:9) | krok 1 „Podłącz GALAKTIS”: dłoń wkłada wtyk USB szyjki do ładowarki |
| GALAKTIS_STEP_02_CHOOSE | masters/…_STEP_02_CHOOSE.png | krok 2 „Wybierz projekcję”: dłoń wsuwa slajd, projekcja na suficie |
| GALAKTIS_STEP_03_ENJOY | masters/…_STEP_03_ENJOY.png (master sesji) | krok 3 „Ciesz się galaktyką”: osoba w łóżku patrzy na sufit |
| GALAKTIS_STEP_03_VIDEO | video/GALAKTIS_STEP_03_VIDEO.mp4 | 6 s powolnego najazdu kamery na master (ffmpeg, 0 kredytów) |

Formaty 16:9, 4:5 i 1:1 w `crops/`; 4:5 i 1:1 przycięte z przesunięciem na produkt. W sklepie wgrane wersje 1:1, bo sekcja kroków ma kwadratowe kadry.
Uwaga produktowa: GALAKTIS nie ma gniazda kabla. Szyjka kończy się własnym wtykiem USB, dlatego krok 1 pokazuje wkładanie wtyku do ładowarki, a krok 2 wsuwanie slajdu (jedyny realny „wybór projekcji”).
Odrzucone w kontroli jakości: pierwsza wersja ENJOY (wymyślona podstawka i dodatkowy kabel) i pierwsza wersja CONNECT (wtyk w dłoni niepołączony z szyjką). Obie poprawione edycją, bez nowych generacji od zera. Koszt: 5 generacji gpt_image_2_5 high 2k.

## 4. Wideo i gotowe reklamy

| Plik | Co to jest | Gdzie użyty |
|---|---|---|
| video/GALAKTIS_VIDEO_HERO_01.mp4 | 5 s, sypialnia nocą, projekcja księżyca, kamera lekko płynie (Kling) | tło hero (Shopify: Pliki, wideo), reklamy |
| video/GALAKTIS_VIDEO_HERO_01_web.mp4 | lekka wersja 200 KB | zapasowa do strony |
| video/GALAKTIS_VIDEO_POV_01.mp4 | 5 s, POV z łóżka, projekcja na suficie (Kling) | reklamy „po 22:00” |
| ads/GALAKTIS_AD_01_POV_9x16.mp4 | 10 s, hook „POV: odkrywasz, czego brakowało w Twoim pokoju” | TikTok, Reels, Meta 9:16 |
| ads/GALAKTIS_AD_02_SUFIT_9x16.mp4 | 10 s, „Wsuwasz slajd. Gasisz światło.” → „Poczekaj, aż zobaczysz sufit” | TikTok, Reels, Meta 9:16 |
| ads/GALAKTIS_AD_03_PO22_9x16.mp4 | 10 s, „Mój pokój po 22:00” | TikTok, Reels |
| ads/GALAKTIS_AD_05_PRZED_PO_9x16.mp4 | 9,5 s, „Mój pokój wieczorem” → „Klik. I to samo miejsce.” (BEFORE_02 → AFTER_02) | TikTok, Reels, Meta 9:16 |
| ads/GALAKTIS_AD_04_PREZENT_9x16.mp4 | 9,5 s, „Prezent dla kogoś, kto ma już wszystko” | Meta, sezon prezentowy |

Reklamy składa skrypt `make_ads.sh` (ffmpeg, 0 kredytów): zmień tekst hooka i uruchom ponownie. Każda kończy się planszą: logo, „od 149 zł · dostawa 7 do 12 dni”, „Kup teraz”. Muzykę dodaj w aplikacji TikTok lub Meta (licencjonowana biblioteka platformy).

**Odrzucone:** GALAKTIS_VIDEO_TRANSFORMATION_01 (MiniMax). Lampka zamieniała się w projektor, widoczne nierealne promienie, gwiazdy na całym suficie. Nie pokazuje prawdziwego działania produktu, więc nie trafiło do sklepu ani reklam.

### Rozmieszczenie w sklepie

* Hero: GALAKTIS_HERO_01 (zdjęcie, ładuje się od razu) + GALAKTIS_VIDEO_HERO_01 (włącza się po załadowaniu strony; nie przy oszczędzaniu danych i ograniczonym ruchu)
* Galeria produktu: PRODUCT_CLOSEUP_01, HERO_01, UGC_01, GIFT_01, BEDROOM_01
* Jak to działa, krok 2: UGC_01
* Zastosowania: sypialnia BEDROOM_01, prezent GIFT_01, pokój dziecięcy, gaming, salon (wcześniejsze kadry)
* Końcowe CTA: BEDROOM_01

### Koszt kredytów Higgsfield

Mastery i poprawki około 3,5; wideo Kling 2 × 7,5; MiniMax 10 (odrzucone). Razem około 28,5 kredytu. Upscale nie był potrzebny: mastery mają 2k, a sklep wyświetla maksymalnie 1500 px.

## 5. Uczciwość reklam (ważne przed publikacją)

* **Materiały są wygenerowane przez AI.** TikTok i Meta wymagają oznaczenia realistycznych treści AI (na TikToku przełącznik „AI-generated content”). Bez oznaczenia grozi usunięcie filmu albo blokada konta reklamowego.
* **Hooków „To nie jest filtr” i „To wygląda jeszcze lepiej na żywo” używaj tylko z prawdziwym nagraniem** projektora. Z materiałem AI byłyby wprowadzaniem w błąd.
* **Najlepszy materiał zrobisz sam za 0 zł:** zamów 1 projektor i nagraj telefonem schemat z punktu 1.3. Takie wideo wygrywa z każdym AI w kosztach i zaufaniu.

## 6. Koncepty: 10 TikTok, 10 Reels, 10 Meta Ads

Każdy koncept składa się z gotowych assetów: inny hook, napisy, crop, tempo i CTA. Bez nowych generacji.

### TikTok (9:16, tekst u góry, bez lektora, 8 do 15 s)

1. **„POV: odkrywasz, czego brakowało w Twoim pokoju”:** VIDEO_HERO_01, cięcie na sufit.
2. **„Poczekaj, aż zobaczysz sufit”:** UGC_01 (wsuwanie slajdu), potem VIDEO_HERO_01.
3. **„Każdy rodzic przedszkolaka potrzebuje tego wieczorem”:** BEFORE_01 → KIDS_01 (przejście zdjęć), potem VIDEO_HERO_01.
4. **„Mój pokój po 22:00”:** VIDEO_POV_01, wolne tempo, muzyka lo-fi.
5. **„Zgadnij, ile kosztuje ten klimat”:** HERO_01, odliczanie, „149 zł”.
6. **„Prezent dla kogoś, kto ma już wszystko”:** GIFT_01, potem projekcje (galeria motywów).
7. **„Setup gamingowy: ostatni element”:** GAMING_01 + projekcja galaktyki.
8. **„12 slajdów, 12 wieczorów”:** szybki montaż kafli projekcji, 0,6 s na kadr.
9. **„Zamieniłem lampkę nocną na to”:** przed i po (BEFORE_01 i KIDS_01).
10. **„Bez aplikacji, bez baterii, wystarczy USB”:** UGC_01 + CLOSEUP_01, napisy krok po kroku.

### Instagram Reels (9:16, bardziej estetyczne, wolniejsze cięcia)

1. „Twój pokój po zmroku wygląda zupełnie inaczej”: VIDEO_HERO_01 w całości.
2. „Wieczorny rytuał, który zastąpił scrollowanie”: VIDEO_POV_01.
3. „Mały przedmiot, duża zmiana klimatu”: CLOSEUP_01 → HERO_01.
4. „Kino domowe pod gwiazdami”: kadr salonu + projekcja księżyca.
5. „Prezent, który zostaje na dłużej”: GIFT_01, ciepłe kolory.
6. „Jeden projektor. Niezliczone klimaty.”: karuzela projekcji.
7. „Przed / po”: BEFORE_01 i KIDS_01 jako przesuwany slider.
8. „Pokój dziecka bez walki o zgaszenie światła”: BEFORE_01 → KIDS_01, wolne przenikanie.
9. „Gaming setup, level: kosmos”: GAMING_01.
10. „3 kroki do własnej galaktyki”: kroki ze strony jako Reel.

### Meta Ads (9:16 i 4:5 oraz 1:1; zawsze cena i CTA „Kup teraz”)

1. **AD 01, „POV: odkrywasz, czego brakowało w Twoim pokoju”:** VIDEO_HERO_01, 4:5.
2. **AD 02, „Twój pokój po zmroku wygląda zupełnie inaczej”:** HERO_01, statyczna.
3. **AD 03, „Poczekaj, aż zobaczysz sufit”:** UGC_01 → HERO_01, 9:16.
4. **AD 04, przed i po:** BEFORE_01 i KIDS_01 obok siebie, 1:1.
5. **AD 05, reakcja na produkt:** VIDEO_POV_01, 9:16.
6. **AD 06, reakcja na prezent:** GIFT_01 + „2 szt. za 259 zł, darmowa dostawa”.
7. **AD 07, gaming setup:** GAMING_01, 4:5.
8. **AD 08, transformacja sypialni:** BEDROOM_01 + VIDEO_POV_01, 9:16 (docelowo prawdziwe nagranie „światło zgaszone, sufit”).
9. **AD 09, close-up i projekcja:** CLOSEUP_01 + kafel projekcji, karuzela 1:1.
10. **AD 10, styl rekomendacji UGC:** UGC_01 + napisy „kupiłam, polecam, bo…” (tylko z prawdziwą opinią klienta).

## 7. Hooki (po polsku)

* „Zobacz, co zrobiłam z pokojem w kilka sekund.”
* „Poczekaj, aż zobaczysz sufit.”
* „POV: zamieniasz pokój w galaktykę.”
* „Najbardziej klimatyczna rzecz, jaką kupiłam do pokoju.”
* „Twój pokój tego potrzebuje.”
* „Nie wiedziałam, że mój pokój może tak wyglądać.”
* „Wieczór bez walki o zgaszenie światła.”
* „12 slajdów. Jeden port USB. Zero aplikacji.”
* Tylko z prawdziwym nagraniem: „To nie jest filtr.”, „Na żywo wygląda jeszcze lepiej.”
