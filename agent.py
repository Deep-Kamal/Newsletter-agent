import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import (
    search_ai_news,
    save_newsletter
)

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    )
)


def ask_llm(prompt):

    result = llm.invoke(
        prompt
    )

    return result.content


# -----------------
# PLAN
# -----------------

def create_plan(goal):

    prompt = f"""You are an AI Newsletter Agent.
    
Goal:
{goal}

Create execution plan.

Steps:
1 Research
2 Summarize
3 Generate
4 Review
5 Publish
"""

    return ask_llm(prompt)


# -----------------
# RESEARCH
# -----------------

def research():

    return search_ai_news()


# -----------------
# SUMMARY
# -----------------

def summarize(articles):

    data = ""

    for a in articles:

        data += f"""
Title:
{a['title']}

Content:
{a['content']}

URL:
{a['url']}
"""

    prompt = f"""
Create concise summary.

Select top 5–7 articles.

{data}
"""

    return ask_llm(prompt)


# -----------------
# NEWSLETTER
# -----------------

def generate_newsletter(summary):

    prompt = f"""
Create markdown newsletter.

Include:

Title

Introduction

Top News

Conclusion

Summary:

{summary}
"""

    return ask_llm(prompt)


# -----------------
# REVIEW
# -----------------

def review(newsletter):

    prompt = f"""
Review this newsletter.

Check:

- readability
- clarity
- missing info
- formatting

Improve it.

Newsletter:

{newsletter}
"""

    return ask_llm(prompt)


# -----------------
# APPROVAL
# -----------------

def approval(mode):

    if mode == "human":

        ans = input(
            "\nApprove newsletter? y/n: "
        )

        return (ans.lower()== "y")

    return True


# -----------------
# MAIN AGENT
# -----------------

def run_newsletter_agent(
    goal,
    mode="auto"
):

    print(
        "\nPlanning..."
    )

    plan = create_plan(
        goal
    )

    print(
        "\nResearching..."
    )

    articles = research()

    print(
        "\nSummarizing..."
    )

    summary = summarize(
        articles
    )

    print(
        "\nWriting..."
    )

    newsletter = (
        generate_newsletter(
            summary
        )
    )

    print(
        "\nReviewing..."
    )

    final_newsletter = (
        review(
            newsletter
        )
    )

    if not approval(
        mode
    ):

        return (
            "Rejected"
        )

    path = (
        save_newsletter(
            final_newsletter
        )
    )

    return {
        "plan": plan,
        "newsletter": final_newsletter,
        "file": path
    }