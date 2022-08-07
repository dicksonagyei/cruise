# Function to get the nearest factorial to a number including its offset(difference) - By Dickson Agyei
def nearest_factorial(num):
    steps = []
    n = 1
    fact = 1
    stop = False
    while not stop:
        old_fact = fact
        fact *= n

        if fact >= num:
            offset1 = fact - num
            offset2 = num - old_fact

            if offset1 < offset2:
                steps.append((n, -offset1))
            else:
                steps.append((n - 1, offset2))

            stop = True
        else:
            n += 1

    return steps

print(nearest_factorial(int(input("Enter Number: "))))
