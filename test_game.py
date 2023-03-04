import unittest
from game import roll, health, strength, char_generator, epic_quotes

from unittest.mock import patch
class TestGame(unittest.TestCase):
    def test_roll(self):
        for i in range(100):
            result = roll(6)
            self.assertTrue(result >= 1 and result <= 6)
            
        result = roll(10)
        self.assertTrue(result >= 1 and result <= 10)

    def test_health(self):
        result = health()
        self.assertTrue(0 <= result <= 100)
    
    def test_strength(self):
        result = strength()
        self.assertTrue(0 <= result <= 100)
    

    @patch('builtins.input', side_effect=["John Doe", 'Human'])   
    def test_char_generator(self, mock_input):
        result = char_generator()
        self.assertIsInstance(result, dict)
        self.assertIn("name", result)
        self.assertEqual(result["name"], "John Doe")
        self.assertIn("type", result)
        self.assertIn("health", result)
        self.assertIn("strength", result)
        self.assertIn("quote", result)

        self.assertIn(result["type"], ["Human", "Elf", "Wizard", "Orc"])
        self.assertIn(result["quote"], epic_quotes[result["type"]])



