def read_non_empty_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                yield line.strip()

filename = "sample.txt"

res = read_non_empty_lines(filename)

for line in res:
    print(line)

