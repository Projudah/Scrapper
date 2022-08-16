import difflib


class Comment:
    def __init__(self, commentString: str) -> None:
        self.commentString = commentString.lower()
        self.request = None
        self.similarComments = []

    def compare(self, otherComment):
        mergedMatch = ''
        matcher = difflib.SequenceMatcher(
            None, self.commentString, otherComment.commentString)
        ratio = matcher.ratio()

        if(ratio > 0.1):
            blocks = matcher.get_matching_blocks()
            for block in blocks:
                start = block[0]
                length = block[2]
                sequence = self.commentString[start: start + length]
                mergedMatch = mergedMatch + sequence
        return mergedMatch, ratio

    def looksLike(self, otherComment):
        match, ratio = self.compare(otherComment)
        return ratio >= 0.7

    def addSimilar(self, otherComment):
        self.similarComments.append(otherComment)

    def size(self):
        return len(self.similarComments)
