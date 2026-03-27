import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r'color:\s*#2A2A2A': 'color:#888',
    r'color:\s*#333': 'color:#999',
    r'color:\s*#3A3A3A': 'color:#999',
    r'color:\s*#444': 'color:#A0A0A0',
    r'color:\s*#4A4A4A': 'color:#B0B0B0',
    r'color:\s*#555': 'color:#A0A0A0',
    r'color:\s*#666': 'color:#C0C0C0',
    r'color:\s*#777': 'color:#C0C0C0',
    r'color:\s*#161616': 'color:#333'
}

for old, new in replacements.items():
    content = re.sub(old, new, content, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Colors updated successfully.')
