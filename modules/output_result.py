def output_result(data):
    with open("output_files/result.txt", 'a', encoding="UTF-8") as fout:
        fout.write(data)

    return "done"


# test output_result()
if __name__ == "__main__":
    from tabulate import tabulate

    data = [
        ["雞蛋", "1 公克", 50],
        ["牛奶", "5 公克", 20],
        ["雞蛋糕", "16 公克", 80],
        ["糖果", "29 公克", 2200],
        ["冰塊", "1 公克", 810],
    ]

    print(output_result(tabulate(data, tablefmt="grid")))
