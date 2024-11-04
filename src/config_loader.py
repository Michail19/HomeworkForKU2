import subprocess

def get_commits(repo_path):
    cmd = ['git', '-C', repo_path, 'log', '--pretty=format:%H|%ai|%an']
    result = subprocess.run(cmd, capture_output=True, text=True)
    return [line.split('|') for line in result.stdout.splitlines() if line]