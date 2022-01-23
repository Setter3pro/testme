import requests
for i in range(1,43):

    page = requests.get(f"https://www.rfc-editor.org/rfc/rfc{i}.txt")

    text1 = page.text

    count_word = dict()

    for word in text1.split():

        word = word.lower()

        if word not in ['the','a','as','am','is','are','to','for' , 'be','in','of','and','|','that','we','by','only','their','much','it']:


            if word not in count_word.keys():

                count_word[word] = 1

            else:

                count_word[word] += 1

print(sorted(count_word.items() , key = lambda item: -item[1]))