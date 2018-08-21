countries = {'Ukraine': 'UA',
             'Russia': 'RU',
             'Belaruss': 'BY',
             'German': 'DE',
             'Britain': 'UK'
}

capitals = {'UA': 'Kiev',
            'RU': 'Moskva',
            'BY': 'Minsk',
            'DE': 'Berlin',
            'UK': 'London'
}

countries['Poland'] = 'PL'
capitals['PL'] = 'Warsaw'

for key, value in countries.items():
    print('Domain for {} is {}'.format(key, value))
for a, b in capitals.items():
    print ('The capital of {} is {}'.format(a,b))
for a in capitals.items():
    print ('Domain {}'.format(a))
for a, b in countries.items():
    print ('Domain for {} is {}, The capital is {}'.format(a, b, capitals[b]))
for a, b in countries.items():
    countries[a] = [b, 'COM', 'GOV']

print(countries.items())


for a, b in countries.items():
    print('Domain for {} is {}.The capital is {}'.format(a, b, capitals[b[0]]))


# ab = {'Swaroop': 'swaroop@swaroopch.com',
#         'Larry': 'larry@wall.org',
#         'Matsumoto': 'matz@ruby-lang.org',
#         'Spammer': 'spammer@hotmail.com'
#      }
#
# print(f"Адрес Swaroop'а:", ab['Swaroop'])
# print("Адрес Swaroop'а:", ab['Larry'])