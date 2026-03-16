def main():
 
    guests = ["Mario", "Luigi", "Daisy", "Yoshi"]
    
    for guest in guests:
        print(write_letter(guest, "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    +-----------------------------------------+
        Dear {receiver}, 
    you are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.
            Yours truly, {sender}.
    +-----------------------------------------+
    """

if __name__ == "__main__":
    main()