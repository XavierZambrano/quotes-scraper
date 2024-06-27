from scrapegraphai.graphs import SmartScraperGraph, ScriptCreatorGraph
from dotenv import load_dotenv
import os
import json


load_dotenv()

graph_config = {
    "llm": {
        "api_key": os.getenv('OPENAI_API_KEY'),
        "model": "gpt-3.5-turbo",
    },
    "verbose": True,
    "library": "beautifulsoup"
}

smart_scraper_graph = ScriptCreatorGraph(
    prompt="Get the quotes.",
    source="https://quotes.toscrape.com/",
    config=graph_config,
)

result = smart_scraper_graph.run()
# print(json.dumps(result, indent=4))
with open('quotes.py', 'w') as f:
    f.write(result)