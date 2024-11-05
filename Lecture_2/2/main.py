from xml.etree import ElementTree
import json

tree = ElementTree.parse("xml_practice.xml")
root = tree.getroot()

print(f"Number of books: {len(root)}\n")

book_names = []
book_descriptions = []
authors = []

for book in root:
    for element in book:
        if element.tag == "title":
            book_names.append(element.text)
        if element.tag == "description":
            book_descriptions.append(element.text.replace("\n", "").replace("      ", " "))
        if element.tag == "author":
            authors.append(element.text)

index = 0
for i in authors:
    i = i.split(", ")
    i = f"{i[1]} {i[0]}"
    authors[index] = i
    index += 1

data = {}

book_index = 1
for name, desc, author in zip(book_names, book_descriptions, authors):
    # print(f"Book title: {name}")
    # print(f"Book description: {desc}")
    # print(f"Author: {author}\n")
    data[f"Book_{book_index}"] = f"book_title: {name}", f"book_description: {desc}", f"author: {author}"
    book_index += 1

with open("books.json", "w") as file:
    json.dump(data, file, indent=4)
