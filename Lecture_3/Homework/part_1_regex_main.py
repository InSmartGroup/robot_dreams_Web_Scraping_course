import re


def find_emails(text_to_parse):
    pattern = r"[a-zA-Z0-9-._]+@[a-zA-Z0-9-_]+\.[a-zA-Z]+|[a-zA-Z0-9-._]+@[a-zA-Z0-9-_]+\.[a-zA-Z]+\.[a-zA-Z]+"
    emails = re.findall(pattern, text_to_parse)

    return emails


def find_dates(text_to_parse, current_year=2024):
    pattern = r"\d{4}[./-]\d{2}[./-]\d{2}|\d{2}[-/.]\d{2}[./-][12]\d{3}|[A-Za-z]+\s?\d{2},?\s\d{4}"
    dates = re.findall(pattern, text_to_parse)

    return dates


with open("part_1_text.txt", "r") as file:
    text = file.read()

if __name__ == "__main__":
    # the text contains 8 emails
    find_emails(text)
    print(f"{len(find_emails(text))} emails found.")
    print(f"Emails: {find_emails(text)}")

    # the text contains 8 dates (6 commonly used and 2 text-based)
    find_dates(text)
    print(f"{len(find_dates(text))} dates found.")
    print(f"Dates: {find_dates(text)}")
