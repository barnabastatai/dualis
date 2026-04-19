class Adapter:

    def __init__(self, adapter_name):
        self.properties = {
            "adapter_name": adapter_name,
            "description": "",
            "physical_address": "",
            "dhcp_enabled": "",
            "ipv4_address": "",
            "subnet_mask": "",
            "default_gateway": "",
            "dns_servers": []
        }

    def to_dict(self):
        return self.properties

    def clean_value(self, value):
        value = value.strip()
        if "(" in value:
            value = value.split("(")[0].strip()
        return value