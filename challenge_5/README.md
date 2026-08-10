# Výzva #5

- [zdrojový kód](app/main.js)

**Tento zdrojový kód je náchylný k:**

- SQL Injection

Ukázka obsahuje i možnost opravy v [main_fix.js](app/main_fix.js)

## Možnosti exploitace

1. Normální použití
    - přihlášení přes formulář: `alice` / `tajne123`

2. Přes SQL Injection (bypass hesla)
    - username: `admin'--`
    - heslo: cokoliv
    - dotaz se stane: `WHERE name = 'admin'--' AND password = '...'`
    - `--` zakomentuje kontrolu hesla → přihlášení bez znalosti hesla
