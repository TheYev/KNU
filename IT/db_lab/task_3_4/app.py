from flask import Flask, request, jsonify, render_template, redirect, url_for
from db import DatabaseManager, TableManager, RowManager, FieldManager
import os

app = Flask(__name__, template_folder='templates')

base_dir = os.getcwd()
db_manager = DatabaseManager(base_dir)
table_manager = TableManager(db_manager)
row_manager = RowManager(db_manager)
field_manager = FieldManager(db_manager)

@app.route('/')
def index():
    if db_manager.active_db is None:
        return render_template('select_db.html')

    tables = db_manager.list_tables()
    return render_template('index.html', tables=tables)

@app.route('/databases', methods=['POST'])
def create_database():
    db_name = request.form.get('db_name')
    if not db_name:
        return jsonify({"error": "Database name is required."}), 400

    try:
        db_manager.create_database(db_name)
        return redirect(url_for('index'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/databases/use', methods=['POST'])
def use_database():
    db_name = request.form.get('db_name')
    try:
        db_manager.select_database(db_name)
        return redirect(url_for('index'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables', methods=['POST'])
def create_table():
    table_name = request.form.get('table_name')
    if not table_name:
        return jsonify({"error": "Table name is required."}), 400

    try:
        table_manager.create_table(table_name)
        return redirect(url_for('index'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/delete', methods=['POST'])
def delete_table(table_name):
    try:
        table_manager.delete_table(table_name)
        return redirect(url_for('index'))
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/tables/<table_name>')
def table_view(table_name):
    try:
        table_data = row_manager.load_table(table_name)
        return render_template('table.html', table_name=table_name, table_data=table_data)
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/tables/<table_name>/add_field', methods=['POST'])
def add_field(table_name):
    field_name = request.form.get('field_name')
    field_type = request.form.get('field_type')

    try:
        field_manager.add_field(table_name, field_name, field_type)
        return redirect(url_for('table_view', table_name=table_name))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/add_data', methods=['POST'])
def add_data(table_name):
    row_data = request.form.to_dict()

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
        return redirect(url_for('table_view', table_name=table_name))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/delete_row/<row_id>', methods=['POST'])
def delete_row(table_name, row_id):
    try:
        row_manager.delete_row(table_name, row_id)
        return redirect(url_for('table_view', table_name=table_name))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/table/rename', methods=['POST'])
def rename_table():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    try:
        table_manager.rename_table(old_name, new_name)
        return redirect(url_for('index'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/search', methods=['POST'])
def search_row(table_name):
    field_name = request.form.get('field_name')
    field_value = request.form.get('field_value')

    try:
        table_data = row_manager.load_table(table_name)

        result_row = next((row for row in table_data if row.get(field_name) == field_value), None)

        if result_row:
            return render_template('table.html', table_name=table_name, table_data=[result_row], message=None)
        else:
            return render_template('table.html', table_name=table_name, table_data=[], message="Row not found.")
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
