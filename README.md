# 🤖 JARVIS - AI Voice Assistant

> Your personal AI assistant powered by LiveKit, inspired by Iron Man's JARVIS


## 🌟 Overview

JARVIS is a real-time voice assistant built with Python and LiveKit that can check weather, search the web, and respond to natural language queries. It works both in terminal and via LiveKit Playground for seamless voice interactions.

### ✨ Features

- 🌤️ **Real-time Weather Detection** - Get current weather for any city in Bangladesh
- 🔍 **Web Search** - Search the internet using natural language queries
- 🎙️ **Voice Interaction** - Natural conversation with low-latency responses
- 💻 **Dual Deployment** - Works in terminal and LiveKit Playground
- ⚡ **Fast Response** - Sub-2 second response times
- 🛡️ **Error Handling** - Robust fallback systems for API failures

## 🚀 Demo

[Add your demo video or GIF here]

```
User: "What's the weather in Dhaka?"
JARVIS: "Weather in Dhaka: Clear sky, 28°C, Humidity: 65%, Wind: 12 km/h"

User: "Search for latest AI news"
JARVIS: "Here's what I found: [search results]..."
```

## 🛠️ Tech Stack

- **Python 3.10+** - Core programming language
- **LiveKit** - Real-time voice communication
- **LiveKit Agents** - AI agent framework
- **Open-Meteo API** - Weather data
- **DuckDuckGo** - Web search
- **LangChain** - AI tool integration

## 📋 Prerequisites

- Python 3.10 or higher
- LiveKit account (free tier available)
- Internet connection

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2. Create virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
OPENAI_API_KEY=your_openai_key
```

### 5. Download required files

```bash
python agent.py download-files
```

## 🎮 Usage

### Running in Terminal

```bash
python agent.py dev
```

### Using LiveKit Playground

1. Start the agent:
```bash
python agent.py start
```

2. Visit [LiveKit Agents Playground](https://agents-playground.livekit.io/)

3. Enter your LiveKit credentials

4. Start talking to JARVIS!

## 📁 Project Structure

```
jarvis-voice-assistant/
│
├── agent.py              # Main agent file
├── prompts.py           # AI prompts and instructions
├── tools.py             # Function tools (weather, search)
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── README.md           # This file
└── venv/               # Virtual environment (not in repo)
```

## 🔑 Key Components

### Function Tools

#### Weather Detection
```python
@function_tool()
async def get_weather(context: RunContext, city: str) -> str:
    """Get current weather for any city"""
    # Implementation details
```

#### Web Search
```python
@function_tool()
async def search_web(context: RunContext, query: str) -> str:
    """Search the web using DuckDuckGo"""
    # Implementation details
```

## 🌐 API Endpoints Used

- **Open-Meteo API** - `https://api.open-meteo.com/v1/forecast`
- **DuckDuckGo Search** - Via LangChain integration

## 🎯 Roadmap

- [ ] Email integration for sending/reading emails
- [ ] Calendar management
- [ ] Smart home device control
- [ ] News briefings
- [ ] Multi-language support
- [ ] Custom voice selection
- [ ] Conversation history
- [ ] Mobile app integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LiveKit](https://livekit.io/) - Real-time communication platform
- [Open-Meteo](https://open-meteo.com/) - Free weather API
- [LangChain](https://python.langchain.com/) - AI framework
- Inspired by Marvel's Iron Man JARVIS

## 📧 Contact

Your Name - Shofi Ahmed (frex19shofi@gmail.com)


## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ and lots of ☕ in Bangladesh 🇧🇩**
