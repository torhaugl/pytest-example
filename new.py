def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    assert(factorial(0) == 1)
    assert(factorial(3) == 6)
    assert(factorial(4) == 24)


def count_word_occurence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def test_count_word_occurence_in_string():
    string = "one two one two three four"
    assert(count_word_occurence_in_string(string, 'one') == 2)
    assert(count_word_occurence_in_string(string, 'two') == 2)
    assert(count_word_occurence_in_string(string, 'three') == 1)
    assert(count_word_occurence_in_string(string, 'five') == 0)

def count_word_occurence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

def test_count_word_occurence_in_file():
    assert(count_word_occurence_in_file('test.txt', 'one') == 2)
    assert(count_word_occurence_in_file('test.txt', 'two') == 2)
    assert(count_word_occurence_in_file('test.txt', 'three') == 1)
    assert(count_word_occurence_in_file('test.txt', 'five') == 0)

def check_reactor_temperature(temperature_celsius):
    """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    from reactor import max_temperature
    print(max_temperature)
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status

def test_check_reactor_temperature():
    assert(check_reactor_temperature(-273) == 0)
    assert(check_reactor_temperature(9999999) == 1)

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1

def test_Pet():
    dog = Pet("Bark")
    assert(dog.name == "Bark")
    assert(dog.hunger == 0)
    dog.go_for_a_walk()
    dog.go_for_a_walk()
    assert(dog.hunger == 2)

