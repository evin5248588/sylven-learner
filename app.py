"""
Sylven Language Learner — Streamlit Web App
Run with: streamlit run app.py
"""

import streamlit as st
import random

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sylven Language Learner",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;700&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0d1117;
    color: #e6edf3;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161b22;
    border-right: 1px solid #30363d;
}
section[data-testid="stSidebar"] .stRadio label {
    color: #e6edf3 !important;
    font-size: 15px;
}

/* Main area */
.main .block-container { padding-top: 2rem; }

/* Title */
h1 { font-family: 'EB Garamond', serif !important; color: #58a6ff !important; }
h2, h3 { font-family: 'EB Garamond', serif !important; color: #d4a017 !important; }

/* Card */
.sylven-card {
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 40px 30px;
    text-align: center;
    margin: 16px 0;
}
.sylven-word {
    font-family: 'EB Garamond', serif;
    font-size: 2.6rem;
    color: #e6edf3;
    margin-bottom: 6px;
}
.sylven-answer {
    font-family: 'EB Garamond', serif;
    font-size: 2.2rem;
    color: #d4a017;
}
.sylven-pos {
    color: #8b949e;
    font-size: 0.85rem;
    margin-top: 4px;
}
.hint-text {
    color: #8b949e;
    font-size: 0.82rem;
    margin-top: 10px;
}

/* Score badge */
.score-badge {
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 10px 18px;
    text-align: center;
    font-size: 0.9rem;
    color: #8b949e;
}
.score-badge span { color: #58a6ff; font-weight: bold; font-size: 1.1rem; }

/* Quiz buttons */
.stButton > button {
    width: 100%;
    background-color: #21262d;
    color: #e6edf3;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 12px;
    font-size: 15px;
    transition: all 0.15s;
}
.stButton > button:hover {
    border-color: #58a6ff;
    color: #58a6ff;
}

/* Result boxes */
.result-correct {
    background: #1a3a2a;
    border: 1px solid #3fb950;
    border-radius: 8px;
    padding: 14px;
    color: #3fb950;
    font-weight: bold;
    text-align: center;
    font-size: 1.1rem;
}
.result-wrong {
    background: #3a1a1a;
    border: 1px solid #f85149;
    border-radius: 8px;
    padding: 14px;
    color: #f85149;
    font-weight: bold;
    text-align: center;
    font-size: 1.1rem;
}

/* Sentence cards */
.sentence-card {
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 16px 20px;
    margin: 8px 0;
}
.sentence-sylven {
    font-family: 'EB Garamond', serif;
    font-size: 1.25rem;
    color: #d4a017;
}
.sentence-english { color: #e6edf3; margin-top: 4px; font-size: 0.95rem; }

/* Grammar cards */
.grammar-card {
    background: #21262d;
    border-left: 3px solid #58a6ff;
    border-radius: 0 10px 10px 0;
    padding: 16px 20px;
    margin: 10px 0;
}
.grammar-title { color: #58a6ff; font-weight: bold; font-size: 1rem; margin-bottom: 6px; }
.grammar-body { color: #e6edf3; font-family: monospace; font-size: 0.88rem; white-space: pre-wrap; }

/* Progress bar override */
.stProgress > div > div { background-color: #58a6ff; }

/* Input */
.stTextInput > div > div > input {
    background-color: #21262d !important;
    color: #e6edf3 !important;
    border: 1px solid #30363d !important;
    border-radius: 8px !important;
}

/* Table */
.stDataFrame { border: 1px solid #30363d; border-radius: 8px; }

div[data-testid="stMetricValue"] { color: #58a6ff !important; }
</style>
""", unsafe_allow_html=True)

# ── VOCABULARY ───────────────────────────────────────────────────────────────
VOCABULARY = [
    ("kxïralen","god / deity","noun"),("havan","home","noun"),("melen","grace","noun"),
    ("tsäva","life","noun"),("radan","path","noun"),("rynä","person","noun"),
    ("txevol","world","noun"),("huna","water","noun"),("fìrax","fire","noun"),
    ("sewa","wind / air","noun"),("koral","stone","noun"),("syelva","tree","noun"),
    ("rìuva","sun","noun"),("tsölun","moon","noun"),("estran","star","noun"),
    ("vorak","mountain","noun"),("hunara","river","noun"),
    ("oyu","I / me","pronoun"),("tiyä","you (singular)","pronoun"),
    ("e","he / she / it","pronoun"),("syi","we / us","pronoun"),
    ("enu","they / them","pronoun"),("oyun","my / mine","pronoun"),
    ("tiyän","your","pronoun"),("enun","their","pronoun"),
    ("shi","this / that","pronoun"),("oni","all","determiner"),
    ("ten","each / every","determiner"),
    ("esa","to be / exist","verb"),("melen","to bless","verb"),
    ("hivan","to live","verb"),("virak","to walk","verb"),("salan","to run","verb"),
    ("alon","to see","verb"),("lithan","to speak / pray","verb"),
    ("solan","to protect / guard","verb"),("novak","to create","verb"),
    ("suan","to give","verb"),("amrá","to love","verb"),
    ("tanan","to know / learn","verb"),("miran","to think","verb"),
    ("soman","to sleep","verb"),("drimak","to dream","verb"),
    ("Bona","good","adjective"),("Mala","bad / evil / black","adjective"),
    ("Maha","big / great","adjective"),("Tini","small","adjective"),
    ("Lysa","bright","adjective"),("Mure","dark","adjective"),
    ("Vara","strong","adjective"),("Tera","weak","adjective"),
    ("Nova","new","adjective"),("Veta","old","adjective"),
    ("Shiva","holy","adjective"),("Mora","cursed","adjective"),
    ("Pure","clear","adjective"),("Dera","hidden","adjective"),
    ("E","and","conjunction"),("Su","with","preposition"),
    ("O","in / on / at","preposition"),("Qa","to / toward","preposition"),
    ("Fra","from","preposition"),("Tre","through","preposition"),
    ("De","of / belonging to","preposition"),("Rada","because","conjunction"),
    ("Svi","if","conjunction"),("Ni","or","conjunction"),
    ("Nua","now","adverb"),("Rena","then","adverb"),("Cura","soon","adverb"),
    ("Oniqa","always","adverb"),("Malaqa","never","adverb"),
    ("Ráven","far","adverb"),("Tenna","near","adverb"),
    ("Een","one","number"),("Dua","two","number"),("Tre","three","number"),
    ("Kua","four","number"),("Penta","five","number"),("Sexa","six","number"),
    ("Seta","seven","number"),("Okta","eight","number"),
    ("Novae","nine","number"),("Dekka","ten","number"),
    ("Aurosa","dawn","noun"),("Krepsa","dusk","noun"),("Tonra","thunder","noun"),
    ("Flusmara","tide","noun"),("Nebra","mist / fog","noun"),
    ("Arkopluna","rainbow","noun"),("Eklipsa","eclipse","noun"),
    ("Pyravora","volcano","noun"),("Terramota","earthquake","noun"),
    ("Spaltera","canyon","noun"),("Estravola","comet","noun"),
    ("Estragruppa","constellation","noun"),("Finlina","horizon","noun"),
    ("Abissa","abyss","noun"),("Gelmonta","glacier","noun"),
    ("Paludra","swamp","noun"),("Insula","island","noun"),("Krupta","cliff","noun"),
    ("Kapra","head","noun"),("Fasia","face","noun"),("Boka","mouth","noun"),
    ("Lingua","tongue","noun"),("Denta","tooth","noun"),("Aura","ear","noun"),
    ("Nasa","nose","noun"),("Kola","neck","noun"),("Skapra","shoulder","noun"),
    ("Brakja","arm","noun"),("Digita","finger","noun"),("Krusa","leg","noun"),
    ("Peda","foot","noun"),("Sangra","blood","noun"),("Osta","bone","noun"),
    ("Pela","skin","noun"),("Spirita","breath","noun"),("Lakrim","tear (crying)","noun"),
    ("Sudora","sweat","noun"),("Voksa","voice","noun"),
    ("Lorna","wolf","noun"),("Fela","cat","noun"),("Vira","bird","noun"),
    ("Draka","dragon","noun"),("Sela","fish","noun"),("Fruna","frog","noun"),
    ("Hira","horse","noun"),("Mura","mouse","noun"),("Vapa","snake","noun"),
    ("Moojoomeh","cow","noun"),
    ("Rava","red","adjective"),("Vana","green","adjective"),
    ("Sila","blue","adjective"),("Kora","gray / stone-gray","adjective"),
    ("Kupa","cup","noun"),("Vasa","vase","noun"),("Lampa","lamp","noun"),
    ("Kloka","clock","noun"),("Fenstra","window","noun"),("Porta","door","noun"),
    ("Kasa","house","noun"),("Karta","map","noun"),("Tablara","table","noun"),
    ("Stola","chair","noun"),("Penka","pen","noun"),("Libara","book","noun"),
    ("Brelka","bottle","noun"),("Dabra","hammer","noun"),("Kresta","knife","noun"),
    ("Vena","hope","noun"),("Sura","calm","adjective"),("Vika","shy","adjective"),
    ("Fira","anger","noun"),("Trista","sadness","noun"),("Sora","joy","noun"),
    ("Familia","family","noun"),("Triba","tribe","noun"),("Klana","clan","noun"),
    ("Nasiona","nation","noun"),("Regnara","kingdom","noun"),("Impera","empire","noun"),
    ("Sakora","priest","noun"),("Batora","warrior","noun"),
    ("Solasora","guardian","noun"),("Merkara","merchant","noun"),
    ("Artisa","craftsman","noun"),("Servora","servant","noun"),
    ("Magistra","master","noun"),("Senora","elder","noun"),
    ("Konsila","council","noun"),("Throna","throne","noun"),
    ("Korona","crown","noun"),("Leksara","law","noun"),
    ("Festara","festival","noun"),("Matrara","marriage","noun"),
    ("Juramenta","oath","noun"),
    ("Fatuma","destiny","noun"),("Eternita","eternity","noun"),
    ("Infinora","infinity","noun"),("Mistara","mystery","noun"),
    ("Mirakla","miracle","noun"),("Profeza","prophecy","noun"),
    ("Revelara","revelation","noun"),("Sakrifa","sacrifice","noun"),
    ("Paktura","covenant","noun"),("Redemsa","redemption","noun"),
    ("Transmuta","transformation","noun"),("Lumensa","enlightenment","noun"),
    ("Peregrina","pilgrimage","noun"),("Meditara","meditation","noun"),
    ("Ritara","ritual","noun"),("Benedikta","blessing","noun"),
    ("Judikara","judgment","noun"),("Miserka","mercy","noun"),
    ("Justara","justice","noun"),("Vengara","vengeance","noun"),
    ("Pardonara","forgiveness","noun"),("Temptara","temptation","noun"),
    ("Virtara","virtue","noun"),("Pekara","sin","noun"),("Salvara","salvation","noun"),
    ("Esensa","essence","noun"),("Realita","reality","noun"),
    ("Haramacrua","harmony","noun"),("Distakatoo","discord","noun"),
    ("Balansa","balance","noun"),("Kaossa","chaos","noun"),
    ("Yxah","order","noun"),("Vakuma","void","noun"),("Unita","unity","noun"),
    ("Dualita","duality","noun"),("Transenda","transcendence","noun"),
    ("Imanensa","immanence","noun"),
    ("Asendera","to ascend","verb"),("Desendera","to descend","verb"),
    ("Konselara","to conceal","verb"),("Manifesta","to manifest","verb"),
    ("Invoka","to invoke","verb"),("Banisha","to banish","verb"),
    ("Komunara","to commune","verb"),("Jornara","to journey","verb"),
    ("Vagara","to wander","verb"),("Habitara","to dwell","verb"),
    ("Gathera","to gather","verb"),("Unitra","to unite","verb"),
    ("Dividara","to divide","verb"),("Ligara","to bind","verb"),
    ("Liberara","to release","verb"),("Sumara","to summon","verb"),
    ("Enkanta","to enchant","verb"),("Dispela","to dispel","verb"),
    ("Vekara","to awaken","verb"),("Slumbara","to slumber","verb"),
    ("Kontempla","to contemplate","verb"),
]

SAMPLE_SENTENCES = [
    ("Hivan oyu o havan.", "I live in a home."),
    ("Amara vi ti.", "I love you."),
    ("Alon vi.", "I see."),
    ("Hyva bona.", "Life is good."),
    ("Solas vi o lys.", "Protect me in the light."),
    ("Litha vi o shivalen.", "Speak me to God."),
    ("Mala terra, bona lys.", "Dark earth, bright light."),
    ("Tana shi melen hyva.", "We know the grace of life."),
    ("Nova shivalen terra.", "God created the world."),
    ("Solasa shivalen en.", "God protects them."),
]

GRAMMAR_NOTES = [
    ("Word Order", "Sylven uses Verb–Subject–Object (VSO) order by default.\nExample: Hivan oyu o havan. → 'live I in home' = 'I live in a home.'"),
    ("Plural", "Add -ni to make a noun plural.\nExample: kxïralen → kxïralenni (gods)\n         txevol → txevolni (worlds)"),
    ("Past Tense", "Insert ‹ìm› before the stressed vowel.\nExample: hivan (live) → hìmivan (lived)"),
    ("Future Tense", "Insert ‹ay› before the stressed vowel.\nExample: hivan (live) → hayivan (will live)"),
    ("Adjectives", "Adjectives follow the noun they describe.\nExample: Txevol mahrä = 'great world' (lit: world great)"),
    ("Questions", "Use rising tone + particles:\nQa? = What?    Oa? = Where?"),
    ("Cases (optional)", "Agent: -ku  |  Patient: -ti  |  Goal: -ru\nThese are optional; prepositions can substitute."),
    ("Possessives", "Add a nasal ending to pronouns:\noyu (I) → oyun (my/mine)\ntiyä (you) → tiyän (your)"),
    ("Evidentiality", "za = I witnessed it\nsu = I infer\nke = I heard\nsha = divine truth\nPlace particle after the verb."),
    ("Honorifics", "Ti = intimate\nVos = respectful\nTheon = to deity\nRex = to royalty"),
]

# ── SESSION STATE INIT ───────────────────────────────────────────────────────
def init_state():
    defaults = {
        "score_correct": 0,
        "score_total": 0,
        "fc_index": 0,
        "fc_flipped": False,
        "fc_deck": random.sample(VOCABULARY, len(VOCABULARY)),
        "fc_direction": "Sylven → English",
        "quiz_word": None,
        "quiz_choices": [],
        "quiz_answered": False,
        "quiz_chosen": None,
        "quiz_direction": "Sylven → English",
        "quiz_filter": "All",
        "trans_word": None,
        "trans_direction": "Sylven → English",
        "trans_checked": False,
        "trans_result": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ✦ SYLVEN")
    st.markdown("<span style='color:#8b949e;font-size:0.85rem'>Language Learner</span>", unsafe_allow_html=True)
    st.divider()
    page = st.radio("Navigate", ["🃏 Flashcards", "🎯 Quiz", "✍️ Translation",
                                  "📖 Sentences", "📚 Grammar", "📋 Full Vocab"])
    st.divider()
    correct = st.session_state.score_correct
    total = st.session_state.score_total
    pct = int(correct / total * 100) if total else 0
    st.markdown(f"""
    <div class='score-badge'>
        Score<br>
        <span>{correct} / {total}</span>
        {'&nbsp;&nbsp;' + str(pct) + '%' if total else ''}
    </div>
    """, unsafe_allow_html=True)
    if total > 0:
        st.progress(pct / 100)
    if st.button("Reset Score"):
        st.session_state.score_correct = 0
        st.session_state.score_total = 0
        st.rerun()

# ── HELPERS ──────────────────────────────────────────────────────────────────
def record(correct):
    st.session_state.score_total += 1
    if correct:
        st.session_state.score_correct += 1

def new_quiz_question():
    pos_filter = st.session_state.quiz_filter
    pool = [v for v in VOCABULARY if pos_filter == "All" or v[2] == pos_filter]
    if len(pool) < 4:
        return
    correct = random.choice(pool)
    wrongs = random.sample([v for v in pool if v != correct], 3)
    choices = [correct] + wrongs
    random.shuffle(choices)
    st.session_state.quiz_word = correct
    st.session_state.quiz_choices = choices
    st.session_state.quiz_answered = False
    st.session_state.quiz_chosen = None

def new_trans_word():
    st.session_state.trans_word = random.choice(VOCABULARY)
    st.session_state.trans_checked = False
    st.session_state.trans_result = None

# ── PAGES ─────────────────────────────────────────────────────────────────────

# ── FLASHCARDS ────────────────────────────────────────────────────────────────
if page == "🃏 Flashcards":
    st.title("🃏 Flashcards")
    st.caption(f"{len(VOCABULARY)} cards in deck")

    col1, col2 = st.columns(2)
    with col1:
        direction = st.radio("Direction", ["Sylven → English", "English → Sylven"],
                             horizontal=True, key="fc_dir_radio",
                             label_visibility="collapsed")
        if direction != st.session_state.fc_direction:
            st.session_state.fc_direction = direction
            st.session_state.fc_flipped = False
    with col2:
        st.markdown(f"<div style='color:#8b949e;text-align:right;padding-top:6px'>"
                    f"Card {st.session_state.fc_index + 1} of {len(st.session_state.fc_deck)}</div>",
                    unsafe_allow_html=True)

    word = st.session_state.fc_deck[st.session_state.fc_index]
    sylven, english, pos = word
    show_sylven_first = st.session_state.fc_direction == "Sylven → English"
    front = sylven if show_sylven_first else english
    back  = english if show_sylven_first else sylven

    if not st.session_state.fc_flipped:
        st.markdown(f"""
        <div class='sylven-card'>
            <div class='sylven-word'>{front}</div>
            <div class='hint-text'>Click "Flip" to reveal</div>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='sylven-card'>
            <div class='sylven-word'>{front}</div>
            <div style='color:#30363d;font-size:1.2rem;margin:6px 0'>↓</div>
            <div class='sylven-answer'>{back}</div>
            <div class='sylven-pos'>({pos})</div>
        </div>""", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("◀ Prev"):
            st.session_state.fc_index = (st.session_state.fc_index - 1) % len(st.session_state.fc_deck)
            st.session_state.fc_flipped = False
            st.rerun()
    with c2:
        flip_label = "Flip ↩" if not st.session_state.fc_flipped else "Hide ↩"
        if st.button(flip_label):
            st.session_state.fc_flipped = not st.session_state.fc_flipped
            st.rerun()
    with c3:
        if st.button("Next ▶"):
            st.session_state.fc_index = (st.session_state.fc_index + 1) % len(st.session_state.fc_deck)
            st.session_state.fc_flipped = False
            st.rerun()
    with c4:
        if st.button("🔀 Shuffle"):
            st.session_state.fc_deck = random.sample(VOCABULARY, len(VOCABULARY))
            st.session_state.fc_index = 0
            st.session_state.fc_flipped = False
            st.rerun()

    # Progress bar
    prog = (st.session_state.fc_index + 1) / len(st.session_state.fc_deck)
    st.progress(prog)

# ── QUIZ ─────────────────────────────────────────────────────────────────────
elif page == "🎯 Quiz":
    st.title("🎯 Multiple Choice Quiz")

    col1, col2 = st.columns(2)
    with col1:
        q_dir = st.radio("Direction", ["Sylven → English", "English → Sylven"],
                         horizontal=True, label_visibility="collapsed")
        if q_dir != st.session_state.quiz_direction:
            st.session_state.quiz_direction = q_dir
            st.session_state.quiz_word = None
    with col2:
        pos_opts = ["All", "noun", "verb", "adjective", "pronoun", "number", "adverb"]
        q_filter = st.selectbox("Filter by part of speech", pos_opts,
                                label_visibility="collapsed")
        if q_filter != st.session_state.quiz_filter:
            st.session_state.quiz_filter = q_filter
            st.session_state.quiz_word = None

    if st.session_state.quiz_word is None:
        new_quiz_question()

    if st.session_state.quiz_word:
        correct_word = st.session_state.quiz_word
        choices = st.session_state.quiz_choices
        show_sylven = st.session_state.quiz_direction == "Sylven → English"
        question = correct_word[0] if show_sylven else correct_word[1]
        correct_answer = correct_word[1] if show_sylven else correct_word[0]

        st.markdown(f"""
        <div class='sylven-card'>
            <div style='color:#8b949e;font-size:0.85rem;margin-bottom:8px'>What does this mean?</div>
            <div class='sylven-word'>{question}</div>
        </div>""", unsafe_allow_html=True)

        for choice in choices:
            display = choice[1] if show_sylven else choice[0]
            is_correct = (choice == correct_word)
            is_chosen = (st.session_state.quiz_chosen == display)

            if st.session_state.quiz_answered:
                if is_correct:
                    st.markdown(f"<div class='result-correct'>✓ {display}</div>", unsafe_allow_html=True)
                elif is_chosen:
                    st.markdown(f"<div class='result-wrong'>✗ {display}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='background:#21262d;border:1px solid #30363d;border-radius:8px;"
                                f"padding:12px;margin:4px 0;color:#8b949e;text-align:center'>{display}</div>",
                                unsafe_allow_html=True)
            else:
                if st.button(display, key=f"choice_{display}"):
                    st.session_state.quiz_answered = True
                    st.session_state.quiz_chosen = display
                    record(is_correct)
                    st.rerun()

        if st.session_state.quiz_answered:
            chosen = st.session_state.quiz_chosen
            was_correct = any(
                (c[1] if show_sylven else c[0]) == chosen and c == correct_word
                for c in choices
            )
            if was_correct:
                st.success("🎉 Correct!")
            else:
                st.error(f"The answer was: **{correct_answer}**")

            if st.button("Next Question →"):
                new_quiz_question()
                st.rerun()

# ── TRANSLATION ───────────────────────────────────────────────────────────────
elif page == "✍️ Translation":
    st.title("✍️ Translation Practice")
    st.caption("Type your translation and press Enter or click Check.")

    t_dir = st.radio("Direction", ["Sylven → English", "English → Sylven"],
                     horizontal=True, label_visibility="collapsed")
    if t_dir != st.session_state.trans_direction:
        st.session_state.trans_direction = t_dir
        st.session_state.trans_word = None

    if st.session_state.trans_word is None:
        new_trans_word()

    word = st.session_state.trans_word
    sylven, english, pos = word
    show_sylven = st.session_state.trans_direction == "Sylven → English"
    prompt  = sylven if show_sylven else english
    answer  = english if show_sylven else sylven

    st.markdown(f"""
    <div class='sylven-card'>
        <div style='color:#8b949e;font-size:0.85rem'>Translate this {pos}:</div>
        <div class='sylven-word'>{prompt}</div>
    </div>""", unsafe_allow_html=True)

    user_input = st.text_input("Your answer", key="trans_input",
                               placeholder="Type here and press Enter…",
                               label_visibility="collapsed")

    c1, c2 = st.columns(2)
    with c1:
        check = st.button("✓ Check", use_container_width=True)
    with c2:
        skip = st.button("Skip →", use_container_width=True)

    if check and user_input:
        user = user_input.strip().lower()
        accepted = [a.strip().lower() for a in answer.split("/")]
        is_correct = any(user == a or user in a or a in user for a in accepted)
        record(is_correct)
        if is_correct:
            st.markdown("<div class='result-correct'>✓ Correct!</div>", unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown(f"<div class='result-wrong'>✗ Expected: {answer}</div>", unsafe_allow_html=True)
        st.session_state.trans_checked = True

    if skip or (st.session_state.trans_checked and st.button("Next Word →")):
        new_trans_word()
        st.rerun()

# ── SENTENCES ─────────────────────────────────────────────────────────────────
elif page == "📖 Sentences":
    st.title("📖 Sample Sentences")
    st.caption("Cultural phrases and example sentences from the Sylven language.")
    for sylven, english in SAMPLE_SENTENCES:
        st.markdown(f"""
        <div class='sentence-card'>
            <div class='sentence-sylven'>{sylven}</div>
            <div class='sentence-english'>{english}</div>
        </div>""", unsafe_allow_html=True)

# ── GRAMMAR ───────────────────────────────────────────────────────────────────
elif page == "📚 Grammar":
    st.title("📚 Grammar Notes")
    for title, body in GRAMMAR_NOTES:
        st.markdown(f"""
        <div class='grammar-card'>
            <div class='grammar-title'>{title}</div>
            <div class='grammar-body'>{body}</div>
        </div>""", unsafe_allow_html=True)

# ── FULL VOCAB ────────────────────────────────────────────────────────────────
elif page == "📋 Full Vocab":
    st.title("📋 Full Vocabulary")
    st.caption(f"{len(VOCABULARY)} words total")

    search = st.text_input("🔍 Search", placeholder="Search Sylven, English, or part of speech…",
                           label_visibility="collapsed")
    pos_filter = st.selectbox("Filter", ["All"] + sorted(set(v[2] for v in VOCABULARY)),
                               label_visibility="collapsed")

    filtered = VOCABULARY
    if search:
        q = search.lower()
        filtered = [v for v in filtered if q in v[0].lower() or q in v[1].lower() or q in v[2].lower()]
    if pos_filter != "All":
        filtered = [v for v in filtered if v[2] == pos_filter]

    st.caption(f"Showing {len(filtered)} words")

    import pandas as pd
    df = pd.DataFrame(filtered, columns=["Sylven", "English", "Part of Speech"])
    st.dataframe(df, use_container_width=True, hide_index=True,
                 column_config={
                     "Sylven": st.column_config.TextColumn("Sylven", width="medium"),
                     "English": st.column_config.TextColumn("English", width="large"),
                     "Part of Speech": st.column_config.TextColumn("Type", width="small"),
                 })
