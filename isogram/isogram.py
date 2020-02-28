def is_isogram(string):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = 0
        for word in string:
            if letter == word.lower():
                count += 1
            if count > 1:
               return False
	           return True
