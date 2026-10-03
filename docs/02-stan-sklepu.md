# Stan sklepu po wdrożeniu (3.10.2026)

## Zrobione w Shopify
* Produkt „Projektor gwiazd i księżyca” (`/products/projektor-gwiazd`), aktywny w Sklepie online i Shop.
  * 1 projektor: 149 zł, SKU NN-PROJ-12-X1, 0,154 kg, koszt 65,35 zł
  * 2 projektory: 259 zł (przekreślone 298 zł, czyli 2 × 149), SKU NN-PROJ-12-X2, 0,308 kg, koszt 130,70 zł
  * Śledzenie stanu wyłączone, sprzedaż przy braku stanu włączona, szablon `product.nocne-niebo`
  * Koszt liczony od wariantu dostawcy „12 star slices”
* Stary produkt z importu (angielski tytuł, ceny 44 do 77 zł) ustawiony jako wersja robocza.
* Wysyłka: tylko Polska. 14,99 zł poniżej 200 zł, darmowa od 200 zł. Usunięta wysyłka ekspresowa i strefa międzynarodowa.
* Strony: /pages/regulamin, /pages/zwroty, /pages/wysylka, /pages/kontakt.
* Motyw Horizon (nieopublikowany): layout `nocne-niebo`, sekcja `nn-landing`, logo `nn-logo`, szablony `index.json` i `product.nocne-niebo.json`.
* Pliki graficzne nn-*.png w Treści, Pliki.

## Do zrobienia przez Ciebie
1. Opublikuj motyw Horizon (Sklep online, Motywy, Horizon, Opublikuj). Konektor nie ma prawa publikować motywu.
2. Uzupełnij nazwę sprzedawcy i NIP w stronach Regulamin, Zwroty, Kontakt (miejsca w nawiasach kwadratowych).
3. Wklej treści z folderu `polityki/` w Ustawienia, Polityki (konektor nie ma uprawnienia write_legal_policies).
4. Sprawdź czas dostawy na ofercie AliExpress. Jeśli inny niż 7 do 12 dni, zmień go w: ustawieniach sekcji (pole „Czas dostawy”), nazwach stawek wysyłki, stronie Wysyłka, regulaminie §6, FAQ.
5. Podłącz nowy produkt w aplikacji do realizacji zamówień (DSers lub inna) do wariantu „12 star slices”.
6. Obejrzyj grafiki: nie mogłem ich zobaczyć (sieć środowiska blokuje CDN), więc zgodności kształtu produktu nie zweryfikowałem.
