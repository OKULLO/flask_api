import os


user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DATABASE']
port = os.environ['POSTGRES_PORT']

def format_url(section):

  if section == 'postgresql':
    return f'postgres://{user}:{password}@{password}:{host}/{database}'
    
        
        