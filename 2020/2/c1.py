files = ("input_ex.txt", "input.txt")

for file in files:
    print(file)
    data = []
    with open(file) as f:
        for line in f.read().splitlines():
            linedat = line.split(" ")
            tempdict = {}
            tempdict["min"] = int(linedat[0].split("-")[0])
            tempdict["max"] = int(linedat[0].split("-")[1])
            tempdict["letter"] = linedat[1].split(":")[0]
            tempdict["password"] = linedat[2]
            data.append(tempdict)
    valid = 0
    for datum in data:
        count = datum["password"].count(datum["letter"])
        if datum["min"] <= count and count <= datum["max"]:
            valid += 1
 
    print("Valid: " + str(valid))
    print("")
