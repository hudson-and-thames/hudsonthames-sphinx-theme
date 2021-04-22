"""
Setup for Hudson and Thames Sphinx theme.
"""

from io import open

from setuptools import setup


setup(
    name='hudsonthames_rtd_theme',
    version='0.1.0',
    url='https://github.com/hudson-and-thames/hudsonthames_sphinx_theme',
    license='Other/Proprietary License',
    author='Hudson and Thames Quantitative Research Limited',
    author_email='research@hudsonthames.org',
    description='Hudson and Thames theme for Sphinx',
    long_description=open('README.md').read(),
    zip_safe=False,
    packages=['hudsonthames_sphinx_theme'],
    package_data={'hudsonthames_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/css/fonts/*.*'
        'static/images/*.*'
        'static/js/*.js',
    ]},
    include_package_data=True,
    # See https://smobsc.readthedocs.io/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'hudsonthames_sphinx_theme = hudsonthames_sphinx_theme',
        ]
    },
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    project_urls={
        'Source Code': 'https://github.com/hudson-and-thames/hudsonthames_sphinx_theme',
        'Issue Tracker': 'https://github.com/hudson-and-thames/hudsonthames_sphinx_theme/issues',
    },
)
