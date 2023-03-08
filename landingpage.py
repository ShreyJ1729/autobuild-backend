import os
import modal
import openai
from fastapi import FastAPI
from pydantic import BaseModel
from utils import load_openai_key, build_message_list, build_messages_from_file

app = FastAPI()
image = modal.Image.debian_slim().pip_install_from_requirements("requirements.txt")
stub = modal.Stub("landingpage-autobuild", image=image)
mounts = [
    modal.Mount.from_local_file("./.env", remote_path="/root/.env"),
    modal.Mount.from_local_file("./utils.py", remote_path="/root/utils.py"),
    modal.Mount.from_local_dir("./prompts", remote_path="/root/prompts"),
]


@stub.webhook(method="GET", mounts=mounts)
def feature_gen(description: str):
    print("feature_gen request received: ", description)

    load_openai_key("./.env")
    messageList = build_messages_from_file(
        path="./prompts/landingpage/feature_gen.json",
        prompt=description,
    )

    print("Built messageList:", messageList)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messageList
    )

    response = completion.choices[0].message.content

    print("feature_gen response:", response)

    return response


@stub.webhook(method="GET", mounts=mounts)
def component_gen(component, description):
    print("component-gen request received: ", description)

    load_openai_key("../.env")
    messageList = build_message_list(
        component=component,
        prompt=description,
        prompt_instructions="You are a helpful React.js component generation bot. Given a description of a component, you generate the code for that component using React and ChakraUI. You only use javascript and never use typescript. You only return the code and nothing else.",
    )

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messageList
    )

    code = completion.choices[0].message.content.rstrip("<<|END|>>")

    return code


def main():
    # req = {
    #     "name": "Supabase",
    #     "description": "an open source Firebase alternative. It offers developers a full Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage to help build their projects quickly and with a focus on their products.",
    # }

    print(
        component_gen(
            "Hero",
            "full-page Hero section with a title and background gradient, all with a purple color scheme.",
        ),
        file=open(f"./Hero.jsx", "w+"),
    )

    print(
        component_gen(
            "Navbar",
            "Navbar section with subnavigation and a dark mode toggle with icons.",
        ),
        file=open(f"./Navbar.jsx", "w+"),
    )

    print(
        component_gen(
            "Footer",
            "Large Footer section with social icons and app store links",
        ),
        file=open(f"./Footer.jsx", "w+"),
    )

    exit()

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


if __name__ == "__main__":
    main()
