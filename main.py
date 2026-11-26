import os

# One-star review of the Moon (<=120 chars); written verbatim to entry.txt.
import sys

LINE = "1/5* Blocked the Sun with no warning. My day is gone and support just says 'eclipse.'"

def main() -> int:
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(LINE)
    
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    char_count = len(content)
    if not (1 <= char_count <= 120):
        print(f'ERROR: character count {char_count} out of range [1, 120]', file=sys.stderr)
        return 1
    
    print(f'{output_path} {char_count}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
