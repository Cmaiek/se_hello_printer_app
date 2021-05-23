from hello_world.formater import plain_text_upper_case, format_to_xml
import unittest
from lxml import etree
from lxml.etree import tostring
from lxml.builder import E


#TODO Propably better to use faker
EXAMPLE_MESSAGE = "MyMessage"
EXAMPLE_NAME = "MyName"


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())


    def test_xml(self):
        formated_xml = format_to_xml(EXAMPLE_MESSAGE, EXAMPLE_NAME)
        # this could be better used to generate xml
        #generated_xml = tostring(E.greetings(E.name(EXAMPLE_NAME), E.msg(EXAMPLE_MESSAGE)), pretty_print=True, xml_declaration=True, encoding='UTF-8')
        #self.assertEqual(generated_xml, formated_xml)
        root = etree.fromstring(formated_xml)
        self.assertEqual(root.tag, "greetings")
        self.assertEqual(root[0].tag, "name")
        self.assertEqual(root[1].tag, "msg")
        self.assertEqual(root[0].text, EXAMPLE_NAME)
        self.assertEqual(root[1].text, EXAMPLE_MESSAGE)
