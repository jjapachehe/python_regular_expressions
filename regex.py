import re

def regex_email(str):
    pm = re.compile(r'email:')
    m = pm.match(str)
    
    return m.group()