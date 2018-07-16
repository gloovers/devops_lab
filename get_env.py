"""Task 1
Create a script that outputs information about the current versions
of python in the system:
1. version
2. name (alias)
3. virtual environment
4. python executable location
5. pip location (each python version has its own version of pip)
6. PYTHONPATH
7. installed packages: name, version
8. site-packages location

Script should output result to .json and .yaml files.

Additional task (optional): Output info about all python
versions and environments.

"""

import json
import os
import sys
# pyyaml
import yaml


def vers():
    """Get version of python"""
    val_vers = os.popen("python -V").read()
    return {"python_version": str(val_vers).rstrip("\n")}


def name_alias():
    """Get name (alias)"""
    return {"name_alias": os.getenv("PYENV_VERSION", default=None)}


def venv():
    """Get virtual environment"""
    return {"venv": os.getenv("VIRTUAL_ENV", default=None)}


def exec_location():
    """Get python executable location"""
    return {"exec_location": os.get_exec_path()[0]}


def pip_location():
    """Get pip location"""
    pip_val = os.popen("pyenv which pip").read()
    return {"pip_location": str(pip_val).rstrip("\n")}


def python_path():
    """Get PYTHONPATH"""
    return {"python_path": os.getenv("PYTHONPATH", default=None)}


def inst_packs():
    """Get installed packages"""
    modules_list = list(sys.modules.keys())
    return {"inst_packs": modules_list}


def s_packs_location():
    """Get site-packages location"""
    return {"s_packs_location": sys.path}


def write_json(dicc, path):
    """Write info to json format"""
    with open(path, "w") as ff:
        json.dump(dicc, ff, indent=4)


def write_yaml(dicc, path):
    """Write info to yaml format"""
    with open(path, "w") as ff:
        yaml.dump(dicc, ff, default_flow_style=False)


def all_envs():
    """Get all versions and environments"""
    venvs = os.popen("pyenv virtualenvs --skip-aliases").read()
    return {"all_envs": venvs.split("\n")}


def main_prog():
    """Main body"""
    current_version = {}
    current_version.update(vers())
    current_version.update(name_alias())
    current_version.update(venv())
    current_version.update(exec_location())
    current_version.update(pip_location())
    current_version.update(python_path())
    current_version.update(inst_packs())
    current_version.update(s_packs_location())
    current_version_output = {"current_version": current_version}
    output = {}
    output.update(current_version_output)
    output.update(all_envs())
    write_json(output, "./env_info.json")
    write_yaml(output, "./env_info.yaml")


if __name__ == '__main__':
    main_prog()
