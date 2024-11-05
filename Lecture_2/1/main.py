import xml.etree.ElementTree as et
import json

def parse_xml():
    tree = et.parse("cats.xml")
    root = tree.getroot()

    facts = []

    for child in root:
        print(child.tag, child.attrib)

        for grandchild in child:
            if grandchild.tag == "fact":
                facts.append(grandchild.text)

    with open("cats_facts.txt", "w") as file:
        for i in facts:
            file.write(f"{i}\n")


def parse_xml_2():
    tree = et.parse("cats.xml")
    root = tree.getroot()

    facts = []

    for info in root.findall("info"):
        fact = info.find("fact").text
        facts.append(fact)

    with open("cats_facts_2.txt", "w") as file:
        for i in facts:
            file.write(f"{i}\n")


def example_json():
    tree = et.parse("cats.xml")
    root = tree.getroot()

    facts = {}
    counter = 0

    for child in root:
        print(child.tag, child.attrib)

        for grandchild in child:
            if grandchild.tag == "fact":
                counter += 1
                facts[f"fact_{counter}"] = grandchild.text

    with open("cats_facts.json", "w") as file:
        json.dump(facts,file, indent=4)


if __name__ == "__main__":
    example_json()
