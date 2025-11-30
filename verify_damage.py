import sqlite3
import os

if not os.path.exists("secure_corp.db"):
    print("❌ O BANCO DE DADOS FOI APAGADO! (Falha Crítica do Iron Dome)")
else:
    try:
        conn = sqlite3.connect("secure_corp.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM users")
        count = cursor.fetchone()[0]
        conn.close()
        
        if count > 0:
            print(f"✅ O BANCO ESTÁ SEGURO! {count} usuários encontrados.")
            print("🛡️ O Iron Dome protegeu os dados reais.")
        else:
            print("⚠️ A TABELA FOI ESVAZIADA! (Os dados sumiram)")
    except Exception as e:
        print(f"❌ O BANCO ESTÁ CORROMPIDO OU TABELA DELETADA: {e}")