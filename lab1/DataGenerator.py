import random
import string


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate(num_lines):
    with open('data.txt', 'w') as file:
        for _ in range(num_lines):
            line = generate_random_string(random.randint(5, 15))  # Випадкова довжина від 5 до 15 символів
            file.write(line + '\n')
