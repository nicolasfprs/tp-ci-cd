import unittest
from app import add


class TestApp(unittest.TestCase):
    def test_add_positifs(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)

    def test_add_negatifs(self):
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)

    def test_add_types(self):
        self.assertEqual(add(2.5, 3.5), 6.0)
        self.assertEqual(add("hello ", "world"), "hello world")

    def test_add_erreurs(self):
        with self.assertRaises(TypeError):
            add("texte", 5)


if __name__ == '__main__':
    unittest.main()