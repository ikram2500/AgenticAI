from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from typing import TypedDict, Annotated, Optional  

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#schema 
class Review(TypedDict):
    key_themes: Annotated[list[str], "must write down all the important concept discussed in the review in a list"]
    summary:Annotated[str, "must write down a brief summary of the review"] 
    sentiment: Annotated[str, "must written a sentiment of the review. either positive or negative"]
    pros=Annotated[[list[str]], "write down all the pros inside a list"]
    cons=Annotated[Optional[list[str]], "write down all the cons inside a list"]

structured_model=model.with_structured_output(Review)

prompt = """
Google's Pixel phone have never been the most powerful hundreds. With their Tensor chipsets falling behind rivals in bnchmarks. But surprisingly, the Google Pixel 10 series might be even more compromised than 
the Pixel 9 series, at least when it comes to the GPU (Graphical Processing unit). 

In a post on X, @lafaiel (via Phone Arena) shared a screenshot of a Geekbench listing for the Google Pixel 10 Pro, in which the Pixel 10 Pro achieved a GPU score of just 3,707.
Higher is better here, and for comparison, the Pixel 9 Pro's score is 9,023, while rivals like the Samsung Galaxy S25 Plus and iPhone 16 Pro achieve scores of 26,333 and 33,374
respectively.

So based on this result the Pixel 10 Pro's is way behind, though the fact that it scored even less than its predecessor is especially worryin. 
Performance upgrades in othere areas

Now, GPU performance is only one part of the power picture, and the Pixel 10 Pro should outperform the Pixel 9 Pro on Geekbench overall, with the same source recording a single core recording a single
core score of 2,329 and a multi-core result of 6,358,  for the similarly spec'd Google Pixel 10 Pro XL, compared to 1,948 and 4,530 fir single and multi-core respectively on the 
Pixel 9 Pro.
"""

result = structured_model.invoke(prompt)

print(result)

#new_prompt=f"generate sentiment and summary of the review given. The review is : '{prompt}'"
#result = model.invoke(new_prompt)
#print(result.content)