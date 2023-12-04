# get rid of card #, split into left and right lists. Run through right list and tabulate points.

with open('day4.txt') as f:
    data = f.readlines()

# strip "game x:" from each line
gamelist = []
for game in data:
    colonindex = game.find(":")
    gamelist.append(game[colonindex+2:-1])

def split_game(game):
    winningnumbers = []
    cardnumbers = []
    game_plays = game.split("|")
    winningnumbers = game_plays[0].split(" ")
    cardnumbers = game_plays[1].split(" ")
    # remove empty strings from lists
    winningnumbers = list(filter(None, winningnumbers))
    cardnumbers = list(filter(None, cardnumbers))
        
    return winningnumbers, cardnumbers

def tabulate_points(winningnumbers, cardnumbers):
    print ('winning numbers:', winningnumbers)
    print ('card numbers:', cardnumbers)

    points = 0.5
    winning_numbers = 0
    for number in cardnumbers:
        if number in winningnumbers:
            winning_numbers += 1
            points = points*2
    if points == 0.5:
        points = 0
    print('winning numbers:', winning_numbers)
    return points

def q1(game_list):
    totalpoints = 0
    for game in game_list:
        winningnumbers, cardnumbers = split_game(game)
        totalpoints += tabulate_points(winningnumbers, cardnumbers)
    return totalpoints

def tabulate_winning_numbers_q2(winningnumbers, cardnumbers):
    print ('winning numbers:', winningnumbers)
    print ('card numbers:', cardnumbers)

    winning_numbers = 0
    for number in cardnumbers:
        if number in winningnumbers:
            winning_numbers += 1
    print('winning numbers:', winning_numbers)
    return winning_numbers

def q2(game_list):
    winning_numbers_list = []
    card_count_list = []

    for game in game_list:
        winningnumbers, cardnumbers = split_game(game)
        procs_per_game = tabulate_winning_numbers_q2(winningnumbers, cardnumbers)
        winning_numbers_list.append(procs_per_game)
        card_count_list.append(1)
    for i in range(len(winning_numbers_list)):
        for j in range(winning_numbers_list[i]):
            card_count_list[i+j+1] += card_count_list[i]

    total_cards = sum(card_count_list)

    return total_cards

if __name__ == "__main__":
    results = q2(gamelist)
    print(results)