import xml.etree.ElementTree as et

# first, parse the data
tree = et.parse("cats.xml")
print(f"XML tree: {tree}")

# next, access the root element (it's "data")
root = tree.getroot()
print(f"XML root: {root}")

print(f"Root type: {type(root)}")

print(f"Root length: {len(root)}")

# let's see how many levels we have
for child in root:
    print(f"Child root element: {child}")

    for grandchild in child:
        print(f"Grandchild element: {grandchild}")

        for grand_grandchild in grandchild:
            print(f"Grand grandchild element: {grand_grandchild}")  # no such elements on this level

# it's possible to access specific root elements; in our case, root has 2 child 'info' elements
print(f"Root, element 0 - info: {root[0]}")
print(f"Root, element 1 - info: {root[1]}")

# we can also access sub-elements of the first 'info' root child element
print(f"The number of info sub-elements: {len(root[0])}")
print(f"First sub-element of root info 0: {root[0][0]}")
print(f"Second sub-element of root info 0: {root[0][1]}")

# and we can access the needed sub-elements of the first 'info' child element
print(f"Sub-element 0 of info 0: {root[0][0].text}")
print(f"Sub-element 0 tag: {root[0][0].tag}")
print(f"Sub-element 1 of info 0: {root[0][1].text}")
print(f"Sub-element 1 tag: {root[0][1].tag}")
