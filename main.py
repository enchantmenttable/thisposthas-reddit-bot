import praw
from random import choice
from datetime import datetime

reddit = praw.Reddit(client_id="*****",
                     client_secret="*****",
                     username="*****",
                     password="*****",
                     user_agent="*****")

emoji = ["🌛", "🌜", "🙉", "🐼", "😎", "🤔", "🥺", "🤬", "🤠", "🐥", "💯", "💰"]

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    submission = reddit.submission(id="*****")
    score = submission.score
    ratio = submission.upvote_ratio
    upvotes = round((score * ratio) / (2*ratio - 1)
                    ) if ratio != 0.5 else score * 2
    # why number of upvotes is calculated this way: https://www.reddit.com/r/theydidthemath/comments/43sufi/self_a_formula_to_determine_the_number_of_upvotes/
    downvotes = round(upvotes - score)

    if upvotes > 1:
        upvote_content = "upvotes"
    else:
        upvote_content = "upvote"

    if downvotes > 1:
        downvote_content = "downvotes"
    else:
        downvote_content = "downvote"

    if submission.num_comments > 1:
        comment_content = "comments"
    else:
        comment_content = "comment"

    content = (
        f"{upvotes} {upvote_content}\n\n"
        f"{downvotes} {downvote_content}\n\n"
        f"{submission.num_comments} {comment_content}\n\n"
        f"{choice(emoji)} {choice(emoji)} {choice(emoji)}\n\n"
        f"Current time: {current_time}\n\n"
        "Due to reddit API request rate limit, please wait 3s before refreshing the page.\n\n"
        "The app is hosted on Heroku, which imposes hour limit per month on hosting time. If nothing changes after refreshing the page, we may have to wait until next month..."
    )
    submission.edit(content)
