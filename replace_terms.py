import os
import re

directory = r"d:\Design Agent"
extensions = ['.md', '.js', '.py', '.sh', '.json', '.jsx', '.html']

replacements = [
    (re.compile(r'\bClaude Code\b'), 'Antigravity'),
    (re.compile(r'\bClaude Design\b', re.IGNORECASE), 'Antigravity Design'),
    (re.compile(r'huashu-design-Antigravity'), 'huashu-design-Antigravity'),
    (re.compile(r'~/\.claude/'), r'~/.gemini/antigravity/'),
    (re.compile(r'\bClaude\.ai\b', re.IGNORECASE), 'Antigravity'),
    (re.compile(r'\bClaude\b(?!-haiku)(?! 3\.)(?! \d)'), 'Antigravity'),
    (re.compile(r'claude\.complete'), 'antigravity.complete'),
    (re.compile(r'window\.claude'), 'window.antigravity'),
    (re.compile(r'Sao chép thư mục vào ~/.gemini/antigravity/skills/huashu-design-Antigravity'), 'Sao chép thư mục vào ~/.gemini/antigravity/skills/huashu-design-Antigravity')
]

for root, dirs, files in os.walk(directory):
    if '.git' in root:
        continue
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for pattern, repl in replacements:
                    new_content = pattern.sub(repl, new_content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {filepath}")
            except Exception as e:
                print(f"Error reading/writing {filepath}: {e}")
