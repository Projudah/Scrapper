import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def isCommentClass(className):
    if not className:
        return False
    return Page.commentClassMatch in className.lower()


def isCommentItem(className):
    if not className:
        return False
    return Page.commentItemMatch in className.lower()


def isVideoClass(className):
    if not className:
        return False
    return Page.videoClassMatch in className.lower()


class Page:
    # Ensure all class matches are in lowercase
    commentClassMatch = "CommentList".lower()
    commentItemMatch = "CommentText".lower()
    videoClassMatch = "DivItemContainerv2".lower()

    def __init__(self, url):
        self.url = url
        options = self.hideMessages()
        self.driver = webdriver.Chrome(
            "D:\Downloads\Software\chromedriver_win32 - 1\chromedriver.exe",
            options=options,
        )
        self.load(url)

    def load(self, url):
        self.driver.get(url)
        time.sleep(2)  # Allow 2 seconds for the web page to op

    def hideMessages(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--disable-web-security")
        options.add_argument("--incognito")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-data-dir=D:/Downloads/Software/chromedriver_win32/temp"
        )
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options

    def scrollPage(self):
        last_height = 0

        while True:
            self.driver.execute_script(
                "document.documentElement.scrollTo({top : document.body.scrollHeight, behavior: 'smooth'});"
            )

            # Wait to load page
            # time.sleep(1)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            print("HEIGHT", new_height)

            if new_height <= last_height:
                break
            last_height = new_height

    def scrollPage2(self):
        last_height = 0

        while True:
            self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(
                webdriver.Keys.CONTROL, webdriver.Keys.END
            )
            # Wait to load page
            time.sleep(1)

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            print("HEIGHT", new_height)

            if new_height <= last_height:
                break
            last_height = new_height

    def scrollEl(self):
        last_height = 0

        while True:
            self.driver.execute_script(
                "window.currentElement.scrollTo({top : window.currentElement.scrollHeight, behavior: 'smooth'});"
            )

            # Wait to load page
            time.sleep(1)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script(
                "return window.currentElement.scrollHeight"
            )

            # print("HEIGHT", new_height)

            if new_height <= last_height:
                break
            last_height = new_height

    def scrollComments(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        comments = soup.find_all(class_=isCommentClass)[0]
        className = comments.get("class")[0]
        # print(className)
        self.driver.execute_script(
            "window.currentElement = document.getElementsByClassName('"
            + className
            + "')[0];"
        )
        time.sleep(2)
        self.scrollEl()

    def scrollComments2(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        time.sleep(1)
        comments = soup.find_all(class_=isCommentClass)[0]
        className = comments.get("class")[0]
        self.driver.execute_script(
            "window.currentElement = document.getElementsByClassName('"
            + className
            + "')[0];"
        )

        time.sleep(2)

        last_height = 0

        while True:
            self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(
                webdriver.Keys.CONTROL, webdriver.Keys.END
            )
            # Wait to load page
            time.sleep(1)

            new_height = self.driver.execute_script(
                "return window.currentElement.scrollHeight"
            )

            # print("HEIGHT", new_height)

            if new_height <= last_height:
                break
            last_height = new_height

    def getComments(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        commentsDivs = soup.find_all(class_=isCommentItem)
        comments = [self.commentsFromCommentDiv(com) for com in commentsDivs]
        return comments

    def commentsFromCommentDiv(self, commentDiv):
        span = commentDiv.find_all("span")
        if len(span) == 0:
            return ""

        content = span[0].contents

        if len(content) == 0:
            return ""

        return content[0]

    def urlFromVideo(self, video):
        aTags = video.find_all("a")

        if len(aTags) == 0:
            return ""

        href = aTags[0].get("href")
        return href + "?is_copy_url=1&is_from_webapp=v1"

    def getVideos(self):
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        videosDivs = soup.find_all(class_=isVideoClass)
        videos = [self.urlFromVideo(vid) for vid in videosDivs]
        return videos
