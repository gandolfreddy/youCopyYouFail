def input_refine(file):
    with open(file, 'r', encoding="UTF-8") as fin:
        contents = fin.readlines()
    refined_contents = ' '.join([content
                                 .replace('\t', ' ')
                                 .replace('\n', ' ')
                                 for content in contents])
    return refined_contents


# test input_refine()
if __name__ == "__main__":
    file = "input_files/作業8.c"
    print(input_refine(file))

    file = "input_files/作業12.6.c"
    print(input_refine(file))
