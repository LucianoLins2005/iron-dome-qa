import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. Carrega a chave do .env
load_dotenv()

def test_brain():
    print("🔌 Testando conexão com a OpenAI...")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERRO: Chave não encontrada no arquivo .env")
        return

    try:
        # 2. Tenta conectar com o modelo GPT-4o-mini (Mais barato para teste)
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        
        # 3. Envia uma pergunta simples
        print("🤖 Perguntando: 'Quanto é 2 + 2?'...")
        resposta = llm.invoke("Quanto é 2 + 2? Responda apenas com o número.")
        
        print(f"✅ SUCESSO! A IA respondeu: {resposta.content}")
        print("💳 Seus créditos estão ativos e o ambiente está pronto.")
        
    except Exception as e:
        print(f"\n❌ FALHA NA CONEXÃO:\n{e}")
        print("\nDica: Verifique se você tem créditos ($) em 'Billing' na plataforma.")

if __name__ == "__main__":
    test_brain()