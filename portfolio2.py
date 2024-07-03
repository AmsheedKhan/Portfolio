import streamlit as st
from streamlit_lottie import st_lottie  # Install streamlit-lottie library: pip install streamlit-lottie

# Lottie Animation for loading screen (Optional)
def show_loader():
  lottie_animation = "https://assets9.lottiefiles.com/packages/lf20_kskFN2.json"  # Replace with your animation URL
  st_lottie(lottie_animation, key="loader", speed=1, loop=True, quality="low")  

# Title and Introduction with animation
st.title("Machine Learning Engineer Portfolio")
with st.spinner("Loading..."):
  st.write("Hi, I'm [Your Name]. I'm a passionate Machine Learning Engineer with [number] years of experience.")
  st.write("This portfolio showcases my skills and projects in the field of Machine Learning.")
st.empty()  # Clear the spinner

# Skills Section with slide-in animation
skills = ["Python", "R", "TensorFlow", "PyTorch", "Scikit-learn", "NumPy", "AWS", "Matplotlib", "Seaborn"]
st.header("Skills")
st.write(", ".join(skills), key="skills")
st.experimental_hide_wiki()  # Hide Streamlit info

# Projects Section with fade-in animation
st.header("Projects")
for i in range(1, 4):  # Adjust the number for your projects
  with st.container():
    st.subheader(f"Project {i}: [Project Title]")
    st.write("A brief description of the problem you aimed to solve.")
    st.write("**Data:** [Describe the data used (source, size, etc.)]")
    st.write("**Methodology:** [Explain the chosen algorithms, models, and techniques.]")
    st.write("**Results:** [Highlight the key achievements and improvements.]")
    st.write("**Challenges:** [Mention any hurdles faced during the project.]")
    # Add a link to your GitHub repository (if applicable)
    st.write("[Link to your GitHub repository](https://github.com/yourusername/project1)")
    # Add visualizations or graphs related to the project (optional)
    st.empty()  # Clear previous content for smooth fade-in

# Education & Certifications Section
st.header("Education & Certifications")
st.write("**[Your Degree]** in [Your Field] from [University Name]")
# Add any relevant certifications

# Contact Section
st.header("Contact")
st.write("Email: [your_email@email.com]")
st.write("LinkedIn: [Link to your LinkedIn profile]")

# Run the Streamlit app
if __name__ == "__main__":
  show_loader()  # Uncomment to show the loading animation
  st.sidebar.title("Navigation")
  st.sidebar.text("Use the sidebar to navigate through the sections.")
  st.sidebar.text("Feel free to explore my projects and skills!")
