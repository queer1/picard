# -*- coding: utf-8 -*-

import unittest
from picard import (version_to_string,
                    version_from_string,
                    VersionError)


class VersionsTest(unittest.TestCase):

    def test_version_conv_1(self):
        l, s = (0, 0, 1, 'dev', 1), '0.0.1dev1'
        self.assertEqual(version_to_string(l), s)
        self.assertEqual(l, version_from_string(s))

    def test_version_conv_2(self):
        l, s = (1, 1, 0, 'final', 0), '1.1.0final0'
        self.assertEqual(version_to_string(l), s)
        self.assertEqual(l, version_from_string(s))

    def test_version_conv_3(self):
        l, s = (1, 1, 0, 'dev', 0), '1.1.0dev0'
        self.assertEqual(version_to_string(l), s)
        self.assertEqual(l, version_from_string(s))

    def test_version_conv_4(self):
        l, s = (1, 0, 2, '', 0), '1.0.2'
        self.assertRaises(VersionError, version_to_string, (l))
        self.assertRaises(VersionError, version_from_string, (s))

    def test_version_conv_5(self):
        l, s = (999, 999, 999, 'dev', 999), '999.999.999dev999'
        self.assertEqual(version_to_string(l), s)
        self.assertEqual(l, version_from_string(s))

    def test_version_conv_6(self):
        l = (1, 0, 2, 'xx', 0)
        self.assertRaises(VersionError, version_to_string, (l))

    def test_version_conv_7(self):
        l, s = (1, 1, 0, 'final', 0), '1.1'
        self.assertEqual(version_to_string(l, short=True), s)

    def test_version_conv_8(self):
        l, s = (1, 1, 1, 'final', 0), '1.1.1'
        self.assertEqual(version_to_string(l, short=True), s)

    def test_version_conv_9(self):
        l, s = (1, 1, 0, 'final', 1), '1.1'
        self.assertEqual(version_to_string(l, short=True), s)

    def test_version_conv_10(self):
        l, s = (1, 1, 0, 'dev', 0), '1.1.0dev0'
        self.assertEqual(version_to_string(l, short=True), s)

    def test_version_conv_11(self):
        l, s = ('1', '1', '0', 'dev', '0'), '1.1.0dev0'
        self.assertEqual(version_to_string(l), s)

    def test_version_conv_12(self):
        l, s = (1, 1, 0, 'dev', 0), '1_1_0_dev_0'
        self.assertEqual(l, version_from_string(s))

    def test_version_conv_13(self):
        l, s = (1, 1, 0, 'dev', 0), 'anything_28_1_1_0_dev_0'
        self.assertEqual(l, version_from_string(s))

    def test_version_conv_14(self):
        l = 'anything_28x_1_0_dev_0'
        self.assertRaises(VersionError, version_to_string, (l))
