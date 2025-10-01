import wikipedia

# asking user for a Wikipedia link

url = input("Enter a Wikipedia link: ")

# extracting the page title from the URL

topic = url.split("/")[-1]

# grabbing a short summary

text = wikipedia.summary(topic, sentences=5)

# words that might alert opinionated or biased writing

bias_indicators = [
"clearly", "obviously", "undeniably", "disaster",
"failure", "success", "harmful", "dangerous",
"best", "worst", "must", "should"
]

print(f"\nHere's what I found about {topic.replace('_', ' ')}:")
print(text)

print("\nLooking for bias words.")
found = []
for word in bias_indicators:
    if word.lower() in text.lower():
        found.append(word)

if found:
    print("Found these bias words")
    for word in found:
        print(f" - {word}")
else:
    print("Looks pretty neutral")
