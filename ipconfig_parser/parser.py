from adapter import Adapter


class Parser:
    def __init__(self, path):
        self.path = path
        self.adapters = []

    def parse(self):
        with open(self.path, "r", encoding="utf-16") as f:
            lines = f.readlines()

            current_adapter = None
            last_key = None

            for line in lines:
                raw_line = line.strip()

                if not raw_line:
                    continue

                if raw_line.endswith(':'):
                    if " . " not in raw_line:
                        name = raw_line[:-1].strip()
                        current_adapter = Adapter(name)
                        self.adapters.append(current_adapter)
                        last_key = None
                        continue

                if current_adapter:
                    if ':' in raw_line and " . " in raw_line:
                        parts = raw_line.split(":", 1)
                        key = parts[0].replace('.', "").strip().lower().replace(' ', '_')
                        value = current_adapter.clean_value(parts[1])

                        if "dns_servers" in key:
                            if value:
                                current_adapter.properties["dns_servers"] = [value]
                            else:
                                current_adapter.properties["dns_servers"] = []
                            last_key = "dns"
                        else:
                            current_adapter.properties[key] = value
                            last_key = key

                    elif raw_line.startswith(" " * 4) and last_key:
                        value = current_adapter.clean_value(raw_line)
                        if value:
                            if last_key == "dns":
                                current_adapter.properties["dns_servers"].append(value)
                            elif not current_adapter.properties.get(last_key):
                                current_adapter.properties[last_key] = value

            return {
                "file_name": self.path.name,
                "adapters": [adapter.to_dict() for adapter in self.adapters]
            }

