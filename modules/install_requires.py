import os


def install_requires():
    print("============ 安裝 requirements.txt 內容中 ============")
    os.system("pip install -r requirements/requirements.txt")

    print("============ 安裝 nltk 所需工具中 ============")
    import nltk
    nltk.download("stopwords")
    nltk.download("punkt")

    print("============ 安裝完畢 ============")


if __name__ == "__main__":
    install_requires()
