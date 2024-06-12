import unittest
from consistent_hash_map import ConsistentHashMap

class TestConsistentHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map = ConsistentHashMap(3, 512, 9)

    def test_add_node(self):
        self.hash_map.add_node("Server1")
        self.assertIn("Server1", self.hash_map.nodes, "Server1 should be added to hash map nodes")

    def test_remove_node(self):
        self.hash_map.add_node("Server1")
        self.hash_map.remove_node("Server1")
        self.assertNotIn("Server1", self.hash_map.nodes, "Server1 should be removed from hash map nodes")

    def test_get_node(self):
        self.hash_map.add_node("Server1")
        node = self.hash_map.get_node("Request1")
        self.assertEqual(node, "Server1", "Request1 should be mapped to Server1")

if __name__ == '__main__':
    unittest.main()
