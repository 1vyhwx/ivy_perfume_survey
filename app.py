import streamlit as st

# Set up the page
st.set_page_config(page_title="Ivy's Perfume Customization", page_icon="🌸", layout="centered")

# Soft pastel background color
page_bg_img = '''
<style>
body {
background: linear-gradient(to bottom right, #fce4ec, #e0f7fa);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Cute title
st.title("🎀 Ivy's Dreamy Perfume Customization Survey 🎀")
st.write("Welcome to your personal scent journey 🌸✨")

# Survey Questions
name = st.text_input("💬 What is your name?")

pronouns = st.text_input("💬 What are your pronouns? (she/her, he/him, they/them, etc.)")

gender = st.selectbox("💬 What is your gender?", ["Female", "Male", "Non-binary", "Prefer not to say", "Other"])

age = st.selectbox("💬 What is your age group?", ["Under 18", "18-25", "26-40", "41-60", "Over 60"])

occupation = st.selectbox("💬 What is your occupation?", ["Student", "Working Professional", "Outdoor Worker", "Artist", "Retired", "Other"])

scenario = st.selectbox("💬 When will you wear this perfume?", ["Daily Use", "Special Events", "Romantic Moments", "Relaxation", "Adventure"])

vibe = st.selectbox("💬 Desired Vibe:", [
    "Fresh & Clean", "Subtle & Elegant", "Energetic & Bright",
    "Bold & Glamorous", "Soft & Sweet", "Light & Airy",
    "Cozy & Comforting", "Dreamy & Romantic", "Earthy & Natural",
    "Free-Spirited & Bright"
])

scent_family = st.selectbox("💬 Preferred Scent Family:", [
    "Citrus", "Floral", "Woody", "Fruity", "Sweet", "Aquatic", "Spicy", "Amber"
])

longevity = st.selectbox("💬 Desired Longevity:", [
    "Light (2-4 hours)", "Medium (6-8 hours)", "Strong (10+ hours)"
])

# Submit Button
if st.button("✨ Reveal My Perfume Match ✨"):
    recommendation = "A surprise perfume awaits you! ✨"

    # Matching logic
    if vibe == "Fresh & Clean" and scent_family == "Citrus":
        recommendation = "🍋 Clinique Happy or Marc Jacobs Daisy Eau So Fresh"
    elif vibe == "Dreamy & Romantic" and scent_family == "Floral":
        recommendation = "🌸 Chanel Chance Eau Tendre or Gucci Bloom"
    elif vibe == "Energetic & Bright" and scent_family == "Fruity":
        recommendation = "🍓 Escada Sorbetto Rosso or Hollister Wave"
    elif vibe == "Soft & Sweet" and scent_family == "Sweet":
        recommendation = "🍬 Ariana Grande Cloud or Kayali Vanilla 28"
    elif vibe == "Earthy & Natural" and scent_family == "Woody":
        recommendation = "🌿 Le Labo Another 13 or Jo Malone Wood Sage & Sea Salt"
    elif vibe == "Bold & Glamorous" and scent_family == "Amber":
        recommendation = "🔥 YSL Black Opium or Givenchy L'Interdit"

    # Display the result
    st.markdown(f"""
    <div style="background-color:#ffe4f2;padding:30px;border-radius:15px;">
    <h2 style="color:#ff4081;text-align:center;">🎀 Hi {name or 'Lovely Friend'}! 🎀</h2>
    <h3 style="color:#5d5d5d;text-align:center;">Your perfect perfume match is:</h3>
    <h1 style="color:#ff80ab;text-align:center;">{recommendation}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()  # 🎈 Cute effect when result is shown!