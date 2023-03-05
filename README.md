# autobuild-backend

Fully autonomous code-generation

### Development tips

#### Creating a venv with required packages

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Each time you want to run code here you need to activate the venv, VsCode will do this for you automatically if you have the Python extension installed.

```bash
source venv/bin/activate
```

#### OpenAI key setup

Create a file called `.env` in the root of the project with the following contents:

```bash
OPENAI_API_KEY=<your key>
```

#### Dealing with modal labs

`modal serve <filename>` will start a dev run of the file, and will automatically re-run the file when it changes.
This run is only alive for the duration of the command, but the server is not local, so you can access it from anywhere.

`modal deploy <filename>` will deploy the file to the modal server, converting each webhook, function, or endpoint into a modal endpoint and give you a URL for each.
