# Twitter Bot

This repository contains the code for a Twitter bot that monitors Twitter for specific activities based on certain criteria. The bot is currently set up to fetch recent accounts but can be easily extended to include additional functionalities.

## Features

- Fetch recent Twitter accounts based on configurable parameters.

(Note: More features like searching by keywords, interacting with tweets, or filtering based on bio can be envisioned for future updates.)

## Getting Started

These instructions will guide you through the setup and deployment of your own instance of the Twitter bot for development and testing purposes.

### Prerequisites

You need to have the following installed on your system:

- Python 3.6 or higher
- Virtual environment (recommended)

Additionally, you'll need:

- A Twitter Developer account
- API keys and access tokens from Twitter

### Installation

To get your development environment running:

1. Clone the repo:
   ```sh
   git clone https://github.com/stafamu/twitter-bot
2. Navigate to the cloned directory:
   ```sh
   cd twitter-bot
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt


### Configuration

Configure your bot by setting the appropriate environment variables in the .env file and adjusting any parameters in config.py.

### Running the bot

Execute the bot using:

```sh
python main.py
```

This will start the bot using the parameters defined in your configuration.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

Tweepy Library
Twitter API

