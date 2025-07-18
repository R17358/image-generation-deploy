# 🎨 Streamlit Image Generator

This is a simple **Streamlit web app** that generates images using an external image generation API (such as Hugging Face models). The app takes a text prompt, sends it to the API, and displays and saves the generated image locally.

---

## 🚀 Features

* User-friendly Streamlit interface
* Text-to-image generation using API
* Saves generated image with timestamp
* Displays image in app with custom caption

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/streamlit-image-generator.git
cd streamlit-image-generator
```

### 2. Create a `.env` File

Create a `.env` file in the root directory and add your API credentials:

```
API_URL=https://your-api-url.com
API_KEY=your_api_key_here
```

> ⚠️ Ensure the API supports direct image response (e.g., from Hugging Face image models).

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Sample `requirements.txt`:**

```txt
streamlit
requests
python-dotenv
Pillow
opencv-python
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

> Make sure your file is named `app.py` or change the filename accordingly in the command.

---

## 📃 Usage

1. Enter a text prompt in the input box.
2. Click **Generate Image**.
3. View the generated image and its filename.

---

## 🔧 How It Works

* `query(payload)`: Sends the prompt to the API and returns the image bytes.
* `ImageGenerator(prompt)`: Uses the API response to generate and save the image.
* Streamlit displays the generated image and its saved filename.

---

## 📅 Example Prompt

```
a futuristic city at sunset, digital art style
```

---

## 📊 API Requirements

* Must support text-to-image generation
* Must return raw image data in response body
* Accepts JSON payloads in the form:

```json
{
  "inputs": "your prompt here"
}
```

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙋️ Author

Made by Ritesh Pandit. Feel free to contribute or suggest improvements!
