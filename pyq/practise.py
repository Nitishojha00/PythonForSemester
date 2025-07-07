lines = []

while True:
    line = input("Enter a line (press Enter to stop): ")
    if not line:
        break
    lines.append(line)

for line in lines:
    print(line.upper())