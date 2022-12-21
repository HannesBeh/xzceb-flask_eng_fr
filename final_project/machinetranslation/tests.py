import unittest
from translator import language_translator, englishToFrench, frenchToEnglish

class MyTestTranslator(unittest.TestCase):

    # Self-made tests
    def test_goodbye(self):
        self.assertEqual(englishToFrench('Goodbye', language_translator), 'Au revoir')

    def test_au_revoir(self):
        self.assertEqual(frenchToEnglish('Au revoir', language_translator), 'Goodbye')
    
    # Null tests
    def test_null_input_english(self):
        self.assertEqual(englishToFrench(None, language_translator), '')
    
    def test_null_input_french(self):
        self.assertEqual(frenchToEnglish(None, language_translator), '')

    # Hello / Bonjour tests
    def test_hello(self):
        self.assertEqual(englishToFrench('Hello', language_translator), 'Bonjour')
    
    def test_bonjour(self):
        self.assertEqual(frenchToEnglish('Bonjour', language_translator), 'Hello')
