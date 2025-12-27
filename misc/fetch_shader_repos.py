#!/usr/bin/env python3
"""
Fetch shader repositories from PCGamingWiki using MediaWiki API.
This script queries the ReShade page and extracts the shader repository table.
Output format: "URL";Name;Author;Description
"""

import json
import re
import sys
import urllib.request
import urllib.error
import urllib.parse


def fetch_shader_repositories():
    """Fetch shader repositories from PCGamingWiki using MediaWiki API."""
    api_url = "https://www.pcgamingwiki.com/w/api.php"
    params = {
        'action': 'parse',
        'page': 'ReShade',
        'prop': 'text',
        'format': 'json',
        'formatversion': '2'
    }
    
    # Build URL with properly encoded parameters
    query_string = urllib.parse.urlencode(params)
    url = f"{api_url}?{query_string}"
    
    try:
        request = urllib.request.Request(url)
        request.add_header('User-Agent', 'SteamTinkerLaunch/1.0')
        
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        if 'parse' not in data or 'text' not in data['parse']:
            print("Error: Unexpected API response format", file=sys.stderr)
            return []
            
        html_content = data['parse']['text']
        
        # Look for the shader repositories table section
        # The table is in a section titled "List of known shader repositories"
        section_pattern = (
            r'<span[^>]*id="List_of_known_shader_repositories"[^>]*>.*?</span>.*?'
            r'<table[^>]*class="wikitable"[^>]*>(.*?)</table>'
        )
        section_match = re.search(section_pattern, html_content, re.DOTALL | re.IGNORECASE)
        
        if not section_match:
            print("Error: Could not find shader repositories table", file=sys.stderr)
            return []
            
        table_html = section_match.group(0)
        
        # Parse table rows
        repositories = []
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        
        for row in rows[1:]:  # Skip header row
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
            if len(cells) >= 4:
                # Extract URL from first cell
                url_match = re.search(r'href="([^"]+)"', cells[0])
                if not url_match:
                    continue
                    
                repo_url = url_match.group(1)
                
                # Skip AstrayFX as it's in the custom list
                if 'blueskydefender' in repo_url.lower() or 'astrayfx' in repo_url.lower():
                    continue
                
                # Extract text content from cells, removing HTML tags
                name = re.sub(r'<[^>]+>', '', cells[1]).strip()
                author = re.sub(r'<[^>]+>', '', cells[2]).strip()
                description = re.sub(r'<[^>]+>', '', cells[3]).strip()
                
                # Clean up text (remove extra whitespace, newlines, and HTML entities)
                name = ' '.join(name.split())
                author = ' '.join(author.split())
                description = ' '.join(description.split())
                
                # Decode common HTML entities
                for entity, char in [('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), 
                                     ('&quot;', '"'), ('&#39;', "'"), ('&nbsp;', ' ')]:
                    name = name.replace(entity, char)
                    author = author.replace(entity, char)
                    description = description.replace(entity, char)
                
                # Remove semicolons from fields to prevent parsing issues
                name = name.replace(';', ',')
                author = author.replace(';', ',')
                description = description.replace(';', ',')
                
                # Clean URL (remove /tree/master and /reshade/Shaders suffixes)
                repo_url = re.sub(r'(/tree/master|/reshade/Shaders)$', '', repo_url)
                
                # Format output: "URL";Name;Author;Description
                repositories.append(f'"{repo_url}";{name};{author};{description}')
                
        return repositories
        
    except urllib.error.URLError as e:
        print(f"Error: Failed to fetch data from API: {e}", file=sys.stderr)
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON response: {e}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []


def main():
    """Main entry point."""
    repositories = fetch_shader_repositories()
    
    if not repositories:
        sys.exit(1)
    
    for repo in repositories:
        print(repo)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
