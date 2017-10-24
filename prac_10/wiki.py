import wikipedia

search_criteria = str(input("Please enter information to search: "))
while search_criteria != "":
    try:
        search_option = wikipedia.page(search_criteria)
        print(search_option.title)
        print(wikipedia.summary(search_criteria))
        print(search_option.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_criteria = str(input("\n" + "Please enter information to search: "))