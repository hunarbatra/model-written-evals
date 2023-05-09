# Model Written Evals for generating Inverse Scaling effect datasets

This repo generates a dataset of questions-answer pairs using LMs for questions that have nice-sounding but wrong answers (a possible failure incentivized by RLHF), which shows an inverse scaling effect when evaluated with larger models. 
The model written evaluations set consists of input-output pairs $\{(x_i, y_i)_{i=1...n\} | x \in Questions, y \in ['Yes', 'No']}$, where $y_1,...,y_n$ are drawn from the finite set of possible answer labels [‘Yes’, ‘No’].

This model written eval set generation involved the following steps:
1. Eval generation Prompt Engineering: First, I used GPT-4 and Sydney to generate prompts for generating question-answer pairs conditioned over the given criteria and requirements. Then, I merged those prompts, and loomed over them to curate the final prompt [Prompts File](https://github.com/hunarbatra/model-written-evals/blob/main/prompts.py)
2. AI Steering to filter and select QA pairs: This eval generation involves prompt-tuning to loom with LMs for sampling multiple completions of the generational dynamics at each timestep, rank those, and select the high ranked completion to steer the model written eval dataset generation with our required criteria ($\prod_{t=1}^N \max_{t,i} AI\_Rank(x_t|y_i,x_{1:t-1})$). AI Steering provides automated scalable oversight for the dataset generation to filter and steer through the most likely question-answer pairs for the given criteria. Dataset generation and steering has been performed using gpt-3.5-turbo with temperature 1.0 for QA pair generation and temperature 0.0 for AI steering. 
![Screenshot 2023-05-08 at 9 44 56 am](https://user-images.githubusercontent.com/35395835/236920823-897edc19-a693-4509-abc9-f8240ff93996.png)
3. Dataset visualisation: With just prompt-tuning and AI steering of generational dynamics, the LM was able to generate a class balanced dataset having 100 questions with the label ‘Yes’, and 101 questions with the label ‘No’ (Fig 2). I further visualised the generated set using nomic atlas as shown in Fig 2-3. (data visualisation can be accessed and explored [here](https://atlas.nomic.ai/map/b97880be-8595-4dc8-b42b-54bdfe2febb2/1599b66f-f57b-41b2-b06a-3fcb0730b6a7) using nomic’s atlas)
![download (3)](https://user-images.githubusercontent.com/35395835/236920840-4cc21609-b492-44a0-803d-43c0037fce6c.png)
![Screenshot 2023-05-09 at 12 59 29 am](https://user-images.githubusercontent.com/35395835/236964480-3df469bd-5375-46b1-89a5-f0a91bfad420.png)
![Screenshot 2023-05-09 at 12 59 55 am](https://user-images.githubusercontent.com/35395835/236920864-7cb40d90-e516-4dc7-be5a-6ce327370562.png)
4. Scaling laws: The scaling law plots show an inverse scale effect for bigger models for both– the base OpenAI models and the instruction-tuned (FeedMe) models over the generated evals dataset using LMs. 
![download (1)](https://user-images.githubusercontent.com/35395835/236920988-899ed73f-4c11-433d-b3d7-3cb2c89a5c09.png)
![download (2)](https://user-images.githubusercontent.com/35395835/236921000-90f9aa0d-4153-4fe6-ac57-34ca221e699a.png)
![logodds-base](https://user-images.githubusercontent.com/35395835/236964495-7e90f423-4652-47ab-b984-6b866a3eba45.png)
![download (4)](https://user-images.githubusercontent.com/35395835/236964502-0bfac6bd-4185-455d-a3df-6f4d0a69ee3c.png)

Code organisation–
```
/dataset
	atlas-data-visualisation.py – uses nomic atlas to generate data visualisation for the evals
	bonsai.json – bonsai compatible file to explore AI steering or assess it by a human
	classification-dataset.csv – classification score eval dataset
	clean.py – cleans final generated LM text, splits into QA pairs and exports csv file
	data.txt – final generated LM text via steering
	logodds-dataset.csv – logodds metric dataset
eval_generation.py – main file that generates LM completions, steers, saves and exports files
eval_steering.py – prompt-tuned steering to selected one of the n samples
model.py – defines models including base model (code-davinci-002) & chat (gpt-3.5-turbo/4)
prompts.py – defines diff. prompts used: main_prompt, system_prompt, ai_steering_prompt
test_config.py – save this as config.py and add your api_keys here
utils.py – basic util operations
bonsai_export.py – generates a bonsai (web version of LOOM) compatible json file
```

Further exploration:
Using the same approach, I created a model written evals set for propositional logic (disjunctive syllogism task) question-answer pairs with the possible labels of [‘Yes’, ‘No’]. Dataset [link](https://docs.google.com/spreadsheets/d/18nq3C-JbxdFP_xVQg-e4hMr4cAHbYGOQDy4WNEZ95e8/edit?usp=sharing). Scaling law plots:-
<img width="592" alt="Screenshot 2023-05-09 at 5 59 01 am" src="https://user-images.githubusercontent.com/35395835/236964584-7dd9145f-1d82-4c6e-ad8c-36bb78503d83.png">


