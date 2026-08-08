# Výzva #4

- [zdrojový kód](app/main.cpp)

**Tento zdrojový kód je náchylný k:**

- Buffer Overflow

Ukázka obsahuje i možnost opravy v [main_fix.cpp](app/main_fix.cpp)

## Možnosti exploitace

1. Přes Buffer Overflow
    - Do pole ve vstupu vlož více než 16 znaků a přepiš návratovou adresu
    - Ukázka možného [exploitu](exploit.py)