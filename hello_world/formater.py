import json
from lxml import etree

PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, XML]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif format == XML:
        result = format_to_xml(msg, imie)
    return result


def format_to_xml(msg, imie):
    xml_greeting = etree.Element("greetings")

    xml_imie = etree.SubElement(xml_greeting, "imie")
    xml_imie.text = imie

    xml_msg = etree.SubElement(xml_greeting, "msg")
    xml_msg.text = msg

    xml_output = etree.tostring(xml_greeting, pretty_print=True)
    return xml_output


def format_to_json(msg, imie):
    formatted_output = {'imie': imie, 'msg': msg}
    return json.dumps(formatted_output)


def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
