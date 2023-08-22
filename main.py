import g4f


def generate_gpt4_response(message: str) -> str:
    return g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": message}],
        provider=g4f.Provider.ChatgptAi,
        stream=False
    )


def generate_gpt35_response(message) -> str:
    return g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=[{"role": "user", "content": message}],
        stream=False
    )


if __name__ == '__main__':
    print(g4f.Provider.Ails.params)  # supported args
    msg = input("Ask chatgpt anything: ")
    result = generate_gpt4_response(msg)
    print(result)

