def get_num_words(book_text):
    return len(book_text.split())


def dict_of_words(book_text):
    book_text=book_text.lower()
    my_dict={}
    for text in book_text:
        if text not in my_dict:
            my_dict[text]=1
        my_dict[text]+=1
    return my_dict

#hello1gh456