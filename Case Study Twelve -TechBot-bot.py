'''Start
Create a file named bot.py.
Import spaCy.
Use input function for user input.
Process user input,use advanced NLP techniques.
Provide relevant response.
Base this on NLP analysis.
Load up language model.
Use NLP techniques,extract key user input info.
Analyse the intent and entities in the input.
Generate a relevant response.
End'''

# spaCy has to be imported


import spacy

user_input = ("""Ask TechBot about product specifications, 
              return policies, or shipping details""")

print("TechBot : [Response based on NLP analysis]")


# The below language model has been loaded


nlp = spacy.load('en_core_web_md')

def process_input(user_input):

    doc = nlp(user_input)

    intent = 'product_query' # Placeholder, actual intent analysis needed.

    entities = ['product_specifications', 'return_policy', 'shipping_details']

    return intent, entities


# Below is the analysis  of the intent and entities in the input.


def generate_response(intent, entities):

    if intent == 'product_query':

        if "product_specifications" in entities:
            return "TechBot: Here are the specifications for the requested product."
        
        elif "return_policy" in entities:
            return """ TechBot: We offer standard and express shipping options.
            Delivery usually takes 3-5 business days"""
        
    return "TechBot: I'm sorry, I couldn't understand your request.Please try again"
