from configparser import ConfigParser
file = 'config.ini'
config = ConfigParser()
config.read(file)


config['database'] = {
    'host': 'localhost',
    'user' : 'myuser',
    'password': 'mypassword',
    'database': 'mydatabase'
}


section = config['database']
section['port'] = '3306'

with open(file, 'w') as f:
    config.write(f)

