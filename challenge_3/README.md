# Výzva #3

- [zdrojový kód](app/index.php)

**Tento zdrojový kód je náchylný k:**

- Path Traversal

Ukázka obsahuje i možnost opravy v [index_fix.php](app/index_fix.php)

## Možnosti exploitace

1. Přes Path Traversal
    - `/file?name=../etc/passwd`
    - načte soubor mimo povolený adresář

2. Testovací cíl
    - `/file?name=files/secret.txt`
    - obsahuje text `Toto je tajny soubor.`
