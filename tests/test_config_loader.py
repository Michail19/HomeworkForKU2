import unittest
from src.config_loader import load_config


class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        config = load_config('config.xml')
        self.assertEqual(config['graphviz_path'], 'D:\\Programs\\Graphviz\\bin\\dot.exe')
        self.assertEqual(config['repo_path'], 'D:\\Python\\HomeworkForKU2')
        self.assertEqual(config['output_path'], 'D:\\Python\\HomeworkForKU2\\output\\output.png')


if __name__ == "__main__":
    unittest.main()
