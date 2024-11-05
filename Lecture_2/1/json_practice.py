import json
import xml.etree.ElementTree as et

root = et.parse("cats.xml").getroot()

found_facts = {}
counter = 0

for element in root:
    for sub_element in element:
        if sub_element.tag == "fact":
            found_facts[f"fact_{counter}"] = sub_element.text
            counter += 1

    with open("json_practice.json", "w") as file:
        json.dump(found_facts, file, indent=4)
