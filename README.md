# PleaseMC API
A multipurpose Minecraft api that leverages OpenAI's API.

## 🛠️ Tools
- Command geneator
- Datapack generator
- Chat moderation/translation
- More to come!

## 📋 Requirements
- Python 3.8 or greater
- An OpenAI API key

## 💻 Installation
- Clone the repository
- Rename app/.env.example to app/.env, and fill in the values
- pip install -r requirements.txt

## 🚀 Running on localhost
- ## Linux
    - In the app directory run: gunicorn app:app
- ## Windows (Untested)
    - Install waitress
    - In the app directory run: waitress-serve --port=8000 app:app
    
## 📝 Documentation
- [Docs](docs/index.md)

## 🎉 Featured in these apps
- [Pls](https://github.com/md5sha256/Pls) - A paper plugin

## 🤝 Contributing
- Read [contributing guidelines](CONTRIBUTING.md)

## 📜 License
- [MIT](LICENSE.md)
