import unittest
import os
from db import DB

class TestDB(unittest.TestCase):
    
    def setUp(self):
        self.db = DB()
        self.db.create_database('test_db')
        self.db.select_database('test_db')

    def tearDown(self):
        if os.path.exists('test_db'):
            for file in os.listdir('test_db'):
                os.remove(os.path.join('test_db', file))
            os.rmdir('test_db')

    def test_create_table(self):
        self.db.create_table('test_table')
        tables = self.db.list_tables()
        self.assertIn('test_table', tables)

    def test_insert_row(self):
        self.db.create_table('test_table')
        self.db.add_field('test_table', 'name', 'string')
        self.db.insert_row('test_table', {'name': 'Alice'})
        table_data = self.db.load_table('test_table')
        self.assertEqual(len(table_data), 1)
        self.assertEqual(table_data[0]['name'], 'Alice')

    def test_delete_table(self):
        self.db.create_table('test_table')
        self.db.delete_table('test_table')
        tables = self.db.list_tables()
        self.assertNotIn('test_table', tables)
        
    # def test_add_field(self):
    #     self.db.create_table('test_table')
    #     self.db.add_field('test_table', 'name', 'string')
    #     table_fields = self.db.list_table_fields('test_table')
    #     self.assertIn('name', table_fields)

if __name__ == '__main__':
    unittest.main()
