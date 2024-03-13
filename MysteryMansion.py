import random
# player location
player_room = ''
def Player_location():
    global player_room
    # tell player what room they are in
    room_list = ['attic','celler','dinning room', 'living room', 'thither room', 'bed room', 'mud room', 'storage room', 'map room','hallway','kitchen', 'office', 'closet', 'library','laboratory']
    player_room = random.choice(room_list)
    print('you are in the',player_room)

# room ----------------------------------------------------------
# room furniture
room_furniture = []
def Furniture():
    # creating furniture in the room
    if player_room == 'laboratory':
        furniture_list = ['book','map','table', 'candle', 'chair','shelf', 'cabinet', 'lamp','bookshelf','chest','box','painting','bed','rack']
    elif player_room == 'celler':
        furniture_list = ['Barrel','wine bottle','table', 'candle', 'chair', 'radio','shelf', 'cabinet', 'lamp','bookshelf','chest','box','painting','rack']
    elif player_room == 'dinning room':
        furniture_list = ['wine bottle','table','plate','candle','cup','chair','radio','plaint','shelf','cabinet','lamp','bookshelf','painting']
    elif player_room == 'living room':
        furniture_list = ['wine bottle','table','candle', 'chair', 'radio', 'plaint', 'shelf', 'cabinet','couch','lamp','bookshelf','painting']
    elif player_room == 'thither room':
        furniture_list = ['candle', 'chair', 'plaint','couch','lamp','stage','painting','wine bottle']
    elif player_room == 'bed room':
        furniture_list = ['wine bottle','candle', 'chair', 'plaint','bed','lamp','radio','desk','chest','dresser','rack','bookshelf','painting','box']
    elif player_room == 'mud room':
        furniture_list = ['candle', 'plaint','lamp','radio','sink','dryer','washer','rack','chest']
    elif player_room == 'map room':
        furniture_list = ['candle', 'plaint','lamp','radio','map','chest','cabinet','bookshelf','book']
    elif player_room == 'kitchen':
        furniture_list = ['wine bottle','sink','candle', 'plaint','lamp','radio','cabinet','refrigerator','dishwasher','rack','plate','cup','oven']
    elif player_room == 'office':
        furniture_list = ['candle', 'plaint','lamp','radio','cabinet','paper','bookshelf','chair','desk','painting','box','map']
    elif player_room == 'library':
        furniture_list = ['wine bottle','candle', 'plaint','lamp','radio','cabinet','paper','bookshelf','chair','book','news paper','desk','painting','box']
    elif player_room == 'hallway':
        furniture_list = ['candle', 'plaint','lamp','cabinet','bookshelf','chair','book','news paper','table','painting','chest','box','wine bottle','rack','radio']
    else:
        furniture_list = ['table', 'plate', 'candle', 'chair', 'radio', 'plaint', 'shelf', 'cabinet', 'lamp','bookshelf','chest','box','painting','news paper','book','rack']
    # telling the use what's in the room
    print('in the room you the found: ')
    while len(room_furniture) < random.randint(1,5):
        furniture = random.choice(furniture_list)
        if furniture not in room_furniture:
            room_furniture.append(furniture)

# Furniture Amount
furniture_amount = []
def Furniture_Amount():
    # how many of that type of furniture is in the room?
    for x in range(len(room_furniture)):
        amount = random.randint(2,5)
        furniture_amount.append(amount)
        print(amount,room_furniture[x] + '(s)')

# code ------------------------------------------------
code_location_list = []
code_amount = 0
def Code_Location():
    global code_amount
    # adding the codes
    if len(furniture_amount) > 7:
        code_amount = random.randint(1, 7)
    else:
        code_amount = random.randint(1,len(room_furniture))
    while len(code_location_list) != code_amount:
        furniture_type = random.choice(room_furniture)
        top = room_furniture.index(furniture_type)
        furniture_number = random.randint(1,furniture_amount[top])
        # ---------------------------------------------------------------- position of the code
        position = ['top', 'bottom', 'left', 'right', 'behind']
        pick = furniture_type
        list = ['shelf', 'cabinet', 'bookshelf', 'desk', 'chest', 'dresser', 'box', 'book', 'news paper',
                'oven', 'dishwasher', 'refrigerator', 'dryer', 'washer','Barrel','wine bottle']
        if pick in list:
            position.append('inside')
        else:
            if 'inside' in position:
                position.remove('inside')
        code_position = random.choice(position)
        location = [furniture_type,furniture_number,code_position]
        # ---------------------------------------------------------------- if the code already added in a location
        # check
        res1 = any(furniture_type in sub for sub in code_location_list)
        result1 = str(res1)
        res2 = any(furniture_number in sub for sub in code_location_list)
        result2 = str(res2)
        if result1 == 'False' and result2 == 'False':
            code_location_list.append(location)
        if len(code_location_list) > code_amount:
            break
    # ----------------------- tell the user how many code are in the room
    print('in the room there are {} code(s)'.format(code_amount))
    # this prints out the location of the codes
    #print(code_location_list)

#  number input
def Number():
    global number, found
    # asking the player what furniture they want to look at
    try:
        while True:
            user_number = int(input('what {} would you like to look at? (must be a number) > '.format(user)))
            find = room_furniture.index(user)
            if user_number > 0 and user_number < furniture_amount[find] + 1:
                number = user_number
                found = True
                break
            else:
                print('sorry, but "{}" is not an option'.format(user_number))
    except ValueError:
        print('it must be a number. think of it as "i am going to look for my other book"')
        while True:
            # if they want to exit
            question = input('would you like to quit? (yes | no) ')
            question = question.lower().strip()
            if question == 'yes':
                print('thanks for playing')
                quit(0)
            elif question == 'no':
                break
            else:
                print('sorry, but "{}" is not an option'.format(question))


# found codes list
found_list = []
found_amount = 0

# user Position
def Position():
    global found_list,number,found_amount
    while True:
        user_position = input('what position would you like to look for the code? (top | bottom | left | right | behind | inside) > ')
        user_position = user_position.lower().strip()
        list = ['top', 'bottom', 'left', 'right', 'behind','inside']
        # ---------------- if you can look inside
        inside = ['shelf', 'cabinet', 'bookshelf', 'desk', 'chest', 'dresser', 'box', 'book', 'news paper','oven', 'dishwasher', 'refrigerator', 'dryer', 'washer']
        find = room_furniture.index(user)
        if user_position == 'inside' and room_furniture[find] in user and str(inside) not in user:
            print("sorry, but you can't look inside of the {}".format(user))
        else:
            # ---------------- check position input
            if user_position not in str(list):
                if 'quit' in user_position:
                    print('thanks for playing')
                    quit(0)
                else:
                    print('sorry, but "{}" is not an option'.format(user_position))
            else:
                # check if the position is there
                check = 0
                for value in code_location_list:
                    if value[0] == user and value[1] == number and value[2] == user_position:
                        check = 1
                        for p in found_list:
                            if p[0] == user and p[1] == number and p[2] == user_position:
                                # if you have already found at the location
                                print('you already found a code here')
                                check = 2
                            else:
                                pass
                    else:
                        pass
                # if not
                if check == 0:
                    print('sorry, you could not find any codes here')
                    break
                # if yes
                else:
                    if check == 1:
                        print('you have found a code')
                        add = [user,number,user_position]
                        found_list.append(add)
                        found_amount += 1
                    break

# if you win
def win():
    global code_amount,player_room,room_furniture,furniture_amount,code_location_list,found_list,found_amount
    if found_amount == code_amount:
        print('you have found all of the codes')
        question = input('would you like to play again? > ')
        # if the player wants to play again
        if question == 'yes':
            for x in range(200):
                print('')
            # restart
            # player
            player_room = ''
            Player_location()
            # room
            room_furniture = []
            furniture_amount = []
            Furniture()
            Furniture_Amount()
            # code
            code_location_list = []
            code_amount = 0
            Code_Location()
            # found
            found_list = []
            found_amount = 0
        else:
            # else
            print('thanks for playing')
            quit(0)


# game backbone
Player_location()
Furniture()
Furniture_Amount()
Code_Location()

# ------------------------------------------------------------------ game ------------------------------------------------------------------
Game = True
number = 0
found = False

print('')
while Game:
    # check if the player has won
    win()
    user = input('(you have found {} codes) what furniture would you like to look at? > '.format(found_amount))
    user = user.lower().strip()
    # check user input
    if user in str(room_furniture):
        print('')
        Number()
        if found == True:
            print('')
            Position()
            print('')
    elif 'quit' in user:
        # quit
        print('thanks for playing')
        quit(0)
    else:
        print('sorry, but {} is not in the room'.format(user.strip('[]')))
        print('try {}'.format(random.choice(room_furniture)))
