def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    flag = 0
    cuple_num = 0
    last_letter = list ()
    if word != '':
        for letter in word:
            if not last_letter:
                last_letter.append(format(letter))
                continue
            if letter == last_letter[-1]:
                cuple_num += 1
                if cuple_num>=3:
                    flag = 1
                    break
            if letter != last_letter[-1] and len(last_letter)>=2 and last_letter [-2]!= last_letter [-1]:
                cuple_num = 0
            last_letter.append(format(letter))
    return flag

this_word = ''
print (trifeca(this_word))

