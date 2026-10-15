# ------------------LEVEL 1-------------------------
from random import *
import string
# Write a function which generates a six digit/character random_user_id
# def random_user_id(length = 6):
#     choice = string.ascii_letters + string.digits
#     return ''.join(random.choices(choice, k= length))
# print(random_user_id())


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# def user_id_gen_by_user():
#     num_of_char = int(input('Enter the number of characters:').strip())
#     num_of_ids = int(input('Enter number of iDs to be generated:'))
#     choice = string.ascii_letters + string.digits
#     for _ in range(num_of_ids):
#         print(''.join(random.choices(choice, k= num_of_char)))
# user_id_gen_by_user()


# def user_id_gen_by_user():
#     num_of_char = int(input('Enter the number of characters: ').strip())
#     num_of_ids = int(input('Enter number of iDs to be generated: ').strip())
    
#     choice = string.ascii_letters + string.digits
#     generated_ids = []  # Create a bucket to store them
    
#     for _ in range(num_of_ids):
#         new_id = ''.join(random.choices(choice, k=num_of_char))
#         generated_ids.append(new_id)
        
#     return generated_ids  # Hand the list back to the program
# print(user_id_gen_by_user())


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
# def rgb_color_gen():
#     rgb = []
#     for _ in range(3):
#         new_rgb = randint(0,255)
#         rgb.append(new_rgb)
#     return rgb
# print('rgb',rgb_color_gen())


# ------------------------LEVEL 2-------------------------------
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after
 #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.

# def hexa_colors(num =5, chars = 5):
#     hex = string.hexdigits
#     hex_array = []
#     for _ in range(num):
#         new_hex =''.join(choices(hex, k= chars))
#         hex_array.append('#'+new_hex)
#     return hex_array
# print(hexa_colors())
        

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# def list_of_rgb_colors(num =5):
#     rgb_list = []
#     for _ in range(num):
#         new_rgb = randint(0,255)
#         rgb_list.append(new_rgb)
#     return rgb_list
# print('rgb',list_of_rgb_colors())


# Write a function generate_colors which can generate any number of hexa or rgb colors.
# def generate_colors(color, num):
#     color_list = []
#     match color:
#         case 'hexa':
#             for _ in range(num):
#                 new_hex =''.join(choices(string.hexdigits.lower(), k = 6))
#                 color_list.append('#'+new_hex)
#             return color_list
#         case 'rgb':
#             for _ in range(num):
#                 r = randint(0, 255)
#                 g = randint(0, 255)
#                 b = randint(0, 255)
                
#                 # Format it as a standard CSS-style string
#                 color_list.append(f"rgb({r}, {g}, {b})")
#             return  color_list
#         case _:
#             return 'Invalid Choice!'
# print(generate_colors('rgb',5))            
    

# -------------------------------LEVEL 3-----------------------
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# def shuffle_list(lst):
#     shuffle(lst)
#     return(lst)
# print(shuffle_list([1,2,3,4,5]))


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
# def array_of_seven_random_numbers():
#     lst =[]
#     while len(lst) < 7:
#         new_num = randint(0,9)
#         if new_num not in lst:
#             lst.append(new_num)
#     return lst
# print(array_of_seven_random_numbers())
