def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "undo":
            if len(history) > 0:
                undone = history.pop()
                print(f"Undone: {undone}")
            else:
                print("History is empty")
        elif action == "restart":
            history.clear()
            print("History cleared")
        else:
            history.append(action)

        print(history)

# def calculate_index(lst):
#     sum = 0
#     for i in range(len(lst)):
#         sum += i
#     return round(sum / len(lst))

main()