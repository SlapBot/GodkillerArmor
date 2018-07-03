from praw import Reddit
import random


class Savenger:
    AVENGERS = ["Iron Man", "Doctor Strange", "Star-Lord", "Black Widow", "Thor",
                "Spider-Man", "Captain America", "Wanda Maximoff", "Bucky Barnes",
                "Loki", "Hulk", "Black Panther", "Vision", "Gamora", "Drax", "Nebula",
                "Sam Wilson", "Mantis", "Okoye", "Shuri", "Groot", "Rocket", "Heimdall"]

    def __init__(self):
        self.Reddit = Reddit

    def get_superhero(self):
        return random.choice(self.AVENGERS)

    def authenticate(self, username, password, client_id, client_secret, user_agent):
        print("Authenticating...")
        try:
            self.reddit = self.Reddit(user_agent=user_agent, client_id=client_id,
                                      client_secret=client_secret, username=username,
                                      password=password)
            self.user = self.reddit.user.me()
            print(f"Authenticated as {self.user}")
            return self.reddit
        except Exception as e:
            print(e)
            exit()

    def save(self, subreddit):
        try:
            print("Savengers are on the way, stay hold.")
            subreddit = self.reddit.subreddit(subreddit)
            print(f"{self.get_superhero()} finding every threatening submission made in {subreddit}")
            subreddit_submissions = self.get_user_subreddit_submissions(subreddit)
            self.delete_submissions(subreddit_submissions)
            print(f"{self.get_superhero()} saved your from dying by the submission's author")
            print(f"{self.get_superhero()} finding every forbidding comment made in {subreddit}")
            subreddit_comments = self.get_user_subreddit_comments(subreddit)
            self.delete_comments(subreddit_comments)
            print("Savengers have saved you!")
            return True
        except Exception as e:
            print(e)
            exit()

    def get_user_subreddit_comments(self, subreddit):
        subreddit_comments = []
        for comment in self.user.comments.new(limit=None):
            if comment.subreddit == subreddit:
                if comment.body:
                    print(f"{self.get_superhero()} found a comment with the body: {comment.body}")
                subreddit_comments.append(comment)
        return subreddit_comments

    def get_user_subreddit_submissions(self, subreddit):
        subreddit_submissions = []
        for submission in self.user.submissions.new(limit=None):
            if submission.subreddit == subreddit:
                if submission.title:
                    print(f"{self.get_superhero()} found a submission with the title: {submission.title}")
                subreddit_submissions.append(submission)
        return subreddit_submissions

    def delete_comments(self, subreddit_comments):
        for subreddit_comment in subreddit_comments:
            print(f"{self.get_superhero()} successfully eliminated the threatening comment!")
            subreddit_comment.delete()
        return True

    def delete_submissions(self, subreddit_submissions):
        for subreddit_submission in subreddit_submissions:
            print(f"{self.get_superhero()} successfully eliminated the forbidding post!")
            subreddit_submission.delete()
        return True
