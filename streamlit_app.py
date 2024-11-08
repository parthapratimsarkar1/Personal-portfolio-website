import streamlit as st

# CSS styling
st.markdown("""
    <style>
    body, html {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        background-color: #f3f4f6;
    }

    .container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }

    /* Animations */
    .fade-in {
        opacity: 0;
        animation: fadeIn 1.5s ease-in forwards;
    }

    .slide-in {
        opacity: 0;
        transform: translateY(50px);
        animation: slideIn 1s ease-out forwards;
    }

    .fade-up {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 1.2s ease forwards;
    }

    .image-fade {
        opacity: 0;
        animation: imageFade 1.5s ease forwards;
    }

    /* Keyframes */
    @keyframes fadeIn {
        to {
            opacity: 1;
        }
    }

    @keyframes slideIn {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes imageFade {
        to {
            opacity: 1;
        }
    }

    /* Additional Styling */
    header {
        text-align: center;
        padding: 50px 0;
        background-color: #2c3e50;
        color: #ecf0f1;
    }

    header h1 {
        font-size: 2.5em;
        margin: 0.2em 0;
    }

    header h2 {
        font-size: 1.5em;
        margin: 0.2em 0;
    }

    .image-container {
        position: relative;
        margin-top: 15px;
    }

    #profile-photo {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
    }

    .social-links a {
        color: #3498db;
        margin: 0 10px;
        text-decoration: none;
        transition: color 0.3s;
    }

    .social-links a:hover {
        color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# HTML content
html_content = """
    <header id="home">
        <div class="container">
            <h1 class="fade-in">Partha Pratim Sarkar</h1>
            <h2 class="slide-in">Web Development Intern</h2>
            <div class="image-container">
                <img src="https://via.placeholder.com/150" alt="Profile Photo" id="profile-photo" class="image-fade">
            </div>
            <p class="fade-in">Master of Computer Application | Tezpur Central University</p>
            <div class="social-links fade-in">
                <a href="https://github.com/parthapratimsarkar1" target="_blank">Github</a>
                <a href="https://www.linkedin.com/in/partha-pratim-sarkar-5583a522a/" target="_blank">LinkedIn</a>
            </div>
        </div>
    </header>
"""

# Render HTML in Streamlit
st.markdown(html_content, unsafe_allow_html=True)
