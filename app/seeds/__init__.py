from flask.cli import AppGroup
from .users import seed_users, undo_users
from .tags import seed_tags, undo_tags
from .creatures import seed_creatures, undo_creatures
from .userfavorites import seed_userfavorites, undo_userfavorites

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_tags()
    seed_creatures()
    seed_userfavorites()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_tags()
    undo_creatures()
    undo_userfavorites()
    undo_users()
    # Add other undo functions here
