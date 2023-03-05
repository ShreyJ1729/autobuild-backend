import os
import openai
import dotenv


def load_openai_key():
    dotenv.load_dotenv("./.env")
    openai.api_key = os.getenv("OPENAI_API_KEY")


def build_message_list(variables, prompt_path, prompt_instructions):
    prompt = open(prompt_path, "r").read()

    # replace variables in prompt
    for key in variables:
        prompt = prompt.replace(f"{{{{{key}}}}}", variables[key])

    # build and return messageList
    messageList = [
        {
            "role": "system",
            "content": prompt_instructions,
        },
    ]

    iterlen = (
        len(os.listdir(f"./prompts/landingpage/{variables['COMPONENT']}")) // 2 + 1
    )

    for i in range(1, iterlen):
        messageList.append(
            {
                "role": "user",
                "content": open(
                    f"./prompts/landingpage/{variables['COMPONENT']}/input{i}.txt",
                    "r",
                ).read(),
            }
        )
        messageList.append(
            {
                "role": "assistant",
                "content": open(
                    f"./prompts/landingpage/{variables['COMPONENT']}/output{i}.txt",
                    "r",
                ).read(),
            }
        )
    messageList.append({"role": "user", "content": prompt})
    return messageList


def component_gen(name, description, component_name):
    print("component-gen request received: ", component_name)

    load_openai_key()
    messageList = build_message_list(
        variables={
            "NAME": name,
            "DESCRIPTION": description,
            "COMPONENT": component_name,
        },
        prompt_path="./prompts/landingpage/format.txt",
        prompt_instructions="You are a helpful React.js navbar generation bot. Given a startup idea, you generate the code for the website navbar using React and material-ui. Stop token: <<|END|>>",
    )

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messageList
    )

    code = completion.choices[0].message.content.rstrip("<<|END|>>")

    return code


if __name__ == "__main__":
    req = {
        "name": "Supabase",
        "description": "an open source Firebase alternative. It offers developers a full Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage to help build their projects quickly and with a focus on their products.",
    }

    component_list = [
        "NavBar",
        "Hero",
        "Details",
        "Testimonial",
        "Waitlist",
        "FAQ",
        "Footer",
    ]

    landingpage_code = {}

    for component in component_list:
        try:
            landingpage_code[component] = component_gen(
                req["name"], req["description"], component
            )
        except Exception as e:
            print(f"Failed to generate {component} component")
            print(e)

    # take all the generated code and write to files under landingpage/src
    if not os.path.exists("./landingpage/src"):
        os.system("npx create-react-app landingpage")
    for component in landingpage_code:
        code = landingpage_code[component]
        print(f"Writing {component} component to file")
        print(code, file=open(f"./landingpage/src/{component}.jsx", "w+"))

    # Build App.jsx component from other components
