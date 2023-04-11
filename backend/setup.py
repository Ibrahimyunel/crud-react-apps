from setuptools import setup

requirements = [
    "flask>=2",
    "flask-mysqldb>=1",
]

setup(
    name='flaskpackage',
    packages=['flask_package'],
    include_package_data=True,
    install_requires=requirements,
)

# pip install -e .