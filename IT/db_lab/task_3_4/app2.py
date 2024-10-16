from flask import Flask, request, jsonify
from db import DatabaseManager, TableManager, RowManager, FieldManager
import os

app = Flask(__name__)

# Ініціалізація менеджерів
base_dir = os.getcwd()
db_manager = DatabaseManager(base_dir)
table_manager = TableManager(db_manager)
row_manager = RowManager(db_manager)
field_manager = FieldManager(db_manager)

@app.route('/')
def index():
    if db_manager.active_db is None:
        return jsonify({"error": "No database selected."}), 400

    tables = db_manager.list_tables()
    return jsonify({"tables": tables}), 200


@app.route('/databases', methods=['POST'])
def create_database():
    db_name = request.json.get('db_name')
    if not db_name:
        return jsonify({"error": "Database name is required."}), 400

    try:
        db_manager.create_database(db_name)
        return jsonify({"message": f"Database '{db_name}' created successfully."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/databases/use', methods=['POST'])
def use_database():
    db_name = request.json.get('db_name')
    try:
        db_manager.select_database(db_name)
        return jsonify({"message": f"Database '{db_name}' selected."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables', methods=['POST'])
def create_table():
    table_name = request.json.get('table_name')
    if not table_name:
        return jsonify({"error": "Table name is required."}), 400

    try:
        table_manager.create_table(table_name)
        return jsonify({"message": f"Table '{table_name}' created successfully."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/delete', methods=['DELETE'])
def delete_table(table_name):
    try:
        table_manager.delete_table(table_name)
        return jsonify({"message": f"Table '{table_name}' deleted successfully."}), 200
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/tables/<table_name>', methods=['GET'])
def table_view(table_name):
    try:
        table_data = row_manager.load_table(table_name)
        return jsonify({"table_name": table_name, "table_data": table_data}), 200
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/tables/<table_name>/add_field', methods=['POST'])
def add_field(table_name):
    field_name = request.json.get('field_name')
    field_type = request.json.get('field_type')

    try:
        field_manager.add_field(table_name, field_name, field_type)
        return jsonify({"message": f"Field '{field_name}' of type '{field_type}' added to table '{table_name}'."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/add_data', methods=['POST'])
def add_data(table_name):
    row_data = request.json

    if 'txtFile' in row_data:
        file = request.files['txtFile']
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        row_data['txtFile'] = file_path

    if 'integerInvl' in row_data:
        try:
            row_data['integerInvl'] = eval(row_data['integerInvl'])
        except Exception as e:
            return jsonify({"error": "Invalid range format."}), 400

    try:
        row_manager.insert_row(table_name, row_data)
        return jsonify({"message": f"Data added to table '{table_name}'."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/delete_row/<row_id>', methods=['DELETE'])
def delete_row(table_name, row_id):
    try:
        row_manager.delete_row(table_name, row_id)
        return jsonify({"message": f"Row with id '{row_id}' deleted from table '{table_name}'."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/table/rename', methods=['PATCH'])
def rename_table():
    old_name = request.json.get('old_name')
    new_name = request.json.get('new_name')
    try:
        table_manager.rename_table(old_name, new_name)
        return jsonify({"message": f"Table '{old_name}' renamed to '{new_name}'."}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/search', methods=['GET'])
def search_row(table_name):
    field_name = request.args.get('field_name')
    field_value = request.args.get('field_value')

    try:
        table_data = row_manager.load_table(table_name)
        result_row = next((row for row in table_data if row.get(field_name) == field_value), None)

        if result_row:
            return jsonify({"result": result_row}), 200
        else:
            return jsonify({"message": "Row not found."}), 404
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
