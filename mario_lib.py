import csv

def read_and_combine(bodies_file, char_file):

    """
    read from the bodies file and the char file
    (CSV) and then iterate thru both of them (nested)
    and to print out all the combinations
    """

    my_dict_body=dict()
    my_dict_char=dict()
    with open(bodies_file, 'r') as b, open(char_file, 'r') as c:
        csv_body = csv.reader(b)
        csv_char = csv.reader(c)
        next(csv_body)
        next(csv_char)

        for row_body in csv_body:
            key_body_body = row_body[0]
            key_body_type = row_body[1]
            key_body_speed = row_body[2]
            key_body_acceleration = row_body[3]
            key_body_weight = row_body[4]
            key_body_handeling = row_body[5]
            key_body_traction = row_body[6]
            key_body_mini_turbo = row_body[7]

            body_value = (key_body_body, key_body_type, key_body_speed, key_body_acceleration, key_body_weight,
            key_body_handeling, key_body_traction, key_body_mini_turbo)
            my_dict_body[key_body_body] = body_value

        for row_char in csv_char:
            key_char_character = row_char[0]
            key_char_speed = row_char[1]
            key_char_acceleration = row_char[2]
            key_char_weight = row_char[3]
            key_char_handeling = row_char[4]
            key_char_traction = row_char[5]
            key_char_mini_turbo = row_char[6]

            char_value = (key_char_character, key_char_speed, key_char_acceleration, key_char_weight,
            key_char_handeling, key_char_traction, key_char_mini_turbo)
            my_dict_char[key_char_character] = char_value


        return my_dict_body, my_dict_char





def best_speed(bodies_dict, char_dict):
    """
    read from bodies and char files
    iterate thru them all and get the speed
    sum the speed for the character and the body
    print out the character/body combo that has the highest
    speed.  And print out the highest (total) speed.
    """
    speed_n = 0
    for speed_char in char_dict:
        for speed_body in bodies_dict:
            #row = char_dict[x]
            #speed = row[1]
            #print(char_dict[speed_char][1],'-----', bodies_dict[speed_body][2])
            speed_current_char = float(char_dict[speed_char][1])
            speed_current_body = float(bodies_dict[speed_body][2])


            #speed_add = char_dict[speed_char][1] + bodies_dict[speed_body][2]
            #'character is,', char_dict[speed_char][0], ', and body is,', bodies_dict[speed_body][0], ', their total speed is,', speed_addition
            speed_add = speed_current_body + speed_current_char
            #print(speed_add)
            if speed_add > speed_n:
                speed_n = speed_add
            else:
                pass




    return speed_n
















def best_acceleration(bodies_dict, char_dict):
    """
    """
    acc_n = 0
    for acc_char in char_dict:
        for acc_body in bodies_dict:
            #row = char_dict[x]
            #speed = row[1]
            #print(char_dict[speed_char][1],'-----', bodies_dict[speed_body][2])
            acc_current_char = float(char_dict[acc_char][2])
            acc_current_body = float(bodies_dict[acc_body][3])


            #speed_add = char_dict[speed_char][1] + bodies_dict[speed_body][2]
            #'character is,', char_dict[speed_char][0], ', and body is,', bodies_dict[speed_body][0], ', their total speed is,', speed_addition
            acc_add = acc_current_body + acc_current_char
            #print(speed_add)
            if acc_add > acc_n:
                acc_n = acc_add
            else:
                pass
    return acc_n


# TODO refactor and consider if there's a better way than passing in the
# filename each time
