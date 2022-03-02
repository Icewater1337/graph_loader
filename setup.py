from setuptools import setup

setup(
    name='graph_loader',
    version='0.1.0',
    description='A package to load graphs in various ways and formats',
    author='Mathias Fuchs',
    author_email='fuchsmath@gmail.com',
    packages=['graph_loader'],
    install_requires=['networkx',
                      'numpy',
                      ],

)