import bisect


class ConsistentHashMap:
    def __init__(self, num_servers, num_slots, num_virtual_servers):
        self.hash_map = {}
        self.sorted_keys = []
        self.num_slots = num_slots

        for i in range(num_servers):
            for j in range(num_virtual_servers):
                hash_value = self.virtual_server_hash(i, j)
                self.hash_map[hash_value] = i
                self.sorted_keys.append(hash_value)

        self.sorted_keys.sort()

    def request_hash(self, i):
        return (i + 2 * i + 17) % self.num_slots

    def virtual_server_hash(self, i, j):
        return (i + j + 2 * j + 25) % self.num_slots

    def get_server(self, request):
        request_hash = self.request_hash(request)
        index = bisect.bisect(self.sorted_keys, request_hash)
        if index == len(self.sorted_keys):
            index = 0
        return self.hash_map[self.sorted_keys[index]]


# Initialize the consistent hash map with 3 servers, 512 slots, and 9 virtual servers per server
chm = ConsistentHashMap(3, 512, 9)

# Get the server for a request
server = chm.get_server(123)
print(f"Request 123 is handled by server {server}")
