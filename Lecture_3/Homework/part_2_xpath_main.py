from lxml import html

with open("part_2_webpage.html", "r") as file:
    content = file.read()

tree = html.fromstring(content)

search_pattern = r"//input[@id='text-input-what']"
location_pattern = r"//input[@id='text-input-where']"
button_pattern = r"//button[@class='yosegi-InlineWhatWhere-primaryButton' and @type='submit']"

search_xpath = tree.xpath(search_pattern)
print(search_xpath)

location_xpath = tree.xpath(location_pattern)
print(location_xpath)

button_xpath = tree.xpath(button_pattern)
print(button_xpath)
