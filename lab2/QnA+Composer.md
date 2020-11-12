# Sprawozdanie z lab2 QnA - Build a bot with QnA Maker and Azure Bot Service

## 1. Build a bot with QnA Maker and Azure Bot Service

### 1.1 Opis laboratorium

Aby zabrać się za pracę z QnA service trzeba najpierw stworzyć workspace na Azure za pomocą obiektu Machine Learing. Potem należy przejść do Machine Learning Studio i tam  zacząć od stworznia jednostki oblicznioewj.
Kolejnym krokiem jest stworzenie Cognitive Service na Azure do usługi QnA. Gdy ten krok zostanie zrealizowany następuje proces tworzenia bazy wiedzy. W przypadku laboratorium skorzystano z gotowej bazy, która odpowiadała na pytania związane z informacjami jakie można otrzymać od agencji tursytycznej Margie's Travel ale również jakieś pytania niezwiązane z pyatniem o podróże. Dodałem własne pytanie "Hello" i "Hi" oraz odpiwedź na nie "Hello".
Jednym kliknięciem został wytrenowany serwis i następnie przetestowany przeze mnie co prezentuje poniższe zdjęcie. 

![cennikTA](https://github.com/edsuch21/AI-on-Microsoft-Azure/edit/main/lab2/)

Następnym krokiem jest udostępnienie serwisu i przesłanie go do nowostworzonego bota. Po szybkim stworzeniu bota następuje jego test jak na zdjęciu poniżej.


ZDJECIE

Ostatnim korkiem jest uruchomienie bota na stronie internetwej, co następuje przez prostą komendę html korzystającą ze specjalnego klucza dostępu do bota, który jest dostępny w zakładce Channel w Web App Bot.
Efektem laboratorium jest strona internetowa działająca jak na zdjęciu poniżej.

ZDJĘCIE

### 1.2 Cennik

Za Cogintive Services do QnA płaci się według poniższego cennika:


![CennikCS](https://github.com/edsuch21/AI-on-Microsoft-Azure/edit/main/lab2/Cennik_Cognitive_Service_QnA_maker.png)

Koszty VM do obilczeń w Machine Learing Studio:

![CennikJO](https://github.com/edsuch21/AI-on-Microsoft-Azure/edit/main/lab2/Cennik_jednostki_obilczeniowej.png)

Koszty Bota:

![CennikBota](https://github.com/edsuch21/AI-on-Microsoft-Azure/edit/main/lab2/Cennik_Bota.png)



## 2.  Create a Bot with the Bot Framework Composer

### 2.1 Opis

![CennikBota](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/cennikTA.png)


