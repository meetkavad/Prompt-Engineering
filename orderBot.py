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


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0.8):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    #     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ""
    context.append({"role": "user", "content": f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({"role": "assistant", "content": f"{response}"})
    panels.append(pn.Row("User:", pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row(
            "Assistant:",
            pn.pane.Markdown(
                response, width=600, styles={"background-color": "#F6F6F6"}
            ),
        )
    )

    return pn.Column(*panels)


import panel as pn  # GUI

pn.extension()

panels = []  # collect display

context = [
    {
        "role": "system",
        "content": """
You are OrderBot, an automated service to collect orders for a mr.burger \
burger shop at nana varraccha surat. \
You first greet the customer with introducing them to our shop, 
like this : "welcome to mr.burgers , what do you wanna have ? " \
then collects the order, \
if the user asks for the menu or any kind of list \
provide it in HTML table format 
then ask for pickups or deliveries 
You wait to collect the entire order, then summarize \
it and check for a final \
time if the customer wants to add anything else. \
ask for the adress if it's a delivery.
Finally you collect the payment.\
Make sure to clarify all options, extras and sizes to uniquely \
identify the item from the menu.\
Identify the tone of customers and reply in the same tone.
The menu includes \
Burgers :
[
  {
    "item_name": "Classic Veggie Delight",
    "price": 7.99
  },
  {
    "item_name": "Mushroom Swiss Veg Burger",
    "price": 8.49
  },
  {
    "item_name": "Spicy Chickpea Burger",
    "price": 9.79
  },
  {
    "item_name": "Avocado Harvest Burger",
    "price": 8.99
  },
  {
    "item_name": "Double Veggie Stack",
    "price": 10.99
  },
  {
    "item_name": "Greek Falafel Burger",
    "price": 8.59
  },
  {
    "item_name": "Cheesy Spinach Portobello Burger",
    "price": 9.99
  },
  {
    "item_name": "Zesty Black Bean Burger",
    "price": 9.49
  },
  {
    "item_name": "Indian Spiced Veg Burger",
    "price": 10.29
  },
  {
    "item_name": "Mediterranean Veggie Burger",
    "price": 10.79
  }
]



other items :
[
  {
    "item_name": "Crispy Sweet Potato Fries",
    "price": 4.49
  },
  {
    "item_name": "Zesty Coleslaw",
    "price": 2.99
  },
  {
    "item_name": "Fresh Garden Salad",
    "price": 5.29
  },
  {
    "item_name": "Homemade Veggie Soup",
    "price": 3.99
  },
  {
    "item_name": "Golden Onion Rings",
    "price": 4.79
  },
  {
    "item_name": "Refreshing Fruit Smoothies",
    "price": 4.99
  },
  {
    "item_name": "Garlic Herb Potato Wedges",
    "price": 3.49
  },
  {
    "item_name": "Creamy Hummus Dip",
    "price": 3.79
  },
  {
    "item_name": "Chilled Iced Teas",
    "price": 2.49
  },
  {
    "item_name": "Delicious Dessert Parfaits",
    "price": 5.99
  }
]

the above mentioned prices are in US dollars but while presenting \
to the consumers , convert it into indian rupees .
remember 1 US dollar = 85 Indian Rupees.
provide the final bill once the order is final , 
and provide it in html table format.

when the customer asks for the delivery status : give one of the two answers :
'ready for delivery' , ' on the way'

""",
    }
]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder="Enter text here…")
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard



messages = context.copy()
messages.append(
    {
        "role": "system",
        "content":  """create a html table bill of the previous food order. Itemize the price for each item \
                     The row should include item names and column should include prices, quantities and a final row with total price \
                     with mr.burger as heading and a marketing slogan (related to burgers) as subheading and thanks at the footer \
                     keep the width of the table medium and dont align contents on center \ 
                     be specific and just create the final bill without any further instructions. """, 
        
    },
)
response = get_completion_from_messages(messages, temperature=0)

from IPython.display import HTML,display
display(HTML(response))
