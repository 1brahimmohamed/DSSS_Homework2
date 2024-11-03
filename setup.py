from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.0.1",
    description='A simple math quiz game',
    packages=find_packages(),
    author='Ibrahim Mohamed',
    license='Apache License 2.0',

    entry_points={
        'console_scripts': [
            'quiz = math_quiz.math_quiz:main'
        ]
    },
    include_package_data=True,
)
