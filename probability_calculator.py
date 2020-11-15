import random
import copy


class Hat:
	''' Finding the probability of drawing a specific balls'''
	def __init__(self,**kwargs):
		self.contents = []
		for k,v in kwargs.items():
			for i in range(v):
				self.contents.append(k)

	# Drawing random balls
	def draw(self, draw_num):
		draw_num = min(draw_num, len(self.contents))
		balls = []
		for draw in range(draw_num):
			random_num = random.randint(0, len(self.contents) -1)
			balls.append(self.contents.pop(random_num))
		return balls


# Experiment returning a probability.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	match = 0
	for attempt in range(num_experiments):
		example = copy.deepcopy(hat)
		drawn_balls = example.draw(num_balls_drawn)
		num_of_matches = 0
		for color in expected_balls:
			if drawn_balls.count(color) >= expected_balls[color]:
				num_of_matches += 1
		if num_of_matches == len(expected_balls):
			match += 1
	probability = float(match) / num_experiments
	return probability
