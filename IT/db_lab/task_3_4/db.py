import json
import os
from uuid import uuid4

class DatabaseManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.active_db = None
        self.ensure_directory(self.base_dir)

    def ensure_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def select_database(self, db_name):
        db_path = os.path.join(self.base_dir, db_name)
        if not os.path.isdir(db_path):
            raise ValueError(f"Database '{db_name}' does not exist.")
        self.active_db = db_path

    def create_database(self, db_name):
        db_path = os.path.join(self.base_dir, db_name)
        if os.path.exists(db_path):
            raise ValueError(f"Database '{db_name}' already exists.")
        os.makedirs(db_path)

    def list_tables(self):
        self._check_db_selected()
        return [f[:-5] for f in os.listdir(self.active_db) if f.endswith('.json')]

    def _check_db_selected(self):
        if self.active_db is None:
            raise ValueError("No database selected. Please select a database first.")


class TableManager:
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager

    def create_table(self, table_name):
        self.database_manager._check_db_selected()
        table_path = os.path.join(self.database_manager.active_db, f"{table_name}.json")
        if os.path.exists(table_path):
            raise ValueError(f"Table '{table_name}' already exists.")

        with open(table_path, 'w') as file:
            json.dump([], file, indent=4)

    def delete_table(self, table_name):
        self.database_manager._check_db_selected()
        table_path = os.path.join(self.database_manager.active_db, f"{table_name}.json")
        if os.path.exists(table_path):
            os.remove(table_path)
        else:
            raise FileNotFoundError(f"Table '{table_name}' does not exist.")

    def rename_table(self, old_name, new_name):
        self.database_manager._check_db_selected()
        old_table_path = os.path.join(self.database_manager.active_db, f"{old_name}.json")
        new_table_path = os.path.join(self.database_manager.active_db, f"{new_name}.json")

        if not os.path.exists(old_table_path):
            raise FileNotFoundError(f"Table '{old_name}' does not exist.")

        if os.path.exists(new_table_path):
            raise ValueError(f"Table with name {new_name} already exists.")

        os.rename(old_table_path, new_table_path)


class RowManager:
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager

    def insert_row(self, table_name, row_data):
        self.database_manager._check_db_selected()
        table_path = os.path.join(self.database_manager.active_db, f"{table_name}.json")
        if not os.path.exists(table_path):
            raise ValueError(f"Table '{table_name}' does not exist.")

        with open(table_path, 'r') as file:
            rows = json.load(file)

        rows.append(row_data)

        with open(table_path, 'w') as file:
            json.dump(rows, file, indent=4)

    def delete_row(self, table_name, row_id):
        self.database_manager._check_db_selected()
        table_path = os.path.join(self.database_manager.active_db, f"{table_name}.json")
        if not os.path.exists(table_path):
            raise FileNotFoundError(f"Table '{table_name}' does not exist.")

        with open(table_path, 'r') as file:
            rows = json.load(file)

        rows = [row for row in rows if row['id'] != row_id]

        with open(table_path, 'w') as file:
            json.dump(rows, file, indent=4)

    def load_table(self, table_name):
        self.database_manager._check_db_selected()
        table_path = os.path.join(self.database_manager.active_db, f"{table_name}.json")
        if os.path.exists(table_path):
            with open(table_path, 'r') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"Table '{table_name}' does not exist.")


class FieldManager:
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager

    def add_field(self, table_name, field_name, field_type):
        self.database_manager._check_db_selected()
        valid_types = ['integer', 'real', 'char', 'string', 'txtFile', 'integerInvl']
        if field_type not in valid_types:
            raise ValueError(f"Field type '{field_type}' is not valid.")

        table_path = os.path.join(self.database_manager.active_db, f"{table_name}.json")
        if not os.path.exists(table_path):
            raise ValueError(f"Table '{table_name}' does not exist.")

        with open(table_path, 'r') as file:
            rows = json.load(file)

        for row in rows:
            row[field_name] = None

        with open(table_path, 'w') as file:
            json.dump(rows, file, indent=4)
