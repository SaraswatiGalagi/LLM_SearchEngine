# Research Assistant using OpenAI Chat API and Google Custom Search API
import openai
import requests
import sys
import os

# Retrieve API keys from environment variables.
# Replace with your actual keys or set these variables in your system.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "Add your OPEN API KEY")
SEARCH_API_KEY = os.environ.get("SEARCH_API_KEY", "Add your SEARCH OPEN API KEY")
SEARCH_ENGINE_ID = os.environ.get("SEARCH_ENGINE_ID", "Add your SEARCH_ENGINE_ID")

# Validate API keys.
if OPENAI_API_KEY == "your_openai_api_key":
    print("Error: Please set your OPENAI_API_KEY environment variable.")
    sys.exit(1)
if SEARCH_API_KEY == "your_google_search_api_key":
    print("Error: Please set your SEARCH_API_KEY environment variable.")
    sys.exit(1)
if SEARCH_ENGINE_ID == "your_google_search_engine_id":
    print("Error: Please set your SEARCH_ENGINE_ID environment variable.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY

def break_down_question(question):
    """
    Uses OpenAI's gpt-3.5-turbo model to break down a research question
    into 3-5 effective web search queries.
    """
    prompt = (
        f"Break down the following research question into 3-5 effective web search queries:\n\n"
        f"Question: {question}\n\nSearch Queries:"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "system", "content": "You are a helpful assistant specialized in generating precise search queries." },
                { "role": "user", "content": prompt }
            ],
            max_tokens=100,
            temperature=0.5
        )
        # Retrieve and process the response.
        text_response = response['choices'][0]['message']['content'].strip()
        # Split by newline and remove bullet points or numbering.
        queries = [q.strip(" -0123456789.") for q in text_response.split("\n") if q.strip()]
        return queries
    except Exception as e:
        print(f"Error in break_down_question: {e}")
        return []

def perform_search(query):
    """
    Uses Google's Custom Search API to perform a web search based on the provided query.
    Returns a list of results with each result's title, snippet, and URL.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": SEARCH_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": query
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            results = data.get("items", [])
            formatted_results = [
                {
                    "title": item.get("title", "No Title"),
                    "snippet": item.get("snippet", "No Snippet"),
                    "link": item.get("link", "No URL")
                }
                for item in results
            ]
            return formatted_results
        else:
            print(f"Search API error for query '{query}': {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error in perform_search for query '{query}': {e}")
    return []

def synthesize_answer(question, search_results):
    """
    Synthesizes an answer for the research question using the provided search results.
    The answer includes citations in the format [Source X].
    """
    context = ""
    for i, result in enumerate(search_results):
        context += f"Source {i+1}: {result['title']}\n{result['snippet']}\nURL: {result['link']}\n\n"
    
    prompt = (
        f"Using the following sources, answer the question: '{question}'\n\n"
        f"{context}\nAnswer with citations in the format [Source X]."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "system", "content": "You are a knowledgeable research assistant." },
                { "role": "user", "content": prompt }
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error in synthesize_answer: {e}")
        return "Error synthesizing answer."

def main():
    if len(sys.argv) < 2:
        print("Usage: python research_assistant.py \"<your research question>\"")
        sys.exit(1)

    question = sys.argv[1]
    print(f"\n🔍 Research Question: {question}\n")

    # Generate search queries based on the research question.
    queries = break_down_question(question)
    if not queries:
        print("Error: Could not generate search queries from the research question.")
        sys.exit(1)

    print("🔎 Generated Search Queries:")
    for q in queries:
        print(f" - {q}")

    # Fetch search results for each generated query (limiting to top 2 per query).
    all_results = []
    for query in queries:
        results = perform_search(query)
        if results:
            all_results.extend(results[:2])
    
    if not all_results:
        print("\n⚠️ Insufficient information found to answer the question.")
        sys.exit(1)

    # Synthesize and output the answer using the compiled search results.
    answer = synthesize_answer(question, all_results)
    print("\n🧠 Synthesized Answer:\n")
    print(answer)

if __name__ == "__main__":
    main()