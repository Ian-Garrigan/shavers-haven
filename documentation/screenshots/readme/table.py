def print_issues(file_path):
    """function to print issues for readme in the form of a table"""
    with open(file_path, 'w') as file:
        for i in range(140):
            print(f'|  [#{i}](https://github.com/Ian-Garrigan/shavers-haven/issues/{i}) |  |', file=file)

print_issues('table.txt')
