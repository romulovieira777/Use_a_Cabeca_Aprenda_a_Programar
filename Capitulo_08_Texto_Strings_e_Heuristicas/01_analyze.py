import ch1text


def count_sentences(text):
    count = 0
    terminals = '.;?!'

    for char in text:
        if char in terminals:
            count = count + 1

    return count


def compute_readability(text):
    total_word = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split()
    total_word = len(words)

    total_sentences = count_sentences(text)

    print(total_word, 'words')
    print(total_sentences, 'sentences')


compute_readability(ch1text.text)

"""
    count_word = 0
    count_sentences = 0
    count_syallables = 0

    score = 206.835 - 1.015 * (total_word / total_sentences) - 84.6 * (total_syllables / total_word)

    if score >= 90.0:
        print('Reading level of 5th Grade')
    elif score >= 80.0:
        print('Reading level of 6th Grade')
    elif score >= 70.0:
        print('Reading level of 7th Grade')
    elif score >= 60.0:
        print('Reading level of 8-9th Grade')
    elif score >= 50.0:
        print('Reading level of 10-12th Grade')
    elif score >= 30.0:
        print('Reading level of College Student')
    else:
        print('Reading level of College Graduate')

    return score
"""