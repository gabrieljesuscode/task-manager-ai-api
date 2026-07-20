import os
import json

from fastapi import HTTPException
from mistralai.client import Mistral
from app.models.task import Task


def make_task_string(index: int, task: Task):
    return f"Tarefa{index}: \nTítulo Da Tarefa: {task.title}. \nExplicação da Tarefa: {task.description}"




def categorize_tasks(tasks: list[Task]):


    api_key = os.environ["MISTRAL_API_KEY"]

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="MISTRAL_API_KEY not configured."
        )
    
    client = Mistral(api_key=api_key)


    # String com tarefas para mandar na IA
    tasks_string = [make_task_string(index, task) for index, task in enumerate(tasks, start=1)]
    tasks_string = ", ".join(tasks_string)


    response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "user",
                "content":
                f"""
                Agrupe as tarefas abaixo em 1 a 3 categorias genéricas, cada categoria deve ter em seu 
                nome apenas uma palavra. Pode usar acentuação. Lembre-se que só pode haver 3 categorias no máximo, 
                e cada tarefa deve pertencer a apenas uma categoria. Mantenha uma lógica para que no próximo prompt a IA 
                possa categorizar novas tarefas usando as mesmas categorias criadas nesse prompt.
                Não pode usar essas categorias: "Outros, Diversos, Vários, Tarefas" e sinônimos dessas.
                Responda **exclusivamente** com um objeto JSON no formato:
                {{"Categoria1": ["TítuloDaTarefa1", "TítuloDaTarefa2"], "Categoria2": ["TítuloDaTarefa3"]}}

                Tarefas:
                {tasks_string}
                """
            }
        ],
    )

    content = response.choices[0].message.content
    
    # limpar para transfomar em JSON
    if "```" in content:
        content = content.replace("```", "").replace("json", "")

    content = content.strip()
    if not type(content) == str:
        return ""
    

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Invalid JSON returned by AI"   
        )