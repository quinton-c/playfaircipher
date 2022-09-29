

class Data:   #holds and generates data
    
    def __init__(self, plain, key):
        self.RAWplain = plain
        self.RAWkey = key
        self.plain = self.string_cleaner(self.RAWplain)
        self.key = self.string_cleaner(self.RAWkey)
        self.dipoles = self.grouper(self.plain)


    def string_cleaner(self, string): #removes unacceptable characters and makes all letters lowercase
        accepted_chars = list('abcdefghijklmnopqrstuvwxyz0123456789')
        lst = list(string.lower())
        for ltr in lst:
            if ltr not in accepted_chars:
                lst.remove(ltr)
        string = ''.join(lst)
        return string

    def grouper(self, string): #split string into dipoles -- takes in a string and returns a list of sublists with letters grouped in twos; also changes 2nd letter if letters are the same

        split = list(string)
        output = []

        if len(split) % 2 != 0:
            split.append('x')

        for i in range(0,len(split)-1,2):
            dipole = []
            dipole.append(split[i])
            dipole.append(split[i+1])
            output.append(dipole)

        for dip in output:
            if dip[0] == dip[1]:
                if dip[1] == 'x':
                    dip[1] = 'b'
                else:
                    dip[1] = 'x'
            
        return output

    def get_coords(self, grid): #takes in a grid object and returns coordinates of dipoles
        grd = grid
        dips = self.dipoles
        coords = [['',''] for i in range(len(dips))]
        for i in range(len(dips)):
            coords[i][0] = grd.coord(dips[i][0])
            coords[i][1] = grd.coord(dips[i][1])
        return coords    



class Grid: #builds grid and provides grid services

    def __init__(self, key):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        self.chars = self.unduplicator(self.string_cleaner(key) + self.alphabet)

    def unduplicator(self, txt): #unduplicates letters for the grid text
        lst = list(txt)
        for i in reversed(range(len(lst))):
            if lst[i] in lst[0:i-1] and i != 0:
                del lst[i]
        return ''.join(lst)

    def string_cleaner(self, string): #removes unacceptable characters and makes all letters lowercase
        accepted_chars = list('abcdefghijklmnopqrstuvwxyz0123456789')
        lst = list(string.lower())
        for ltr in lst:
            if ltr not in accepted_chars:
                lst.remove(ltr)
        string = ''.join(lst)
        return string

    def coord(self, ltr): #returns a coordinate object containing the letter and x and y coordinates
        ltr = ltr.lower()
        spot = self.chars.index(ltr)
        x = spot % 6
        y = spot // 6
        return {'Letter': ltr, 'X': x, 'Y': y}


    def get_letter(self, x, y): #returns a letter for a given x,y coordinate value
        return self.chars[(y*6)+x]
        
    
    def shift_right(self, coord): #actions to implement rules -- takes in a coordinate object and shifts it up, down, left, or right; all rules wrap on lines appropriately
        newx = (coord['X'] + 1) % 6
        y = coord['Y']
        newcoord = self.coord(self.get_letter(newx, y))
        return newcoord
    
    def shift_left(self, coord):
        newx = (coord['X'] - 1) % 6
        y = coord['Y']
        newcoord = self.coord(self.get_letter(newx, y))
        return newcoord

    def shift_up(self, coord):
        newy = coord['Y'] - 1
        x = coord['X']
        newcoord = self.coord(self.get_letter(x, newy))
        return newcoord

    def shift_down(self, coord):
        newy = (coord['Y'] + 1) % 6
        x = coord['X']
        newcoord = self.coord(self.get_letter(x, newy))
        return newcoord

    def swapx(self, coord1, coord2): #takes in two coordinate objects and returns a list of two new coordinate objects with X values swapped (updates letters accordingly too)
        coord1 = coord1
        coord2 = coord2
        aux = coord1['X']
        coord1['X'] = coord2['X']
        coord2['X'] = aux
        coord1['Letter'] = self.get_letter(coord1['X'], coord1['Y'])
        coord2['Letter'] = self.get_letter(coord2['X'], coord2['Y'])
        return [coord1, coord2]

    '''
    takes in a list of two coordinate objects (if len(list) > 2, code ignores all objects past index 1)
    and applies the appropriate playfair rules and returns a list of two new coordinate objects with rules applied
    '''
    def apply_rules(self, coords, direction): 
        if direction not in ['encode', 'decode']:
            return [{'Letter': i} for i in list('ERROR: direction argument must be "encode" or "decode". Please try again.')]
        new_coords = []
        for coord in coords:
            if coord[0]['X'] == coord[1]['X']:
                if direction == 'encode':
                    new0 = self.shift_up(coord[0])
                    new1 = self.shift_up(coord[1])
                    new_coords.append(new0)
                    new_coords.append(new1)
                
                elif direction == 'decode':
                    new0 = self.shift_down(coord[0])
                    new1 = self.shift_down(coord[1])
                    new_coords.append(new0)
                    new_coords.append(new1)
                else:
                    print('SERIOUS ISSUE')
            
            elif coord[0]['Y'] == coord[1]['Y']:
                if direction == 'encode':
                    new0 = self.shift_right(coord[0])
                    new1 = self.shift_right(coord[1])
                    new_coords.append(new0)
                    new_coords.append(new1)
                
                elif direction == 'decode':
                    new0 = self.shift_left(coord[0])
                    new1 = self.shift_left(coord[1])
                    new_coords.append(new0)
                    new_coords.append(new1)
                else:
                    print('SERIOUS ISSUE')
            else:
                shifted = self.swapx(coord[0], coord[1])
                new_coords.append(shifted[0])
                new_coords.append(shifted[1])
        return new_coords

    def __repr__(self):
        return "|" + "|".join(list(self.chars[0:5])) + '|\n|' + "|".join(list(self.chars[6:11])) + '|\n|' + "|".join(list(self.chars[12:17])) + '|\n|' + "|".join(list(self.chars[18:23])) + '|\n|' + "|".join(list(self.chars[24:29])) + '|\n|' + "|".join(list(self.chars[30:35])) + "|"



if __name__ == '__main__': #main program
    print(
        '''
*************************************************************************
        
PPPPPPP  L            A      Y       Y  FFFFFF      A       I   RRRRRR
P     P  L           A A      Y     Y   F          A A      I   R    R
P     P  L          A   A      Y   Y    F         A   A     I   R    R
PPPPPPP  L         A     A      Y Y     FFFF     A     A    I   RRRRRR
P        L        AAAAAAAAA      Y      F       AAAAAAAAA   I   R R    
P        L        A       A      Y      F       A       A   I   R  R
P        L        A       A      Y      F       A       A   I   R   R
P        LLLLLLL  A       A      Y      F       A       A   I   R    R

*************************************************************************        

What text would you like to encode or decode?

    ''')

    plaintxt = input()

    print('\nWhat is the key phrase? \n')
    
    key_phrase = input()

    data = Data(plaintxt, key_phrase)

    grd = Grid(data.key)

    coords = data.get_coords(grd)
   
    #print(grd) <-- can print the grid for debuggin purposes (not printed by default)

    print('\nWould you like to encode or decode? (Please enter encode or decode exactly)\n')

    direction = input()
    
    valid = False

    while not valid:
        if direction == 'encode' or direction == 'decode':
            valid = True
        else:
            print('\nERROR Please enter either \'encode\' or \'decode\'\n')
            direction = input()
    

    new_coords = grd.apply_rules(coords,direction)
        
    new_letters = [coord['Letter'] for coord in new_coords]
    
    output = ''.join(new_letters)
    print('\n' * 2  + output + '\n')
