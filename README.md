# ghostTexter

GhostTexter is an automated, AI-powered WhatsApp auto-responder built with Python. It uses screen coordinates and GUI automation (`pyautogui` and `pydirectinput`) to capture incoming chat messages from WhatsApp Desktop, processes them using Google's **Gemini 3.5 Flash** model along with a custom user persona, and automatically types and sends personalized responses.

---

##  Features

- **GUI Automation**: Uses `pyautogui` and `pydirectinput` for smooth mouse movement, chat text selection, and keyboard shortcuts.
- **AI Persona Mimicry**: Tailor AI replies to match your exact texting style, tone, vocabulary, and background using `profile.txt` and `chat.txt`.
- **Google Gemini Integration**: Built on Google's official `google-genai` SDK (`gemini-3.5-flash` model) with automatic retry handling for API availability.
- **Rich Terminal Interface**: Features progress spinners and status panels powered by the `rich` library.
- **Custom Coordinate Mapping**: Easy setup helper script to inspect mouse position and adapt to any display resolution.

---

##  Repository Structure

```text
ghostTexter/
├── main.py          # Main execution script (GUI automation & Gemini AI integration)
├── profile.txt      # Persona definition, texting rules, and user context
├── chat.txt         # Few-shot example chat conversations for style matching
├── setup.txt        # Helper script to find screen coordinates for WhatsApp UI
├── .env             # Environment variables (API keys & WhatsApp launcher command)
├── .gitignore       # Git ignore rules for virtual environments, cache, and secrets
└── README.md        # Project documentation
```

---

## 📋 Prerequisites

- **Operating System**: Windows (configured for Windows command execution and standard shortcuts).
- **Python**: Python 3.8 or higher.
- **WhatsApp**: WhatsApp Desktop app or WhatsApp Web running on screen.
- **Google Gemini API Key**: An active API key from [Google AI Studio](https://aistudio.google.com/).

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd ghostTexter
   ```

2. **Install dependencies**:
   ```bash
   pip install pydirectinput pyautogui pyperclip python-dotenv google-genai rich
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   WHATSAPP_START=start whatsapp:
   ```

---

## 🔧 Configuration & Coordinate Setup

GhostTexter interacts with WhatsApp using screen coordinates. Because display resolutions vary, you need to map out the exact pixel coordinates for your setup.

### 1. Find Screen Coordinates
Run the helper script snippet in `setup.txt` to display your mouse cursor coordinates in real-time:

```python
import pyautogui

while True:
    pos = pyautogui.position()
    print(pos)
```

Hover your mouse over the following elements on your screen and note their `(X, Y)` coordinates:
1. **First Chat**: Location of the target chat in the left list.
2. **Chat Start**: Top-left corner of the message history area to start text selection.
3. **Chat End**: Bottom-right corner of the message history area to end text selection.
4. **Input Box**: WhatsApp message input text area.
5. **Send Button**: Send button location.

### 2. Update `main.py`
Open `main.py` and update the coordinate constants with your measured values:

```python
FIRST_CHAT = (X1, Y1)
CHAT_START = (X2, Y2)
CHAT_END   = (X3, Y3)
INPUT_BOX  = (X4, Y4)   
SEND_BUTTON = (1868, 968)
```

### 3. Customize Personality & Style
- **`profile.txt`**: Define your persona, role, texting rules (e.g. Hinglish mix, sentence brevity, emoji limits), and facts about yourself.
- **`chat.txt`**: Provide example message exchanges to give the AI context on how you typically format and respond to texts.

---

## 🚀 Usage

1. Open WhatsApp Desktop or Web on your screen.
2. Run `main.py`:
   ```bash
   python main.py
   ```
3. **Do not move your mouse** while the script is running. GhostTexter will:
   - Open/focus WhatsApp via `WHATSAPP_START`.
   - Click the chat item and drag-select the recent messages.
   - Copy the chat text to the clipboard.
   - Generate a reply using Gemini AI.
   - Paste the reply into the input box and click Send.

---

## ⚠️ Disclaimer

- This application performs automated mouse clicks and keystrokes. Avoid manual mouse/keyboard interaction while the script executes.
- Use responsibly and in accordance with WhatsApp's Terms of Service.
