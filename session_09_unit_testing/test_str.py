import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('aCg'.upper(), 'ACG')

    def test_isupper(self):
        self.assertTrue('ACGTT'.isupper())
        self.assertFalse('acgT'.isupper())

    def test_count(self):
        self.assertEqual("ACCGT".count("C"), 2)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main()

