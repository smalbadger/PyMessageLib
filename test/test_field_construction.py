import unittest
from message_builder import MessageBuilder
from msg_definitions import msg_fmts, register_defs
from field import Bit, Bits
from _exceptions import InvalidFormatException, InvalidFieldDataException, InvalidDataFormatException


class TestFieldConstruction(unittest.TestCase):
    def testSingularField(self):
        field = Bit()
        field = Bit(1)
        with self.assertRaises(InvalidFormatException):
            field = Bit(length=2)
        with self.assertRaises(InvalidFormatException):
            field = Bit(length=0)

    def testPluralField(self):
        field = Bits(length=2)
        with self.assertRaises(InvalidFormatException):
            field = Bits()
        with self.assertRaises(InvalidFormatException):
            field = Bits(0)
        with self.assertRaises(InvalidFormatException):
            field = Bits(1)

    def testEmptyFieldName(self):
        field = Bit()
        self.assertEqual(field.name, "")
        
    def testInvalidValue(self):
        with self.assertRaises(InvalidFieldDataException):
            Bit(value='x2')
            
    def testInvalidValueFormat(self):
        with self.assertRaises(InvalidDataFormatException):
            Bit(value='2')
