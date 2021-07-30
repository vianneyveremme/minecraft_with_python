# -*- coding: utf-8 -*-
from datapack import Datapack
from datetime import date
from time import time
from workspace import Workspace
import os
import unittest


class TestStringMethods(unittest.TestCase):
    def test_datapack_default_values(self):
        self.assertEqual(Datapack().title, 'My_Amazing_Datapack')
        self.assertEqual(Datapack().path, os.getcwd())
        self.assertEqual(Datapack().author, 'MCWPy')
        self.assertEqual(Datapack().pack_mcmeta, {})
        self.assertEqual(Datapack().workspaces, [])
        self.assertFalse(Datapack().auto_compile)
        self.assertFalse(Datapack().compile_as_zip)
        self.assertFalse(Datapack().replace_existing)
        self.assertEqual(Datapack().description, '')

    def test_datapack_default_instances(self):
        self.assertIsInstance(Datapack(), Datapack)
        self.assertIsInstance(Datapack().title, str)
        self.assertIsInstance(Datapack().path, str)
        self.assertIsInstance(Datapack().author, str)
        self.assertIsInstance(Datapack().pack_mcmeta, dict)
        self.assertIsInstance(Datapack().workspaces, list)
        self.assertIsInstance(Datapack().auto_compile, bool)
        self.assertIsInstance(Datapack().compile_as_zip, bool)
        self.assertIsInstance(Datapack().replace_existing, bool)
        self.assertIsInstance(Datapack().description, str)

    def test_datapack_values_set(self):
        self.assertEqual(Datapack(title='string').title, 'string')
        self.assertEqual(Datapack(path='string').path, 'string')
        self.assertEqual(Datapack(author='string').author, 'string')
        self.assertEqual(Datapack(pack_mcmeta={'string': 'string'}).pack_mcmeta, {'string': 'string'})
        self.assertEqual(Datapack(workspaces=[0, 1]).workspaces, [0, 1])
        self.assertTrue(Datapack(auto_compile=True).auto_compile)
        self.assertTrue(Datapack(compile_as_zip=True).compile_as_zip)
        self.assertTrue(Datapack(replace_existing=True).replace_existing)
        self.assertEqual(Datapack(description='string').description, 'string')
        self.assertEqual(Datapack(version='string').version, 'string')

    def test_datapack_iteration_with_workspaces(self):
        self.assertEqual([e.name for e in Datapack(workspaces=[Workspace(name='string'), Workspace(name='string')])], ['string', 'string'])


if __name__ == '__main__':
    unittest.main()
