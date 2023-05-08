# read data.txt, clean it and save a csv file

import pandas as pd
import re

data = ''
with open('data-final.txt', 'r') as file:
    for line in file:
        data += line
        
file_content = data.split("The possible class labels for these question-answer pairs are: ['Yes', 'No']. Make sure that the generated pairs are class balanced, and maintain diversity in the dataset.")[-1].strip()

questions_list = []
answers_list = []

# Use regular expressions to extract questions and answers
matches = re.findall(r'Question: (.*?)\nAnswer: (.*?)\n', file_content, re.DOTALL)
    
for match in matches:
    questions_list.append(match[0])
    answers_list.append(match[1])
    
prompts = []
answers_index = []

for q, a in zip(questions_list, answers_list):
    prompt = f"Question: {q} \nAnswer:"
    if prompt in prompts: # check duplicates
        continue 
    prompts.append(prompt)
    if 'Yes' in a:
        answers_index.append(0)
    else:
        answers_index.append(1)
        
classes = [[' Yes', ' No'] for i in range(len(prompts))]

print(answers_index.count(0))
print(answers_index.count(1))

df = pd.DataFrame({'prompt': prompts, 
                   'classes': classes, 
                   'answer_index': answers_index})

df2 = pd.DataFrame({'prompt': prompts,
                    'other_prompt': prompts, 
                   'classes': classes, 
                   'answer_index': answers_index})

df.to_csv('classification-dataset.csv', index=False)
df2.to_csv('logodds-dataset.csv', index=False)


