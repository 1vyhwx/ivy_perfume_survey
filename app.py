import streamlit as st

# Set up the page
st.set_page_config(page_title="Ivy's Perfume Customization", page_icon="🌸", layout="centered")

# Soft pastel background
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
gender = st.selectbox("💬 What is your gender?", ["Female", "Male", "Non-binary", "Prefer not to say", "Other"])
age = st.selectbox("💬 What is your age group?", ["A: Under 18", "B: 18-25", "C: 26-40", "D: 41-60", "E: Over 60"])
occupation = st.selectbox("💬 What is your occupation?", ["A: Student", "B: Working Professional", "C: Outdoor Worker", "D: Artist", "E: Retired", "F: Other"])
scenario = st.selectbox("💬 When will you wear this perfume?", ["A: Daily", "B: Special Events", "C: Romantic Moments", "D: Relaxation", "E: Adventure"])

# Vibe based on Scenario
if scenario == 'A: Daily':
    vibe = st.selectbox("💬 Choose a vibe:", ["A: Fresh & Clean", "B: Subtle & Elegant", "C: Energetic & Bright"])
elif scenario == 'B: Special Events':
    vibe = st.selectbox("💬 Choose a vibe:", ["A: Bold & Glamorous", "B: Rich & Mysterious", "C: Luxurious & Warm"])
elif scenario == 'C: Romantic Moments':
    vibe = st.selectbox("💬 Choose a vibe:", ["A: Soft & Sweet", "B: Sensual & Deep", "C: Dreamy & Romantic"])
elif scenario == 'D: Relaxation':
    vibe = st.selectbox("💬 Choose a vibe:", ["A: Light & Airy", "B: Cozy & Comforting", "C: Soft Floral"])
elif scenario == 'E: Adventure':
    vibe = st.selectbox("💬 Choose a vibe:", ["A: Vibrant & Playful", "B: Earthy & Natural", "C: Free-Spirited & Bright"])
else:
    vibe = 'Unknown'

# Scent Family based on Vibe
vibe_mapping = {
    'A': ['Citrus', 'Aquatic', 'Green'],
    'B': ['Woody', 'Spicy', 'Amber'],
    'C': ['Floral', 'Sweet', 'Gourmand']
}

vibe_key = vibe[0] if vibe else 'A'
scent_options = vibe_mapping.get(vibe_key, ['Floral', 'Woody', 'Fruity'])
scent_family = st.selectbox("💬 Choose a scent family:", scent_options)

longevity = st.selectbox("💬 How long do you want the scent to last?", ["A: Light (2-4hrs)", "B: Medium (6-8hrs)", "C: Strong (10+hrs)"])

# Recommendation Button
if st.button("✨ Reveal My Perfume Match ✨"):
    recommendation = "✨ A surprise perfume awaits you! ✨"

    # Matching Logic
    matching_conditions = {
        ('A', 'A', 'A', 'A', 'Citrus'): "🍋 Clinique Happy, Marc Jacobs Daisy Eau So Fresh",
        ('A', 'A', 'B', 'A', 'Floral'): "🌸 Ariana Grande Cloud Pink, Miss Dior Blooming Bouquet",
        ('A', 'A', 'C', 'A', 'Fruity'): "🍓 Escada Candy Love, Victoria's Secret Tease",
        ('A', 'A', 'D', 'A', 'Aquatic'): "🌊 Bath and Body Works Sea Island Cotton, Dolce & Gabbana Light Blue",
        ('A', 'A', 'E', 'A', 'Fruity'): "🍉 Escada Sorbetto Rosso, Hollister Wave for Her",
        ('A', 'A', 'A', 'C', 'Green'): "🌿 Moschino Toy 2 Bubble Gum, Gucci Flora Gorgeous Jasmine",
        ('A', 'A', 'B', 'C', 'Sweet'): "🍬 YSL Mon Paris Eau de Toilette, Vera Wang Princess",
        ('B', 'B', 'B', 'A', 'Amber'): "🔥 YSL Libre Intense, Carolina Herrera Good Girl",
        ('C', 'B', 'A', 'B', 'Woody'): "🌳 Chanel Coco Mademoiselle EDT, Hermès Terre d’Hermès",
        ('B', 'D', 'C', 'C', 'Floral'): "🌸 Maison Margiela Replica Bubble Bath, Chanel Chance Eau Tendre",
        ('E', 'E', 'D', 'B', 'Vanilla'): "🍦 Guerlain Mon Guerlain, Prada L’Homme Intense",
        ('D', 'D', 'E', 'A', 'Fruity'): "🍍 Dolce & Gabbana Dolce Garden, Mancera Holidays",
        ('B', 'B', 'A', 'C', 'Green'): "🌿 Chanel Chance Eau Fraîche, Hermès Un Jardin Sur Le Nil",
        ('C', 'B', 'C', 'B', 'Spicy'): "🔥 Tom Ford Black Orchid, Lancôme La Nuit Trésor"
    }

    key = (age[0], occupation[0], scenario[0], vibe[0], scent_family)

    if key in matching_conditions:
        recommendation = matching_conditions[key]
    else:
        fallback_recommendations = {
            'Floral': "🌸 Chloe Eau de Parfum, Gucci Bloom",
            'Woody': "🌳 Tom Ford Oud Wood, Le Labo Another 13",
            'Citrus': "🍋 Dior Eau Sauvage, Jo Malone Lime Basil & Mandarin",
            'Fruity': "🍓 Escada Cherry in the Air, Ariana Grande Sweet Like Candy",
            'Sweet': "🍬 Kayali Vanilla 28, Viktor & Rolf Bonbon",
            'Amber': "🔥 YSL Black Opium, Givenchy L'Interdit",
            'Aquatic': "🌊 Davidoff Cool Water, Giorgio Armani Acqua di Gioia",
            'Spicy': "🌶️ Viktor & Rolf Spicebomb, Tom Ford Noir Extreme",
            'Green': "🌿 Maison Margiela Replica Under the Lemon Trees"
        }
        recommendation = fallback_recommendations.get(scent_family, "✨ No fallback available ✨")

    # Result Card
    st.markdown(f"""
    <div style="background-color:#ffe4f2;padding:30px;border-radius:15px;">
    <h2 style="color:#ff4081;text-align:center;">🎀 Hi {name or 'Lovely Friend'}! 🎀</h2>
    <h3 style="color:#5d5d5d;text-align:center;">Your perfect perfume match is:</h3>
    <h1 style="color:#ff80ab;text-align:center;">{recommendation}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()  # 🎈 Cute balloons animation
