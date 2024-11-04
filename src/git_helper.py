import subprocess


def get_commits(repo_path):
    cmd = ['git', '-C', repo_path, 'log', '--all', '--pretty=format:%H|%ai|%an|%P']
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception("Ошибка при получении коммитов из репозитория.")

    commits = []
    for line in result.stdout.splitlines():
        if line:
            parts = line.split('|')
            commit_data = {
                "hash": parts[0],
                "date": parts[1],
                "author": parts[2],
                "dependencies": parts[3].split() if parts[3] else []
            }
            commits.append(commit_data)
    return commits
