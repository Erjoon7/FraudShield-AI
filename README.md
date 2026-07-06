# FraudShield-AI

Sistem inteligjent për zbulimin e mashtrimeve me karta krediti, i bazuar në Machine Learning (TensorFlow/Keras), me një aplikacion web Flask dhe bazë të dhënash MySQL.

## Parakushtet

- Python 3.9+ (rekomandohet 3.10/3.11 për përputhshmëri me TensorFlow)
- MySQL Server (5.7+ ose 8.0+)
- pip

## Hapat për ta ngritur projektin

### 1. Krijoni një virtual environment

```bash
python -m venv venv
```

Aktivizimi i venv (Windows PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

### 2. Instaloni dependencat

```bash
pip install -r requirements.txt
```

### 3. Krijoni bazën e të dhënave MySQL

Hapni MySQL (p.sh. me `mysql -u root -p`) dhe ekzekutoni skemën:

```bash
mysql -u root -p < database/schema.sql
```

Kjo krijon bazën `fraudshield` me tabelat `users` dhe `predictions`.

### 4. Konfiguroni kredencialet e bazës së të dhënave

Hapni [app/database.py](app/database.py) dhe përditësoni `host`, `user`, `password` dhe `database` sipas konfigurimit tuaj lokal të MySQL:

```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="<password-i-juaj>",
        database="fraudshield"
    )
```

> ⚠️ Mos e commitoni fjalëkalimin real në git. Për përdorim afatgjatë, konsideroni lëvizjen e këtyre vlerave në variabla ambienti (`os.environ`).

### 5. Sigurohuni që modeli ekziston

Modeli i trajnuar duhet të jetë te [models/best_model.h5](models/best_model.h5). Nëse mungon, trajnoni/vendoseni modelin para se të startoni aplikacionin, përndryshe `app/model.py` do të dështojë gjatë `load_model(...)`.

### 6. Startoni aplikacionin

```bash
cd app
python app.py
```

Aplikacioni do të startojë në mënyrë default në `http://127.0.0.1:5000` (debug mode aktiv).
