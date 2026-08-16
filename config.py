from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

DATABASE_DIR = DATA_DIR / "codevault.db"

def create_DATA_DIR():
    DATA_DIR.mkdir(parents = True, exist_ok =  True)