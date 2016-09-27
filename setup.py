__doc__ = """
Convert audio files to a common format and allow them to be downloaded through HTTP request.
"""

from setuptools import setup

requirements = [
    'pydub',
    'mutagen',
    'gi',
]

setup(
    name='pyMServer',
    version='0.0.1',
    author='Vinicius de F. Marques',
    description='Convert and serve audio files.',
    license='',
    keywords='audio sound server converter',
    url='',
    packages=['pymserver'],
    long_description=__doc__,
    setup_requires=['pip'],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 0 - Development/Unstable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers and Final Users',
        'Operating System :: OS Independent',
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Multimedia :: Sound/Audio :: Editors",
        "Topic :: Multimedia :: Sound/Audio :: Mixers",
        'Topic :: Utilities',
    ],
    # Scripts and execution
    entry_points={
        'console_scripts': [
            'pymserver=pymserver.core:main'
        ]
    },

)