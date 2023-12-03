mastercubebag = [12,13,14] # Red, Green, Blue

with open("day2.txt") as f:
    content = f.readlines()

totalsumgames = 0 
gameindex = 0

# strip "game x:" from each line
gamelist = []
for game in content:
    colonindex = game.find(":")
    gamelist.append(game[colonindex+2:])

def check_if_draw_possible(gameresults, mastercubebag):
    if gameresults[0] > mastercubebag[0] or gameresults[1] > mastercubebag[1] or gameresults[2] > mastercubebag[2]:
        return False
    else:
        return True
    
def check_if_game_possible(game, mastercubebag):
    game_plays = game.split(";")
    rednumber, greennumber, bluenumber = 0, 0, 0
    print('game_plays: ', game_plays)
    for play in game_plays:
        if 'red' in play:
            rednumber = find_number_of_color(" red", play)
        if 'green' in play:
            greennumber = find_number_of_color(" green", play)
        if 'blue' in play:
            bluenumber = find_number_of_color(" blue", play)
        j = [rednumber, greennumber, bluenumber]
        print('processed play: ', j)
        print(play)
        if check_if_draw_possible(j, mastercubebag) == False:
            return False
    return True
        
def find_number_of_color(color, play):
    # print(play)
    colorindex = play.find(color)
    commaindex = -1
    for i in range(colorindex):
        # print('scanning: ', play[colorindex-i])
        if play[colorindex-i] == ',':
            commaindex = colorindex-i
            break
    # print('colorindex: ', colorindex)
    # print('commaindex: ', commaindex)
    numberofcolor = play[commaindex+1:colorindex]
    # print('numberofcolor: ', numberofcolor)
    return int(numberofcolor)
        
# for game in gamelist:
#     gameindex += 1
#     print('game: ' , game)
#     if check_if_game_possible(game, mastercubebag):
#         totalsumgames += gameindex

print(totalsumgames)

# part 2

def determine_fewest_possible_cubes(game):
    game_plays = game.split(";")
    maxred, maxgreen, maxblue = 0, 0, 0
    for play in game_plays:
        cur_red, cur_green, cur_blue = 0, 0, 0
        if 'red' in play:
            cur_red = find_number_of_color(" red", play)
        if 'green' in play:
            cur_green = find_number_of_color(" green", play)
        if 'blue' in play:
            cur_blue = find_number_of_color(" blue", play)
        if cur_red > maxred:
            maxred = cur_red
        if cur_green > maxgreen :
            maxgreen  = cur_green
        if cur_blue > maxblue:
            maxblue = cur_blue
    return maxred, maxgreen , maxblue

totalpower = 0
for game in gamelist:
    gameindex += 1
    print('game: ' , game)
    minred, mingreen, minblue = determine_fewest_possible_cubes(game)
    totalpower += minred*mingreen*minblue
print(totalpower)
    