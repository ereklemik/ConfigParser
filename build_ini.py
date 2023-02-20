from configparser import ConfigParser
config = ConfigParser()
file = 'applicant.ini'
config.read(file)

config.add_section('Applicant')

section = config['Applicant']
section['name'] = 'John'
section['surname'] = 'Doe'
section['position'] = 'DevOps Engineer'

config.add_section('Skills')
section = config['Skills']

section['Cloud'] = 'AWS'
section['Infrastructure'] = 'Terraform'
section['Automation'] = 'Python'
section['Monitoring'] = 'Prometheus'

config.add_section('Education')
section = config['Education']
section['University'] = 'Harvard'
section['Faculty'] = 'Information Systems'
section['Degree'] = 'Bachelor'


with open(file, 'w') as f:
    config.write(f)
