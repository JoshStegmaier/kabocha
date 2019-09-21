from distutils.core import setup

setup(
    name="kabocha",
    version="1.0",
    description="JSON error extension to tastypie ",
    long_description="Extension to django-tastypie to help deal with more errors directly with JSON",
    keywords="django, tastypie, json, errors, api, rest",
    author="Josh Stegmaier <jrs@joshstegmaier.com>",
    author_email="jrs@joshstegmaier.com",
    url="https://github.com/JoshStegmaier/kabocha/",
    license="MIT",
    packages=["kabocha"],
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)