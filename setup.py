from setuptools import setup, find_packages

__version__ = '0.1'


setup(
    name='accounts_service',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask_restplus',
        'flask-migrate',
        'python-dotenv',
        'passlib'
    ],
    entry_points={
        'console_scripts': [
            'accounts_service = accounts_service.manage:cli'
        ]
    }
)
