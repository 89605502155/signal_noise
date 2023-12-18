from io import open
from setuptools import setup


version = '0.0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='signal_noise',
    version=version,

    author='Andrey Ferubko',
    author_email='ferubko1999@yandex.ru',

    description=(
        'It is a Python library for the calculation signal-noise metric in data. '
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/89605502155/signal_noise',
    # download_url='https://github.com/89605502155/signal_noise/archive/v{}.zip'.format(
    #     version
    # ),
    download_url='https://github.com/89605502155/signal_noise/archive/main.zip',

    license='GNU General Public License v3.0',

    packages=['signal_noise'],
    install_requires=['numpy'],

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)