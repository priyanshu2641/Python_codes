def searcher():
    import time
    # Some time for the function to run
    intro="My name is Priyanshu. I am currently a sophomore at IIT Ropar in Chemical Engineering Branch."
    time.sleep(5)
    # In the very first time, function will run from the stratch and then onwards it will start from after this.

    while True:
        text = (yield)
        if text in intro:
            print("The Text is in the Intro.")
        else:
            print("The Text is not in the Intro.")

search=searcher()
next(search)
search.send("Priyanshu")
a=input("Press any Key")
search.send("is Priyanshu")
search.send("Virat Kohli")
search.send("sophomore")