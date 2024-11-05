import re


def find_emails(text_to_parse):
    pattern = r"[a-zA-Z0-9-._]+@[a-zA-Z0-9-_]+\.[a-zA-Z]+|[a-zA-Z0-9-._]+@[a-zA-Z0-9-_]+\.[a-zA-Z]+\.[a-zA-Z]+"
    emails = re.findall(pattern, text_to_parse)

    return emails


def find_dates(text_to_parse):
    pattern = r"\d{4}[./-]\d{2}[./-]\d{2}|\d{2}[-/.]\d{2}[./-][12]\d{3}|[A-Za-z]+\s?\d{2},?\s\d{4}"
    dates = re.findall(pattern, text_to_parse)

    return dates


def find_urls(text_to_parse):
    pattern = r"((www|ftp|https|http)[./:]{1,}[-a-zA-Z0-9._\?\!=]+)"
    urls = re.findall(pattern, text_to_parse)

    return [i[0] for i in urls]


def find_phones(text_to_parse):
    pattern = r"((\+[0-9]{1,}[-. ]?\d{3,}[-. ]?\d{3,}))"
    phones = re.findall(pattern, text_to_parse)

    return [i[0] for i in phones]


with open("part_1_text.txt", "r") as file:
    text = file.read()

if __name__ == "__main__":
    # # the text contains 8 emails
    # find_emails(text)
    # print(f"{len(find_emails(text))} emails found.")
    # print(f"Emails: {find_emails(text)}")
    #
    # # there are 8 dates (6 commonly used and 2 text-based)
    # find_dates(text)
    # print(f"{len(find_dates(text))} dates found.")
    # print(f"Dates: {find_dates(text)}")
    #
    # # there are 9 URLs
    # find_urls(text)
    # print(f"{len(find_urls(text))} URLs found.")
    # print(f"URLs: {find_urls(text)}")

    # there are 7 phone numbers
    find_phones(text)
    print(f"{len(find_phones(text))} phone numbers found.")
    print(f"Phone numbers: {find_phones(text)}")
