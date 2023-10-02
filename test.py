import g4f


print(g4f.Provider.Ails.params)  # supported args

# Automatic selection of provider
'''
# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}],
    stream=True,
)


for message in response:
    print(message, flush=True, end='')
'''

'''
# normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": question}],
)  # alterative model setting

print(response)

'''
question = input("How can I help you?:")

while (question != "quit()"):
# Set with provider
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.DeepAi,
        messages=[{"role": "user", "content": question}],
        stream=True,
    )

    for message in response:
        print(message)
    question = input("How can I help you?: \n")