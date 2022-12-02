def main(lines):
    return(0)


if __name__ == "__main__":
    files = ("input_ex.txt", "input.txt")
    for file in files:

        with open(file) as f:
            lines = f.read().splitlines()
        print(file + ": " + str(main(lines)))
