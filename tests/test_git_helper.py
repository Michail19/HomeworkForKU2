import unittest
from src.git_helper import get_commits


class TestGitHelper(unittest.TestCase):
    def test_get_commits(self):
        # Замените на путь к тестовому git-репозиторию
        commits = get_commits('/path/to/test/repo')
        self.assertIsInstance(commits, list)
        self.assertGreater(len(commits), 0)
        for commit in commits:
            self.assertEqual(len(commit), 3)  # Проверяем, что у нас 3 поля


if __name__ == "__main__":
    unittest.main()
