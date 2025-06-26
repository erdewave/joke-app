
# Joke App 🎭

[![License](https://img.shields.io/badge/license-Unlicense-blue.svg)](LICENSE)

## 📖 About The Project

**Joke App** is a simple, multilingual joke **generator** app that **creates** jokes dynamically using the [JokeAPI v2](https://v2.jokeapi.dev). It’s built purely for fun and does **not** have any commercial purpose.

The app supports both **English** and **Turkish** languages. Users can select joke categories, optionally exclude sensitive topics (such as NSFW, religion, or politics), and choose between **single-line jokes** or **two-part dialogue-style jokes**.

This project was created to experiment with API integration, localization, and Flet-based UI development — and most importantly, to bring smiles to users 😊

**Why this project?**

* Generates fresh jokes tailored to your preferences
* Bilingual support for English and Turkish audiences
* Simple, intuitive, and fun to use
* Created for learning, sharing, and laughter

> "Your time should be focused on creating something amazing. A project that solves a problem and helps others — even if it’s just by making them laugh."

---

## 🚧 Built With

This project was built using the following technologies:

* [Flet](https://flet.dev)
* [DeepL API](https://www.deepl.com)
* [JokeAPI](https://v2.jokeapi.dev)

---

## ⚙️ Getting Started

To get a local copy up and running, follow these simple steps.

### 📋 Prerequisites

Make sure you have the following installed:

* Python 3.8+
* pip

You will also need a [DeepL API key](https://www.deepl.com/pro#developer) for translation.

### 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/erdewave/joke-app.git
cd joke-app
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. The app currently uses my DeepL API key, which allows up to 10,000 characters per month. You can use it freely within this limit, but for uninterrupted usage, it’s recommended to get your own API key from DeepL and replace it in the code.

```python
DEEPL_API_KEY = 'your-api-key-here'
```

4. Run the app:

```bash
python main.py
```

---

## 🚀 Usage

Once the app is running, you can:

* Select your preferred **language** (English or Turkish)
* Choose a **joke category**
* Exclude **sensitive content**
* Pick joke **type**: single-line or two-part

Enjoy freshly generated jokes tailored to your preferences! 😂

---


## 🤝 Contributing

Contributions are what make the open-source community amazing! If you have suggestions, improvements, or bug fixes:

1. Fork the repo
2. Create your branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📄 License

Distributed under the **Unlicense** license. See [`LICENSE`](LICENSE) for more information.

---

## 📬 Contact

[GitHub Profile](https://github.com/erdewave)

[erdemcelik212@icloud.com](mailto:erdemcelik212@icloud.com)

Project Link: [https://github.com/erdewave/joke-app](https://github.com/erdewave/joke-app)

---


## 🙏 Acknowledgments

Here are some resources and tools that helped in building this project:

* [JokeAPI](https://v2.jokeapi.dev)
* [DeepL Translator](https://www.deepl.com)
* [Flet Framework](https://flet.dev)
* [Img Shields](https://shields.io/)
* [GitHub Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet)
