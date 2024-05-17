# MyGitHubAssistant

MyGitHubAssistant is a Python-based application designed to manage various aspects of your GitHub account using Selenium for automation and OpenAI's ChatGPT API for dynamic interactions with the GitHub interface. This tool helps you manage followers, like projects, monitor activity, and gain insights into your repositories.

## Features

- **Follow/Unfollow Users**: Automatically follow or unfollow users based on specified criteria.
- **Like Projects**: Automatically like repositories based on specific criteria, such as most starred or particular topics.
- **Activity Monitor**: Track and report on your GitHub activity.
- **Project Insights**: Analyze and report on the popularity and contributions of your repositories.
- **Dynamic Interaction**: Use ChatGPT API to identify HTML components dynamically, making the automation robust against changes in GitHub's interface.

## Project Structure


```
MyGitHubAssistant/
├── README.md
├── requirements.txt
├── .gitignore
├── config/
│   ├── config.yaml
├── data/
│   └── cookies/
├── docs/
│   ├── architecture.md
│   ├── usage.md
│   └── api.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── github_manager.py
│   ├── chatgpt_api.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── selenium_utils.py
│   │   ├── github_utils.py
│   │   ├── chatgpt_utils.py
│   └── constants.py
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_github_manager.py
│   ├── test_chatgpt_api.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── test_selenium_utils.py
│   │   ├── test_github_utils.py
│   │   ├── test_chatgpt_utils.py
└── scripts/
    ├── setup.py
    ├── start.py
    ├── follow_unfollow.py
    └── like_projects.py
```

## Installation

1. **Clone the repository**:

   git clone https://github.com/yourusername/MyGitHubAssistant.git
   cd MyGitHubAssistant

2. **Create and activate a virtual environment**:

   python3 -m venv venv
   source venv/bin/activate

3. **Install the dependencies**:

   pip install -r requirements.txt

4. **Set up environment variables**:

   Create a `.env` file in the root directory:

   GITHUB_USERNAME=your_github_username

5. **Create the `config.yaml` file** in the `config` directory with your ChatGPT API key:

    github:
      username: YOUR_GITHUB_USERNAME 
    chatgpt:
      api_key: YOUR_CHATGPT_API_KEY

## Usage

1. **Run the application**:

   python src/main.py

2. **Follow/Unfollow Users**:

   Use the `follow_unfollow.py` script to manage followers:

   python scripts/follow_unfollow.py

3. **Like Projects**:

   Use the `like_projects.py` script to like repositories:

   python scripts/like_projects.py

## Configuration

- **config/config.yaml**: Stores configuration settings like ChatGPT API key.
- **.env**: Stores environment variables like GitHub username.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Selenium](https://www.selenium.dev/) for browser automation.
- [OpenAI](https://www.openai.com/) for the ChatGPT API.
- [PyYAML](https://pyyaml.org/) for YAML parsing.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.