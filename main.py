import sys
from ruamel.yaml import YAML
from jinja2 import Template



yaml=YAML()
with open('bk_template.yml', 'r') as doc:
  code = yaml.load(doc.read())

print(code)

steps = []
for step in code['steps']:
  print(step['command'])
  steps.append(step['command'])

template = Template(open('bk_template.yml','r').read())

data= {'comequieto': 'aaaaa'}

print(template.render(data))