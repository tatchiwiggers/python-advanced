london = {}
london['star_monument'] = 'Big Ben'
london['country'] = 'England'
london['population'] = 8_982_000
london['population'] = 8_982_010
print(type(london))

print(london)
print(london['star_monument'])
print(london['population'])

london = {
  'star_monument': 'Big Ben',
  'country': 'England',
  'population': 8982010,
  'population': 898200
  }

del london['population']

print(london)

for key in london:
  print(key)

for value in london.values():
  print(value)

for key, value in london.items():
  print(f'{key}:', value)
  print(key)
  print(value)
print(london)
print(len(london))


london = {'star_monument': 'Big Ben', 'country': 'England', 'population': 8982010}

print(london['country']) #=> "England"
print(london.get('country', "não existe essa chave no seu dict!")) #=> "England"
print(london['prime_minister']) # => breaks!!
print(london.get('prime minister', "não existe essa chave no seu dict!")) #=> "No key prime minister"

students = ['Peter', 'Mary', 'George', 'Emma']
student_ages = [24, 25, 22, 20]

students_dict = dict(zip(students, student_ages))
print(students_dict)

student_ages_dict = {key: value for key, value in zip(students, student_ages)}
print(student_ages_dict)