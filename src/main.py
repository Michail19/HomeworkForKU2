import os
from config_loader import load_config
from dependency_graph import DependencyGraph


def main():
    config = load_config('config.xml')
    graphviz_path = config['graphviz_path']
    repo_path = config['repo_path']
    output_path = config['output_path']

    graph = DependencyGraph(graphviz_path, repo_path, output_path)
    graph.run()


if __name__ == "__main__":
    main()
