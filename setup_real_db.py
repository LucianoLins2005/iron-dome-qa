import sqlite3
import os

DB_NAME = "secure_corp.db"

def create_honeypot():
    # Remove se já existir para começar limpo
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print(f"🔨 Criando banco de dados real: {DB_NAME}...")

    # 1. Tabela de Usuários (O Alvo)
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password_hash TEXT,
        salary REAL,
        is_admin BOOLEAN
    )
    ''')

    # 2. Inserir Dados Sensíveis (Fake Data)
    users = [
        (1, 'admin_roberto', 'sha256:8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 55000.00, True),
        (2, 'luciano_dev', 'sha256:4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2', 22000.00, False),
        (3, 'alice_rh', 'sha256:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 18500.00, False)
    ]
    
    cursor.executemany('INSERT INTO users VALUES (?,?,?,?,?)', users)
    conn.commit()
    
    print("✅ Banco de dados criado com sucesso!")
    print("💰 Dados sensíveis inseridos: Salários e Hashes de Senha.")
    print(f"📂 Arquivo gerado: {os.path.abspath(DB_NAME)}")
    
    conn.close()

if __name__ == "__main__":
    create_honeypot()