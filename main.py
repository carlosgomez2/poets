import nltk


def clean_poems(writers):
    datasets = []
    for writer in writers:
        with open(f"raw/{writer}.txt", "r") as f:
            data = f.readlines()

        if not data:
            print(f"No se encontraron poemas para el autor '{writer}'")
            break

        data = [d.strip() for d in data]

        verses = []
        for poem in data:
            if poem.startswith("Poem:"):
                verses.append(poem)

        datasets.append(verses)

    return datasets


writer = "paz"
datasets = clean_poems([writer])

print(datasets[0])

# # Create a list of bigrams using ngrams
# bigrams = list(nltk.util.ngrams(dataset, n=2))

# print(bigrams)

# # Generate a poem from the bigrams
# poem = []
# for bigram in bigrams:
#     poem.append(bigram[0])
#     poem.append(bigram[1])

# # Add a newline character at the end of the poem
# poem.append("\n")

# print(poem)