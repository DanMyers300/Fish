import os
import time
import random

class Fish:
    def __init__(self, name, species, health, age, hunger, happiness):
        self.name = name
        self.species = species
        self.health = health
        self.age = age
        self.hunger = hunger
        self.happiness = happiness

    def feed(self):
        self.hunger = 0
        self.happiness += 1

    def play(self):
        self.happiness += 1
        self.hunger += 1

    def check_health(self):
        if self.hunger > 5:
            self.health -= 1
        if self.happiness < 5:
            self.health -= 1

    def max_happiness(self):
        if self.happiness > 5:
            self.happiness = 5
        if self.happiness < 0:
            self.happiness = 0

    def max_hunger(self):
        if self.hunger > 5:
            self.hunger = 5
        if self.hunger < 0:
            self.hunger = 0

    def max_age(self):
        if self.age > 10:
            self.health -= 0

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
