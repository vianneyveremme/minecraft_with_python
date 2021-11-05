# -*- coding: ascii -*-
from minecraft_with_python.mcwpy import Datapack, Workspace, Pack_Meta
import os
import unittest
import shutil


class TestDatapack(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.example_datapack = Datapack(workspaces=[Workspace(name='string'), Workspace(name='string')])

    def test_datapack_default_values(self):
        self.assertEqual(Datapack().title, 'My_Amazing_Datapack')
        self.assertEqual(Datapack().path, os.getcwd())
        self.assertEqual(Datapack().workspaces, [])
        self.assertFalse(Datapack().auto_compile)
        self.assertFalse(Datapack().compile_as_zip)
        self.assertFalse(Datapack().replace_existing)

    def test_datapack_default_instances(self):
        self.assertIsInstance(Datapack(), Datapack)
        self.assertIsInstance(Datapack().title, str)
        self.assertIsInstance(Datapack().path, str)
        self.assertIsInstance(Datapack().pack_mcmeta, Pack_Meta)
        self.assertIsInstance(Datapack().workspaces, list)
        self.assertIsInstance(Datapack().auto_compile, bool)
        self.assertIsInstance(Datapack().compile_as_zip, bool)
        self.assertIsInstance(Datapack().replace_existing, bool)

    def test_datapack_values_set(self):
        self.assertEqual(Datapack(title='string').title, 'string')
        self.assertEqual(Datapack(path='string').path, 'string')
        self.assertEqual(Datapack(pack_mcmeta={'string': 'string'}).pack_mcmeta, {'string': 'string'})
        self.assertEqual(Datapack(workspaces=[]).workspaces, [])
        self.assertTrue(Datapack(auto_compile=True).auto_compile)
        self.assertTrue(Datapack(compile_as_zip=True).compile_as_zip)
        self.assertTrue(Datapack(replace_existing=True).replace_existing)

        # Remove the generated files
        shutil.rmtree(os.path.join(os.getcwd(), Datapack().title))

    def test_datapack_workspaces(self):
        with self.assertRaises(TypeError):
            Datapack(workspaces=object)
            Datapack(workspaces=[int()])
            Datapack(workspaces=[bool()])
            Datapack(workspaces=[list()])
            Datapack(workspaces=[dict()])
            Datapack(workspaces=['string'])
            self.example_datapack.append('string')

    ##############################
    # Datapack methods
    ##############################
    def test_datapack___getitem__(self):
        self.assertEqual(self.example_datapack[0].name, 'string')
        self.assertEqual(self.example_datapack[0].name, self.example_datapack[0].name)

    def test_datapack___iter__(self):
        self.assertEqual([e.name for e in self.example_datapack], ['string', 'string'])

    def test_datapack___len__(self):
        self.assertEqual(len(self.example_datapack), 2)


if __name__ == '__main__':
    unittest.main()
