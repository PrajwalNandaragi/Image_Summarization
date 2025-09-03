import streamlit as st
import ollama
from PIL import Image
import base64
import io

# Page configuration
st.set_page_config(
    page_title="AI Image Reader",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
    <style>
    /* Main container styling */
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    /* Header styling */
    .header {
        text-align: center;
        margin-bottom: 3rem;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        color: white;
    }
    
    .header h1 {
        font-size: 3rem;
        margin: 0;
        font-weight: 700;
    }
    
    .header p {
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Upload area styling */
    .upload-container {
        background: #f8f9fa;
        border: 3px dashed #667eea;
        border-radius: 15px;
        padding: 3rem;
        text-align: center;
        margin: 2rem 0;
        transition: all 0.3s ease;
    }
    
    .upload-container:hover {
        border-color: #764ba2;
        background: #f0f2f6;
    }
    
    /* Results container */
    .results-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    /* Expander styling */
    .stExpander {
        background: #f8f9fa !important;
        border: 1px solid #e9ecef !important;
        border-radius: 10px !important;
        margin-bottom: 1rem !important;
    }
    
    .stExpanderHeader {
        background: #2c3e50 !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 10px 10px 0 0 !important;
        padding: 1rem !important;
    }
    
    .stExpanderHeader p {
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }
    
    .stExpanderHeader:hover {
        background: #34495e !important;
    }
    
    /* Content styling */
    .result-content {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        line-height: 1.6;
        color: #2c3e50;
        font-size: 1rem;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "results" not in st.session_state:
    st.session_state.results = None

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 style="color: white; margin-bottom: 1rem;">🤖 AI Image Reader</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    ### 📋 Features
    - **Image Description**: Detailed analysis of visual content
    - **Text Extraction**: OCR-like text recognition
    - **Smart Summarization**: Key points extraction
    
    ### 🎯 How to Use
    1. Upload an image (PNG, JPG, JPEG)
    2. Wait for AI processing
    3. View results in organized sections
    """)

# Main content
st.markdown("""
<div class="header">
    <h1>🤖 AI Image Reader</h1>
    <p>Upload any image and get AI-powered analysis, text extraction, and summarization</p>
</div>
""", unsafe_allow_html=True)

# Upload section
image_input = st.file_uploader(
    "📤 Choose an image file",
    type=["png", "jpg", "jpeg"],
    help="Supported formats: PNG, JPG, JPEG"
)

# Process image if uploaded
if image_input:
    # Display uploaded image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image_input, caption="Uploaded Image", use_container_width=True)
    
    # Convert image to base64
    image = Image.open(image_input)
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Process with AI
    with st.spinner('🤖 AI is analyzing your image...'):
        try:
            # Image Description
            describe = ollama.chat(
                model='llava:7b',
                messages=[{
                    'role': 'user',
                    'content': (
                        "Describe this image in detail. List all visible objects, people, text, and the scene context. "
                        "Be precise and avoid assumptions. Use bullet points if possible."
                    ),
                    'images': [image_base64]
                }]
            )
            
            # Text Extraction
            extract = ollama.chat(
                model='llava:7b',
                messages=[{
                    'role': 'user',
                    'content': (
                        "Extract all visible text from this image as accurately as possible. "
                        "Preserve line breaks and formatting. Return only the extracted text."
                    ),
                    'images': [image_base64]
                }]
            )
            
            # Text Summarization
            summarize = ollama.chat(
                model='llava:7b',
                messages=[{
                    'role': 'user',
                    'content': (
                        "Extract all text from this image, then summarize the main points in 3-4 concise bullet points. "
                        "Focus on the most important information. Return only the bullet points."
                    ),
                    'images': [image_base64]
                }]
            )
            
            # Store results
            st.session_state.results = {
                'describe': describe['message'].content,
                'extract': extract['message'].content,
                'summarize': summarize['message'].content
            }
            
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            st.session_state.results = None
    
    # Display results
    if st.session_state.results:
        st.markdown("""
        <div class="results-container">
            <h2 style="text-align: center; color: #667eea; margin-bottom: 2rem;">🧠 AI Analysis Results</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Image Description
        with st.expander("🖼️ **Image Description**", expanded=True):
            st.markdown(f"""
            <div class="result-content">
                {st.session_state.results['describe']}
            </div>
            """, unsafe_allow_html=True)
        
        # Text Extraction
        with st.expander("🔤 **Text Extraction**", expanded=True):
            st.markdown(f"""
            <div class="result-content">
                {st.session_state.results['extract']}
            </div>
            """, unsafe_allow_html=True)
        
        # Text Summarization
        with st.expander("📝 **Text Summarization**", expanded=True):
            st.markdown(f"""
            <div class="result-content">
                {st.session_state.results['summarize']}
            </div>
            """, unsafe_allow_html=True)

else:
    # Show placeholder when no image is uploaded
    st.markdown("""
    <div style="text-align: center; padding: 4rem 2rem; color: #6c757d;">
        <h3>👆 Upload an image to get started</h3>
        <p>Your image will be analyzed by AI to provide detailed descriptions, text extraction, and summarization</p>
    </div>
    """, unsafe_allow_html=True)