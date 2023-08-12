import os
import time
import random

def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

def flip_fish(fish):
    return fish[::-1]

def main():
    rows, columns = get_terminal_size()

    fish = ">°)))彡"
    fish_flipped = flip_fish(fish)
    fish_length = len(fish)
    
    num_fish_lines = random.randint(1, rows - 1)
    fish_lines = random.sample(range(1, rows), num_fish_lines)

    fish_swimming = [0] * rows
    for line in fish_lines:
        fish_swimming[line] = 1

    fish_positions = [random.randint(0, columns - fish_length) for _ in range(rows)]
    fish_directions = [1 if random.randint(0, 1) == 0 else -1 for _ in range(rows)]

    while True:
        rows, columns = get_terminal_size()

        os.system('clear')  # Clear the terminal screen
        for line_idx, fish_present in enumerate(fish_swimming):
            if fish_present:
                fish_x = fish_positions[line_idx]
                direction = fish_directions[line_idx]
                
                if direction == 1:
                    fish_char = fish_flipped
                else:
                    fish_char = fish
                
                if 0 <= fish_x + direction < columns - fish_length:
                    fish_positions[line_idx] += direction
                else:
                    fish_directions[line_idx] = -direction  # Reverse direction
                
                print(" " * fish_positions[line_idx] + fish_char)
                
            else:
                print()

        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nFish tank simulation stopped.")
