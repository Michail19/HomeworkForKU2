import unittest
from src.git_helper import get_commits


class TestGitHelper(unittest.TestCase):
    def test_get_commits(self):
        commits = get_commits('D:\\Python\\HomeworkForKU2')
        self.assertIsInstance(commits, list)
        self.assertGreater(len(commits), 0)
        for commit in commits:
            self.assertEqual(len(commit), 3)


if __name__ == "__main__":
    unittest.main()
