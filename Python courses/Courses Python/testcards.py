player1=Player()
player2=Player()
while len(game.cards)!=0:
				player1.doStep()
				player2.doStep()
				game.solve()
				player1.takeCard()
				player2.takeCard()
