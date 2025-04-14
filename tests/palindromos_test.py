import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.palindrome import is_palindrome

import unittest


class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        """Pruebas para palíndromos simples"""
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("reconocer"))
    
    def test_phrase_palindromes(self):
        """Pruebas para frases palíndromas"""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Anita lava la tina"))
    
    #def test_non_palindromes(self):
    #    """Pruebas para no palíndromos"""
    #   self.assertFalse(is_palindrome("hello"))
    #   self.assertFalse(is_palindrome("python"))
   #    self.assertFalse(is_palindrome("This is not a palindrome"))
     #  self.assertFalse(is_palindrome("palindrome"))
    
    #def test_edge_cases(self):
    #    """Pruebas para casos especiales"""
    #    self.assertTrue(is_palindrome(""))  # Cadena vacía
    #    self.assertTrue(is_palindrome("a"))  # Un solo carácter
    #    self.assertTrue(is_palindrome("A"))  # Un solo carácter mayúscula
    #    self.assertTrue(is_palindrome(" "))  # Solo espacio
    #    self.assertTrue(is_palindrome(".,"))  # Solo puntuación
if __name__ == '__main__':
    unittest.main()