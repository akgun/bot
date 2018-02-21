from setuptools import setup


setup(
    name='bot',
    version='0.1',
    packages=['bot'],
    install_requires=[
        'click',
        'python-telegram-bot'
    ],
    entry_points={
        'console_scripts': [
            'bot = bot.cli:cli'
        ],
    },
)
