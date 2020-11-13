# Sprawozdanie z lab2 QnA - Build a bot with QnA Maker and Azure Bot Service

## 1. Build a bot with QnA Maker and Azure Bot Service

### 1.1 Opis laboratorium

Aby zabrać się za pracę z QnA service trzeba najpierw stworzyć workspace na Azure za pomocą obiektu Machine Learing. Potem należy przejść do Machine Learning Studio i tam  zacząć od stworznia jednostki oblicznioewj.
Kolejnym krokiem jest stworzenie Cognitive Service na Azure do usługi QnA. Gdy ten krok zostanie zrealizowany następuje proces tworzenia bazy wiedzy. W przypadku laboratorium skorzystano z gotowej bazy, która odpowiadała na pytania związane z informacjami jakie można otrzymać od agencji tursytycznej Margie's Travel ale również jakieś pytania niezwiązane z pyatniem o podróże. Dodałem własne pytanie "Hello" i "Hi" oraz odpiwedź na nie "Hello".
Jednym kliknięciem został wytrenowany serwis i następnie przetestowany przeze mnie co prezentuje poniższe zdjęcie. 

![TestSerwsu](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab2/TestSerwisu.png)

Następnym krokiem jest udostępnienie serwisu i przesłanie go do nowostworzonego bota. Po szybkim stworzeniu bota następuje jego test jak na zdjęciu poniżej.

![TestBota](https://raw.githubusercontent.com/AI-on-Microsoft-Azure/main/lab2/TestBota.png)


Ostatnim korkiem jest uruchomienie bota na stronie internetwej, co następuje przez prostą komendę html korzystającą ze specjalnego klucza dostępu do bota, który jest dostępny w zakładce Channel w Web App Bot.
Efektem laboratorium jest strona internetowa działająca jak na zdjęciu poniżej.

![TestStrony](https://raw.githubusercontent.com/AI-on-Microsoft-Azure/main/lab2/TestStrony.png)

### 1.2 Cennik

Za Cogintive Services do QnA płaci się według poniższego cennika:


![CennikCS](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab2/Cennik_Cognitive_Service_QnA_maker.png)

Koszty VM do obilczeń w Machine Learing Studio:

![CennikJO](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab2/Cennik_jednostki_obilczeniowej.png)

Koszty Bota:

![CennikBota](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab2/Cennik_Bota.png)

### 1.3 Use case

Takiego bota można użyć w informacji turystycznej w biurze podróży na dowolnej stronie internetowej posiadającej czat, który pyta jak możemy ci pomóc. Często taki czat na stronie będzie pomagał korzytsać z nowoczesnego produktu o skomplikowanym działaniu lub będzie to czast doradzający przy zakupach.

## 2.  Create a Bot with the Bot Framework Composer

### 2.1 Opis

Composer to program umożliwiający budowanie grafu sekwencji działania bota. W pierwszej części pokazano prostego bota, który pyta o imię i wita użytkownika wyświetlając jego imię. Pytanie i odpowiedź to osobne bloki w grafie występujące po sobie. Narzędzie to wykorzytsuje jednak silne narzędzia i bardzo łatwo można też tworzyć bardziej skomplikowane zadania jak np. opisywanie pogody na podstawie podanego kodu pocztowego z USA.
W drugiej części pokazano jak można wykorzystać metody http (w tym wypadku metodę get) i przy pomocy klucza api otrzymać informacje z odpowiedniego serwera. Pokazano jak działają wyzwalacze, które powodują przejście do nowego grafu. Korzytano z triggerów: weather, cancel i help. Można było w ten sposób przejść do grafu sprawdzającego pogodę, grafu pomocy lub grafu kończącego pracę bota.
W ćwiczeniu również pokazano zasadę dziąłania Language Generation Library, które umożliwia rożnorodność wypowiedzi w takiej samej sytucaji (przez to robot wydaje się być bardziej ludzki) oraz warunkowe odpowiedzi. np. jeśli pogoda == pada deszcz, to można wyświetlić "lepiej weź parasol, bo na dworze pada ;)".
Ciekaawą opcją jest też możliwość przyciskania guzików na czacie. Zamiast wpisywać "help" można poprostu kliknąć na niego. Jak również bot może odpowiadać za pomocą mini kart z odpowiedzią. Dzięki temu odpowiedź jest łatwiejsza do odczytania.
W Composer'ze można też wykorzystać LUIS poznany w poprzednim laboratorium do analizy intencji i parametrów wypowiedzi. Dzięki temu nie trzeba tworzyć bazy z każdą możliwą wypowiedzią użytkownika tylko określane jest prawdopodobieństwo danej intencji i wartości parametrów.

Emulator pokazuje jakie operacje są wykonywane "pod spodem" podczas działania robota jak również pokazuje jak działa sam robot.

### 2.2 Cennik

Samo tworzenie bota w Composerze nic nie kosztuje. Nawet nie trzeba mieć konta na Azure. Płaci się jedynie za LUIS, jeśli się z niego korzysta. Cennik Luisa poniżej:

![CennikLUIS](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab1/cennikLU.png)

### 2.3 Use Case

Zastosowanie takie samo jak w przypadku punktu 1.3


