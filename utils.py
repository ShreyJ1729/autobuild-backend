import os
import json
import openai
import dotenv


def load_openai_key(path):
    dotenv.load_dotenv(path)
    openai.api_key = os.getenv("OPENAI_API_KEY")


def get_component_types(path):
    return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


def build_messages_from_file(path, prompt):
    messages = json.load(open(path, "r"))
    messages.append({"role": "user", "content": prompt})
    return messages


def build_messages_from_dir(prompt_path, data_path, prompt):
    messages = json.load(open(prompt_path, "r"))

    for i in range(1, len(os.listdir(data_path)) // 2 + 1):
        # read input/output files, removing all indents to significantly reduce token count
        inputContent = (
            open(os.path.join(data_path, f"input{i}.txt"), "r")
            .read()
            .replace(" " * 4, "")
        )
        outputContent = (
            open(os.path.join(data_path, f"output{i}.txt"), "r")
            .read()
            .replace(" " * 4, "")
        )

        messages.extend(
            [
                {
                    "role": "user",
                    "content": inputContent,
                },
                {
                    "role": "assistant",
                    "content": outputContent,
                },
            ]
        )

    messages.append({"role": "user", "content": prompt})
    return messages
