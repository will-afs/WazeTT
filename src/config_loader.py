"""Load configuration from .toml file."""
import toml


# Read local `config.toml` file.
config = toml.load('settings/config.toml')
print(config)

# Retrieving a dictionary of values
config['project']
config.get('project')

# Retrieving a value
config['project']['author']
config.get('project').get('author')