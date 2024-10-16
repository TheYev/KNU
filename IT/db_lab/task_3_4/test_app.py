import unittest
import os
from db import DatabaseManager, TableManager, RowManager, FieldManager

class TestDB(unittest.TestCase):

    def setUp(self):
        base_dir = os.getcwd()
        self.db_manager = DatabaseManager(base_dir)
        self.db_manager.create_database('test_db')
        self.db_manager.select_database('test_db')
        self.table_manager = TableManager(self.db_manager)
        self.row_manager = RowManager(self.db_manager)
        self.field_manager = FieldManager(self.db_manager)

    def tearDown(self):
        if os.path.exists('test_db'):
            for file in os.listdir('test_db'):
                os.remove(os.path.join('test_db', file))
            os.rmdir('test_db')

    def test_create_table(self):
        self.table_manager.create_table('test_table')
        tables = self.db_manager.list_tables()
        self.assertIn('test_table', tables)

    def test_insert_row(self):
        self.table_manager.create_table('test_table')
        self.field_manager.add_field('test_table', 'name', 'string')
        self.row_manager.insert_row('test_table', {'name': 'Alice'})
        table_data = self.row_manager.load_table('test_table')
        self.assertEqual(len(table_data), 1)
        self.assertEqual(table_data[0]['name'], 'Alice')

    def test_delete_table(self):
        self.table_manager.create_table('test_table')
        self.table_manager.delete_table('test_table')
        tables = self.db_manager.list_tables()
        self.assertNotIn('test_table', tables)

    def test_search_row(self):
        self.table_manager.create_table('test_table')
        self.field_manager.add_field('test_table', 'name', 'string')

        self.row_manager.insert_row('test_table', {'name': 'Alice'})
        self.row_manager.insert_row('test_table', {'name': 'Bob'})

        table_data = self.row_manager.load_table('test_table')
        search_result = next((row for row in table_data if row.get('name') == 'Alice'), None)

        self.assertIsNotNone(search_result)
        self.assertEqual(search_result['name'], 'Alice')

        search_result = next((row for row in table_data if row.get('name') == 'Charlie'), None)

        self.assertIsNone(search_result)

if __name__ == '__main__':
    unittest.main()
