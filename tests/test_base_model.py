import unittest
from datetime import datetime, timezone, timedelta
from uuid import uuid4
from base_model import BaseModel

# Assuming gmt_plus_2 is defined somewhere in your module
gmt_plus_2 = timezone(timedelta(hours=2))

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_initialization(self):
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at.tzinfo, gmt_plus_2)
        self.assertEqual(self.model.updated_at.tzinfo, gmt_plus_2)

    def test_str(self):
        model_str = str(self.model)
        self.assertIn(f'class_mame: {self.model.__class__.__name__}', model_str)
        self.assertIn(f'id = {self.model.id}', model_str)
        self.assertIn('content :', model_str)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        self.model.my_number = 89
        self.model.name = 'My First Model'
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(model_dict['name'], 'My First Model')
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

