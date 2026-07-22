import os

import json

from fastapi import HTTPException
from mistralai.client import Mistral
from app.models.task import Task

from dotenv import load_dotenv
load_dotenv()

def make_task_string(index: int, task: Task):
    return f"Tarefa{index}: \n ID da tarefa{index}: {task.id} \nTítulo Da Tarefa{index}: {task.title}. \nExplicação da Tarefa{index}: {task.description}"




def categorize_tasks(tasks: list[Task]):


    api_key = os.getenv("MISTRAL_API_KEY")

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
                Agrupe as tarefas abaixo em categorias genéricas, cada categoria deve ter em seu 
                nome apenas uma palavra. Pode usar acentuação. Lembre-se que 
                cada tarefa deve pertencer a apenas uma categoria. Mantenha uma lógica para que no próximo prompt a IA 
                possa categorizar novas tarefas usando as mesmas categorias criadas nesse prompt.
                Você deve classificar cada tarefa utilizando apenas uma das categorias abaixo.

                Categorias permitidas:
                - Estudos
                - Trabalho
                - Casa
                - Compras
                - Saúde
                - Finanças
                - Exercícios
                - Lazer
                - Tecnologia
                - Projetos
                - Viagem
                - Família
                - Documentos

                Não crie novas categorias.
                Cada tarefa deve pertencer a apenas uma categoria.
                Escolha a categoria que melhor representa o objetivo principal da tarefa.


                Exemplos:

                "Lavar a louça" -> Casa
                "Limpar o banheiro" -> Casa
                "Varrer a garagem" -> Casa

                "Trocar o óleo do carro" -> Manutenção

                "Comprar arroz" -> Compras
                "Comprar pasta de dente" -> Compras

                "Estudar FastAPI" -> Estudos
                
                Não pode usar essas categorias: "Outros, Geral, Diversos, Vários, Tarefas" e sinônimos dessas.
                
                É obrigatório classificar TODAS as tarefas recebidas.

                Nenhum ID pode ser omitido.

                Se alguma tarefa tiver pouca informação, escolha a categoria mais provável com base no título.

                A resposta deve conter exatamente todos os IDs enviados.

                Antes de responder, verifique se todos os IDs aparecem exatamente uma vez no JSON.

                Responda **exclusivamente** com um objeto JSON no formato:
                {{"Categoria1": ["IdDaTarefa1", "IdDaTarefa2"], "Categoria2": ["IdDaTarefa3"]}}

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
        return {}
    

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500,
            detail="Invalid JSON returned by AI"   
        )