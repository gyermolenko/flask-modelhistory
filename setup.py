from setuptools import setup


setup(
    name='flask-modelhistory',
    version='0.1',
    url='https://github.com/gyermolenko/flask-modelhistory/',
    license='BSD',
    author='gyermolenko',
    author_email='gyermolenko@gmail.com',
    description='Track changes in instances of sqlalchemy db model',
    packages=['flask_modelhistory'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'flask-sqlalchemy',
        'flask-login'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
