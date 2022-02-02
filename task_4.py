with open("text_4.txt", "r", encoding="utf-8") as f:
    with open("task4_1.txt", "w", encoding="utf-8") as f2:
        for line in f:
            str1 = ''
            if 'One' in line:
                str1 = line.replace('One', 'Один')
            if 'Two' in line:
                str1 = line.replace('Two', 'Два')
            if 'Three' in line:
                str1 = line.replace('Three', 'Три')
            if 'Four' in line:
                str1 = line.replace('Four', 'Четыре')
            f2.write(str1)
