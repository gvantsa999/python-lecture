distances = {
    "voyager 1": 163,
    "voyager 2": 136,
    "Pioner 10": 80,
    "New Horizonts": 58,
    "Pioneer 11": 44,
}

def convert(au):
    return au * 150_000_000

def main():
    for d in distances.values():
        print(f"{d} AU is {convert(d):,} km")

main()