from distutils.core import setup

setup(
    name='edumaite-api',
    version='0.1',
    packages=['edumaite_api',],
    long_description=open('README.md').read(),

    requires=['Django',
              'django-rest-framework',
              'djangorestframework'

    ]
)