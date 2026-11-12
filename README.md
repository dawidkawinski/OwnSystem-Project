## 🚀 Jak uruchomić projekt lokalnie (Krok po kroku)

### 1. Sklonuj repozytorium lub pobierz pliki projektu
Otwórz terminal (wiersz poleceń) i przejdź do folderu, w którym chcesz zapisać projekt lub uruchom go przez codespace, wtedy od razu przejdź do punktu 2:

```bash
git clone <adres-twojego-repozytorium>
cd OwnSystem-Project-main
```
> Jeśli pobrałeś projekt jako archiwum `.zip`, po prostu wypakuj go i otwórz terminal wewnątrz wypakowanego folderu.

---

### 2. Utwórz i aktywuj środowisko wirtualne (`venv`)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Zainstaluj wymagane biblioteki

```bash
pip install -r requirements.txt
```

---

### 4. Przygotuj bazę danych (Migracje)

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Uruchom serwer deweloperski

```bash
python manage.py runserver
```

Aby zalogować się do panelu studenta:\
Identyfikator: 019659\
Hasło: dawid123

Aby zalogować się do panelu wykładowcy:\
Identyfikator: 369830\
Hasło: dawid123

🎉 **Aplikacja jest już aktywna!** Otwórz przeglądarkę i wejdź pod adres:
* **Logowanie:** [http://127.0.0.1:8000/konta/login/](http://127.0.0.1:8000/konta/login/)
* **Rejestracja kandydata:** [http://127.0.0.1:8000/rejestracja/](http://127.0.0.1:8000/rejestracja/)
