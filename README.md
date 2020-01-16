###MAKEREQ
___
Tool for creating requirements.txt from any dep files
___
INSTALL:
```shell script
pip install makereq
```
___
Usage:
```shell script
makereq /home/user/Project/Pipfile.lock > requirements.txt
makereq /home/user/Project/Pipfile.lock --dev > requirements-dev.txt
```
TODO:
 * Add pipfile support
 * Add poetry pyproject.toml support
 * Add poetry.lock support
