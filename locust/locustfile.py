from locust import HttpUser, task
from requests_toolbelt.adapters.source import SourceAddressAdapter
import random

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        ips = [
            '192.168.5.2', '192.168.5.3', '192.168.5.4',
            '192.168.5.5','192.168.5.6', '192.168.5.7',
            '192.168.5.8', '192.168.5.9', '192.168.5.10', '192.168.5.11'
            ]
        i = random.randint(0, len(ips)-1)
        self.client.mount("http://", SourceAddressAdapter(ips[i]))
        self.client.get("/")