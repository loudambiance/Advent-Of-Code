fail = False
for num in range(2520, 999999999999, 10):
    # print("Attempt: {}".format(num))
    for div in range(1, 21):
        # print("div: {} - {}".format(div, num % div))
        if num % div == 0:
            continue
        else:
            fail = True
            break
    if fail:
        continue
    else:
        print("Success: {}".format(num))
        break
