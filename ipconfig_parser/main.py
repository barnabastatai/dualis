import json
from pathlib import Path
from parser import Parser

adapters = []

def main():
    results = []
    for path in sorted(Path(".").glob("*.txt")):
        parser = Parser(path)
        data = parser.parse()
        if data:
            results.append(data)

    json_string = json.dumps(results, ensure_ascii=False, indent=4)
    print(json_string)

    with open("network_config.json", "w", encoding="utf-8") as f:
        f.write(json_string)


if __name__ == "__main__":
    main()
