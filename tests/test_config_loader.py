import unittest
from src.config_loader import load_config


class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        config = load_config('config.xml')
        self.assertEqual(config['graphviz_path'], '/path/to/graphviz')
        self.assertEqual(config['repo_path'], '/path/to/git/repo')
        self.assertEqual(config['output_path'], '/path/to/output.png')


if __name__ == "__main__":
    unittest.main()
