with open('./Input/Names/invited_names.txt', 'r') as file:
    name_lst = file.read()
    name_lst = name_lst.splitlines()
    file.close()

with open('./Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.read()
    letter = letter.splitlines()
    file.close()

for i in range(len(name_lst)-1):
    new_greet = letter[0].replace('[name]', name_lst[i])
    new_letter = new_greet + '\n' + '\n'.join(letter[1:])
    # here can be changed to
    # new_letter = letter.replace('[name]', name_lst[i])
    f = open(f'./Output/ReadyToSend/letter_to_{name_lst[i]}.txt', 'w')
    f.write(new_letter)


# the standard answer
with open('./Input/Names/invited_names.txt', 'r') as name_file:
    names = name_file.readlines()

with open('./Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace('[name]', stripped_name)
        # here assign a new list to new_letter without modifying the original letter_contents
        with open(f'./Output/ReadyToSend/letter_to_{name_lst[i]}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)


# If use: letter[0] = letter.replace('[name]', name_lst[i]),
# It will always output 'Dear Aang', because the first element has been changed to 'Dear Aang' forever,
# thus it can't fine '[name]' anymore.

# Creating a new letter list 'new_letter' using phrase new_letter = letter also wouldn't help,
# because 'new_letter' and 'letter' are two variables pointing to the same value/data.
# You can modify the original date via both the two variables.
# But if you use new_letter = [str, str, ...] it will work,
# because now letter and new_letter are pointing to different data which have exactly the same value.
