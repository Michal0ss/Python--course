# dictionary = a changeable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us t o access quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Katowice'})
capitals.pop('China')
#capitals.clear()

# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)
#...........................................
