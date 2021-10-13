# -*- coding: ascii -*-
import minecraft_with_python.mcwpy.datapack as mcwpy_datapack
import os
import unittest


class TestDatapack(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.example_workspace = mcwpy_datapack.Datapack(workspaces=[mcwpy_datapack.Workspace(name='string'), mcwpy_datapack.Workspace(name='string')])

    def test_datapack_default_values(self):
        self.assertEqual(mcwpy_datapack.Datapack().title, 'My_Amazing_Datapack')
        self.assertEqual(mcwpy_datapack.Datapack().path, os.getcwd())
        self.assertEqual(mcwpy_datapack.Datapack().author, 'MCWPy')
        self.assertEqual(mcwpy_datapack.Datapack().pack_mcmeta, {})
        self.assertEqual(mcwpy_datapack.Datapack().workspaces, [])
        self.assertFalse(mcwpy_datapack.Datapack().auto_compile)
        self.assertFalse(mcwpy_datapack.Datapack().compile_as_zip)
        self.assertFalse(mcwpy_datapack.Datapack().replace_existing)
        self.assertEqual(mcwpy_datapack.Datapack().description, '')

    def test_datapack_default_instances(self):
        self.assertIsInstance(mcwpy_datapack.Datapack(), mcwpy_datapack.Datapack)
        self.assertIsInstance(mcwpy_datapack.Datapack().title, str)
        self.assertIsInstance(mcwpy_datapack.Datapack().path, str)
        self.assertIsInstance(mcwpy_datapack.Datapack().author, str)
        self.assertIsInstance(mcwpy_datapack.Datapack().pack_mcmeta, dict)
        self.assertIsInstance(mcwpy_datapack.Datapack().workspaces, list)
        self.assertIsInstance(mcwpy_datapack.Datapack().auto_compile, bool)
        self.assertIsInstance(mcwpy_datapack.Datapack().compile_as_zip, bool)
        self.assertIsInstance(mcwpy_datapack.Datapack().replace_existing, bool)
        self.assertIsInstance(mcwpy_datapack.Datapack().description, str)

    def test_datapack_values_set(self):
        self.assertEqual(mcwpy_datapack.Datapack(title='string').title, 'string')
        self.assertEqual(mcwpy_datapack.Datapack(path='string').path, 'string')
        self.assertEqual(mcwpy_datapack.Datapack(author='string').author, 'string')
        self.assertEqual(mcwpy_datapack.Datapack(pack_mcmeta={'string': 'string'}).pack_mcmeta, {'string': 'string'})
        self.assertEqual(mcwpy_datapack.Datapack(workspaces=[]).workspaces, [])
        self.assertTrue(mcwpy_datapack.Datapack(auto_compile=True).auto_compile)
        self.assertTrue(mcwpy_datapack.Datapack(compile_as_zip=True).compile_as_zip)
        self.assertTrue(mcwpy_datapack.Datapack(replace_existing=True).replace_existing)
        self.assertEqual(mcwpy_datapack.Datapack(description='string').description, 'string')
        self.assertEqual(mcwpy_datapack.Datapack(version='string').version, 'string')

    def test_datapack_workspaces(self):
        with self.assertRaises(TypeError):
            mcwpy_datapack.Datapack(workspaces=object)
            mcwpy_datapack.Datapack(workspaces=[int()])
            mcwpy_datapack.Datapack(workspaces=[bool()])
            mcwpy_datapack.Datapack(workspaces=[list()])
            mcwpy_datapack.Datapack(workspaces=[dict()])
            mcwpy_datapack.Datapack(workspaces=['string'])

    ##############################
    # Datapack methods
    ##############################
    def test_datapack___str__(self):
        self.assertEqual(str(mcwpy_datapack.Datapack()),
            "---- {}\n\t|\n\t---- pack.mcmeta: {}\n\t---- pack.png\n\t---- data\n\t\t|\n\t\t".format(
                mcwpy_datapack.Datapack().title, mcwpy_datapack.Datapack().pack_mcmeta
        ))
        self.assertEqual(str(self.example_workspace),
            "---- {}\n\t|\n\t---- pack.mcmeta: {}\n\t---- pack.png\n\t---- data\n\t\t|\n\t\t{}".format(
                self.example_workspace.title, self.example_workspace.pack_mcmeta,
                ', \n\t\t'.join(map(lambda x: f'---- {x.name}', self.example_workspace))
        ))

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
        self.example_workspace.append(mcwpy_datapack.Workspace(name='remove'))
        self.assertEqual(len(self.example_workspace), 3)

        # Remove last item.
        self.assertEqual(self.example_workspace.pop().name, 'remove')


if __name__ == '__main__':
    unittest.main()
