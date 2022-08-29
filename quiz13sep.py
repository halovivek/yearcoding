languages = ['python', 'javascript']
for language in languages:
    if language != 'python':
        print(f'Are you sure want to program in {language.title()}?')
    else:
        print(f'{language.upper()} is a great choice')
