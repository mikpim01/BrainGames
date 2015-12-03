import pyglet
from utils import draw


class GameArea():
	'''
	GameArea class.. create a new game
	'''

	def __init__(self, title, width, height, description=''):
		'''
		Init Game Area class
		'''

		self.score = 0
		self.positive = 10
		self.negative = -20
		self.syncKey = False
		self.gameTime = 5

		pyglet.clock.set_fps_limit(30)

		self.components = []
		self.window = pyglet.window.Window(width, height)
		self.width = width
		self.height = height
		self.heading = pyglet.text.Label(title, font_size=30, x = width // 2, y = height - 50, anchor_x = 'center')

		self.description = pyglet.text.Label(description, x = 30, y = height - 90)
		self.descriptiontext = description

		self.lblScore = pyglet.text.Label(str(self.score), font_size=20, font_name='Lucida Console', x = width - 80, y = self.heading.y)
		self.scorebox = draw.rectangle(width - 90, self.lblScore.y + 40, 60, 50, filled=False)

		self.components = [self.heading, self.description, self.lblScore, self.scorebox]


		@self.window.event
		def on_draw():
			self.window.clear()
			for obj in self.components:
				obj.draw()


	def show(self):
		'''
		Make the game window visible
		'''
		pyglet.app.run()


	def descStatus(self, show=True):
		'''
		Shows or hides the description
		'''
		if show:
			self.description.text = self.descriptiontext
		else:
			self.description.text = ''
		self.description.draw()


	def updateScore(self, by):
		'''
		Updates the score
		'''
		self.score += by
		self.lblScore.text = str(self.score)
		self.lblScore.draw()


	def endGame(self, dt):
		print('Game over')
		while self.syncKey:
			pass
		self.syncKey = True


if __name__ == '__main__':
	newgame = GameArea('My Game', 500, 500)
	newgame.show()