"""
Description:
Author:
Date:
Usage:
"""
import unittest 
from unittest.mock import patch
from src.chatbot import get_account
from src.chatbot import VALID_TASKS, ACCOUNTS


class ChatbotTests(unittest.TestCase):
    def test_valid_account_number(self):
        with patch("builtins.input") as mock_input:
            # Arrange
            mock_input.side_effect = ["123456"]
            expected_result = 123456
            # Act
            result = get_account()
            # Assert
            self.assertEqual(expected_result, result)

    def test_non_numeric_account(self):
        with patch("builtins.input") as mock_input: 
            # Arrange
            mock_input.side_effect = ["non_numeric_data"]
            expected_result = 'Account number must be a whole number.'

            # Act & Assert
            with self.assertRaises(ValueError) as context: 
                get_account() 
            
            self.assertEqual(str(context.exception), "Account number must be a whole number.")
    
    def test_non_existent_account(self):
        with patch("builtins.input") as mock_input:
            # Arrange
            mock_input.side_effect = ["112233"]
            expected_result = 'Account number does not exist.'
            
            # Act & Assert
            with self.assertRaises(ValueError) as context:
                get_account()
                
            self.assertEqual(str(context.exception), "Account number entered does not exist.")