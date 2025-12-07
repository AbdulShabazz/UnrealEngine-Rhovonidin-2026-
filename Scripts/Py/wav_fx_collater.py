import re
from collections import defaultdict
from pathlib import Path

def parse_catalog(filepath):
    """Parse a catalog file, returning dict of category -> list of entries."""
    categories = defaultdict(list)
    current_category = None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if match := re.match(r'^\[(.+)\]$', line.strip()):
                current_category = match.group(1)
            elif current_category and line.strip():
                categories[current_category].append(line)
    
    return categories

def main():
    # Collect all categories from source files
    all_categories = defaultdict(list)
    
    for i in range(2, 7):
        filepath = f'{i}_catalog.txt'
        if Path(filepath).exists():
            for cat, entries in parse_catalog(filepath).items():
                all_categories[cat].extend(entries)
    
    # Sort categories and distribute evenly across 5 output files
    sorted_cats = sorted(all_categories.keys())
    num_outputs = 5
    
    # Split categories into chunks
    chunks = [[] for _ in range(num_outputs)]
    for idx, cat in enumerate(sorted_cats):
        chunks[idx % num_outputs].append(cat)
    
    # Write output files
    for i, chunk in enumerate(chunks, start=2):
        output_path = f'catalog_{i}.txt'
        with open(output_path, 'w', encoding='utf-8') as f:
            for cat in chunk:
                f.write(f'[{cat}]\n')
                for entry in all_categories[cat]:
                    f.write(f'{entry}\n')
                f.write('\n')
        print(f'Wrote {output_path} with {len(chunk)} categories')

if __name__ == '__main__':
    main()