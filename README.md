<h1 align="center">🤖 Mehu - Telegram AI Chatbot</h1>

<p align="center">
  <strong>A conversational AI Telegram bot powered by Groq's LLaMA 3.1 model</strong><br>
  Created with <code>aiogram</code>, <code>Groq API</code>, and <code>Python</code>.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This repository contains <strong>Mehu</strong>, an AI chatbot integrated with <strong>Telegram</strong> using the <code>aiogram</code> framework.  
The bot leverages <strong>Groq’s LLaMA 3.1-8B-Instant model</strong> to provide human-like responses and context-aware interactions.  
</p>

<ul>
  <li>💬 <strong>Chatbot</strong>: Engage in natural conversations</li>
  <li>🙏 <strong>Greetings</strong>: Detects Islamic greetings & responds kindly</li>
  <li>🧹 <strong>Clear Context</strong>: Reset the conversation anytime</li>
  <li>⚙️ <strong>Custom Commands</strong>: /start, /help, /clear supported</li>
</ul>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>✅ Built with <code>aiogram</code> for async Telegram bot handling</li>
  <li>⚡ Powered by <code>Groq API</code> (LLaMA 3.1 models)</li>
  <li>📂 Context-aware chat with option to reset</li>
  <li>🌸 Custom greeting detection: "Assalamu Alaikum" → "Wa Alaikum Salam"</li>
</ul>

<hr>

<h2>🧠 How It Works</h2>

<ol>
  <li>User sends a message on Telegram</li>
  <li>The bot checks for greetings or commands</li>
  <li>If none match, it forwards the input to Groq's <code>chat.completions</code> endpoint</li>
  <li>Groq generates a response → Mehu replies instantly</li>
</ol>

<hr>

<h2>📂 Folder Structure</h2>

<pre>
telegram-ai-chatbot-groq/
├── main.py                 ← Main bot script
├── .gitignore              ← .env file here
├── requirements.txt        ← Dependencies
└── README.md               ← Documentation
</pre>

<hr>

<h2>⚙️ Setup Instructions</h2>

<ol>
  <li>Clone the repository</li>
  <pre><code>git clone https://github.com/yourusername/telegram-ai-chatbot-groq</code></pre>

  <li>Install dependencies</li>
  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Set up environment variables (<code>.env</code>)</li>
  <pre><code>
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
GROQ_API_KEY=your-groq-api-key
</code></pre>

  <li>Run the bot</li>
  <pre><code>python bot.py</code></pre>
</ol>

<hr>

<h2>🧪 Commands & Sample Usage</h2>

- **/start**  
  <code>Hi...\nI am Mehu! Created by Mehedi Hassan.\nHow can I assist you?</code>  

- **/help**  
  Displays a list of supported commands  

- **/clear**  
  Clears previous conversation context  

- **Greeting**  
  Input: <code>"Assalamu Alaikum"</code> → Output: <code>"Wa Alaikum Salam! 🌸 I am Mehu..."</code>  

<hr>

<h2>🙌 Credits</h2>

<p>
Created by <strong>Mehedi Hassan</strong> using <code>aiogram</code> and <code>Groq API</code> (LLaMA 3.1).  
Special thanks to Groq for providing fast inference models.
</p>

<hr>

<p align="center">⭐ Star this repo if you enjoy building Telegram AI bots!</p>
