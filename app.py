from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
items = []

@app.route('/')
def home():
    return "Welcome to the Flask CRUD App!"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    items.append(data)
    return jsonify({'message': 'Item added'}), 201

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data = request.get_json()
    if index < len(items):
        items[index] = data
        return jsonify({'message': 'Item updated'})
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < len(items):
        items.pop(index)
        return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
