import unittest
from datetime import datetime, timezone, timedelta
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up the BaseModel instance before each test."""
        self.model = BaseModel()
        self.model.my_number = 89
        self.model.name = 'My First Model'
        # Setting specific datetime values for testing purposes
        self.model.created_at = datetime(2017, 9, 28, 21, 5, 54, 119427, tzinfo=timezone.utc)
        self.model.updated_at = datetime(2017, 9, 28, 21, 5, 54, 119434, tzinfo=timezone.utc)

    def test_initialization(self):
        """Test if the BaseModel is correctly initialized."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test the string representation of the BaseModel."""
        expected_output = f"class_mame: {self.model.__class__.__name__}\nid = {self.model.id}\ncontent : {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_output)

    def test_save(self):
        """Test if the save method updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel."""
        self.model.updated_at = datetime(2017, 9, 28, 21, 5, 54, 119572, tzinfo=timezone.utc)
        model_dict = self.model.to_dict()
        expected_dict = {
            'my_number': 89,
            'name': 'My First Model',
            '__class__': 'BaseModel',
            'updated_at': '2017-09-28T21:05:54.119572+00:00',
            'id': self.model.id,
            'created_at': '2017-09-28T21:05:54.119427+00:00'
        }
        self.assertEqual(model_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

