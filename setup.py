import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


PACKAGE = "payments"
NAME = "drf-stripe"
DESCRIPTION = "Django REST Framework wrapper of the payments Django app for Stripe"
AUTHOR = "Kalinin Mitko"
AUTHOR_EMAIL = "kalinin.mitko@gmail.com"
URL = "https://github.com/null-none/drf-stripe"

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=read("README.rst"),
    version="1.0.2",
    license="MIT",
    url=URL,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
    install_requires=[
        "stripe>=1.7.9",
        "django>=1.6",
        "pytz",
        "six",
        "djangorestframework>=3.1.1",
        "jsonfield>=1.0.3",
    ],
    test_suite="runtests.runtests",
    tests_require=[
        "mock",
    ],
    zip_safe=False,
)
