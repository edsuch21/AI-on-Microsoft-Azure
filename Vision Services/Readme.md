# Sprawozdanie - teoria

## 1. Copmuter Vision API

### Opis

W tym serwisie istnieje dużo funckjonalności klasyfikacji ludzkich twarzy. Oprócz typowego wykrywania na fotografii twarzy istnieje też możliwość badania wieku danej osoby, emocji jakie jej towarzyszą a nawet rozróżniania osób w grupie i określania czy na danym zdjęciu znajduje się osoba X czy tylko osoba do niej podobna a może wcale nie podobna. Usługa może też wykrywać płeć, natężenie uśmiechu a nawet podać informacje o 27 szczegółach naszej twarzy (lokalizacje 27 części twarzy). Dzięki temu że serwis jest dostępny przez API to dzięki paczkom azurowym można go łatwo wykorzytstywać w skryptach w językach Pyhton i C#. 

Oprócz bardzo rozwiniętej opcji detekcji i fory opisu twarzy na obrazie usuługa ta umożliwa też analizy innych obrazów. Dzięki niej można odpowiednio otagować obraz w zależnośći od kategori obrazu na której chcemy się skoncentrować. Można uzysakć tagi widoku górskiego krajobrazu lub opis rodzinnego zdjęcia.

Usługa też umożliwia inteligente tworzenie miniatur tak, by zachowywać z obrazu jak najwięcej istotnych informacji (przykładowo może trochę przyciąć nieistotne tło).

Usługa ta pozwala również na wykrywanie tekstow na obrazach. Nie tylko liter drukowanych ale również pisanych ręcznie.

### Zastosowania

* Serwisu można użyć do wyszukiwania niebezpiecznych przestępców na nagraniach video z publicznych kamer np. na lotnisku.
* Serwisu czytające pismo ręczne można użyć do digitalizacji notatek a w szczególności długich rówanań matematycznych, których wpisywanie do kopmutera to udręka.
* Serwsiu wyznaczającego tagi do danego zdjęcia można użyć wyszukiwać informacji co jest na danym obrazie (w przypadku malowidła kto go namalował a w przypadku pięknego pejzażu w jakim regionie zostało wykonanne jego zdjęcie.

### Cennik

![](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/Vision%20Services/Computer%20Vision%20API.png)

## 2. Custom Vision

### Opis

Dzięki temu serwisowi istnieje możliwość trenowania klasyfikatorów (lub detektorów) obrazów na bardzo małym zbiorze danych (od 5 obrazów w każdej klasie). Można też łatwo dotrenowywać model dodając nowe dane treningowe bez konieczności trenowania całego modelu od początku. Ten serwis daje bardzo dobre wyniki a trenowanie odbywa się w przejrzystej aplikacji webowej. Usługa ma też opcje połaczenia przez endpointy, więc łatwo z niej korzytsać w dowolnym środowisku. Dzięki API można zarówno trenować jak i testować modele.

### Zastosowania

Można wytrenować model do rozróżniania charakteru pisma studentów i sprawdzać czy ich praca jest samodzielna.

### Cennik

![](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/Vision%20Services/Custom%20Vison.png)


## 3. Video Indexer

### Opis

Servis ten służy do analizy filmów. Dzięki niemu istnieje możliwość wysukania wycinku z filmu gdzie pojawia się nawiazanie do iteresującego nas hasła. Cały film może zostać poddany analizie i w wyniku można otrzymać co pojdwiło sie w fimie i których odcinkach czasu. W filmach istnieje możliwość modyfickajcji listy haseł, które zostały wykryte dla danego filmu, gdy uważamy np, że dane hasło nie pasuje do filmu. Istnieje też możliwość wybory miniatury dla danego filmu. Usługa dostępna również przez API, więc może być wykorzystywana w różnych środowiskach.

### Zastosowania

Gdy mamy długi film możemy szybko wyszukać to czego w nim szukamy. Można np. przeprowadzić badanie ile motorów przejeżdża daną ulicą w ciągu doby.

### Cennik

![](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/Vision%20Services/Video%20Indexer.png)
