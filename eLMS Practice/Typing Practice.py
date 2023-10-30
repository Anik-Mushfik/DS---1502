line = 'a quick brown fox jumps over the lazy dog'
first_input = input(f"Write: ['a quick brown fox jumps over the lazy dog'] to test your typing skills.\n => ")
user_input = 'a quick brown fox jumps over the lazy dog'
while user_input == line:
    user_input = input(f'You are doing great. Try to do it faster!!!\n => ')
else:
    print(f'Your typing is wrong.Try again.')
