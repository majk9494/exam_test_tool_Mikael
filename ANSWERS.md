
# Answers

## Skillnaden mellan olika typer av tester

Enhetstester är det mest grundläggande, man testar en enskild funktion 
helt isolerat för att se att den gör precis det den ska. Det är lite som 
att kontrollera varje pusselbit för sig innan man lägger ihop hela 
pusslet.

Integrationstester tar det ett steg längre och kollar att bitarna faktiskt 
passar ihop. Det räcker inte att varje del fungerar på egen hand dom 
måste också kunna samarbeta.

Regressionstester är något man kör när man gjort ändringar i koden, för 
att försäkra sig om att man inte råkat förstöra något som fungerade 
tidigare. Det har nog hänt de flesta att man fixar en sak och oavsiktligt 
trassar till något annat.

Prestandatester handlar om att se hur systemet beter sig under press. 
Fungerar det lika bra när hundra användare är inne samtidigt som när det 
bara är en?

---

## Hur man arbetar med TDD

Det som kännetecknar TDD är att man skriver testet innan koden. Det låter 
konstigt i början, men det tvingar en att tänka igenom vad man faktiskt 
vill att koden ska göra innan man börjar skriva den.

Flödet är enkelt: först skriver man ett test som misslyckas, sedan skriver 
man koden som får testet att gå igenom, och till sist städar man upp koden 
utan att testerna slutar fungera. Sedan börjar man om med nästa funktion.

---

## Hur BDD skiljer sig från TDD

BDD känns som en naturlig vidareutveckling av TDD. Den stora skillnaden 
är att man i BDD fokuserar på hur systemet ska bete sig ur användarens 
perspektiv, snarare än hur koden fungerar tekniskt.

Det som verkligen skiljer dem åt är språket. I BDD skriver man scenarion 
med Given, When och Then på ett sätt som även en beställare eller 
projektledare kan läsa och förstå. Det gör kommunikationen mycket enklare 
när alla i teamet pratar samma språk.

---

## Vilka tester jag skulle använda för en liknande webbsida

Om jag fick bygga något liknande Läslistan från scratch skulle jag 
definitivt använda en kombination av enhetstester, integrationstester 
och end-to-end-tester.

Enhetstesterna skulle ge snabb feedback när jag jobbar med backend-logiken. 
Integrationstesterna skulle ge mig trygghet i att de olika delarna 
fungerar ihop. Och end-to-end-testerna med Playwright och BDD skulle 
simulera hur en riktig användare faktiskt använder sidan.

Jag tror den kombinationen ger en bra balans, man får både snabba tester 
som är lätta att felsöka och bredare tester som fångar upp de konstiga 
buggar som bara dyker upp när allt körs tillsammans.