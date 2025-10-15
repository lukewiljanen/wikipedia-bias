import wikipedia
import statistics

# Lists of male and female scientists for data analysis
female_scientists = ["Hypatia of Alexandria", "Rosalind Franklin", "Jennifer Doudna", "Jane Goodall", "May-Britt Moser"]
male_scientists = ["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Charles Darwin", "Niels Bohr"]


# method for finding average number of links
def average_links(names):
    counts = []
    for name in names:
        try:
            page = wikipedia.page(name)
            counts.append(len(page.links))
            print(f"{name}: {len(page.links)} links")
        except Exception as e:
            print(f"Skipping {name}: {e}")
    return statistics.mean(counts)


female_avg = average_links(female_scientists)
male_avg = average_links(male_scientists)


print("\nAverage links:")
print(f"Average female links: {female_avg:.2f}")
print(f"Average male links:   {male_avg:.2f}")
