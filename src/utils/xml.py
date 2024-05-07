from xml.etree import ElementTree as ET


def extract_from_xml(xml_string, selector):
    # Parse the XML string
    root = ET.fromstring(xml_string)
    # Find the tag in the XML
    extracted = root.find(selector)

    if extracted is not None:
        # Extract the text of the searched element
        return extracted.text
    else:
        return None
