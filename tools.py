import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_ai_news():

    query = """Latest AI Agent news, AI autonomous agents, LLM agents, multi-agent systems"""

    response = tavily.search(
        query=query,
        max_results=7
    )

    articles = []

    for item in response["results"]:

        articles.append({
            "title": item["title"],
            "content": item["content"],
            "url": item["url"]
        })

    return articles


def save_newsletter(content):

    os.makedirs(
        "output",
        exist_ok=True
    )

    path = "output/newsletter.md"

    with open(path,"w",encoding="utf-8") as f:
        f.write(content)

    return path