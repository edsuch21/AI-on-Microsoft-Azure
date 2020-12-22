# Cześć praktyczna

## Scenariusz

Mój program umożliwia klasyfikację charateru pisma do danej osoby. Docelowo myślałem, żeby to był serwis pomocny dla wykładowców. Mamy grupę studentów, których mamy próbki pisma np. z kartówki z zajęć. Zdaża się, że studenci zamieniają się pracami na kolokwium i mądry student wypełnia prace kolegów. Biedy wykładowca mając 300 prac do sprawdzenia nie jest w stanie wykryć oszystwa i tu przychodzi rozwiązanie które proponuję.

##Rozwiązanie

* pobranie niewielkiej próbki pisma od 3 osób na takim samym papierze i pisane tym sammym długopisem
* zeskanowanie tesktu i podzielenie go na wycinki pojedynczych słow
* trenowanie modelu multilabel za pomocą servisu Custom Vision
* stworznie skryptu w pythonie z który wysyła zdjęcie przez API do stworzonego w poprzednim kroku  modelu
* testowanie grupy słów z jednego wypracowania (zbiór testowy, nieznany modelowi) i wyciągniecia średniej z wyników dla każdego słowa
* eksperymentalne wyznaczenie thresholdu, który pozwala na poprawną klasyfikację i zmniejsza ryzyko błędu

## Kod

Kod zamieszczono w tym folderze w pliku o nazwie 'script.py'
