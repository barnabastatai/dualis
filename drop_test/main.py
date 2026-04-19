from pathlib import Path

def min_num_of_drops(n, h):
    if h <= 1:
        return h

    if n == 1:
        return h

    matrix = [[0] * (h + 1) for _ in range(n + 1)]

    for i in range(1, h + 1):
        for j in range(1, n + 1):
            matrix[j][i] = matrix[j - 1][i - 1] + matrix[j][i - 1] + 1

        if matrix[n][i] >= h:
            return i

    return h


def main():
    data = Path("input.txt").read_text(encoding="utf-8").splitlines()

    for line in data:
        sp = line.replace(" ", "").split(",")
        print(min_num_of_drops(int(sp[0]), int(sp[1])))


if __name__ == "__main__":
    main()
