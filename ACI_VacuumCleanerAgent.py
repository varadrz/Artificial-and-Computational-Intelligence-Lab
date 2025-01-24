import random

def vacuum_cleaner_agent():
    # Environment setup
    rooms = {
        "A": random.choice(["clean", "dirty"]),
        "B": random.choice(["clean", "dirty"])
    }
    
    # Initial position of the vacuum
    vacuum_position = random.choice(["A", "B"])
    
    print(f"Initial room states: {rooms}")
    print(f"Vacuum starts in room: {vacuum_position}\n")

    # Agent logic
    steps = 0
    while "dirty" in rooms.values():  # Continue until all rooms are clean
        steps += 1
        print(f"Step {steps}: Vacuum in room {vacuum_position}, Room state: {rooms[vacuum_position]}")

        if rooms[vacuum_position] == "dirty":
            print(f"Room {vacuum_position} is dirty. Cleaning...")
            rooms[vacuum_position] = "clean"
        else:
            print(f"Room {vacuum_position} is clean.")

        # Move to the next room
        vacuum_position = "B" if vacuum_position == "A" else "A"

    print(f"\nAll rooms are clean: {rooms}")
    print(f"Total steps taken: {steps}")

if __name__ == "__main__":
    vacuum_cleaner_agent()
