import os
from mario_lib import *

my_dir = os.path.dirname(os.path.realpath(__file__))

bodies_file = my_dir + '/' + 'bodies.csv'
char_file = my_dir + '/' + 'characters.csv'

bodies_dict, char_dict = read_and_combine(bodies_file, char_file)
#print(bodies_dict)

#for x in char_dict:
#    for x_2 in bodies_dict:
        #row = char_dict[x]
        #speed = row[1]
#        print(char_dict[x][1],'-----',bodies_dict[x_2][2])







output = best_speed(bodies_dict, char_dict)

print(output)
