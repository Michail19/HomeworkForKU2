import os


class DependencyGraph:
    def __init__(self, graphviz_path, repo_path, output_path):
        self.graphviz_path = graphviz_path
        self.repo_path = repo_path
        self.output_path = output_path
        self.commits = []

    def build_graph(self):
        # Получаем коммиты из git
        self.commits = get_commits(self.repo_path)
        graph = "digraph G {\n"

        # Добавляем узлы для каждого коммита
        for commit in self.commits:
            commit_hash, commit_date, commit_author = commit
            graph += f'    "{commit_hash}" [label="{commit_date}\\n{commit_author}"];\n'

        # Тут нужно добавить логику для транзитивных зависимостей
        # Например, можно добавлять ребра между коммитами на основе их родительских коммитов

        graph += "}\n"

        # Сохраняем граф в файл
        with open('graph.dot', 'w') as f:
            f.write(graph)

        # Визуализируем граф с помощью Graphviz
        cmd = [self.graphviz_path, 'dot', '-Tpng', 'graph.dot', '-o', self.output_path]
        subprocess.run(cmd)

    def run(self):
        self.build_graph()
        print(f"Граф зависимостей успешно построен и сохранен в {self.output_path}.")
