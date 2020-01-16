#!/usr/bin/env python3

__projectname__ = "makereq"
__verison__ = "0.1.0"

from typing import Union

from requirementslib import Lockfile

import click


def get_reqs_from_pipfile(file: str, dev: bool) -> str:
    raise AttributeError("Yet not supported type")


def get_reqs_from_pipfile_lock(file: str, dev: bool) -> str:
    lockfile = Lockfile.create(file)
    reqs = lockfile.as_requirements()
    if dev:
        reqs += lockfile.as_requirements(dev=dev)
    return "\n".join(reqs)


def get_reqs_from_poetry_lock(file: list, dev: bool) -> str:
    raise AttributeError("Yet not supported type")


def get_reqs_from_pyproject_toml(file: list, dev: bool) -> str:
    raise AttributeError("Yet not supported type")


def get_reqs_from_setup_py(file: list, dev: bool) -> str:
    raise AttributeError("Yet not supported type")


type_mapping = {
    "Pipfile": get_reqs_from_pipfile,
    "Pipfile.lock": get_reqs_from_pipfile_lock,
    "poetry.lock": get_reqs_from_poetry_lock,
    "pyproject.toml": get_reqs_from_pyproject_toml,
    "setup.py": get_reqs_from_setup_py,
}


def get_reqs_object(path: str, dev=False) -> Union[AttributeError, str]:
    func = type_mapping.get(path.split("/")[-1].strip())
    if not func:
        raise AttributeError("Not supported type")
    return func(path, dev)


@click.command()
@click.argument("path", type=click.Path(exists=True, file_okay=True, resolve_path=True), default="Pipfile.lock")
@click.option("--dev", type=click.BOOL, default=False, is_flag=True, help="Add development dependencies")
def main(path, dev):
    """Tool for creating requirements.txt from any dep files"""
    print(get_reqs_object(path, dev))


if __name__ == "__main__":
    main()
