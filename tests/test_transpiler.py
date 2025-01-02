import unittest
from pachamalayalam.transpiler import transpile

class TestPachaMalayalam(unittest.TestCase):
    def test_transpile(self):
        malayalam_code = "വ്യാഖ്യാനം ഗണന():\n    അച്ചടിക്കുക(10)"
        expected_python_code = "def ഗണന():\n    print(10)"
        self.assertEqual(transpile(malayalam_code), expected_python_code)

if __name__ == "__main__":
    unittest.main()
