# -*- coding: ascii -*-
import minecraft_with_python.mcwpy.pack_meta as mcwpy_pack_meta
import minecraft_with_python.mcwpy.utility as mcwpy_utility
import unittest


class TestDatapack(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.example_pack_meta = mcwpy_pack_meta.Pack_Meta(author='MCWPy', description='An amazing Minecraft datapack!', minecraft_version=7)

    def test_datapack_default_values(self):
        self.assertEqual(mcwpy_pack_meta.Pack_Meta().meta['description'], 'A Minecraft datapack.')
        self.assertEqual(mcwpy_pack_meta.Pack_Meta().meta['pack_format'], mcwpy_utility.Minecraft_Pack_Version.LATEST)

    def test_datapack_default_instances(self):
        self.assertIsInstance(mcwpy_pack_meta.Pack_Meta(), mcwpy_pack_meta.Pack_Meta)
        self.assertIsInstance(mcwpy_pack_meta.Pack_Meta()(), str)
        self.assertIsInstance(mcwpy_pack_meta.Pack_Meta().__call__(), str)
        self.assertIsInstance(mcwpy_pack_meta.Pack_Meta().__repr__(), str)

    def test_datapack_equal_values(self):
        self.assertEqual(mcwpy_pack_meta.Pack_Meta()(), mcwpy_pack_meta.Pack_Meta().__call__())
        self.assertEqual(mcwpy_pack_meta.Pack_Meta().__call__(), mcwpy_pack_meta.Pack_Meta().__repr__())
        self.assertEqual(self.example_pack_meta(), self.example_pack_meta.__call__())
        self.assertEqual(self.example_pack_meta.__call__(), self.example_pack_meta.__repr__())


if __name__ == '__main__':
    unittest.main()
