import xml.etree.ElementTree as ET


def load_config(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()

    config = {
        'graphviz_path': root.find('graphviz_path').text,
        'repo_path': root.find('repo_path').text,
        'output_path': root.find('output_path').text
    }

    return config
