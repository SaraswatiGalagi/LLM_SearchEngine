# LLM_SearchEngine

Research Assistant using OpenAI Chat API and Google Custom Search API
=======================================================================

Description:
------------
This command‐line research assistant takes a user’s research question, uses 
OpenAI’s GPT-3.5-turbo model to break the question into effective search queries, 
and then retrieves web results using the Google Custom Search API. Finally, it 
synthesizes an answer by combining the search results and appends source citations.

Features:
- Automatically generates search queries from your research question.
- Uses Google Custom Search to gather relevant titles, snippets, and URLs.
- Synthesizes a coherent answer with in-text citations ([Source X]).
- Outputs both the synthesized answer and the list of source URLs.

Requirements:
-------------
• Python 3.7 or later  
• Required Python libraries:
  - openai
  - requests
  - google-api-python-client

Installation:
-------------
1. **Clone/Download the Script:**
   Download the file `research_assistant_OpenAI.py` to your local machine.

2. **Install the Required Packages:**
   Open a terminal (or command prompt) and run the following command:
   
       pip install openai requests google-api-python-client

3. **Set Up API Keys:**
   This script uses two APIs:
   
   a) **OpenAI API:**
      - Sign up at https://platform.openai.com/ if you haven’t already.
      - Generate your API key.
      
   b) **Google Custom Search API:**
      - Obtain your API key from the Google Developers Console.
      - Create a Custom Search Engine (CSE) and obtain your SEARCH_ENGINE_ID.
   
   **Setting Your API Keys in Environment Variables:**
   For Unix/Linux/Mac, in your terminal execute:
   
       export OPENAI_API_KEY="your_openai_api_key"
       export SEARCH_API_KEY="your_google_search_api_key"
       export SEARCH_ENGINE_ID="your_google_search_engine_id"
   
   For Windows, use:
   
       set OPENAI_API_KEY="your_openai_api_key"
       set SEARCH_API_KEY="your_google_search_api_key"
       set SEARCH_ENGINE_ID="your_google_search_engine_id"

Usage:
------
Run the script from the command line by providing your research question as
an argument. For example:

    python research_assistant.py "What are the benefits of meditation?"

The script will output:
   - Your original research question.
   - The generated search queries.
   - A synthesized answer with source citations in the format [Source X].

Troubleshooting:
----------------
• **Missing or Invalid API Keys:**
  Ensure that the environment variables (OPENAI_API_KEY, SEARCH_API_KEY, SEARCH_ENGINE_ID) are correctly set. If any key is missing or set to its placeholder value, the script will display an error and exit.

• **Google Custom Search API Errors:**
  If you see errors related to the search API (e.g., quota exceeded or incorrect SEARCH_ENGINE_ID), verify your API credentials and ensure that your CSE is correctly configured.

• **OpenAI API Errors:**
  If errors occur when making calls to the OpenAI API, check your API key, billing status, and API usage limits on the OpenAI dashboard.

Security Note:
--------------
Your API keys are sensitive. Do not commit them to public repositories. It is recommended 
to use environment variables (or secure configuration management) to safeguard your keys.

License:
--------
[Include license information here if applicable.]



