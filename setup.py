from setuptools import setup

setup(
    name="todo-cli",
    version="0.1",
    py_modules=["todo"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "todo=todo:main",
        ],
    },
)