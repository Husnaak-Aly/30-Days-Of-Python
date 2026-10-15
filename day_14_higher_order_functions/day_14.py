from functools import reduce

countries2 = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
#------------------LEVEL 1-------------------------
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1. Use for loop to print each country in the countries list.

# for i in countries:
#     print(i)

#2. Use for to print each name in the names list.
# num = 1
# for name in names:
#     print("Name", num, ":", name)
#     num += 1

# 3.Use for to print each number in the numbers list.
# for num in numbers:
#     print(num)

#------------------LEVEL 2-------------------------
#1. Use map to create a new list by changing each country to uppercase in the countries list
# def upp(country):
#     return country.upper()
# upper_name = map(upp, countries)
# print(list(upper_name))


#2. Use map to create a new list by changing each number to its square in the numbers list
# def sqr(num):
#     return num ** 2
# sqr_nums = map(sqr, numbers)
# print(list(sqr_nums))

#3. Use map to change each name to uppercase in the names list
# upper_name = list(map(str.upper, names))
# print(upper_name)

#4. Use filter to filter out countries containing 'land'
# def contain_land(country):
#     if 'land' in country:
#         return True
#     return False
# land = list(filter(contain_land, countries))
# print(land)

# land = list(filter(lambda x: x[-4:] ==  'land', countries))
# land = list(filter(lambda x: x.endswith('land'), countries))
# print(land)


#5. Use filter to filter out countries having exactly six characters.
# six_letter_countries = list(filter(lambda x: len(x) == 6, countries))
# print(six_letter_countries)


#6. Use filter to filter out countries containing six letters and more in the country list.
# six_or_more_letter_countries = list(filter(lambda x: len(x) >= 6, countries))
# print(six_or_more_letter_countries)


#7. Use filter to filter out countries starting with an 'E'
# start_with_E = list(filter(lambda x: x.startswith('E'), countries ))
# print(start_with_E)

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# mapped = list(map(lambda x: x ** 2, numbers))
# filtered = list(filter(lambda x: x > 5, mapped))
# reduced = reduce(lambda a,b: a +b, filtered)
# print(reduced)


#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# item_list = ['Husnaak', 'Ali', 23, 21, 'Sachin', 48]
# def get_string_list(item):
#     if type(item) == str :
#         return True
#     return False
# string_only = list(filter(get_string_list, item_list))
# print(string_only)


#10. Use reduce to sum all the numbers in the numbers list.
# sum_of_all_numbers = reduce(lambda a,b: a+b, numbers)
# print(sum_of_all_numbers)


#11. Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# sentence = reduce(lambda a,b: a+ ', '+b  , countries[:-1])
# sentence += ', and ' + countries[-1] + ' are north European countries'

# print(sentence)


#12. Declare a function called categorize_countries that returns a list of countries with some common pattern
#  (you can find the countries list in this repository as countries2.js(eg 'land', 'ia', 'island', 'stan')).
# def categorize_countries(countries2, pattern):
    # return list(filter(lambda country: country.endswith(pattern), countries2))
# print(categorize_countries(countries2, 'land'))
# print(categorize_countries(countries2, 'ia'))
# print(categorize_countries(countries2, 'Islands'))
# print(categorize_countries(countries2, 'stan'))


#13. Create a function returning a dictionary, where keys stand for starting letters of countries 
# and values are the number of country names starting with that letter.
# def country_count(countries):
#     letters = list(map(lambda country: country[0], countries))

#     result = {}

#     for letter in letters:
#         if letter in result:
#             result[letter] += 1
#         else:
#             result[letter] = 1

#     return result
# print(country_count(countries2))


# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# def get_first_ten_countries(countires):
#     ten_countries = list(filter(lambda country: countires.index(country) < 10 , countires))

#     return ten_countries
# print(get_first_ten_countries(countries2))


#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries (countries):
     ten_last_countries = list(filter(lambda country: country in countries[-10:] , countries))
     return ten_last_countries
print(get_last_ten_countries(countries2))