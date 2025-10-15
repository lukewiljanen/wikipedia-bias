# wikipedia-bias
Luke Wiljanen, Luca Heines

[literature Review](literature-review.md)


## Abstract
This project explores how AI can be used to detect and analyze bias in Wikipedia content. Using prior research on structural, gender, and representation biases, it examines how biased language appears, evolves, or is corrected over time. Using Wikipedia's text and edit histories, the study applies word embeddings, metadata analysis, and simple bias detection tools to trace patterns of bias across articles and topics. A key focus is on how AI-assisted editing impacts the persistence or reduction of these biases, and whether community revisions help mitigate or unintentionally reinforce them. Furthermore, this project dives into gender biases and how credible AI is at detecting such bias.


## Research Questions
<b>How does AI-assisted editing influence the introduction and persistence of bias in Wikipedia, and what patterns show whether community revisions reduce or reinforce these biases?</b>

As AI tools become more integrated into Wikipedia editing, they have the potential to both reduce and introduce bias. While they can flag problematic content, they may also replicate biases from the data they are trained on. This project examines how AI-assisted edits influence the presence of bias over time, and whether human revisions help correct or unintentionally reinforce those biases.

<br>

<b>Can AI models actually detect gender bias in Wikipedia articles?</b>

Gender bias in Wikipedia articles often shows up through unequal coverage, language, or framing of women compared to men. AI models offer a way to detect these patterns, but they may also reflect the same biases present in their training data. This project explores how effectively AI can identify gender bias and what limitations exist when relying on automated tools for such issue.


## Research Question Week 7
<b>Do articles about women link to fewer other Wikipedia articles than articles about men?</b>

-Selected two groups of articles: male and female scientists.

-Retrieved each article’s number of internal links using page.links.

-Calculated the average number of links for male and female groups.

-Compared averages to see if female articles link to fewer other pages.

### week7.py
[week7.py](week7.py)
Our program can simply just be ran and the average number of links for males and females will be displayed. Alternatively, any other names of males and females from other fields can be entered into the lists at the top of the program and the same data analysis can be ran on professional athletes for example.

With the help of this program we were able to determine that on average, male scientists had 943 links from articles,while female scientists had only 612 links from articles. Therefore, from this example we can determine that there is a favored bias towards males over their female counterparts.

Using the results of this program, and with more trials in different areas of study, we can truly answer if there is a specific male bias on wikiepedia when it comes to links. Considering links are how users jump from article to article, we can predict if male articles obtain more traffic than female articles due to this bias. 



## Methodology
This project will analyze Wikipedia articles to investigate how bias can be detected. Using Python, we can extract text summaries from Wikipedia pages and identify potential biased language by searching for specific indicator words associated with biased writing.

We also incorporate research from prior studies on Wikipedia bias, such as structural editor biases, gender bias in text, and the influence of automation on content representation. By combining text analysis with metadata on edits and editor activity, we track patterns of bias introduction and correction over time.

### test_wikipedia_api.py
This simple python program takes a Wikipedia link as input, extracts the page title, and fetches a short summary of the topic. Then it scans the summary for a set of predefined bias indicators that may suggest biased language. If any of these words appear in the summary, the script displays them, if not, it reports that no bias indicators were found.

