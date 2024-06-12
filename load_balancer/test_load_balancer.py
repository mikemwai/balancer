import unittest
from load_balancer import add_server, remove_server, handle_request

class TestLoadBalancer(unittest.TestCase):

    def setUp(self):
        self.servers = []
        add_server(self.servers, "Server1")
        add_server(self.servers, "Server2")

    def test_initial_state(self):
        self.assertEqual(len(self.servers), 2, "Initial server list should have two servers")

    def test_add_server(self):
        add_server(self.servers, "Server3")
        self.assertIn("Server3", self.servers, "Server3 should be added to servers")

    def test_remove_server(self):
        remove_server(self.servers, "Server1")
        self.assertNotIn("Server1", self.servers, "Server1 should be removed from servers")

    def test_handle_request(self):
        response, status = handle_request(self.servers, "/home")
        self.assertTrue("Hello from" in response, "Request should be handled by one of the servers")
        self.assertEqual(status, 200, "Status code should be 200")

if __name__ == '__main__':
    unittest.main()
