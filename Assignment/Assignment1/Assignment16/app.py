from flask import Flask, render_template

app = Flask(__name__)

# In-memory data
comments = [
    {
        "username": "John",
        "comment": "This product is good",
        "likes": 120,
        "flagged": False
    },
    {
        "username": "Amit",
        "comment": "This is a dumb product and stupid design",
        "likes": 50,
        "flagged": True
    },
    {
        "username": "Sara",
        "comment": "Excellent quality!" * 20,
        "likes": 250,
        "flagged": False
    }
]

# Inappropriate words list
bad_words = ["dumb", "stupid"]


@app.route("/comments")
def show_comments():
    processed_comments = []

    for c in comments:
        # 1️⃣ Text Filters
        username_upper = c["username"].upper()
        comment_trimmed = c["comment"].strip()

        # Replace bad words
        for word in bad_words:
            comment_trimmed = comment_trimmed.replace(word, "***")

        processed_comments.append({
            "username": username_upper,
            "comment": comment_trimmed,
            "likes": c["likes"],
            "flagged": c["flagged"]
        })

    # 3️⃣ Statistics
    total_comments = len(processed_comments)
    total_flagged = len([c for c in processed_comments if c["flagged"]])

    most_liked = max(processed_comments, key=lambda x: x["likes"])

    all_usernames = ", ".join([c["username"] for c in processed_comments])

    return render_template(
        "comments.html",
        comments=processed_comments,
        total_comments=total_comments,
        total_flagged=total_flagged,
        most_liked=most_liked,
        all_usernames=all_usernames
    )


if __name__ == "__main__":
    app.run(debug=True)