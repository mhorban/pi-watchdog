from setuptools import setup, find_packages

setup(
    name='pi-watchdog',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyA20',
        'pyyaml',
    ],
    entry_points='''
        [console_scripts]
        pi-watchdog=pi_watchdog.run:main
    ''',
    script_name='setup.py',
    author='Marian Horban',
    author_email='horban.marian@gmail.com'
)
