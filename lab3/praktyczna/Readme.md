# Bot zastępujący infolinię sanepidu do spraw COVID-19

## 1. Use case

Jest to chat bot, który potrafi wymienić symptomy zarażenia koronawirusem, podać podstawowe informacje o dostępnych testach i poradzić co robić gdy ma się objawy. Gdy bot czegoś nie rozumie to komunikuje to i radzi skorzystać z komendy help, która tłumaczy działanie bota. 

## 2. Wykonane kroki

Bot zbudowano w narzędziu Bot Framework Composer z użyciem servisu LUIS. Wykorzystano wyzwalacze w zależności od tego o co zapyta użytkownik.

## 3. Architektura

Na początku architektury jest schemat pokazujący, że jeśli zaloguje się użytkownik to jest on witany przez bota. Oprócz tego jest 5 różnych wyzwalaczy.
Wyzwalacz help jest uruchamiany komendą zgłaszającą potrzebę pomocy typu "help" lub "what is this bot for". Po takiej komendzie pokazuje się odpowiedź jaka jest funkcjonalność bota.
Wyzwalacz Unknown intent uaktywnia się wtedy, gdy użytkownik wpiszę wypowiedź, której nie był w stanie zakwalifikowac do żadnego innego wyzwalacza. Pojawia się komunikat, że wypoiwedź jest nie zrozumiała i należy wpisać "help" by dowiedzieć się jakie jest przeznacznie bota.
Wyzwalacz covidSymptoms uaktywania się gdy ktoś spyta jakie są sympotmy. Bot wypisuje objawy i pyta się czy u użytkownika wystąpiły wszytskie objawy (wykorzystanie multi-choice question). Następnie jest instrukcja warunkowa zależna od odopowiedzi na zadane pytanie i pojawiają się różne komunikaty.
Wyzwalacz userSympotms uaktywania się gdy ktoś zaczyna podawać swoje objawy lub mówi, że jest chory. Pojawia sie wtedy pytanie od bota i instrukcja warunkowa w zależności od odpowiedzi.
Wyzwalazcz COVIDtest uaktywania się gdy użytkownik pyta o testy na koronawirusa. Informuje, że można dostać sierowanie na darmowy test tylko jeśli ma się wszytskie objawy i pyta się czy użytkownik chce poznać informacje o testach komercyjnych. Następuje instrukcja warunkowai odpowiedź jest udzielana albo nie.

## 4. Kod

kod znajduje się w tym folderze w pliku bot.json

