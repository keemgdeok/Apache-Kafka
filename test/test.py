with open('./topic.txt', 'w', encoding='utf-8') as file:
    # Write numbers 1 to 1000, each on a new line
    for i in range(1, 10001):
        file.write(f"{i}\n")