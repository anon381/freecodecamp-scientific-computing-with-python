import copy
import random

class Hat:
    def __init__(self, **balls):
        # Create a list of balls with repetitions
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If asking for more than available, return all
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn

        # Randomly choose without replacement
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        # Make a deep copy so original hat isn’t changed
        hat_copy = copy.deepcopy(hat)

        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the drawn balls
        counts = {}
        for ball in drawn_balls:
            counts[ball] = counts.get(ball, 0) + 1

        # Check if expected balls condition is satisfied
        success = True
        for color, needed in expected_balls.items():
            if counts.get(color, 0) < needed:
                success = False
                break

        if success:
            successes += 1

    return successes / num_experiments
