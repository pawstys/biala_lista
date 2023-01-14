# biala_lista
Program służy do masowej weryfikacji rachunków bankowych podatników na białej liście VAT.
W związku z ograniczeniami nakładanymi przez udostępione API, źródłem danych są pliki płaskie udostępniane przez Ministerstwo Finansów na stronie:
https://www.podatki.gov.pl/vat/bezpieczna-transakcja/wykaz-podatnikow-vat/plik-plaski/

Aby możliwa była weryfikacja transakcji z danego dnia, należy wypakować archiwum z odpowiednim plikiem do katalogu pliki_json.
Udostępnione przez Ministerstwo Finansów archiwum zawiera dwa pliki: jeden z zaszyfrowanymi danymi z danego dnia oraz drugi z sumą kontrolną pliku z danymi.
Przed wczytaniem pliku program dokonuje weryfikacji sumy kontrolnej. W przypadku ewentualnej niezgodności plik nie zostanie wczytany.
Po pomyślnym zweryfikowaniu pliku źródłowego program importuje zawarte w nim dane do bazy danych SQLite3 'biala_lista.db',
po uprzednim sprawdzeniu czy plik z danego dnia nie został już wcześniej wczytany.

Następnie program przechodzi do weryfikacji płatności.
Zestawienie płatności do weryfikacji należy umieścić w katalogu z programem w pliku Excel wg zamieszczonego wzoru: 'biala_lista.xlsx'.
Podczas weryfikacji program w oparciu o uzupełnione pola 'Data', 'NIP' oraz 'Numer rachunku bankowego' dokonuje sprawdzenia,
czy podany rachunek znajduje się na białej liście podatników VAT z danego dnia, a następnie wynik weryfikacji umieszcza w kolumnie 'Status'.
Program nie ma ograniczeń co do ilości weryfikowanych operacji, wymaga jedynie aby dla weryfikowanych transakcji
zostały wczytane odpowiednie pliki płaskie z danych dni.

Dla funkcji szyfrujących zostały napisane testy sprawdzające poprawność ich działania w oparciu o przykłady podane w specyfikacji technicznej pliku płaskiego
udostępnionej przez Ministerstwo Finansów w linku powyżej. Wyniki tych testów można zweryfikować za pomocą narzędzia pytest.
