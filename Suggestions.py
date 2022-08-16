from Comment import Comment


class Suggestions:

    def __init__(self):
        self.suggestionList = []

    def add(self, comment: Comment):
        highestRatio = 0
        similarComment = None
        for index in range(len(self.suggestionList)):
            existingComment = self.suggestionList[index]
            _, ratio = comment.compare(existingComment)
            if ratio > highestRatio:
                highestRatio = ratio
                similarComment = existingComment

        if highestRatio > 0.7:
            similarComment.addSimilar(comment)
        else:
            self.suggestionList.append(comment)

    # def sort(self, index):
    #     comment = self.suggestionList[index]

    #     for i in range(index-1, -1, -1):
    #         higherComment = self.suggestionList[i]
    #         if comment.size() > higherComment.size():
    #             self.suggestionList[i], self.suggestionList[index] = self.suggestionList[index], self.suggestionList[i]
    #             break

    def save(self):
        fileString = ''
        for comment in self.suggestionList:
            fileString += str(comment.size())
            fileString += ',' + comment.commentString

            for similar in comment.similarComments:
                fileString += ',' + similar.commentString
            fileString += '\n'

        file = open("comments.csv", "w", encoding="utf-8")
        file.write(fileString)
        file.close()
