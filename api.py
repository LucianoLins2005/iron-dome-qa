from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import run_attack
import datetime
import os

# 1. Cria a Aplicação
app = FastAPI(
    title="Iron Dome API",
    description="Interface de Red Teaming Automatizado para LLMs",
    version="2.0"
)

# 2. Modelo de Dados (O que a API recebe)
class AttackRequest(BaseModel):
    target_name: str = "SysAdminBot"
    intensity: str = "high"

# 3. Função Auxiliar para rodar em segundo plano
def run_audit_task():
    print("🚀 API: Iniciando auditoria via requisição externa...")
    run_attack.run_agentic_attack()
    print("✅ API: Auditoria concluída.")

# 4. Endpoints (As "Portas" da API)
@app.get("/")
def health_check():
    """Verifica se o Iron Dome está online."""
    return {"status": "online", "system": "Iron Dome v2", "time": str(datetime.datetime.now())}

@app.post("/scan")
def trigger_scan(request: AttackRequest, background_tasks: BackgroundTasks):
    """
    Dispara um ataque Red Team contra o Agente.
    O ataque roda em background para não travar a API.
    """
    # Adiciona a tarefa na fila (Background)
    background_tasks.add_task(run_audit_task)
    
    return {
        "message": "Ataque iniciado com sucesso",
        "target": request.target_name,
        "status": "processing",
        "audit_id": f"audit_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    }

@app.get("/reports")
def list_reports():
    """Lista os relatórios gerados na pasta reports."""
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        return {"count": 0, "reports": []}
    
    files = [f for f in os.listdir(reports_dir) if f.endswith(".json")]
    return {"count": len(files), "reports": files}