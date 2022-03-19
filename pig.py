import random




def roll_die(sides=6):
    seed = 0
    """ function to simulate roll of a die"""
    return random.randint(1, sides)

class player:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def __str__(self):
        return f"{self.name} total is {self.total}"

    def play_turn(self):
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != 'h':
            die = roll_die()
            if die == 1:
                print(f"{self.name} rolled a {die}, no points added this turn")
                break
            turn_total += die
            print(
                f"{self.name} rolled a {die}"
                f"{self.name}  possible total is {turn_total}"

            )
            roll_hold = input('roll or hold?').lower()
            if roll_hold == 'h':
                self.total += turn_total
            print (f"{self.name} total: {self.total}")




class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None


    def check_winner(self):
        '''return true if there is winner'''
        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True



    def play_game(self):
        current_player = self.players[0]

        while not self.check_winner():
            current_player.play_turn()
            if current_player == self.players[0]:
                current_player = self.players[1]
            elif current_player == self.players[1]:
                current_player = self.players[0]
        print(f"The winner is {self.winner}, thanks for playing goodbye")



if __name__ == "__main__":
    p1 = player('p1')
    p2 = player('p2')
    pig_game = Game(p1, p2)
    pig_game.play_game()












