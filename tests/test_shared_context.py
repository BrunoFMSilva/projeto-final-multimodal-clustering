import sys
sys.path.append('/Users/bruno.silva/Documents/Mestrado_PUC/projeto-final-multimodal-clustering/app/')
import unittest
from unittest import TestCase
from unittest.mock import patch
import shared_context


class TestSharedContext(TestCase):
    """
    Function that tests if the connection with Redis can be set
    @author Bruno Francisco
    """
    def test_set_connect(self):
        with patch('shared_context.start_queueing') as mock_start_queueing:
            mock_redis_instance = mock_start_queueing.return_value
            actual = shared_context.start_queueing()
            self.assertEqual(actual, mock_redis_instance)
            mock_start_queueing.assert_called_once_with()

    """
    Function that tests if the connection with Redis can be obtained   
    @author Bruno Francisco
    """
    @patch('shared_context.start_queueing')
    def test_get_conn(self, mock_start_queueing):
        mock_redis_instance = mock_start_queueing.return_value
        self.assertEqual(shared_context.start_queueing(), mock_redis_instance)

    """
    Function that tests if the model used in the text_enconder is loaded in the correct format   
    @author Bruno Francisco
    """
    @patch('shared_context.load_txt_model')
    def test_get_model(self, mock_load_txt_model):
        mock_model_instance = mock_load_txt_model.return_value
        self.assertEqual(shared_context.load_txt_model(), mock_model_instance)

if __name__ == '__main__':
    unittest.main()
