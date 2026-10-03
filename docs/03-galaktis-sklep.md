# GALAKTIS: nowy sklep (motyw „GALAKTIS”)

Motyw jest gotowy w Shopify jako **nieopublikowany motyw „GALAKTIS”**. Konektor nie może publikować motywów, więc publikujesz go sam: Sklep online, Motywy, GALAKTIS, Opublikuj.

Podgląd przed publikacją: https://xpii1s-1p.myshopify.com/?preview_theme_id=201873293639

## Struktura strony głównej

1. Pasek ogłoszeń + sticky header (desktop: menu, szukaj, konto, koszyk; telefon: hamburger, logo, koszyk)
2. Hero: na telefonie zdjęcie w tle, nagłówek i CTA na pierwszym ekranie
3. Social proof: zdjęcia kupujących; ocena i liczba opinii ukryte, dopóki nie wpiszesz prawdziwych
4. Przed i po
5. Dlaczego GALAKTIS (6 kart)
6. Produkt: galeria z powiększeniem, warianty 1/2/3 szt., dodanie do koszyka bez przeładowania, akordeony
7. Pakiety: 1×, 2× (najpopularniejszy), 3× (najlepsza wartość)
8. Jak to działa (3 kroki)
9. Projekcje (5 przykładowych motywów)
10. Zastosowania (pokój dziecięcy, gaming room, salon, prezent)
11. Sekcja emocjonalna
12. Opinie
13. FAQ (10 pytań, z danymi strukturalnymi FAQ)
14. Gwarancja / zakup bez ryzyka
15. Końcowe CTA
16. Stopka z newsletterem (formularz klienta Shopify, tag „newsletter”)

Strona produktu ma te same sekcje, z produktem na górze (H1). Strony tekstowe (O nas, Kontakt, Regulamin, Zwroty, Wysyłka, Śledzenie zamówienia) używają szablonu `page.galaktis`.

## Architektura kodu (`galaktis-theme/`)

* `layout/galaktis.liquid`: szkielet strony, SEO, favicon, CSS i JS
* `assets/galaktis.css`: cały wygląd, tokeny kolorów na górze pliku
* `assets/galaktis.js`: menu, koszyk wysuwany, galeria, warianty, sticky, animacje (bez bibliotek)
* `sections/gx-*.liquid`: każda sekcja osobno, wszystkie teksty edytowalne w edytorze motywu
* `snippets/`: logo, ikony, obrazy z placeholderami, gwiazdki, SEO, dane strukturalne produktu, koszyk
* `templates/*.json`: kolejność sekcji i treści; generowane skryptem `build_templates.py`

## Testy (iPhone 13 i desktop 1440 px, podgląd motywu)

* Brak błędów Liquid i błędów JavaScript; brak przewijania w bok
* Działa: menu mobilne, zmiana wariantu (cena i cena przekreślona), koszyk wysuwany, zmiana ilości, przyciski pakietów, sticky pasek, link do kasy
* Wszystkie linki wewnętrzne zwracają 200
* Szybkość na telefonie (symulowane 4G, procesor 4× wolniej): strona główna LCP 1,3 s, produkt LCP 0,8 s

## Uczciwość i miejsca do uzupełnienia

* Ocena, liczba klientów, „Zweryfikowany zakup”: pola istnieją, ale są puste i ukryte. Wpisz tylko prawdziwe dane.
* Opinie na stronie to przetłumaczone opinie kupujących ten sam model; zastąp je swoimi po pierwszych zamówieniach.
* Zdjęcia lifestyle i projekcji są wizualizacjami (Higgsfield); na stronie jest to zaznaczone.
* Czas dostawy 7 do 12 dni roboczych: potwierdź w ofercie dostawcy.
* Nazwa sprzedawcy i NIP w regulaminie, zwrotach i kontakcie: do uzupełnienia.
