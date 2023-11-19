import os

filename = 'index.html'

def read_html_file(filename):
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        html_content = file.read()
    print(html_content)

p = read_html_file('index.html')

print(p)