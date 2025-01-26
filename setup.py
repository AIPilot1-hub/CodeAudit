from setuptools import setup, find_packages

setup(
    name="test_bench",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "sqlalchemy",
    ],
    entry_points={
        'console_scripts': [
            'test_bench=app.main:main',
        ],
    },
)
