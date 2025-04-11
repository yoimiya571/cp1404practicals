import wikipedia


def search_wikipedia():
    """Search Wikipedia and handle exceptions."""
    while True:
        search_term = input("Enter page title: ").strip()
        if not search_term:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(search_term, autosuggest=False)
            print(f"{page.title}\n{page.summary[:500]}...\n{page.url}\n")
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following:")
            print(e.options)
        except wikipedia.PageError:
            print(f"Page id \"{search_term}\" does not match any pages. Try another id!")


# Uncomment this to run interactively
# search_wikipedia()
