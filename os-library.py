from github import Github

g = Github('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')

repo = g.get_repo('bobby-bose/datastorage1')

with open('main.py', 'r') as file:
    data = file.read()

repo.create_file('main.py', 'upload csv', data, branch='main')