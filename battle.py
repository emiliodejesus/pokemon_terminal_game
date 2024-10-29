import player
import trainer
import pokémon

class Battle:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        self.party = []
        self.foes = []
        for pokémon in player.pokémon:
            self.party.append(pokémon)
        for pokémon in opponent.pokémon:
            self.foes.append(pokémon)


    def battle(self):
        #Pokémons to battle
        players_poké = choose_mon()
        opponents_poké = choose_next_foe()

        if players_poké is None:
            print('Your pokémon are unable to battle!\nGo to pokémon center immediately')
            return 'battle lost'
        if opponents_poké is None:
            print(f"{player.name} has won the battle!\n")

        if self.opponent is 'encounter':
            print(f'A wild {self.opponent} has appeared!')
            print(f'{player.name} threw in {players_poké.name}!')
            option = input(f"Choose by typing:\nAttack\nRun\n")
            while (option.title() != ('Attack' or 'Run' or 'A' or 'R')):
                print('Please type again.')
                option = input(f"Choose by typing:\nAttack\nRun\n")
            if option.title() == ("Attack" or "a"):
                pass
        else:
            print(f"Challenger {self.opponent} wants to battle!")

    def choose_mon(self):
        for poké in self.party:
            if poké is pokémon:
                if not poké.is_knocked_out:
                    return poké
        return None
    def choose_next_foe(self):
        for poké in self.foes:
            if poké is pokémon:
                if not poké.is_knocked_out:
                    return poké
        return None