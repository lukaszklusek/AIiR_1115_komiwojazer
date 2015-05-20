# AIiR_1115_komiwojazer

20-05-2015 Zmiany w bazie danych i sposobie obslugi punktow

Dodalem 2 nowe tabele point_in, point_out<br>

Przechowuja one poszczegolne wspolrzedne i ich numer.<br>

Format pliku tekstowego:<br>
Ilosc punktow<br>
Maksymalny punkt (maksymalna wartosc punktu)<br>
x1 y1<br>
...<br>
xN yN<br>




19-05-2015 Wielki commit frontendowy

Dodano:

Obsluga zadan<br>
Wyswietlanie progresu w czasie rzeczywistym<br>

Opis:

-Gdy uzytkownik nie ma zadnych zadan, nalezy przycisnosc przycisk nowe zadanie: Spowoduje to stworzenie, nowego pustego zadania<br>
-W momencie kiedy uzytkownik stworzyl juz jakies zadanie, musi je wystartowacz pliku poruszy to zmodyfikowany przezemnie event, zmodyfikowany w ten sposob, ze po kliknieciu 'rozpocznij algorytm', punkty przypisane sa do stworzonego juz uzytkownika, do pierwszego wolnego zadania.<br>
-Zmiana progress w zadaniu spowoduje przesuniecie sie progres baru.<br>

-Dodatkowo uzytkownik nie moze zaczac nowego zadania dopoki otwarte juz nie zostaly zaczete

<strong>Statusy zadania:</strong>
-waiting<br>
-working<br>
-done</br>

<strong>TODO:  (jeli chodzi o to co potrzebuje do frontendu)</strong>
Przypisanie wyników do osobnej tabeli, tak aby kazdy punkt byl w osobnym wierszu<br>
id_user <-> id_task <->points biggestX, biggestY<br>
<br>
Zmienne biggestX, biggestY, pozwola na przeskalowanie plotna, tak aby bez wzgledu na wielkosc wspolrzednych punkty mogly sie zmiescie.<br>
Pozwoli to na dosc latwe wyswietlanie danych uzytkownikowi i da mozliwosc do zaimplementowania zaznaczania<br>

