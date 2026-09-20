"""Check public project structure only; never read identity records or private siblings."""
from pathlib import Path
import sys

REQUIRED = ("README.md", "AGENTS.md", "PROJECT_CONTEXT.md", "PARTICIPATION.md",
            "CONTRIBUTIONS.md", "SECURITY.md", "STATUS.md", "SOURCES.md",
            "economics.py", "test_economics.py", ".gitignore")

def main():
    root = Path(__file__).resolve().parent
    missing = [name for name in REQUIRED if not (root / name).is_file()]
    if missing:
        print("Missing public project files: " + ", ".join(missing))
        return 1
    print("Public project structure: PASS")
    print("Identity records and private directories: not opened")
    print("FLOP eligibility/allocation: UNVERIFIED; this check cannot certify rewards")
    return 0

if __name__ == "__main__":
    sys.exit(main())
