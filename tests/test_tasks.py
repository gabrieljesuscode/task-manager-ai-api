from tests.conftest import client


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "string 1",
            "description": "string 2"
        }
    )
    
    data = response.json()

    assert response.status_code == 201

    assert data["title"] == "string 1"
    assert data["description"] == "string 2"
    assert data["completed"] == False

def test_get_one_task():
    response = client.post(
        "/tasks",
        json={
            "title": "string 1",
            "description": "string 2"
        }
    )

    task_created = response.json()

    assert task_created

    # GET para ver uma tarefa
    response = client.get(f"/tasks/{task_created["id"]}")

    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "string 1"
    assert data["description"] == "string 2"
    assert data["completed"] == False

def test_update_task():
    create = client.post(
        "/tasks",
        json={
            "title": "string 1",
            "description": "string 2"
        }
    )

    task_created = create.json()

    assert task_created

    # Novas informações para atualização
    update_json = {
        "title": "string 3",
        "description": "string 4",
        "completed": True # O valor criado já vem como "false"
    } 

    # PUT para atualizar informações
    response = client.put(
        f"/tasks/{task_created["id"]}",
        json=update_json
    )
    
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "string 3"
    assert data["description"] == "string 4"
    assert data["completed"] == True

def test_delete_task():

    create = client.post(
        "/tasks",
        json={
            "title": "string 1",
            "description": "string 2"
        }
    )

    task_created = create.json()

    assert task_created

    # DELETE para remoção da tarefa

    response = client.delete(f"/tasks/{task_created["id"]}")

    
    assert response.status_code == 204
