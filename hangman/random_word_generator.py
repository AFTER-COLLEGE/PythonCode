from random import randint
def pick_random_word():
    list_of_words=['this', 'warning', 'theif', 'offered', 'mentor', 'biggest', 'hardest', 'something', 'veryfication', 'beautifull', 'international', 'nothing','biggest', 'disappointment', 'trip', 'restaurant', 'received', 'good', 'reviews', 'expectations', 'highest', 'service', 'slowest', 'evenly', 'thoughest', 'restaurant', 'fullfilment', 'house', 'salad', 'could', 'come', 'sizzler', 'moniter', 'keshi', 'roadways', 'although', 'tasty', 'reminded', 'barbequed', 'pulled', 'chicken', 'restaurant', 'overrated']
    index_mumber=randint(0,len(list_of_words)-1)
    return list_of_words[index_mumber]


