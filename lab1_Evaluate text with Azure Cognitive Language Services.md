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

