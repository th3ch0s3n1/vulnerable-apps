# Ukázky zranitelných aplikací a programů

Obsahuje také ukázku možné opravy.

## Jak sestavit (webovou) výzvu v Dockeru?

1. `cd challenge_1`

2. `docker build -t challenge_1 . `

3. `docker run -p 5000:5000 challenge_1`

4. jdi na http://127.0.0.1:5000

### Seznam výzev k vyřešení

- Výzva #1 (Command Injection ve Flask)
    - [Výzva #1 - zdrojový kód](challenge_1/app/main.py)
    - [Výzva #1 - možné řešení](challenge_1/README.md)

- Výzva #2 (SSTI / XSS ve Flask)
    - [Výzva #2 - zdrojový kód](challenge_2/app/main.py)
    - [Výzva #2 - možné řešení](challenge_2/README.md)

- Výzva #3 (Path Traversal v PHP)
    - [Výzva #3 - zdrojový kód](challenge_3/app/index.php)
    - [Výzva #3 - možné řešení](challenge_3/README.md)

- Výzva #4 (Přetečení bufferu v C++)
    - [Výzva #4 - zdrojový kód](challenge_4/app/main.cpp)
    - [Výzva #4 - možné řešení](challenge_4/README.md)

- Výzva #5 (SQL Injection)
    - [Výzva #4 - zdrojový kód](challenge_5/app/main.js)
    - [Výzva #4 - možné řešení](challenge_5/README.md)
