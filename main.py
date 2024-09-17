import dictionaryEST
from rapidfuzz import process, fuzz


# Move lookup_article outside of main() to make it accessible globally
def lookup_article(topic):
    topic = topic.strip().capitalize()  # Normalize Input
    result = process.extractOne(topic, dictionaryEST.weather_dict.keys(), scorer=fuzz.ratio)

    if result:
        best_match, score, *_ = result  # Unpack the first two values
        if score > 60:
            return f"{best_match}: {dictionaryEST.weather_dict[best_match]}"
    return "No close enough match found."


def main():
    view = input("Enter 1 to see a list of topics to learn about: ")
    if view == "1":
        for i in dictionaryEST.weather_dict.keys():
            print(i)
        x = True
        print("\n\n")
    else:
        x = True

    while x:
        query = input("Enter a search term and we will match it as best as possible: ")
        print(lookup_article(query))
        x = input("----------------------------------------------------------------------------------------------------"
                  "---------------------------------------------------------------\n"
                  "Do you want to try again? (y/n): ").lower()
        print("\n\n")
        if x != "y":
            x = False


if __name__ == "__main__":
    main()
