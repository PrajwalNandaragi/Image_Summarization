# 🤖 AI Image Reader

A modern, user-friendly web application that uses AI to analyze images and extract text, descriptions, and summaries. Built with Streamlit and powered by Llama3.2-Vision through Ollama.


## ✨ Features

- **🖼️ Image Description**: Detailed AI-powered analysis of visual content
- **🔤 Text Extraction**: OCR-like text recognition from images
- **📝 Smart Summarization**: Key points extraction in bullet format
- **🎨 Modern UI**: Clean, responsive design with gradient styling
- **⚡ Fast Processing**: Real-time AI analysis with loading indicators
- **🏠 Local Processing**: Runs entirely on your local machine for privacy

## 📋 Prerequisites

Before running this application, make sure you have:

- **Python 3.8+** installed on your system
- **Ollama** installed and running locally
- **Llama3.2-Vision model** downloaded and ready

### Step 1: Install Ollama

1. **Download Ollama** from [ollama.ai](https://ollama.ai)
2. **Install the application** following the platform-specific instructions:
   - **Windows**: Download the installer and run it
   - **macOS**: Download the installer or use Homebrew: `brew install ollama`
   - **Linux**: Run the installation script: `curl -fsSL https://ollama.ai/install.sh | sh`

### Step 2: Download the AI Model

After installing Ollama, download the required model:

```bash
ollama pull llava:7b
```

**Note**: This model is approximately 4GB in size, so ensure you have sufficient disk space and a stable internet connection.

### Step 3: Verify Installation

Test that Ollama is working correctly:

```bash
ollama list
```

You should see `llava:7b` in the list of available models.

## 🛠️ Installation & Setup

### Step 1: Download the Project

1. **Clone the repository** (if using Git):
   ```bash
   git clone https://github.com/PrajwalNandaragi/Image_Summarization.git
   cd ai-image-reader
   ```

   **OR** download the project files directly and extract them to a folder.

### Step 2: Install Python Dependencies

1. **Open terminal/command prompt** in the project directory
2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

   **Alternative**: Install packages individually:
   ```bash
   pip install streamlit ollama Pillow
   ```

### Step 3: Start the Application

1. **Make sure Ollama is running** in the background
2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and navigate to `http://localhost:8501`

### Step 4: First Run

- The app will automatically open in your default browser
- If it doesn't open automatically, manually go to `http://localhost:8501`
- You should see the AI Image Reader interface with a beautiful gradient header

## 📦 Dependencies

The project uses the following Python packages:

```
streamlit>=1.28.0
ollama>=0.1.0
Pillow>=9.0.0
```

## 🎯 How to Use

### Quick Start Guide

1. **Launch the App**: Run `streamlit run app.py` and open `http://localhost:8501`
2. **Upload an Image**: 
   - Click the "📤 Choose an image file" button
   - Or drag and drop an image file directly onto the upload area
3. **Supported Formats**: PNG, JPG, JPEG
4. **Wait for Processing**: 
   - The AI will analyze your image (usually takes 10-30 seconds)
   - You'll see a spinner with "🤖 AI is analyzing your image..."
5. **View Results**: Three expandable sections will appear:
   - **🖼️ Image Description**: Detailed visual analysis of what's in the image
   - **🔤 Text Extraction**: All text found in the image (OCR-like functionality)
   - **📝 Text Summarization**: Key points extracted in bullet format

### Tips for Best Results

- **Image Quality**: Use clear, well-lit images for better analysis
- **Text Images**: For text extraction, ensure text is clearly visible and not too small
- **File Size**: Keep images under 10MB for faster processing
- **Format**: PNG and JPG work best for most use cases

## 🏗️ Project Structure

```
ai-image-reader/
├── app.py              # Main Streamlit application
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## 🎨 Features in Detail

### Modern UI Design
- **Gradient Headers**: Beautiful purple-blue gradient styling
- **Card-based Layout**: Clean, organized content sections
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark Theme Headers**: High contrast for better readability
- **Hover Effects**: Interactive elements with smooth transitions

### AI Processing
- **Multiple Analysis Types**: Description, extraction, and summarization
- **Error Handling**: Graceful error messages for failed processing
- **Loading States**: Visual feedback during AI processing
- **Session Management**: Results persist during the session

### Customization
- **Colors**: Modify the CSS variables in the `<style>` section
- **Layout**: Adjust column widths and spacing
- **Prompts**: Customize AI prompts for different analysis types

## 🔧 Running the Application

### Standard Local Run
```bash
streamlit run app.py
```

### Custom Port (if 8501 is busy)
```bash
streamlit run app.py --server.port 8502
```

### Network Access (for other devices on your network)
```bash
streamlit run app.py --server.address 0.0.0.0
```

### Stopping the Application
- Press `Ctrl + C` in the terminal to stop the application
- Close the browser tab when done

## 🙏 Acknowledgments

- **Streamlit** for the amazing web framework
- **Ollama** for providing easy access to AI models
- **Llama3.2-Vision** for powerful image understanding capabilities
- **Pillow** for image processing

## 🐛 Troubleshooting

### Common Issues and Solutions

#### "Connection refused" or "Ollama not found"
- **Solution**: Make sure Ollama is running in the background
- **Check**: Run `ollama list` in terminal to verify Ollama is working
- **Start Ollama**: If not running, start it from your applications or run `ollama serve`

#### "Model not found" error
- **Solution**: Download the required model: `ollama pull llava:7b`
- **Check**: Run `ollama list` to see available models

#### Slow processing or timeouts
- **Solution**: Ensure you have sufficient RAM (8GB+ recommended)
- **Check**: Close other memory-intensive applications
- **Model**: The llava:7b model requires significant resources

#### Streamlit won't start
- **Solution**: Check if port 8501 is already in use
- **Alternative**: Use a different port: `streamlit run app.py --server.port 8502`

#### Image upload issues
- **Solution**: Ensure image is in supported format (PNG, JPG, JPEG)
- **Check**: File size should be under 10MB
- **Browser**: Try refreshing the page or using a different browser


## 💡 Use Cases

This application is perfect for:

- **📄 Document Analysis**: Extract text from scanned documents, receipts, or screenshots
- **📚 Educational Content**: Analyze diagrams, charts, and educational materials
- **🖼️ Image Understanding**: Get detailed descriptions of photos and artwork
- **📋 Data Entry**: Convert image-based text to digital format
- **🔍 Content Research**: Summarize information from images and infographics
- **♿ Accessibility**: Help visually impaired users understand image content

## 🏠 Local Development Benefits

- **🔒 Privacy**: All processing happens on your local machine
- **⚡ Speed**: No internet dependency for AI processing
- **💰 Cost**: No API fees or usage limits
- **🔧 Customization**: Full control over the application and AI models
- **📱 Offline**: Works without internet connection (after initial setup)

---




