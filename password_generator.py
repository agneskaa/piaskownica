import random
import string

def random_password(p = random.randrange(8, 20)):
    
    #import all ASCII characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    #we need at least 2 characters of each type
    n = 2
    rand_lowercase = random.sample(lowercase, n)
    rand_uppercase = random.sample(uppercase, n)
    rand_digits = random.sample(digits, n)
    rand_punctuation = random.sample(punctuation, n)

    #the rest of characters can be whichever type so the script needs to choose the remaining k characters out of all characters
    len_char = len(rand_lowercase + rand_uppercase + rand_digits + rand_punctuation)
    all_chars = random.sample(lowercase + uppercase + digits + punctuation, k = p - len_char)
    
    #add all password characters and shuffle it
    password_chars = rand_lowercase + rand_uppercase + rand_digits + rand_punctuation + all_chars
    random.shuffle(password_chars)

    return ''.join(password_chars)

print(random_password())