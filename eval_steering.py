from model import chat_model

from prompts import ai_steering_prompt

import re
import random

def init_selection_prompt(options):
    prompt = ai_steering_prompt
    
    for i, option in enumerate(options):
        prompt += str(i+1) + ". " + option + "\n"
        
    prompt += "\nReturn only the option number. Note that the option number can only be one of the given options between 1 to 5. The answer cannot be None.\n"
    prompt += "\nOption:"
    return prompt

def extract_choice(response):
    numbers = re.findall(r'\d+', response)
    if numbers:
        return int(numbers[0])
    else:
        return None

def eval_steering_runner(options, eval_steer_counter):
    prompt = init_selection_prompt(options)
    response = chat_model(prompt)
    response = response["choices"][0]["message"]["content"]
    print(response)
    ai_choice = extract_choice(response)
    print(ai_choice)
    if ai_choice == None:
        print('error in selecting generation choice')
        eval_steer_counter += 1
        if eval_steer_counter >= 3:
            ai_choice = random.choice([1, 2, 3, 4, 5])
        else: 
            ai_choice = eval_steering_runner(options, eval_steer_counter) # retry upto 3 times

    return ai_choice 