# Comment Scrapper
This Code collects and analyses a list of comments to automatically sort and collate similar comments with the goal of getting a sorted list of requests from most to least

# Algorithm
the algorithm is a basic implementation of comment similarity analysis that uses the SequenceMatcher class to calculate matching ratios between comments, and maintains a list of similar comments for each comment in a CSV file.

# TDB
Expand the platform support to other platforms than Tiktok


# Docs (Generated by chatGPT)
# Comment.py
__init__(self, commentString: str, video: str) -> None: This is the constructor method for the Comment class. It takes two arguments, commentString and video, both of which are strings. The method initializes several instance variables, including commentString, request, similarComments, and videoStr.

compare(self, otherComment): This method takes another Comment object as an argument and compares its commentString attribute to the commentString attribute of the current object. It uses the difflib.SequenceMatcher class to find the ratio of matching characters between the two strings. If the ratio is greater than 0.1, it also finds the matching blocks between the two strings and concatenates them to form a merged match string. The method returns both the merged match string and the matching ratio.

looksLike(self, otherComment): This method takes another Comment object as an argument and calls the compare method to find the matching ratio between the two comment strings. If the matching ratio is greater than or equal to 0.7, it returns True. Otherwise, it returns False.

addSimilar(self, otherComment): This method takes another Comment object as an argument and adds it to the similarComments list of the current object.

size(self): This method returns the length of the similarComments list of the current object.

# Suggestions.py
__init__(self): This is the constructor method for the Suggestions class. It initializes an empty list called suggestionList.

add(self, comment: Comment): This method takes a Comment object as an argument and compares it to all the comments in the suggestionList using the compare method. If the matching ratio is greater than 0.7 with any existing comment, it adds the current comment to the similarComments list of the existing comment. Otherwise, it adds the current comment to the suggestionList.

save(self): This method creates a comma-separated string of all the comments and their related similarComments in the suggestionList and writes it to a file called comments.csv. The format of the string is as follows:

[size of similarComments],[commentString],[videoStr],[similarComment1],[similarComment2],...

Each comment (including its similar comments) is written on a new line in the file.