import sys, os
import scrapy_rabbitmq_link

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from codecs import open

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'scrapy_rabbitmq_link'
]

requires = [
    'pika',
    'Scrapy>=0.14'
]

setup(
    name='scrapy-rabbitmq-link',
    author='Mantas Briliauskas',
    description='RabbitMQ Plug-in for Scrapy',
    version='0.1.0',
    author_email='m.briliauskas@gmail.com',
    license='MIT',
    url='https://github.com/mbriliauskas/scrapy-rabbitmq-link',
    install_requires=requires,
    packages=packages
)
