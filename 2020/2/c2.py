files = ("input_ex.txt", "input.txt")

for file in files:
    print(file)
    data = []
    with open(file) as f:
        for line in f.read().splitlines():
            linedat = line.split(" ")
            tempdict = {}
            tempdict["index1"] = int(linedat[0].split("-")[0])
            tempdict["index2"] = int(linedat[0].split("-")[1])
            tempdict["letter"] = linedat[1].split(":")[0]
            tempdict["password"] = linedat[2]
            data.append(tempdict)
    valid = 0
    for datum in data:
        count = datum["password"].count(datum["letter"])
        index1 = datum["password"][datum["index1"]-1]
        index2 = datum["password"][datum["index2"]-1]
        if index1 == datum["letter"] and index2 != datum["letter"]:
            valid += 1
        elif index1 != datum["letter"] and index2 == datum["letter"]:
            valid += 1
 
    print("Valid: " + str(valid))
    print("")
