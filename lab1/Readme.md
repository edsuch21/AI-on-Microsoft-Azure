# Sprawozdanie z lab1 - Evaluate text with Azure Cognitive Language Services

## 1. Classify and moderate text with Azure Content Moderator
W tej częsci poznano usługę Content Moderator, która służy do analizy tekstu i może działać w trzech wariantach:
- wykrywanie przekleństw
- klasyfikacja testów niewłaściwych
  * użycie słownictwa z zakresu seksulanego
  * nieodpowiednie propozycje o kontekście seksualnym
  * obraza drugiego człowieka
- ochrona danych prywatnych (PII)

W przypadku wykrwania przekleństw sprawdzane jest z listą czy jakiekolwiek słowo jest klasyfikowane jako bluzg i jeśli takie istnieje to zwracany jest JSON z ineksem tego słowa na liście wszytskich słów oraz informacja jakie to słowo. Listę słów można modyfikować.

Klasyfikacja tekstów niewłaściwych określa prawdopodobieństwo czy tekst można zklasyfikować do każdej z wyżej wyminionych klas i po przekroczeniu pewnej wartości progowej zwracana jest informacja, że trzeba zweryfikować tekst ręcznie i pokazane są prawdopodobieństwa klasyfikacji każdej z klas.

W przypadku ochrony danych prywatych jeśli jakies PII zostanie wykryte zostaje utworzony JSON, w którym będzie podana kategoria użycia danych prywatnych jak np. adres email, adres zamieszkania czy numer telefonu oraz fragment tekstu, który został sklasyfikwoany do jednej z tych kategorii.

![cennik Content Moderator](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab1/pricing_Content%20Moderator.png "cenik CM")

W jakich sytuacjach można użyć serwisu? Można np. kontrolować treści postów i komentarzy na jakimś forum/blogu i usuwać niewłaściwe wiadomości. Właściwość ochrony danych prywatych można wykorzystać do blokowania publikowania tych informacji w strefach publicznych platformy, które każdy anonimowy użytkownik może przeglądać.

Aby użyć tego serwisu należy do wybranego resource group dodać Content Moderator, a następnie przestować jego działanie na stornie [Content Moderator - Moderate](https://westus.dev.cognitive.microsoft.com/docs/services/57cf753a3f9b070c105bd2c1/operations/57cf753a3f9b070868a1f66f/console). Wystarczy znaznaczyć co się chce w tekście wpisywanym w oknie poniżej wyszukać oraz podać klucz do stowrzonego wczęsniej serwisu Content Moderator.

## 2.  Add conversational intelligence to your apps by using Language Understanding Intelligent Service (LUIS)
LUIS stara się z prostej wypowiedzi wyciągnąć intencje użytkowanika oraz pewnego rodzaju parametry tych intencji. Intencją zwykle jest jakaś czynność a parametry dostarczają dodatkowych szczegółów, które w pełni kształtują to o co chodziło autorowi wypowiedzi. Ostatecznie sparametryzowane intecje powodują wykonywanie jakichś akcji.

W przypadku LUIS'a możliwe jest kilka akcji na raz takie jak: wyszukiwanie obrazu, udostępnianie obrazu czy zamówienie druku obrazu. 
Aby stowrzyć ten serwis należy utworzyć Language Understanding w wybranej resource group. Następnie należy stworzyć aplikację na stronie https://eu.luis.ai/ i nadać jej nazwę.

Następnym krokiem do tworzenia bota jest utworzenie czynności (intencji) jakie zostały zlecone do wykonania. Czynność musi mieć swoją nazwę przykładowo "ZnajdźZdjęcie". Następnie należy wpisać jakie mogą być przykładowe wypowiedzi użytkowników którzy chcą wyszukać jakieś zdjęcie. Np. "Znajdź zdjęcie pociągu", "Pokaż mi jedzenie", Wyszukaj obraz dziecka" itp.
Następnie tworzy się paramtetry zwane też jednostkami lub encjalmi. Trzeba nadać każdej encji nazwę i najlepiej wykorzystać opcję machine learning do wykrywania paramterów.

Dalej trzeba skojarzyć intencję z parametrami. Żeby czynność wykonywała dokładnie takie polecenie jakie nadaje użytkownik.
Dodatkowo jest też czyność, która nic nie wykonuje, gdy wypowiedzi nie pasują do żadnej intencji. 
Teraz już pozotsaje tylko trenowanie modelu, które odbywa się przyciskiem "Train" oraz stworzenie endpointu by móc korzystać z serwisu. W Azure powstaje Prediction Resource oraz Starter_Key. Następnie przyciskiem "Publish" publikje się endpoint i można przechodzić do testów. Po wybraniu opcji "Test" należy podać przykładowe polecnie/zapytanie i sprawdzić czy czy zadanie zostało poprawnie zorumiane.
W przypadku słabych wyników można ponownie trenować model dla źle przenalizowanych wypowiedzi.

LUIS można wykorzystać do w lobby hotelowym jako room service. Można by prawdopodobnie też wykorzystać w aplikacji do zamawiania taksówek, gdzie można podać miejsce i godzinę odbioru oraz liczbę pasażerów. Można też wykorzystać przy różnego rozdaju transakcjach sprzedaży.

![cennikLU](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab1/cennikLU.png)

## 3. Discover sentiment in text with the Text Analytics API
Text Analytics API jest to rodzaj Cognitive Service, czyli różnego rodzaju wytrenowanych modeli do realizacji różnych zadań na wysokim poziomie. W tym wypadku służy on do analizy tekstu. W przerobionym ćwiczniu pokazane było zastosowanie wariantu z analizą sentymentu.

Należy storzyć obiekt Text Analytics w wybranym resource group. Następnie można skorzystać z gotowego endpointu https://eastus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0 i wybrać w pasku po lewej Sentiment. Należy następnie wybrać lokalizację wcześniej stworzonego RG i podać klucz z Text Analytics.

Teraz można analizować z pliku JSON kilka tekstów jednoczesnie w kliku różych językach i po automatycznym przeranalizowaniu zwracany jest JSON z charakterystycznym dla danego tesktu id oraz wynikiem z przedziału <0, 1>, gdzie 0 to tekst negatywny, a 1 to pozytywny (testy neutrale mają +-0.5).

Jak widać za pomocą Text Analytics można też wykrywać język w jakim dany tekst jest napisany, czy szukać kluczowych słów, lub parametryzować wypowiedzi jak w LUIS.

W tym labolatorium pozanao też jak połączyć Function App, Azure Queue Storage i Text Analytics API by zastosować to do realnych potrzeb z którymi może mierzyć się start-up. Po stworzeniu FA należało stworzyć funckję Azure Queue Storage trigger. Po wporwadzeniu kilku wartości w ustawieniach można już utworzyć funckję i ją przetesować za pomocą przycisku Run. Kolejnym korkiem jest edycja kodu JavaScript tak by dołączyć działanie Text Analytics. W tym kodzie definijuemy że wejściem do analizy sentymentu jest to co jest w kolejce wywoływane przez funkcję. Wynik analizy jest zapisywany do logów.

Działanie tego systemu można przetestować za pomocą przycisku "Test" w funkcjach w Funcjtion App. 
Można też przetestować czy działa kolejka wchodząc do Storage Account i tam tworząc nową widaomość i dodając ją do kolejki. Po pewnym czasie automatycznie następuje analiza wiadomości.

Odpowiednia kalibracja ustawień w JSON w FA oraz zmiana kodu umożliwa nawet podział wiadomości na kategorie: pozytywne, neutralne, negatywne i umieszczenie ich do 3 osobnych kolejek.

Zastosowania TA w analizie sentymentu mogą być przykładowo do oceny recenzji książek lub filmów na jakimś portalu. Analiza charateru tekstu może służyć do badania reportażów czy wypowiedzi autora są stronnicze czy nie. Badanie języka w jakim pisany jest tekst można wykorzytsać do autmatycznego tłumaczenia z dowolnego języka. Wyszukiwanie słów kluczowych pozwoli na łatwe porządkowanie dużych zbiorów tekstów po treści a nie tytule itp.

![cennikTA](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/lab1/cennikTA.png)

