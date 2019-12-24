import re
from collections import Counter

def test_password(password):
    password_string = str(password)
    for i in range(len(password_string)):
        if (i > 0 and password_string[i] < password_string[i-1]):
            return False

    for c in Counter(password_string).values():
        if c >= 2:
            return True  
    return False

def test_password_v2(password):
    password_string = str(password)
    for i in range(len(password_string)):
        if (i > 0 and password_string[i] < password_string[i-1]):
            return False
  
    for c in Counter(password_string).values():
        if c == 2:
            return True  
    return False

def find_valid_password_count():
    password_min = 172851
    password_max = 675869

    valid_password_count = 0
    for x in range(password_min, password_max):
        if test_password_v2(x):
            valid_password_count += 1
    
    print(valid_password_count)

def main():
    find_valid_password_count()

if __name__ == "__main__":
    main()