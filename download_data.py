import requests

# English
url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"
with open("the-verdict.txt", "wb") as f:
    f.write(requests.get(url).content)
print("English file downloaded!")