import bisect


class ConsistentHashMap:
    def __init__(self, num_servers, num_slots, num_virtual_servers):
        self.hash_map = {}
        self.sorted_keys = []
        self.num_slots = num_slots
        self.num_virtual_servers = num_virtual_servers  # Store num_virtual_servers as an instance variable

        for i in range(num_servers):
            for j in range(num_virtual_servers):
                hash_value = self.virtual_server_hash(i, j)
                self.hash_map[hash_value] = i
                self.sorted_keys.append(hash_value)

        self.sorted_keys.sort()

    def request_hash(self, i):
        return hash(str(i)) % self.num_slots

    def virtual_server_hash(self, i, j):
        return hash(str(i) + str(j)) % self.num_slots

    def get_server(self, request):
        request_hash = self.request_hash(request)
        index = bisect.bisect(self.sorted_keys, request_hash)
        if index == len(self.sorted_keys):
            index = 0
        server = self.hash_map[self.sorted_keys[index]]

        # Log the request and the server it's mapped to
        print(f'Request: {request}, Server: {server}')

        return server

    def set_num_servers(self, num_servers):
        self.hash_map = {}
        self.sorted_keys = []

        for i in range(num_servers):
            for j in range(self.num_virtual_servers):
                hash_value = self.virtual_server_hash(i, j)
                self.hash_map[hash_value] = i
                self.sorted_keys.append(hash_value)

        self.sorted_keys.sort()


# Initialize the consistent hash map with 3 servers, 512 slots, and 9 virtual servers per server
chm = ConsistentHashMap(3, 512, 9)

# Get the server for a request
server = chm.get_server(123)
print(f"Request 123 is handled by server {server}")
