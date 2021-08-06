# -*- coding: ascii -*-
import minecraft_with_python.mcwpy.datapack as mcwpy
import os
import unittest
import shutil


class TestDatapack(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.example_workspace = mcwpy.Datapack(workspaces=[mcwpy.Workspace(name='string'), mcwpy.Workspace(name='string')])

    ##############################
    # Datapack attributes
    ##############################
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

    ##############################
    # Datapack methods
    ##############################
    def test_datapack___str__(self):
        self.assertEqual(
            str(mcwpy.Datapack()),
            "---- {}\n\t|\n\t---- pack.mcmeta: {}\n\t---- pack.png\n\t---- data\n\t\t|\n\t\t".format(
                mcwpy.Datapack().title, mcwpy.Datapack().pack_mcmeta
            )
        )
        self.assertEqual(
            str(self.example_workspace),
            "---- {}\n\t|\n\t---- pack.mcmeta: {}\n\t---- pack.png\n\t---- data\n\t\t|\n\t\t{}".format(
                self.example_workspace.title, self.example_workspace.pack_mcmeta,
                ', \n\t\t'.join(map(lambda x: f'---- {x.name}', self.example_workspace))
            )
        )

    def test_datapack___getitem__(self):
        self.assertEqual(self.example_workspace[0].name, 'string')

    def test_datapack___iter__(self):
        self.assertEqual([e.name for e in self.example_workspace], ['string', 'string'])
        
    def test_datapack___len__(self):
        self.assertEqual(len(self.example_workspace), 2)

    def test_datapack_append_and_pop(self):
        # Add wrong type.
        example_workspace_len = len(self.example_workspace)
        self.example_workspace.append('string')
        self.assertEqual(len(self.example_workspace), example_workspace_len)

        # Add right type.
        self.example_workspace.append(mcwpy.Workspace(name='remove'))
        self.assertEqual(len(self.example_workspace), 3)

        # Remove last item.
        self.assertEqual(self.example_workspace.pop().name, 'remove')


if __name__ == '__main__':
    unittest.main()
