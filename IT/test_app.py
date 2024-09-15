import unittest
from app import app, db

class DBTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_table('test_table')
    
    def tearDown(self):
        tables = db.list_tables()
        for table in tables:
            db.delete_table(table)

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create New Table', response.data)

    def test_create_table(self):
        response = self.app.post('/tables', data={'table_name': 'new_table'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('new_table', db.list_tables())

    def test_add_field(self):
        # Create a new table to test adding fields
        self.app.post('/tables', data={'table_name': 'test_table_for_fields'})
        
        # Add a field to the table
        response = self.app.post('/tables/test_table_for_fields/add_field', data={'field_name': 'new_field', 'field_type': 'string'})
        self.assertEqual(response.status_code, 302)
        
        # Check if the field was added
        table_data = db.load_table('test_table_for_fields')
        self.assertTrue(all('new_field' in row for row in table_data))

    def test_delete_table(self):
        # Create a table to delete
        self.app.post('/tables', data={'table_name': 'table_to_delete'})
        
        response = self.app.post('/tables/table_to_delete/delete')
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('table_to_delete', db.list_tables())

if __name__ == '__main__':
    unittest.main()
