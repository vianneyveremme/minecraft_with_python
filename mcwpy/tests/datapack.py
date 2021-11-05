# -*- coding: ascii -*-
import minecraft_with_python.mcwpy.datapack as mcwpy_datapack
import minecraft_with_python.mcwpy.pack_meta as mcwpy_pack_meta
import os
import unittest
import shutil



class TestDatapack(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.example_datapack = mcwpy_datapack.Datapack(workspaces=[mcwpy_datapack.Workspace(name='string'), mcwpy_datapack.Workspace(name='string')])

    def test_datapack_default_values(self):
        self.assertEqual(mcwpy_datapack.Datapack().title, 'My_Amazing_Datapack')
        self.assertEqual(mcwpy_datapack.Datapack().path, os.getcwd())
        self.assertEqual(mcwpy_datapack.Datapack().workspaces, [])
        self.assertFalse(mcwpy_datapack.Datapack().auto_compile)
        self.assertFalse(mcwpy_datapack.Datapack().compile_as_zip)
        self.assertFalse(mcwpy_datapack.Datapack().replace_existing)

    def test_datapack_default_instances(self):
        self.assertIsInstance(mcwpy_datapack.Datapack(), mcwpy_datapack.Datapack)
        self.assertIsInstance(mcwpy_datapack.Datapack().title, str)
        self.assertIsInstance(mcwpy_datapack.Datapack().path, str)
        self.assertIsInstance(mcwpy_datapack.Datapack().pack_mcmeta, mcwpy_pack_meta.Pack_Meta)
        self.assertIsInstance(mcwpy_datapack.Datapack().workspaces, list)
        self.assertIsInstance(mcwpy_datapack.Datapack().auto_compile, bool)
        self.assertIsInstance(mcwpy_datapack.Datapack().compile_as_zip, bool)
        self.assertIsInstance(mcwpy_datapack.Datapack().replace_existing, bool)

    def test_datapack_values_set(self):
        self.assertEqual(mcwpy_datapack.Datapack(title='string').title, 'string')
        self.assertEqual(mcwpy_datapack.Datapack(path='string').path, 'string')
        self.assertEqual(mcwpy_datapack.Datapack(pack_mcmeta={'string': 'string'}).pack_mcmeta, {'string': 'string'})
        self.assertEqual(mcwpy_datapack.Datapack(workspaces=[]).workspaces, [])
        self.assertTrue(mcwpy_datapack.Datapack(auto_compile=True).auto_compile)
        self.assertTrue(mcwpy_datapack.Datapack(compile_as_zip=True).compile_as_zip)
        self.assertTrue(mcwpy_datapack.Datapack(replace_existing=True).replace_existing)

        # Remove the generated files
        shutil.rmtree(os.path.join(os.getcwd(), mcwpy_datapack.Datapack().title))

    def test_datapack_workspaces(self):
        with self.assertRaises(TypeError):
            mcwpy_datapack.Datapack(workspaces=object)
            mcwpy_datapack.Datapack(workspaces=[int()])
            mcwpy_datapack.Datapack(workspaces=[bool()])
            mcwpy_datapack.Datapack(workspaces=[list()])
            mcwpy_datapack.Datapack(workspaces=[dict()])
            mcwpy_datapack.Datapack(workspaces=['string'])
            self.example_datapack.append('string')

    ##############################
    # Datapack methods
    ##############################
    def test_datapack___getitem__(self):
        self.assertEqual(self.example_datapack[0].name, 'string')
        self.assertEqual(self.example_datapack[0].name, self.example_datapack.workspaces[0].name)

    def test_datapack___iter__(self):
        self.assertEqual([e.name for e in self.example_datapack], ['string', 'string'])

    def test_datapack___len__(self):
        self.assertEqual(len(self.example_datapack), 2)


if __name__ == '__main__':
    unittest.main()
