# test prep question

# 3a
def scores(word):
    score = 0 
    for i in word.upper(): 
        if i in 'AEIOULNSTR': 
            score += 1
        elif i in 'DG':
            score += 2
        elif i in 'BCMP': 
            score += 3
        elif i in 'FHVWY':
            score += 4 
        elif i in 'K': 
            score += 5
        elif i in 'JX': 
            score += 8
        else: 
            score += 10
    return score 


#3b 
def word_scores(word_list):
    score_list = []
    for word in word_list: 
        score_list.append(scores(word))
    return score_list
#3c 
def bubble(word_list):
    score_list = word_scores(word_list)
    swapped = True 
    while swapped: 
        swapped = False 
        for i in range (1, len(score_list)):
            if score_list[i] > score_list[i-1]: 
                score_list[i], score_list[i-1] = score_list[i-1], score_list[i]
                word_list[i], word_list[i-1] = word_list[i-1], word_list[i]
                swapped = True
    return word_list


words_input = input("Enter words separated by spaces: ").split()
sorted_words = bubble(words_input)
sorted_scores = [scores(word) for word in sorted_words]
print("Words sorted by score (highest to lowest):")
for word, score in zip(sorted_words, sorted_scores):
    print(f"{word}: {score}")