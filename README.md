
# Läslistan – E2E-test med Playwright och BDD

## Vad som testas

**Backend (pytest):**
- Enhetstester för BookStore: lägga till bok och toggla favorit
- Enhetstester för FavoriteBooks: lägga till och ta bort favorit
- Integrationstester för BookStore och FavoriteBooks tillsammans

**Frontend (behave + Playwright):**
- Katalog: att böcker visas på startsidan
- Lägg till bok: fylla i formulär och se att boken sparas i katalogen
- Favoritmarkering: markera en bok och se att den hamnar i Mina böcker
- Ta bort favorit: avmarkera en bok och se att den försvinner från Mina böcker
- Mina böcker: navigera dit och se favoritmarkerade böcker

---

## Hur man startar projektet

### 1. Klona projektet
git clone https://github.com/majk9494/exam_test_tool_Mikael.git
cd exam_test_tool_Mikael

### 2. Skapa och aktivera en virtuell miljö
python -m venv .venv
.venv\Scripts\activate

### 3. Installera beroenden
pip install -r requirements.txt
playwright install chromium

### 4. Kör backend-tester
pytest

### 5. Kör frontend-tester
behave src/features