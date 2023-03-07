import os
import openai
import dotenv


def load_openai_key(path):
    dotenv.load_dotenv(path)
    openai.api_key = os.getenv("OPENAI_API_KEY")


def build_message_list(
    component,
    prompt,
    prompt_instructions,
):
    # build and return messageList
    messageList = [
        {
            "role": "system",
            "content": prompt_instructions,
        },
    ]

    iterlen = 2

    for i in range(1, iterlen):
        messageList.append(
            {
                "role": "user",
                "content": open(
                    f"../prompts/landingpage/{component}/input{i}.txt",
                    "r",
                ).read(),
            }
        )
        messageList.append(
            {
                "role": "assistant",
                "content": open(
                    f"../prompts/landingpage/{component}/output{i}.txt",
                    "r",
                ).read(),
            }
        )
    messageList.append({"role": "user", "content": prompt})
    return messageList


# def build_message_list(description):
#     prompt = open(prompt_path, "r").read()

#     # replace variables in prompt
#     for key in variables:
#         prompt = prompt.replace(f"{{{{{key}}}}}", variables[key])

#     # build and return messageList
#     messageList = [
#         {
#             "role": "system",
#             "content": prompt_instructions,
#         },
#     ]

#     iterlen = (
#         len(os.listdir(f"./prompts/landingpage/{variables['COMPONENT']}")) // 2 + 1
#     )

#     for i in range(1, iterlen):
#         messageList.append(
#             {
#                 "role": "user",
#                 "content": open(
#                     f"./prompts/landingpage/{variables['COMPONENT']}/input{i}.txt",
#                     "r",
#                 ).read(),
#             }
#         )
#         messageList.append(
#             {
#                 "role": "assistant",
#                 "content": open(
#                     f"./prompts/landingpage/{variables['COMPONENT']}/output{i}.txt",
#                     "r",
#                 ).read(),
#             }
#         )
#     messageList.append({"role": "user", "content": prompt})
#     return messageList
