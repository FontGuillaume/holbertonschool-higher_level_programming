#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Classe de test pour la fonction max_integer"""

    def test_empty_list(self):
        """Test avec une liste vide"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test avec une liste contenant un seul élément"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test avec une liste de nombres positifs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test avec une liste de nombres négatifs"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """Test avec une liste contenant des nombres positifs et négatifs"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([4, -3, 2, -1]), 4)

    def test_duplicate_numbers(self):
        """Test avec une liste contenant des nombres en double"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        """Test avec une liste de nombres à virgule flottante"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([4.5, 3.5, 2.5, 1.5]), 4.5)

    def test_mixed_types(self):
        """Test avec une liste contenant différents types numériques"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([4, 3.5, 2, 1.5]), 4)

    def test_max_at_beginning(self):
        """Test avec le maximum au début de la liste"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test avec le maximum au milieu de la liste"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_end(self):
        """Test avec le maximum à la fin de la liste"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_large_list(self):
        """Test avec une grande liste"""
        self.assertEqual(max_integer(range(1000)), 999)

    def test_list_of_strings(self):
        """Test avec une liste de chaînes"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_empty_string(self):
        """Test avec une chaîne vide"""
        self.assertIsNone(max_integer(""))

    def test_string(self):
        """Test avec une chaîne"""
        self.assertEqual(max_integer("abcde"), "e")

    def test_list_with_none(self):
        """Test avec None dans la liste"""
        with self.assertRaises(TypeError):
            max_integer([1, None, 3, 4])


if __name__ == "__main__":
    unittest.main()