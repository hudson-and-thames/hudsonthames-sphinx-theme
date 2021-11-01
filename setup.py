"""
Setup for Hudson and Thames Sphinx theme.
"""

from io import open

from setuptools import setup


setup(
    name='hudsonthames_sphinx_theme',
    version='0.1.4',
    author='Hudson and Thames Quantitative Research Limited',
    author_email='research@hudsonthames.org',
    license='All Rights Reserved',
    license_file=open('LICENSE.txt', encoding='utf-8').read(),
    description='Hudson and Thames theme for Sphinx',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    platform='any',
    url='https://github.com/hudson-and-thames/hudsonthames_sphinx_theme',
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
    entry_points={
        'sphinx.html_themes': [
            'hudsonthames_sphinx_theme = hudsonthames_sphinx_theme',
        ]
    },
    project_urls={
        'Source': 'https://github.com/hudson-and-thames/hudsonthames_sphinx_theme',
        'Bug Reports': 'https://github.com/hudson-and-thames/hudsonthames_sphinx_theme/issues',
        'Project Boards': 'https://github.com/orgs/hudson-and-thames/projects',
        'Blog': 'https://hudsonthames.org/blog/',
        'Apprenticeship Program': 'https://hudsonthames.org/apprenticeship-program/'
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
