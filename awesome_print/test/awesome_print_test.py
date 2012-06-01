# encoding: utf-8
import sys
sys.path.insert(0, 'awesome_print')

import unittest
from awesome_print import format

class Test_awesome_print(unittest.TestCase):

    def test_None(self):
        self.assertEqual(format(None), '\x1b[0;31mNone\x1b[0m')

    def test_True(self):
        self.assertEqual(format(True), '\x1b[1;32mTrue\x1b[0m')

    def test_False(self):
        self.assertEqual(format(False), '\x1b[1;32mFalse\x1b[0m')

    def test_String_plain(self):
        self.assertEqual(format('plain string'), '\x1b[0;33mplain string\x1b[0m')

    def test_String_with_escapes(self):
        self.assertEqual(format("with\n's"), '\x1b[0;33mwith\n\'s\x1b[0m')

    def test_Int_positive(self):
        self.assertEqual(format(12345), '\x1b[1;34m12345\x1b[0m')

    def test_Int_negative(self):
        self.assertEqual(format(-12345), '\x1b[1;34m-12345\x1b[0m')

    def test_Long_positive(self):
        self.assertEqual(format(12345l), '\x1b[1;34m12345\x1b[0m')

    def test_Long_negative(self):
        self.assertEqual(format(-12345l), '\x1b[1;34m-12345\x1b[0m')

    def test_Float_positive(self):
        self.assertEqual(format(123.45), '\x1b[1;34m123.45\x1b[0m')

    def test_Float_negative(self):
        self.assertEqual(format(-123.45), '\x1b[1;34m-123.45\x1b[0m')

    def test_Complex_positive(self):
        self.assertEqual(format(complex('1.2+3.45j')),
                '\x1b[1;34m(1.2+3.45j)\x1b[0m')

    def test_Complex_negative(self):
        self.assertEqual(format(complex('-1.2+3.45j')),
                '\x1b[1;34m(-1.2+3.45j)\x1b[0m')

    def test_Tuple_empty(self):
        self.assertEqual(format(()), '()')

    def test_Tuple_Int(self):
        self.assertEqual(format((1,)), '(\n  [0] \x1b[1;34m1\x1b[0m\n)')

    def test_Tuple_mixed(self):
        self.assertEqual(format((1,True,'string')),
            '(\n' +
            '  [0] \x1b[1;34m1\x1b[0m,\n' +
            '  [1] \x1b[1;32mTrue\x1b[0m,\n' +
            '  [2] \x1b[0;33mstring\x1b[0m\n' +
            ')')

    def test_List_empty(self):
        self.assertEqual(format([]), '[]')

    def test_List_Int(self):
        self.assertEqual(format([1]), '[\n  [0] \x1b[1;34m1\x1b[0m\n]')

    def test_List_mixed(self):
        self.assertEqual(format([1,True,'string']),
            '[\n' +
            '  [0] \x1b[1;34m1\x1b[0m,\n' +
            '  [1] \x1b[1;32mTrue\x1b[0m,\n' +
            '  [2] \x1b[0;33mstring\x1b[0m\n' +
            ']')

    def test_Dict_empty(self):
        self.assertEqual(format({}), '{}')

    def test_Dict_Int(self):
        self.assertEqual(format({1:2}),
                '{\n  \x1b[1;34m1\x1b[0m: \x1b[1;34m2\x1b[0m\n}')

    def test_Dict_mixed(self):
        self.assertEqual(format({None:False,'key':'value',2:5}),
                '{\n' +
                '  \x1b[0;31mNone\x1b[0m: \x1b[1;32mFalse\x1b[0m,\n' +
                '     \x1b[1;34m2\x1b[0m: \x1b[1;34m5\x1b[0m,\n' +
                '   \x1b[0;33mkey\x1b[0m: \x1b[0;33mvalue\x1b[0m\n' +
                '}')

    def test_List_in_List(self):
        self.assertEqual(format(
            [
                [1,2,3],
            ]),
            '[\n' +
            '  [0] [\n' +
            '    [0] \x1b[1;34m1\x1b[0m,\n' +
            '    [1] \x1b[1;34m2\x1b[0m,\n' +
            '    [2] \x1b[1;34m3\x1b[0m\n' +
            '  ]\n' +
            ']'
            )

    def test_Dict_in_List(self):
        self.assertEqual(format(
            [
                {
                    'a': 'b'
                }
            ]),
            '[\n' +
            '  [0] {\n' +
            '    \x1b[0;33ma\x1b[0m: \x1b[0;33mb\x1b[0m\n' +
            '  }\n' +
            ']'
            )


if __name__ == '__main__':
    unittest.main()
