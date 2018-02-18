import click

from . import bot


@click.group()
def cli():
    """Bot"""


@cli.command('start')
def cmdstart():
    """Start bot to obtain chat id"""
    click.echo('Type /start in telegram bot')
    bot.start()


@cli.command('send')
@click.option('--chat-id', '-c',
    envvar='BOT_CHAT_ID',
    required=True,
    help='ID to send message')
@click.argument('text', nargs=-1)
def cmdsend(chat_id, text):
    """Send message"""
    bot.send(chat_id, '\n'.join(text))
