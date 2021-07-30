# -*- coding: utf-8 -*-
import minecraft_with_python.mcwpy as mcwpy
import os
import unittest


class TestDatapackAttributes(unittest.TestCase):
    def test_datapack_default_values(self):
        self.assertEqual(mcwpy.Datapack().title, 'My_Amazing_Datapack')
        self.assertEqual(mcwpy.Datapack().path, os.getcwd())
        self.assertEqual(mcwpy.Datapack().author, 'MCWPy')
        self.assertEqual(mcwpy.Datapack().pack_mcmeta, {})
        self.assertEqual(mcwpy.Datapack().workspaces, [])
        self.assertFalse(mcwpy.Datapack().auto_compile)
        self.assertFalse(mcwpy.Datapack().compile_as_zip)
        self.assertFalse(mcwpy.Datapack().replace_existing)
        self.assertEqual(mcwpy.Datapack().description, '')

    def test_datapack_default_instances(self):
        self.assertIsInstance(mcwpy.Datapack(), mcwpy.Datapack)
        self.assertIsInstance(mcwpy.Datapack().title, str)
        self.assertIsInstance(mcwpy.Datapack().path, str)
        self.assertIsInstance(mcwpy.Datapack().author, str)
        self.assertIsInstance(mcwpy.Datapack().pack_mcmeta, dict)
        self.assertIsInstance(mcwpy.Datapack().workspaces, list)
        self.assertIsInstance(mcwpy.Datapack().auto_compile, bool)
        self.assertIsInstance(mcwpy.Datapack().compile_as_zip, bool)
        self.assertIsInstance(mcwpy.Datapack().replace_existing, bool)
        self.assertIsInstance(mcwpy.Datapack().description, str)

    def test_datapack_values_set(self):
        self.assertEqual(mcwpy.Datapack(title='string').title, 'string')
        self.assertEqual(mcwpy.Datapack(path='string').path, 'string')
        self.assertEqual(mcwpy.Datapack(author='string').author, 'string')
        self.assertEqual(mcwpy.Datapack(pack_mcmeta={'string': 'string'}).pack_mcmeta, {'string': 'string'})
        self.assertEqual(mcwpy.Datapack(workspaces=[]).workspaces, [])
        self.assertTrue(mcwpy.Datapack(auto_compile=True).auto_compile)
        self.assertTrue(mcwpy.Datapack(compile_as_zip=True).compile_as_zip)
        self.assertTrue(mcwpy.Datapack(replace_existing=True).replace_existing)
        self.assertEqual(mcwpy.Datapack(description='string').description, 'string')
        self.assertEqual(mcwpy.Datapack(version='string').version, 'string')

    def test_datapack_workspaces(self):
        with self.assertRaises(TypeError):
            mcwpy.Datapack(workspaces=object)
            mcwpy.Datapack(workspaces=[int()])
            mcwpy.Datapack(workspaces=[bool()])
            mcwpy.Datapack(workspaces=[list()])
            mcwpy.Datapack(workspaces=[dict()])
            mcwpy.Datapack(workspaces=['string'])

    def test_datapack_iteration_with_workspaces(self):
        example_workspace = mcwpy.Datapack(workspaces=[mcwpy.Workspace(name='string'), mcwpy.Workspace(name='string')])

        self.assertEqual([e.name for e in example_workspace], ['string', 'string'])
        self.assertEqual(len(example_workspace), 2)


if __name__ == '__main__':
    unittest.main()
