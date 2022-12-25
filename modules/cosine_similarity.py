def cosine_similarity(X, Y):
    # Program to measure the similarity between
    # two sentences using cosine similarity.
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    # tokenization
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    # sw contains the list of stopwords
    sw = stopwords.words('english')
    l1 = []
    l2 = []

    # remove stop words from the string
    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)

        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)

    # cosine formula
    c = 0
    len_rvector = len(rvector)
    for i in range(len_rvector):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)

    return cosine


# test cosine_similarity()
if __name__ == "__main__":
    from input_refine import input_refine

    file = "input_files/作業8.c"
    X = input_refine(file)

    file = "input_files/作業12.6.c"
    Y = input_refine(file)

    print(cosine_similarity(X, Y))
