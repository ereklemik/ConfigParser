from configparser import ConfigParser
config = ConfigParser()
file = 'applicant.ini'
config.read(file)
if not config.has_section('Applicant'):
    config.add_section('Applicant')
section = config['Applicant']
section['name'] = 'John'
section['surname'] = 'Doe'
section['position'] = 'DevOps Engineer'

if not config.has_section('Skills'):
    config.add_section('Skills')
section = config['Skills']
section['Cloud'] = 'AWS'
section['Infrastructure'] = 'Terraform'
section['Automation'] = 'Python'
section['Monitoring'] = 'Prometheus'

if not config.has_section('Education'):
    config.add_section('Education')
section = config['Education']
section['University'] = 'Harvard'
section['Faculty'] = 'Information Systems'
section['Degree'] = 'Bachelor'


additional_info = {
    'Mobile': '+995 579 111 124',
    'Email' : 'johndoe@example.com',
    'Address': 'Tbilisi',
}

if not config.has_section('AdditionalInfo'):
    config['AdditionalInfo'] = additional_info

with open(file, 'w') as f:
    config.write(f)
