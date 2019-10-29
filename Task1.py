import platform
import os
import sys
import json
import yaml
import pip
from distutils.sysconfig import get_python_lib
from pip._internal.operations.freeze import freeze

py_pack = []
for requirement in freeze(local_only=True):
    py_pack.append(requirement)
    with open('Output.json', 'w', encoding='utf-8') as outfile:
        json.dump({'Python Checker': {
            'Version, environment': platform.python_version(),
            'Executable location': sys.executable,
            'Pip version': pip.__version__,
            'Pip path': pip.__path__,
            'PYTHONPATH': os.environ['PYTHONPATH'].split(os.pathsep),
            'Packages location': get_python_lib(),
            'Packages with version': py_pack,
        }}, outfile, ensure_ascii=False, indent=2)

    with open('Output.yml', 'w') as outfile:
        yaml.dump({'Python Checker': {
            'Version, environment': platform.python_version(),
            'Executable location': sys.executable,
            'Pip version': pip.__version__,
            'Pip path': pip.__path__,
            'PYTHONPATH': os.environ['PYTHONPATH'].split(os.pathsep),
            'Packages location': get_python_lib(),
            'Packages with version': py_pack,
        }}, stream=outfile, default_flow_style=False, indent=3)
