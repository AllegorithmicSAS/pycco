from setuptools import setup, find_packages

setup(
        name = "Pycco",
        version = "1.0.0",
        description = """A Python port of Docco: the original quick-and-dirty,
        hundred-line-long, literate-programming-style documentation generator.
        """,
        author = "Clement Jacob",
        author_email = "clement.jacob@allegorithmic.com",
        url = "https://github.com/AllegorithmicSAS/pycco",
        packages = find_packages(),
        entry_points = {
            'console_scripts': [
                'pycco = pycco.main:main',
                ]
            },
        install_requires = ['markdown', 'pygments', 'pystache', 'smartypants'],
        extras_require = {'monitoring': 'watchdog'},
        )
