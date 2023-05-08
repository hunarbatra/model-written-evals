from model import base_model, chat_model

from prompts import main_prompt

from eval_steering import eval_steering_runner
from bonsai_export import bonsai_export_runner

from utils import read_file, save_file


data_file = 'dataset/data.txt'

save_file(data_file, main_prompt) # init

generation_data = []
ai_choices = []

for i in range(100):
    print(f'round {i}')
    prompt = read_file(data_file)
    # response = base_model(prompt)
    response = chat_model(prompt, temp=1.0, max_tokens=60, n=5)
    # completion_choices = [n_response["text"] for n_response in response["choices"]]
    completion_choices = [n_response["message"]["content"] for n_response in response["choices"]]
    print(completion_choices)
    generation_data.append(completion_choices)
    ai_choice = eval_steering_runner(completion_choices, 0)
    ai_choices.append(ai_choice-1)
    save_file(data_file, prompt + ' ' + completion_choices[ai_choice-1])
    
bonsai_export_runner(main_prompt, generation_data, ai_choices, 'dataset/bonsai.json')
