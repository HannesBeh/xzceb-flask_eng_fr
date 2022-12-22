"""
This module contains unittests
"""
import unittest
import sys
sys.path.insert(0, 'C:\\Users\\hanne\\Downloads\\xzceb-flask_eng_fr\\final_project\\machinetranslation\\')
from translator import english_to_french, french_to_english


class MyTestTranslator(unittest.TestCase):
    """
    Class for tests
    """

    # Self-made tests
    def test_goodbye(self):
        """
        Test goodbye translation
        """
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

    def test_au_revoir(self):
        """
        Test Au revoir translation
        """
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
    
    # Null tests
    def test_null_input_english(self):
        """
        Test null input english to french translation
        """
        self.assertEqual(english_to_french(None), '')

    def test_null_input_french(self):
        """
        Test null input french to english translation
        """
        self.assertEqual(french_to_english(None), '')

    # Hello / Bonjour tests
    def test_hello(self):
        """
        Tests hello translation
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_bonjour(self):
        """
        Tests bonjour translation
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
