line = 'a quick brown fox jumps over the lazy dog'
#checker = 'a,quick,brown,fox,jumps,over,the,lazy,dog'
#check = checker.split(",")
user_input = input(f"Write: ['a quick brown fox jumps over the lazy dog'] to test your typing skills.\n => ")
#user_input = 'a quick brown fox jumps over the lazy dog'
while user_input == line:
    user_input = input(f'You are doing great. Try to do it faster!!!\n => ')
else:
    i = 0
    while i < len(user_input):
        if user_input[i] != line[i]:
            wrong = user_input[i]
            right = line[i]
            break
        i += 1
    print(f"Your typing is wrong! Try again... \nThe word that you typed wrong was '{wrong}', while it should be '{right}'.")
