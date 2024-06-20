import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = <openAI_API_key>


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



    info = input("enter the information about the generation : ")

prompt = f"""
you are an instagram account manager of an instagram account that posts facts related to every fields in world .
your final task is to generate a fascinating caption.
here's what you have to do step by step :
1.generate an unfamous, unknown and not historical fun fact based on information or topic inside the triple inverted commas
 '''{info}'''.
(aspect : the aspect of life, info : information related to fact that is needed to be generated)
2.generate a prompt that will be used to generate an image from the image creators availabe online.
the image is related to the fact that generated above.
the image is basically the one i will post on instagram based on the fact that you have given.
3.the final thing , generate a caption based on the fun fact generated using related emojis, the fact should be included in the caption as "Did you know ..." and below that 
there should be hashtages(atleast 10) related to the fact generated and some related to ai such as #artificialintelligence #ai #art #bing #wow_facts_ai etc. 
the fact and the hashtags should be seperated by a line using '-'.
provide the output in json format with keys :
fact,image_generation_prompt, final_caption.
"""

response = get_completion(prompt)
print(response)

text = input("Wanna Generate more related facts? " )
def contains_yes(text):
    return "yes" in text.lower()

if contains_yes(text):
    prompt = f'''generate 3 more facts related to fact in {response}.'''
    response = get_completion(prompt)
    print(response)
