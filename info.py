#!/usr/bin/env python
# pylint:disable=invalid-name
""" task """

import json
import sys
import os
import site
import pip
import yaml


def py_version():
    """ python version """
    p_vers = sys.version
    return p_vers[:5:]


def venv():
    """ virtual env """
    virt_env = sys.exec_prefix
    return virt_env


def exec_location():
    """ executable location """
    exec_loc = sys.executable
    return exec_loc


def pip_location():
    """ pip location """
    pip_loc = pip.__path__
    return pip_loc


def python_path():
    """ PYTHONPATH """
    py_path = os.environ['PATH']
    return py_path


def installed_pac():
    """ installed packages """
    inst_list = sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])
    return inst_list


def site_packages_loc():
    """ site packages location """
    site_pac_loc = site.getsitepackages()
    return site_pac_loc


def json_output():
    """ writes output to json file """
    keys = {'Python_version': py_version(), 'Virtual_env': venv(), 'executable_location': exec_location(), 'pip_location': pip_location(), 'PYTHONPATH': python_path(), 'installed_packages': installed_pac(), 'site_packages_location': site_packages_loc()}
    json_out = open("out.json", "w")
    json.dump(keys, json_out, sort_keys=True, indent=4, ensure_ascii=False)
    json_out.close()


def yaml_output():
    """ writes output to yaml file """
    keys = dict(
        Python_version=py_version(),
        Virtual_env=venv(),
        executable_location=exec_location(),
        pip_location=pip_location(),
        PYTHONPATH=python_path(),
        installed_packages=installed_pac(),
        site_packages_location=site_packages_loc()
    )
    yaml_out = open("out.yaml", "w")
    yaml.dump(keys, yaml_out, default_flow_style=False)
    yaml_out.close()


yaml_output()
json_output()
