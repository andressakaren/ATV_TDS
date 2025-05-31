from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks/teste")
def rota_teste_tasks():
    return {"mensagem": "Rota de tarefas funcionando"}
