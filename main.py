import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to file")
    args = parser.parse_args()
    
    full_path = os.path.abspath(args.file_path)
    print(f"Path: {full_path}")

if __name__ == "__main__":
    main()
