def get_num_words(book_text):
    return len(book_text.split())


def dict_of_words(book_text):
    book_text=book_text.lower()
    my_dict={}
    for text in book_text:
        if text not in my_dict:
            my_dict[text]=1
        else:
            my_dict[text]+=1
    # my_dict.sort(reverse=True,key=my_dict[text])
    return dict_to_lod(my_dict)

def dict_to_lod(my_dict):
    lod=[]
    i=0
    for key,value in my_dict.items():
        if key.isalpha()!=True:
            continue
        dict_info={"char":key,"value":value}
        lod.append(dict_info)
    lod.sort(reverse=True,key=sort_on)
    return lod

def sort_on(dict):
    return dict["value"]
        




