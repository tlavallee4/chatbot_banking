"""
Description:
Author:
Date:
Usage:
"""
import unittest 
from unittest.mock import patch
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection
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
    
    def test_valid_account_amount(self):
        with patch("builtins.input") as mock_input:
            #Arrange
            mock_input.side_effect = ["500.01"]
            expected_result = 500.01
            
            #Act
            result = get_amount()
            
            #Assert
            self.assertEqual(expected_result, result)
    
    def test_non_numeric_amount(self):
        with patch("builtins.input") as mock_input:
            #Arrange
            mock_input.side_effect = ["non_numeric_data"]
            expected_result = "Invalid amount. Amount must be numeric."
            
            #Act & Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")
    
    def test_positive_amount(self):
        with patch("builtins.input") as mock_input:
            #Arrange
            mock_input.side_effect = ['0']
            expected_result = "Invalid amount. Please enter a positive number."
            
            #Act & Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")
            
    def test_valid_account(self):
        #Arrange
        account = 123456
        expected_result = f'Your current balance for account {account} is $1000.00.'

        #Act
        result = get_balance(account)
        #Assert
        self.assertEqual(expected_result, result)
            
    def test_invalid_account(self):
        #Arrange
        account = 112233
        expected_result = 'Account number does not exist.'
            
        #Act & Assert
        with self.assertRaises(ValueError) as context:
            get_balance(account)
        self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_deposit_update(self):
        #Arrange
        account_number = 123456
        amount = 1500.01
        balance = 1000.0
        new_balance = balance + amount
        expected_result = f"Your current balance for account {account_number} is ${new_balance:.2f}."

        #Act
        result = make_deposit(account_number, amount)

        #Assert
        self.assertEqual(expected_result, result)

    def test_deposit_existent_account(self):
            # Arrange
            account = 112233
            amount = 1500.01
            expected_result = 'Account number does not exist.'
            
            # Act & Assert
            with self.assertRaises(ValueError) as context:
                make_deposit(account, amount)
                
            self.assertEqual(str(context.exception), expected_result)

    def test_deposit_negative_amount(self):
            # Arrange
            account = 123456
            amount = -50.01
            expected_result = 'Invalid Amount. Amount must be positive.'
            
            # Act & Assert
            with self.assertRaises(ValueError) as context:
                make_deposit(account, amount)
                
            self.assertEqual(str(context.exception), expected_result)

    def test_valid_lowercase_selection(self):
        with patch("builtins.input") as mock_input:
            #Arrange
            mock_input.side_effect = ['balance']
            expected_result = "balance"
            
            #Act 
            result = user_selection()
            
            #Assert
            self.assertEqual(expected_result, result)

    def test_returned_selection(self):
        with patch("builtins.input") as mock_input: 
            # Arrange
            mock_input.side_effect = ["DEPOSIT"]
            expected_result = 'deposit'

            # Act
            result = user_selection()
            
            #Assert
            self.assertEqual(expected_result, result)



    def test_invalid_selection(self):
        with patch("builtins.input") as mock_input: 
            # Arrange
            mock_input.side_effect = ["invalid_selection"]
            expected_result = 'Invalid task. Please choose balance, deposit, or exit.'

            #Act & Assert
            with self.assertRaises(ValueError) as context:
                user_selection()
            self.assertEqual(str(context.exception), expected_result)