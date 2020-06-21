names = ['Kelvin', 'Intel']
dates = ['2019-04-04', '2019-05-04']
numbers = ['Some', '40', '0', '41', '15', 'Some', '56', '21', '88', '92',]

result_dict = {}
for name in names:
    for date in dates:
       for number in numbers:
          if number != 'Some':
             result_dict.setdefault(name, []).append({'date': date, 'first': ? , 'second': ?})


# dict = {
#          'Kelvin': [{
#                       'date': '2019-04-04', 'first': 40, 'second': 0
#                     }, 
#                     {
#                       'date': '2019-05-04', 'first': 41, 'second': 15
#                     }], 
#           'Intel': [{
#                       'date': '2019-04-04', 'first': 56, 'second': 21}, 
#                       {'date': '2019-05-04', 'first': 88, 'second': 92} 
#                    ]}
#        }