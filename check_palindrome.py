def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.
    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    def is_pali (palindrome):
        rev = palindrome[::-1]
        if rev == palindrome:
            return True
        else:
            return False

    def check_conditions (num):        
        if is_pali(str(num)[2:6]):
            num += 1
            if is_pali(str(num)[1:6]):
                num += 1
                if is_pali(str(num)[1:5]):
                    num +=1
                    if is_pali(str(num)):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    num_list = list()
    for i in range(100000,1000000):
        if check_conditions (i):
            num_list.append(i)
        else:
            continue
    return num_list

print (check_palindrome())
    

            
