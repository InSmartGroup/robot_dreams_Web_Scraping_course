import csv
import json
import re
import requests
import sqlite3
from xml.etree import ElementTree


# writing data to csv
def write_csv(data: list):
    filename = "result.csv"

    columns = ["first_name", "last_name", "weight", "is_male"]

    with open(f"./Outputs/{filename}", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)


# writing data to json
def write_json(data: list):
    filename = "result.json"

    data = [
        {
            "first_name": i[0],
            "last_name": i[1],
            "weight": i[2],
            "is_male": i[3]
        }
        for i in data
    ]

    with open(f"./Outputs/{filename}", "w") as file:
        json.dump(data, file, indent=4)


# writing data to xml
def write_xml(data: list):
    filename = "result.xml"

    root = ElementTree.Element("People")

    for i in data:
        person = ElementTree.SubElement(root, "Person")
        ElementTree.SubElement(person, "first_name").text = i[0]
        ElementTree.SubElement(person, "last_name").text = i[1]
        ElementTree.SubElement(person, "weight").text = str(i[2])
        ElementTree.SubElement(person, "is_male").text = str(i[3])

    tree = ElementTree.ElementTree(root)

    tree.write(f"./Outputs/{filename}", encoding="utf-8", xml_declaration=True)


# writing data to sqlite
def write_sql(data: list):
    filename = "result.db"

    # create sql table
    connection = sqlite3.connect(f"./Outputs/{filename}")
    cursor = connection.cursor()

    sql = """
        CREATE TABLE if NOT EXISTS people (
            ID INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            weight INTEGER NOT NULL,
            is_male BOOLEAN NOT NULL,
            UNIQUE (first_name, last_name, weight, is_male)
        )
    """

    cursor.execute(sql)

    # write data to the sql table
    for i in data:
        cursor.execute("""
            INSERT INTO people (first_name, last_name, weight, is_male)
            VALUES (?, ?, ?, ?)
        """, (i[0], i[1], i[2], i[3]))

    connection.commit()
    connection.close()


def read_sql():
    filename = "./Outputs/result.db"

    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

    # get people names
    sql = """
        SELECT first_name, last_name
        FROM people
    """


    # get only males
    sql = """
        SELECT first_name, last_name
        FROM people
        WHERE is_male = TRUE
    """

    # get only weights above 80
    sql = """
        SELECT weight
        FROM people
        WHERE weight > 80
    """

    # get max weight
    sql = """
        SELECT weight
        FROM people
        WHERE weight = (SELECT MAX(weight) FROM people)
    """

    response = cursor.execute(sql).fetchall()
    print(response)

    connection.close()


if __name__ == "__main__":
    data_example = [
        ["Tom", "Smith", 80, True],
        ["Alice", "Johnson", 92, False],
        ["Bob", "Williams", 75, True],
        ["Emma", "Brown", 88, False],
        ["David", "Jones", 107, True]
    ]

    # write_csv(data_example)
    # write_json(data_example)
    # write_xml(data_example)
    # write_sql(data_example)
    # read_sql()
