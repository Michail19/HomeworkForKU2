import unittest
from git_helper import get_commits

class TestGitHelper(unittest.TestCase):
    def test_get_commits(self):
        # Предположим, что вы работаете с тестовым репозиторием
        commits = get_commits('/path/to/test/repo')
        self.assertIsInstance(commits, list)
        self.assertGreater(len(commits), 0)
