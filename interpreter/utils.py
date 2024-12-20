def parse_text_from_file(filename: str) -> str:
    """Parse text from file"""
    with open(filename) as f:
        return repr(f.read().strip())[1:-1]
