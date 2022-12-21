import unittest
from translator import englishToFrench, frenchToEnglish

class MyTestTranslator(unittest.TestCase):

    # Self-made tests
    def test_goodbye(self):
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')

    def test_au_revoir(self):
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')
    
    # Null tests
    def test_null_input_english(self):
        self.assertEqual(englishToFrench(None), '')
    
    def test_null_input_french(self):
        self.assertEqual(frenchToEnglish(None), '')

    # Hello / Bonjour tests
    def test_hello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    def test_bonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ =='__main__':
    unittest.main()
