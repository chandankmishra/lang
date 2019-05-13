def fullJustify(words, maxWidth):
    result = []
    num_of_letters = 0
    cur_words_in_line = []
    for word in words:
        if len(word) + len(cur_words_in_line) + num_of_letters > maxWidth:
            n = len(cur_words_in_line)
            for i in range(maxWidth - num_of_letters):
                if len(cur_words_in_line) > 1:
                    cur_words_in_line[i % (n - 1)] += ' '
                else:
                    cur_words_in_line[i] += ' '
            result.append(''.join(cur_words_in_line))
            cur_words_in_line = []
            num_of_letters = 0
        cur_words_in_line.append(word)
        num_of_letters += len(word)
    remaining = ' '.join(cur_words_in_line)
    spaces = (maxWidth - len(remaining)) * ' '
    result.append(remaining + spaces)
    return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
result = fullJustify(words, maxWidth)
print (result)
