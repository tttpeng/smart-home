from setuptools import setup

setup(
    name="celery_chinese_json",
    description="A JSON serializer for Kombu (and therefore also Celery) that "
    "supports encoding objects by defining to_json and from_json methods.",
    version="1.0.18",
    license="Apache License, Version 2.0",
    author="Zakir Durumeric",
    author_email="zakird@gmail.com",
    maintainer="Zakir Durumeric",
    maintainer_email="zakird@gmail.com",
    keywords="python kombu celery json",
    # namespace_packages=['celery_chinese_json'],
    py_modules=['celery_chinese_json'],
    # packages=["zscelery_chinese_jsonon"],
    entry_points={
        'kombu.serializers':
        ['celery_chinese_json = celery_chinese_json:zson_registration_args']
    },
    install_requires=["anyjson"])
