import re


class TextParser:
    def __init__(self, text_file_path):
        with open(text_file_path, "r") as file:
            self.text = file.read()

    def text(self):
        return self.text

    def find_emails(self):
        pattern = r"[a-zA-Z0-9-._]+@[a-zA-Z0-9-_]+\.[a-zA-Z]+|[a-zA-Z0-9-._]+@[a-zA-Z0-9-_]+\.[a-zA-Z]+\.[a-zA-Z]+"
        emails = re.findall(pattern, self.text)

        return emails

    def length_emails(self):
        if self.find_emails():
            return len(self.find_emails())
        else:
            return "No emails found."

    def find_dates(self):
        pattern = r"\d{4}[./-]\d{2}[./-]\d{2}|\d{2}[-/.]\d{2}[./-][12]\d{3}|[A-Za-z]+\s?\d{2},?\s\d{4}"
        dates = re.findall(pattern, self.text)

        return dates

    def length_dates(self):
        if self.find_dates():
            return len(self.find_dates())
        else:
            return "No dates found."

    def find_urls(self):
        pattern = r"((www|ftp|https|http)[./:]{1,}[-a-zA-Z0-9._\?\!=]+)"
        urls = re.findall(pattern, self.text)

        return [i[0] for i in urls]

    def length_urls(self):
        if self.find_urls():
            return len(self.find_dates())
        else:
            return "No URLs found."

    def find_phones(self):
        pattern = r"((\+[0-9]{1,}[-. ]?\d{3,}[-. ]?\d{3,}))"
        phones = re.findall(pattern, self.text)

        return [i[0] for i in phones]

    def length_phones(self):
        if self.find_phones():
            return len(self.find_phones())
        else:
            return "No phones found."


if __name__ == "__main__":
    text_parser = TextParser("part_1_text.txt")

    # print(text_parser.text)
    #
    # # there should be 8 emails
    # print(text_parser.length_emails())
    # print(text_parser.find_emails())
    #
    # # there should be 8 dates
    # print(text_parser.length_dates())
    # print(text_parser.find_dates())
    #
    # # there should be 8 URLs
    # print(text_parser.length_urls())
    # print(text_parser.find_urls())

    # NOTE: this function hasn't been completed yet
    # there should be 9 phone numbers
    print(text_parser.length_phones())
    print(text_parser.find_phones())
