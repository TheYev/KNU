from flask import Flask, request, jsonify, render_template, redirect, url_for
from db import DB

app = Flask(__name__, template_folder='templates')
db = DB()

@app.route('/')
def index():
    tables = db.list_tables()
    return render_template('index.html', tables=tables)

@app.route('/tables', methods=['POST'])
def create_table():
    table_name = request.form.get('table_name')
    if not table_name:
        return jsonify({"error": "Table name is required."}), 400

    try:
        db.create_table(table_name)
        return redirect(url_for('index'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/delete', methods=['POST'])
def delete_table(table_name):
    try:
        db.delete_table(table_name)
        return redirect(url_for('index'))
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/tables/<table_name>')
def table_view(table_name):
    try:
        table_data = db.load_table(table_name)
        return render_template('table.html', table_name=table_name, table_data=table_data)
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/tables/<table_name>/add_field', methods=['POST'])
def add_field(table_name):
    field_name = request.form.get('field_name')
    field_type = request.form.get('field_type')
    
    try:
        db.add_field(table_name, field_name, field_type)
        return redirect(url_for('table_view', table_name=table_name))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tables/<table_name>/add_data', methods=['POST'])
def add_data(table_name):
    row_data = request.form.to_dict()
    
    try:
        db.insert_row(table_name, row_data)
        return redirect(url_for('table_view', table_name=table_name))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
# @app.route('/tables/<table_name>/delete_row/<row_id>', methods=['POST'])
# def delete_row(table_name, row_id):
#     db.delete_row(table_name, row_id)
#     return redirect(url_for('view_table', table_name=table_name))

@app.route('/table/rename', methods=['POST'])
def rename_table():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    db.rename_table(old_name, new_name)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
