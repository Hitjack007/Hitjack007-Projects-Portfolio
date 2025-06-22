import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            # Remove and return all balls if draw count exceeds contents
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        # Randomly remove num_balls from contents
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Deep copy to preserve original hat
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count balls drawn
        drawn_counts = {}
        for color in drawn_balls:
            drawn_counts[color] = drawn_counts.get(color, 0) + 1

        # Check if expected_balls are all satisfied
        success = True
        for color, min_count in expected_balls.items():
            if drawn_counts.get(color, 0) < min_count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments
