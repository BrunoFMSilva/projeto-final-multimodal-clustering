import sys
sys.path.append('/Users/bruno.silva/Documents/Mestrado_PUC/projeto-final-multimodal-clustering/')
import unittest
from unittest import TestCase
from unittest.mock import patch
import app.helper

"""
Function that tests if the the index is created in the correct format    
@author Bruno Francisco
"""
class TestHelper(TestCase):
    @patch('app.helper.create_index')
    def test_get_index(self, mock_get_index):
        mock_index_instance = mock_get_index.return_value
        actual = app.helper.create_index(index_name=f"idx_txt",
                                         distance_metric="L2",
                                         vector_field_name="embedding",
                                         embedding_dimension=768,
                                         number_of_vectors=1000,
                                         index_type="HNSW",
                                         prefix="txt::")
        self.assertEqual(actual, mock_index_instance)


if __name__ == '__main__':
    unittest.main()
