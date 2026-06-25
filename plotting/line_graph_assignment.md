### **Visualiseringsprojekt: Temperatur i Australien**

Din uppgift är att analysera olika mönster hos vädret i Australien.

**Uppgifter:**

1. **Förbered Data**

   - Importera nödvändiga bibliotek som pandas och matplotlib.
   - Ladda in och utforska datasetet för att förstå dess struktur och innehåll.

2. **Analysera Temperaturmönster**

   - Välj ut fem olika platser där du ska mäta temperaturen på och spara dem i en variabel. Detta gör du exempelvis med `albury = weather[weather["Location"] == "Albury"]` där weather är ditt dataset.
   - Jämför maxtemperaturerna på de olika platserna. Börja med en enstaka plats.
   - Sanity-checka dig själv genom att kolla så att linjediagrammet verkar rimliga. Tänk på att Australien är på södra halvklotet.

3. **Presentation och Exportering**
   - Lägg till färger på de olika linjerna.
   - Lägg till titlar, axelmärkningar och förklaringar för att göra diagrammen informativa och lättlästa.
   - Exportera de färdiga diagrammen som bildfiler (t.ex. PNG) för rapporter eller presentationer.


## Fortsättning

- Använd det kompletta datasetet: weatherAUS.csv.
- Istället för maxtemperaturer, undersök medeltemperaturer (i detta fall (max_temp - min_temp) / 2)
- Se om du kan beräkna en medeltemperatur för hela månader och plotta den.
- Kolla på Spotify-settet och se om du kan hitta någon korrelation mellan en kolumn och popularitet! (har inte kollat alla själv, så jag vet faktiskt inte svaret)