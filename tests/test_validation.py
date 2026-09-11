import os
import unittest

class TestInfrastructureIntegrity(unittest.TestCase):
    def test_readme_exists(self):
        self.assertTrue(os.path.exists("README.md"))

    def test_makefile_exists(self):
        self.assertTrue(os.path.exists("Makefile"))

if __name__ == "__main__":
    unittest.main()
