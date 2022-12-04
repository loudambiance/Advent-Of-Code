def main(lines: str):
    runningsum = 0
    for line in lines:
        sac = [*line]
        sacpocket1 = sac[:len(sac)//2]
        sacpocket2 = sac[len(sac)//2:]
        for duplicate in set(sacpocket1).intersection(sacpocket2):
            value = ord(duplicate)
            if value in range(65,91):
                value -= 38
            elif value in range(97,123):
                value -= 96 
            runningsum += value
    return(runningsum)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:

        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
