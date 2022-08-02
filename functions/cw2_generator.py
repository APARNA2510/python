# wap to generate a list of acronyms from a list of words using generators and *args

def acronyms(*names):
    for initial_name in names:
        yield ''.join([i[0].upper() for i in initial_name.split()])

# ex call

for item in acronyms('Aparna Sharma', 'Ayushi Chandra', 'Asmita Maurya'):
    print(item)      

print(list(acronyms('Aparna Sharma', 'Ayushi Chandra', 'Asmita Maurya')))    