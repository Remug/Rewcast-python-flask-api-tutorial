from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        del todos[position]  # Elimina la tarea en la posición indicada
        return jsonify(todos)  # Retorna la lista de tareas actualizada
    else:
        return jsonify({"error": "La posición especificada no es válida"})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)