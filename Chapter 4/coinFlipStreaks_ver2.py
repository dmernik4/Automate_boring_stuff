import random


def has_six_consecutive(sequence, char="T"):
    return char * 6 in "".join(sequence)


total_sets = 10000
failures = 0

for _ in range(total_sets):
    tries = [random.choice(["T", "H"]) for _ in range(100)]
    if not (has_six_consecutive(tries, "T") or has_six_consecutive(tries, "H")):
        failures += 1

failure_percentage = (failures / total_sets) * 100
print(f"Failure percentage: {failure_percentage:.2f}%")
