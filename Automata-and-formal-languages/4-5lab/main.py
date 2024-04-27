import re

pattern = r'^\d{1,10}\.\d{3}+\s*[,;?]\s*[a-zA-Z0-9]{1,27}\s*[,;?]\d{1,10}\.\d{3}+\s*[,;?]\d{1,10}+\s*[,;?]\d{1,9}\s*[,?]\s*[a-zA-Z0-9]{11}\s*+$'

def process_line(line):
    # заміняємо , на ;
    # приклад
    # input: 1234.678, PName, 1000.123, 50, 12345, WASD123
    # output: 1234.678; PName; 1000.123; 50; 12345; WASD123
    return re.sub(r',', ';', line)

with open('input.txt', 'r', encoding='utf-8') as input_file:
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for line in input_file:
            processed_line = process_line(line)
            output_file.write(processed_line)

print("The result of replacing ',' to ';' in - output.txt")
