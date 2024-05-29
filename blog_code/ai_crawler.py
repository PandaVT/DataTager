import requests
from openai import OpenAI

api_key = "sk-xxx"
base_url = "https://xxx/v1"
client = OpenAI(api_key=api_key, base_url=base_url)


# Step 1: Fetch HTML content from a URL
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


# Step 2: Parse content using a large language model
def parse_content_with_model(html_content, model_name="gpt-4o"):
    messages = [{"role": "user", "content": f"Extract titles and links from this HTML: {html_content}"}]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=1500,
        temperature=0.8,
    )
    return response.choices[0].message.content


# Step 3: Process data using a large language model
def process_data_with_model(url, goal, data, model_name="gpt-4o"):
    messages = [{
        "role": "user",
        "content": f"""
                Given the goal to '{goal}', take this list of blog post titles, elements, and links: {data}. 
                Format and structure it into a JSON representation. Ensure each blog post is an object with appropriate keys for title, elements, and links. 
                """
    }]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=1500,
        temperature=0.8,
    )
    return response.choices[0].message.content


# Step 4: Save data to a file
def save_data(data, filename='data.md'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)


if __name__ == "__main__":
    url = 'https://datatager.com/blog'
    goal = "Extract all blog post titles and links"
    html_content = fetch_html(url)
    if html_content:
        parsed_data = parse_content_with_model(html_content)
        processed_data = process_data_with_model(url, goal, parsed_data)
        save_data(processed_data, 'blog_posts.md')
        print("Data has been saved to 'blog_posts.md'。")
