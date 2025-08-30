import sys
from stats import get_chars_dict, chars_dict_to_sorted_list

def get_book_text(path):
    """Reads the content of a file using UTF-8 encoding."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    """
    Main function to run the book analysis.
    Takes a book path from command line and prints character counts.
    """
    # 1. Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 2. Get book path and read the text
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    
    # 3. Convert text to lowercase to ensure case-insensitive counting
    lower_text = text.lower()
    
    # 4. Get character counts and the sorted list from the stats module
    chars_dict = get_chars_dict(lower_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # 5. Print the character report in the required format
    for item in chars_sorted_list:
        # Filter for only lowercase 'a' through 'z' to match test requirements
        if 'a' <= item["char"] <= 'z':
            print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
