# Лабораторна робота 1 "Довгий метод"
### Харченко Віталій  ІКМ-223Б


___


- Вхідний код


```Python
    import os
from DataGenerator import *
import time


class DataProcessor:
    def __init__(self):
        self.data = []

    def process_data(self):
        with open('data.txt', 'r') as file:
            for line in file:
                self.data.append(line.strip())

        processed_data = []
        for item in self.data:
            if item.startswith('A'):
                processed_data.append(self._process_type_a(item))
            elif item.startswith('B'):
                processed_data.append(self._process_type_b(item))
            else:
                processed_data.append(self._process_other(item))

        with open('processed_data.txt', 'w') as file:
            for item in processed_data:
                file.write(f"{item}\n")

    def _process_type_a(self, item):
        return item.upper()

    def _process_type_b(self, item):
        return item.lower()

    def _process_other(self, item):
        return item.capitalize()


if __name__ == '__main__':
    if not os.path.isfile('data.txt'):
        generate(1000)
    start_time = time.time()
    processor = DataProcessor()
    processor.process_data()
    end_time = time.time()
    print(f"Executing time: {end_time - start_time}"
```


### Аналіз


У вихідному коді класу DataProcessor метод process_data виконує кілька операцій: зчитування даних з файлу, обробка даних різних типів та запис оброблених даних у файл. Це призводить до великої кількості коду в одному методі, що робить його важким для розуміння та підтримки.


- Вихідний код


```Python
import os
from DataGenerator import *
import time


class DataProcessor:
    def __init__(self):
        self.data = []

    def process_data(self):
        self._read_data_from_file()
        processed_data = self._process_data()
        self._write_processed_data_to_file(processed_data)

    def _read_data_from_file(self):
        with open('data.txt', 'r') as file:
            for line in file:
                self.data.append(line.strip())

    def _process_data(self):
        processed_data = []
        for item in self.data:
            if item.startswith('A'):
                processed_data.append(self._process_type_a(item))
            elif item.startswith('B'):
                processed_data.append(self._process_type_b(item))
            else:
                processed_data.append(self._process_other(item))
        return processed_data

    def _write_processed_data_to_file(self, processed_data):
        with open('processed_data.txt', 'w') as file:
            for item in processed_data:
                file.write(f"{item}\n")

    def _process_type_a(self, item):
        return item.upper()

    def _process_type_b(self, item):
        return item.lower()

    def _process_other(self, item):
        return item.capitalize()


if __name__ == '__main__':
    if not os.path.isfile('data.txt'):
        generate(1000)
    start_time = time.time()
    processor = DataProcessor()
    processor.process_data()
    end_time = time.time()
    print(f"Executing time: {end_time - start_time}")
```


# Аналіз


Під час рефакторингу великого методу process_data було розділено на кілька менших методів, кожен з яких відповідає за певну частину функціоналу. Це зробило код більш читабельним, керованим та підтримуваним. В результаті код став більш модульним, і його легше розширювати та модифікувати у майбутньому


### Також було реалізовано генератор даних

```Python3
import random
import string


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate(num_lines):
    with open('data.txt', 'w') as file:
        for _ in range(num_lines):
            line = generate_random_string(random.randint(5, 15))  # Випадкова довжина від 5 до 15 символів
            file.write(line + '\n')
```

## Час виконання

- Час виконання з довгим методом складає "Executing time: 0.016537189483642578"
- Час виконання з оптимізованим методом складає "Executing time: 0.004004001617431641"


Різниця в часі виникає в основному через те, що в першому випадку кожен рядок зчитується з файлу і миттєво додається до списку self.data, тоді як у другому випадку рядки зчитуються з файлу за один раз у методі _read_data_from_file().


Отже, в першому варіанті, коли кожен рядок додається безпосередньо в методі process_data, час витрачений на зчитування рядків з файлу, фактично, включається до часу виконання методу process_data. У другому варіанті, де рядки зчитуються у окремому методі, цей час не включається до часу виконання методу process_data, а тільки до часу зчитування даних.


Також можливо, що різниця в часі виконання становиться помітною через вплив оптимізацій операцій вводу/виводу, які можуть відбуватися поза межами програми.


У будь-якому випадку, різниця в часі виконання дуже мала і вважається незначною з точки зору виконання програми.


# Висновки


Для зручнішого використання та читабельності та оптимізації коду, використання довгих методів не є доцільним, але це не є доцільним тоді коли необхідно скоротити час виконання та якщо функція буде виконувати одну конкретну дію, наприклад опрацьовувати данні у VirtualTreeView (що не представлено у даному коді)




