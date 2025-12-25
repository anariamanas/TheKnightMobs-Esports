#!/usr/bin/env python3
import os
import re

directory = r"c:\Users\anari\Documents\New folder\knightmobs\TheKnightMobs-Esports"

# HTML files to convert to PHP
html_files = [
    'contact.html', 'live.html', 'login.html', 'privacy.html', 
    'shop.html', 'team.html', 'terms.html', 'tournament.html', 'thankyou.html'
]

for html_file in html_files:
    filepath = os.path.join(directory, html_file)
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add PHP session start at the beginning
        content = '<?php session_start(); ?>\n' + content
        
        # Replace all .html links with .php
        content = re.sub(r'(["\'])([^"\']*\.html)(["\'])', r'\1\2.replace(".html", ".php")\3', content)
        content = content.replace('\.html"', '.php"').replace("\.html'", ".php'")
        content = re.sub(r'href="([^"]+)\.html"', r'href="\1.php"', content)
        content = re.sub(r"href='([^']+)\.html'", r"href='\1.php'", content)
        
        # Replace the entire header section with the navbar include
        # Find and replace the <header> ... </header> section
        header_pattern = r'<header[^>]*>.*?</header>'
        navbar_include = '<?php include \'includes/navbar.php\'; ?>'
        content = re.sub(header_pattern, navbar_include, content, flags=re.DOTALL)
        
        # Write to PHP file
        php_file = os.path.join(directory, html_file.replace('.html', '.php'))
        with open(php_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created {html_file.replace('.html', '.php')}")
    else:
        print(f"✗ File not found: {html_file}")

print("\nAll files converted!")
