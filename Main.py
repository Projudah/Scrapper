import Page
from Comment import Comment
from Suggestions import Suggestions

window = Page.Page("https://www.tiktok.com/")

print("Login to Tiktok and naviage to profile page")
input("enter to continue")

videos = window.getVideos()
print("Working on ", len(videos), "Videos")

count = 0
suggestions = Suggestions()

for video in videos:
    try:
        count += 1
        print("\n")
        print(count, "/", len(videos))
        window.load(video)
        window.scrollComments2()
        comments = window.getComments()

        commentCount = 0

        for comment in comments:
            commentCount += 1
            print("Comments", commentCount, "/", len(comments), "         ", end="\r")
            commentClass = Comment(comment, video)
            suggestions.add(commentClass)
    except Exception as e:
        print(e)
        print(video)
        print("FAILED ------------ \n")

    # if count > 10:
    #     break

suggestions.save()

print("Done")
