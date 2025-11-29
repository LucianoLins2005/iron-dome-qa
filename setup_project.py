import os

# Estrutura de pastas do nosso projeto QA Agentic
folders = [
    "core",       # O cérebro (Dispatcher)
    "adapters",   # Conectores (Giskard, PyRIT)
    "agents",     # Personas de ataque
    "targets",    # Os bots que vamos testar
    "reports"     # Onde salvaremos os resultados
]

# Cria as pastas e arquivos vazios (__init__.py) para o Python reconhecer
def create_structure():
    print("🚀 Criando estrutura do projeto IRON DOME...")
    
    for folder in folders:
        # Cria a pasta
        os.makedirs(folder, exist_ok=True)
        print(f"   [OK] Pasta criada: /{folder}")
        
        # Cria o arquivo __init__.py dentro dela
        init_file = os.path.join(folder, "__init__.py")
        with open(init_file, "w") as f:
            pass # Apenas cria arquivo vazio
            
    print("\n✅ Estrutura pronta! Você já pode começar a codar.")

if __name__ == "__main__":
    create_structure()