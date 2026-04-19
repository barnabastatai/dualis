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
            print(f"'{path.name}' fajl adatai feldolgozva")

    with open("network_config.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("Az adapterek kiirva a 'network_config.json' fajlba")


if __name__ == "__main__":
    main()
