import random

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.agent_position = (0, 0)
        self.wumpus_position = self.generate_random_position()
        self.gold_position = self.generate_random_position()
        self.pit_positions = [self.generate_random_position() for _ in range(size // 2)]

    def generate_random_position(self):
        return (random.randint(0, self.size - 1), random.randint(0, self.size - 1))

    def print_world(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent_position:
                    print("A", end=" ")
                elif (i, j) == self.wumpus_position:
                    print("W", end=" ")
                elif (i, j) == self.gold_position:
                    print("G", end=" ")
                elif (i, j) in self.pit_positions:
                    print("P", end=" ")
                else:
                    print(".", end=" ")
            print()

    def move_agent(self, direction):
        x, y = self.agent_position
        if direction == "UP" and x > 0:
            self.agent_position = (x - 1, y)
        elif direction == "DOWN" and x < self.size - 1:
            self.agent_position = (x + 1, y)
        elif direction == "LEFT" and y > 0:
            self.agent_position = (x, y - 1)
        elif direction == "RIGHT" and y < self.size - 1:
            self.agent_position = (x, y + 1)

    def is_valid_move(self):
        x, y = self.agent_position
        if (x, y) == self.wumpus_position:
            print("Game Over! Wumpus got you!")
            return False
        elif (x, y) == self.gold_position:
            print("Congratulations! You found the gold!")
            return False
        elif (x, y) in self.pit_positions:
            print("Game Over! You fell into a pit!")
            return False
        else:
            return True

# Example usage:
size = 4
wumpus_world = WumpusWorld(size)

while True:
    wumpus_world.print_world()

    move = input("Enter your move (UP/DOWN/LEFT/RIGHT): ").upper()
    wumpus_world.move_agent(move)

    if not wumpus_world.is_valid_move():
        break