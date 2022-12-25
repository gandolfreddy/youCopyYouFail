import os
from os import walk
import platform
from modules.cosine_similarity import cosine_similarity
from modules.input_refine import input_refine
from modules.install_requires import install_requires
from modules.output_result import output_result


def main():
    # Initialize
    try:
        import nltk
        from tabulate import tabulate
    except ImportError:
        install_requires()
    finally:
        from tabulate import tabulate

    if os.path.isfile("output_files/result.txt"):
        os.remove("output_files/result.txt")

    # Read [XXX].c files
    INPUT_SOURCE = "input_files/"
    _, __, fs = next(walk(INPUT_SOURCE))
    vectors = [(f, input_refine(INPUT_SOURCE + f)) for f in fs]

    # set expected valid similarity
    try:
        valid_similarity = round(float(input(
            "輸入可允許相似度 %（預設為 90%）："
        )), 3) / 100
    except:
        valid_similarity = 0.90

    # Put all the expecting files into cosine_similarity, getting the cosine.
    result_table = [["被比較\\比較"]+fs]
    high_similarity_lt = ["高度相似"]
    for fname_main, vector_main in vectors:
        data_row = [fname_main]
        for fname_sub, vector_sub in vectors:
            ms_cosine = cosine_similarity(vector_main, vector_sub)
            if ms_cosine >= valid_similarity and fname_main != fname_sub and fname_sub not in high_similarity_lt:
                high_similarity_lt.append(fname_sub)
            sign = " 😡" if ms_cosine >= valid_similarity and fname_main != fname_sub else ''
            similarity_percent = f"{round(ms_cosine, 3)*1000/10}%" if fname_main != fname_sub else "X"

            data_row.append(f"{similarity_percent}{sign}")
        result_table.append(data_row)

    # write the result table to result.txt
    output_result(tabulate(result_table, tablefmt="grid"))
    output_result("\n\n")
    output_result(tabulate([high_similarity_lt], tablefmt="grid"))

    # Show the result when the analysis is done
    print("Done (^ v ^)")
    print("====================== Result ======================\n")
    if platform.system() == "Windows":
        os.system("type .\\output_files\\result.txt")
    else:
        os.system("cat './output_files/result.txt'")
    print("\n\n====================================================")


if __name__ == "__main__":
    main()
