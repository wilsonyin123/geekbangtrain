import math
print('The value of Pi is approximately %5.3f.' % math.pi)


print('{1} and {0}'.format('spam', 'eggs'))

print('The story of {0}, {1}, and {other}.'.format(
    'Bill', 'Manfred', other='Georg'))


firstname = 'yin'
lastname = 'wilson'
print('Hello, %s %s.' % (lastname, firstname))
print('Hello, {1} {0}.'.format(firstname, lastname))
print(f'Hello, {lastname} {firstname}.')


f'{ 2 * 5 }'


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'hello, {self.first_name} {self.last_name}.'

    def __repr__(self):
        return f'hello, {self.first_name} {self.last_name}.'


me = Person('yin', 'wilson')

print(f'{me}')
