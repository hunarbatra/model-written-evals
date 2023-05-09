import pandas as pd
import matplotlib.pyplot as plt

df_ada = pd.read_csv('./../results/ada.csv')
df_babbage = pd.read_csv('./../results/babbage.csv')
df_curie = pd.read_csv('./../results/curie.csv')
df_davinci = pd.read_csv('./../results/davinci.csv')

df_text_ada = pd.read_csv('./../results/text-ada-001.csv')
df_text_babbage = pd.read_csv('./../results/text-babbage-001.csv')
df_text_curie = pd.read_csv('./../results/text-curie-001.csv')
df_text_davinci = pd.read_csv('./../results/text-davinci-001.csv')

model_sizes = {
    "ada": 350_000_000,
    "babbage": 1_300_000_000,
    "curie": 6_700_000_000,
    "davinci": 175_000_000_000,
    "text-ada-001": 350_000_000,
    "text-babbage-001": 1_300_000_000,
    "text-curie-001": 6_700_000_000,
    "text-davinci-001": 175_000_000_000,
}

def compute_accuracy(data):
    return data['correct'].sum() / len(data)

accuracy_base, accuracy_feedme = [], []

for i, df_name in enumerate(model_sizes.keys()):
    if i < 4: 
        df = globals()['df_' + df_name]
        accuracy_base.append(compute_accuracy(df))
    else:
        model_name = df_name.split('-')[-2]
        df = globals()['df_text_' + model_name]
        accuracy_feedme.append(compute_accuracy(df))
        
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(list(model_sizes.values())[:4], accuracy_base, marker='o', linestyle='-', color='b', label='Base')
ax.plot(list(model_sizes.values())[4:], accuracy_feedme, marker='o', linestyle='-', color='r', label='FeedMe')

ax.set_xlabel("Model Size")
ax.set_ylabel("Accuracy")
ax.set_title("Accuracy vs. Model Size")

plt.xscale('log')
plt.legend()

plt.savefig('base-vs-feedme.png')