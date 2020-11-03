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

![cennik Content Moderator](https://raw.githubusercontent.com/edsuch21/AI-on-Microsoft-Azure/main/pricing_Content%20Moderator.png "cenik CM")

W jakich sytuacjach można użyć serwisu? Można np. kontrolować treści postów i komentarzy na jakimś forum/blogu i usuwać niewłaściwe wiadomości. Właściwość ochrony danych prywatych można wykorzystać do blokowania publikowania tych informacji w strefach publicznych platformy, które każdy anonimowy użytkownik może przeglądać.

Aby użyć tego serwisu należy do wybranego resource group dodać Content Moderator, a następnie przestować jego działanie na stornie [Content Moderator - Moderate](https://westus.dev.cognitive.microsoft.com/docs/services/57cf753a3f9b070c105bd2c1/operations/57cf753a3f9b070868a1f66f/console). Wystarczy znaznaczyć co się chce w tekście wpisywanym w oknie poniżej wyszukać oraz podać klucz do stowrzonego wczęsniej serwisu Content Moderator.
