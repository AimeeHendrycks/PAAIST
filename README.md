# PAAIST--Personal Assistant Artificial Intelligence Strength Test

This is PAAIST, a personal assistant AI benchmark. With PAAIST, AI's like Siri, Cortana, and Google Now 
attempt to answer 60 questions randomly generated by queryGenerator.py (written in Python 2.7).

On different runs, queryGenerator generates different questions.

To try it yourself, simply run queryGenerator, ask the personal assistant each question while noting the answer, 
and score the AI accordingly.

# Results
The results of one of the runs are available [here](Results/results.html).

# How does it work?
The queryGenerator randomly selects a type of question and from there it randomly selects attributes for that type of question. For example, the generator
might select a geometry problem then run the code
```
print 'Determine the interior angles of a rhombus with side lengths',\
random.randrange(1, 10), 'and', random.randrange(1, 10) + '.'
```

# If I want to try this myself, how should I score it?
Points are assigned as follows:

0%: Award a grand total of nothing if the AI answers incorrectly, does not answer, or cannot understand the question

75%: Possible only for relatively long answers. In this case, give 75% if the AI returns a correct paragraph, video, etc.
with unnecessary information and without highlighting the relevant part (e.g., bolding text, skipping to the relevant part of the video, etc.).
There must be a distinction between the answer and a list of links.

100%: Give full credit if it answers correctly and, if the response is relatively long, highlights or reads the relevant part

Sum the percentages and divide by the number of questions.

# Disclaimer
This is an incomplete benchmark made for fun. Determining the strength of an AI from this benchmark alone
is problematic.

# Credits
Made by Daniel and Aimee Hendrycks.