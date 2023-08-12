import os
import time
import random

class Fish:
    def __init__(self, name, health, age, hunger):
        self.name = name
        self.health = health
        self.age = age
        self.hunger = hunger


class RunTank:
    @staticmethod
    def get_terminal_size():
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(rows), int(columns)

    @staticmethod
    def flip_fish(fish):
        return fish[::-1]

    @classmethod
    def main(cls):
        rows, columns = cls.get_terminal_size()

        fish = ">°)))彡"
        fish_flipped = cls.flip_fish(fish)
        fish_length = len(fish)  # My fish was this long :O

        num_fish_lines = random.randint(1, rows - 1)
        fish_lines = random.sample(range(1, rows), num_fish_lines)

        fish_swimming = [0] * rows
        for line in fish_lines:
            fish_swimming[line] = 1

        fish_objects = []  # List to store fish objects

        for _ in range(rows):
            fish_name = f"Fish{_+1}"
            fish_health = random.randint(1, 5)
            fish_age = random.randint(1, 5)
            fish_hunger = random.randint(1, 5)

            new_fish = Fish(fish_name, fish_health, fish_age, fish_hunger)
            fish_objects.append(new_fish)

        fish_positions = [random.randint(0, columns - fish_length) for _ in range(rows)]
        fish_directions = [1 if random.randint(0, 1) == 0 else -1 for _ in range(rows)]

        while True:
            rows, columns = cls.get_terminal_size()

            os.system('clear' if os.name == 'posix' else 'cls')
            for line_idx, fish_present in enumerate(fish_swimming):
                if fish_present:
                    fish_x = fish_positions[line_idx]
                    direction = fish_directions[line_idx]

                    if direction == -1:
                        fish_char = fish
                    else:
                        fish_char = fish_flipped

                    if 0 <= fish_x + direction < columns - fish_length:
                        fish_positions[line_idx] += direction
                    else:
                        fish_directions[line_idx] = -direction

                    print(" " * fish_positions[line_idx] + fish_char) 

                else:
                    print()

            time.sleep(0.1)

if __name__ == "__main__":
    try:
        RunTank.main()
    except KeyboardInterrupt:
        print("\nFish tank simulation stopped.")
