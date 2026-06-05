"""
Sylven Language Learning App
A tkinter-based app with Flashcards, Multiple Choice Quiz, and Translation Practice.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

# ── FULL VOCABULARY ──────────────────────────────────────────────────────────
VOCABULARY = [
    # Nouns – Core
    ("kxïralen", "god / deity", "noun"),
    ("havan", "home", "noun"),
    ("melen", "grace", "noun"),
    ("tsäva", "life", "noun"),
    ("radan", "path", "noun"),
    ("rynä", "person", "noun"),
    ("txevol", "world", "noun"),
    ("huna", "water", "noun"),
    ("fìrax", "fire", "noun"),
    ("sewa", "wind / air", "noun"),
    ("koral", "stone", "noun"),
    ("syelva", "tree", "noun"),
    ("rìuva", "sun", "noun"),
    ("tsölun", "moon", "noun"),
    ("estran", "star", "noun"),
    ("vorak", "mountain", "noun"),
    ("hunara", "river", "noun"),
    # Pronouns
    ("oyu", "I / me", "pronoun"),
    ("tiyä", "you (singular)", "pronoun"),
    ("e", "he / she / it", "pronoun"),
    ("syi", "we / us", "pronoun"),
    ("enu", "they / them", "pronoun"),
    ("oyun", "my / mine", "pronoun"),
    ("tiyän", "your", "pronoun"),
    ("enun", "their", "pronoun"),
    ("shi", "this / that", "pronoun"),
    ("oni", "all", "determiner"),
    ("ten", "each / every", "determiner"),
    # Verbs – Core
    ("esa", "to be / exist", "verb"),
    ("melen", "to bless", "verb"),
    ("hivan", "to live", "verb"),
    ("virak", "to walk", "verb"),
    ("salan", "to run", "verb"),
    ("alon", "to see", "verb"),
    ("lithan", "to speak / pray", "verb"),
    ("solan", "to protect / guard", "verb"),
    ("novak", "to create", "verb"),
    ("suan", "to give", "verb"),
    ("amrá", "to love", "verb"),
    ("tanan", "to know / learn", "verb"),
    ("miran", "to think", "verb"),
    ("soman", "to sleep", "verb"),
    ("drimak", "to dream", "verb"),
    # Adjectives
    ("Bona", "good", "adjective"),
    ("Mala", "bad / evil / black", "adjective"),
    ("Maha", "big / great", "adjective"),
    ("Tini", "small", "adjective"),
    ("Lysa", "bright", "adjective"),
    ("Mure", "dark", "adjective"),
    ("Vara", "strong", "adjective"),
    ("Tera", "weak", "adjective"),
    ("Nova", "new", "adjective"),
    ("Veta", "old", "adjective"),
    ("Shiva", "holy", "adjective"),
    ("Mora", "cursed", "adjective"),
    ("Pure", "clear", "adjective"),
    ("Dera", "hidden", "adjective"),
    # Prepositions & Conjunctions
    ("E", "and", "conjunction"),
    ("Su", "with", "preposition"),
    ("O", "in / on / at", "preposition"),
    ("Qa", "to / toward", "preposition"),
    ("Fra", "from", "preposition"),
    ("Tre", "through", "preposition"),
    ("De", "of / belonging to", "preposition"),
    ("Rada", "because", "conjunction"),
    ("Svi", "if", "conjunction"),
    ("Ni", "or", "conjunction"),
    # Adverbs
    ("Nua", "now", "adverb"),
    ("Rena", "then", "adverb"),
    ("Cura", "soon", "adverb"),
    ("Oniqa", "always", "adverb"),
    ("Malaqa", "never", "adverb"),
    ("Ráven", "far", "adverb"),
    ("Tenna", "near", "adverb"),
    # Numbers
    ("Een", "one", "number"),
    ("Dua", "two", "number"),
    ("Tre", "three", "number"),
    ("Kua", "four", "number"),
    ("Penta", "five", "number"),
    ("Sexa", "six", "number"),
    ("Seta", "seven", "number"),
    ("Okta", "eight", "number"),
    ("Novae", "nine", "number"),
    ("Dekka", "ten", "number"),
    # Nature & Weather
    ("Aurosa", "dawn", "noun"),
    ("Krepsa", "dusk", "noun"),
    ("Tonra", "thunder", "noun"),
    ("Flusmara", "tide", "noun"),
    ("Nebra", "mist / fog", "noun"),
    ("Arkopluna", "rainbow", "noun"),
    ("Eklipsa", "eclipse", "noun"),
    ("Pyravora", "volcano", "noun"),
    ("Terramota", "earthquake", "noun"),
    ("Spaltera", "canyon", "noun"),
    ("Estravola", "comet", "noun"),
    ("Estragruppa", "constellation", "noun"),
    ("Finlina", "horizon", "noun"),
    ("Abissa", "abyss", "noun"),
    ("Gelmonta", "glacier", "noun"),
    ("Paludra", "swamp", "noun"),
    ("Insula", "island", "noun"),
    ("Krupta", "cliff", "noun"),
    # Body Parts
    ("Kapra", "head", "noun"),
    ("Fasia", "face", "noun"),
    ("Boka", "mouth", "noun"),
    ("Lingua", "tongue", "noun"),
    ("Denta", "tooth", "noun"),
    ("Aura", "ear", "noun"),
    ("Nasa", "nose", "noun"),
    ("Kola", "neck", "noun"),
    ("Skapra", "shoulder", "noun"),
    ("Brakja", "arm", "noun"),
    ("Digita", "finger", "noun"),
    ("Krusa", "leg", "noun"),
    ("Peda", "foot", "noun"),
    ("Sangra", "blood", "noun"),
    ("Osta", "bone", "noun"),
    ("Pela", "skin", "noun"),
    ("Spirita", "breath", "noun"),
    ("Lakrim", "tear (crying)", "noun"),
    ("Sudora", "sweat", "noun"),
    ("Voksa", "voice", "noun"),
    # Animals
    ("Lorna", "wolf", "noun"),
    ("Fela", "cat", "noun"),
    ("Vira", "bird", "noun"),
    ("Draka", "dragon", "noun"),
    ("Sela", "fish", "noun"),
    ("Fruna", "frog", "noun"),
    ("Hira", "horse", "noun"),
    ("Mura", "mouse", "noun"),
    ("Vapa", "snake", "noun"),
    ("Moojoomeh", "cow", "noun"),
    # Colors
    ("Rava", "red", "adjective"),
    ("Vana", "green", "adjective"),
    ("Sila", "blue", "adjective"),
    ("Kora", "gray / stone-gray", "adjective"),
    # Household
    ("Kupa", "cup", "noun"),
    ("Vasa", "vase", "noun"),
    ("Lampa", "lamp", "noun"),
    ("Kloka", "clock", "noun"),
    ("Fenstra", "window", "noun"),
    ("Porta", "door", "noun"),
    ("Kasa", "house", "noun"),
    ("Karta", "map", "noun"),
    ("Tablara", "table", "noun"),
    ("Stola", "chair", "noun"),
    ("Penka", "pen", "noun"),
    ("Libara", "book", "noun"),
    ("Brelka", "bottle", "noun"),
    ("Dabra", "hammer", "noun"),
    ("Kresta", "knife", "noun"),
    # Emotions
    ("Vena", "hope", "noun"),
    ("Sura", "calm", "adjective"),
    ("Vika", "shy", "adjective"),
    ("Fira", "anger", "noun"),
    ("Trista", "sadness", "noun"),
    ("Sora", "joy", "noun"),
    # Social / Cultural
    ("Familia", "family", "noun"),
    ("Triba", "tribe", "noun"),
    ("Klana", "clan", "noun"),
    ("Nasiona", "nation", "noun"),
    ("Regnara", "kingdom", "noun"),
    ("Impera", "empire", "noun"),
    ("Sakora", "priest", "noun"),
    ("Batora", "warrior", "noun"),
    ("Solasora", "guardian", "noun"),
    ("Merkara", "merchant", "noun"),
    ("Artisa", "craftsman", "noun"),
    ("Servora", "servant", "noun"),
    ("Magistra", "master", "noun"),
    ("Senora", "elder", "noun"),
    ("Konsila", "council", "noun"),
    ("Throna", "throne", "noun"),
    ("Korona", "crown", "noun"),
    ("Leksara", "law", "noun"),
    ("Festara", "festival", "noun"),
    ("Matrara", "marriage", "noun"),
    ("Juramenta", "oath", "noun"),
    # Abstract / Philosophical
    ("Fatuma", "destiny", "noun"),
    ("Eternita", "eternity", "noun"),
    ("Infinora", "infinity", "noun"),
    ("Mistara", "mystery", "noun"),
    ("Mirakla", "miracle", "noun"),
    ("Profeza", "prophecy", "noun"),
    ("Revelara", "revelation", "noun"),
    ("Sakrifa", "sacrifice", "noun"),
    ("Paktura", "covenant", "noun"),
    ("Redemsa", "redemption", "noun"),
    ("Transmuta", "transformation", "noun"),
    ("Lumensa", "enlightenment", "noun"),
    ("Peregrina", "pilgrimage", "noun"),
    ("Meditara", "meditation", "noun"),
    ("Ritara", "ritual", "noun"),
    ("Benedikta", "blessing", "noun"),
    ("Judikara", "judgment", "noun"),
    ("Miserka", "mercy", "noun"),
    ("Justara", "justice", "noun"),
    ("Vengara", "vengeance", "noun"),
    ("Pardonara", "forgiveness", "noun"),
    ("Temptara", "temptation", "noun"),
    ("Virtara", "virtue", "noun"),
    ("Pekara", "sin", "noun"),
    ("Salvara", "salvation", "noun"),
    ("Esensa", "essence", "noun"),
    ("Realita", "reality", "noun"),
    ("Haramacrua", "harmony", "noun"),
    ("Distakatoo", "discord", "noun"),
    ("Balansa", "balance", "noun"),
    ("Kaossa", "chaos", "noun"),
    ("Yxah", "order", "noun"),
    ("Vakuma", "void", "noun"),
    ("Unita", "unity", "noun"),
    ("Dualita", "duality", "noun"),
    ("Transenda", "transcendence", "noun"),
    ("Imanensa", "immanence", "noun"),
    # Advanced Verbs
    ("Asendera", "to ascend", "verb"),
    ("Desendera", "to descend", "verb"),
    ("Revelara", "to reveal", "verb"),
    ("Konselara", "to conceal", "verb"),
    ("Manifesta", "to manifest", "verb"),
    ("Invoka", "to invoke", "verb"),
    ("Banisha", "to banish", "verb"),
    ("Transenda", "to transcend", "verb"),
    ("Komunara", "to commune", "verb"),
    ("Jornara", "to journey", "verb"),
    ("Vagara", "to wander", "verb"),
    ("Habitara", "to dwell", "verb"),
    ("Gathera", "to gather", "verb"),
    ("Unitra", "to unite", "verb"),
    ("Dividara", "to divide", "verb"),
    ("Ligara", "to bind", "verb"),
    ("Liberara", "to release", "verb"),
    ("Sumara", "to summon", "verb"),
    ("Enkanta", "to enchant", "verb"),
    ("Dispela", "to dispel", "verb"),
    ("Vekara", "to awaken", "verb"),
    ("Slumbara", "to slumber", "verb"),
    ("Meditara", "to meditate", "verb"),
    ("Kontempla", "to contemplate", "verb"),
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
    ("Plural", "Add -ni to make a noun plural.\nExample: kxïralen → kxïralenni (gods), txevol → txevolni (worlds)"),
    ("Past Tense", "Insert ‹ìm› before the stressed vowel.\nExample: hivan (live) → hìmivan (lived)"),
    ("Future Tense", "Insert ‹ay› before the stressed vowel.\nExample: hivan (live) → hayivan (will live)"),
    ("Adjectives", "Adjectives follow the noun they describe.\nExample: Txevol mahrä = 'great world' (lit: world great)"),
    ("Questions", "Use rising tone + particles:\nQa? = What? | Oa? = Where?"),
    ("Cases (optional)", "Agent: -ku | Patient: -ti | Goal: -ru\nThese are optional; prepositions can substitute in casual speech."),
    ("Possessives", "Add a nasal ending to pronouns:\noyu (I) → oyun (my/mine) | tiyä (you) → tiyän (your)"),
    ("Evidentiality", "za = I witnessed it | su = I infer | ke = I heard | sha = divine truth\nPlace particle after the verb."),
    ("Honorifics", "Ti = intimate | Vos = respectful | Theon = to deity | Rex = to royalty"),
]

# ── COLORS & FONTS ──────────────────────────────────────────────────────────
BG        = "#0d1117"
PANEL     = "#161b22"
ACCENT    = "#58a6ff"
GOLD      = "#d4a017"
GREEN     = "#3fb950"
RED       = "#f85149"
TEXT      = "#e6edf3"
SUBTEXT   = "#8b949e"
CARD_BG   = "#21262d"
BORDER    = "#30363d"

FONT_TITLE  = ("Georgia", 22, "bold")
FONT_HEAD   = ("Georgia", 14, "bold")
FONT_BODY   = ("Helvetica", 12)
FONT_LARGE  = ("Georgia", 28, "bold")
FONT_SMALL  = ("Helvetica", 10)
FONT_MONO   = ("Courier", 11)

# ── MAIN APP ─────────────────────────────────────────────────────────────────
class SylvenApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sylven Language Learner")
        self.geometry("900x680")
        self.minsize(800, 600)
        self.configure(bg=BG)

        self.score = {"correct": 0, "total": 0}
        self._build_ui()

    def _build_ui(self):
        # ── Sidebar ──
        sidebar = tk.Frame(self, bg=PANEL, width=190)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(sidebar, text="✦ SYLVEN", font=("Georgia", 16, "bold"),
                 bg=PANEL, fg=GOLD).pack(pady=(28, 4))
        tk.Label(sidebar, text="Language Learner", font=("Helvetica", 9),
                 bg=PANEL, fg=SUBTEXT).pack(pady=(0, 24))

        self.content = tk.Frame(self, bg=BG)
        self.content.pack(side="left", fill="both", expand=True)

        nav_items = [
            ("🃏  Flashcards",   self._show_flashcards),
            ("🎯  Quiz",         self._show_quiz),
            ("✍️   Translation",  self._show_translation),
            ("📖  Sentences",    self._show_sentences),
            ("📚  Grammar",      self._show_grammar),
            ("📋  Full Vocab",   self._show_vocab),
        ]
        self._nav_btns = []
        for label, cmd in nav_items:
            btn = tk.Button(sidebar, text=label, font=("Helvetica", 11),
                            bg=PANEL, fg=TEXT, bd=0, anchor="w",
                            padx=20, pady=10, cursor="hand2",
                            activebackground=CARD_BG, activeforeground=ACCENT,
                            command=lambda c=cmd, b=label: self._nav(c, b))
            btn.pack(fill="x")
            self._nav_btns.append((btn, label))

        # Score bar
        self.score_var = tk.StringVar(value="Score: 0 / 0")
        tk.Label(sidebar, textvariable=self.score_var, font=FONT_SMALL,
                 bg=PANEL, fg=SUBTEXT).pack(side="bottom", pady=16)

        self._active_nav = None
        self._show_flashcards()

    def _nav(self, cmd, label):
        for btn, lbl in self._nav_btns:
            btn.configure(bg=PANEL, fg=TEXT)
        for btn, lbl in self._nav_btns:
            if lbl == label:
                btn.configure(bg=CARD_BG, fg=ACCENT)
        cmd()

    def _clear(self):
        self.unbind("<space>")
        for w in self.content.winfo_children():
            w.destroy()

    def _update_score(self, correct):
        self.score["total"] += 1
        if correct:
            self.score["correct"] += 1
        self.score_var.set(f"Score: {self.score['correct']} / {self.score['total']}")

    # ── FLASHCARDS ──────────────────────────────────────────────────────────
    def _show_flashcards(self):
        self._clear()
        self._fc_deck = random.sample(VOCABULARY, len(VOCABULARY))
        self._fc_index = 0
        self._fc_flipped = False
        self._fc_direction = tk.StringVar(value="sylven→english")

        tk.Label(self.content, text="Flashcards", font=FONT_TITLE,
                 bg=BG, fg=ACCENT).pack(pady=(24, 4))
        tk.Label(self.content, text=f"{len(VOCABULARY)} cards  •  click card or press Space to flip  •  Space again to advance",
                 font=FONT_SMALL, bg=BG, fg=SUBTEXT).pack()

        dir_frame = tk.Frame(self.content, bg=BG)
        dir_frame.pack(pady=8)
        for val, lbl in [("sylven→english", "Sylven → English"),
                          ("english→sylven", "English → Sylven")]:
            tk.Radiobutton(dir_frame, text=lbl, variable=self._fc_direction,
                           value=val, bg=BG, fg=TEXT, selectcolor=PANEL,
                           font=FONT_SMALL,
                           command=self._fc_reset).pack(side="left", padx=10)

        self._fc_progress = tk.Label(self.content, text="", font=FONT_SMALL,
                                     bg=BG, fg=SUBTEXT)
        self._fc_progress.pack()

        # Card
        card_frame = tk.Frame(self.content, bg=BG)
        card_frame.pack(expand=True)

        self._fc_card = tk.Frame(card_frame, bg=CARD_BG, width=480, height=240,
                                  relief="flat", highlightbackground=BORDER,
                                  highlightthickness=1)
        self._fc_card.pack(pady=10)
        self._fc_card.pack_propagate(False)
        self._fc_card.bind("<Button-1>", lambda e: self._fc_flip())

        self._fc_label = tk.Label(self._fc_card, text="", font=FONT_LARGE,
                                   bg=CARD_BG, fg=TEXT, wraplength=440,
                                   cursor="hand2")
        self._fc_label.pack(expand=True)
        self._fc_label.bind("<Button-1>", lambda e: self._fc_flip())

        self._fc_sub = tk.Label(self._fc_card, text="", font=FONT_SMALL,
                                 bg=CARD_BG, fg=SUBTEXT)
        self._fc_sub.pack(pady=(0, 12))
        self._fc_sub.bind("<Button-1>", lambda e: self._fc_flip())

        # Buttons
        btn_frame = tk.Frame(self.content, bg=BG)
        btn_frame.pack(pady=8)
        for txt, cmd, color in [("◀  Prev", self._fc_prev, SUBTEXT),
                                  ("  Flip  ", self._fc_flip, ACCENT),
                                  ("Next  ▶", self._fc_next, SUBTEXT)]:
            tk.Button(btn_frame, text=txt, font=FONT_BODY, bg=PANEL, fg=color,
                      bd=0, padx=18, pady=8, cursor="hand2",
                      activebackground=CARD_BG, command=cmd).pack(side="left", padx=6)

        # Spacebar: flip if not yet flipped, advance to next if already flipped
        self.bind("<space>", self._fc_space)

        self._fc_render()

    def _fc_space(self, event=None):
        if self._fc_flipped:
            self._fc_next()
        else:
            self._fc_flip()

    def _fc_reset(self):
        self._fc_index = 0
        self._fc_flipped = False
        self._fc_render()

    def _fc_render(self):
        word = self._fc_deck[self._fc_index]
        sylven, english, pos = word
        show_sylven = self._fc_direction.get() == "sylven→english"
        if not self._fc_flipped:
            front = sylven if show_sylven else english
            self._fc_label.configure(text=front, fg=TEXT)
            self._fc_sub.configure(text="[ tap to reveal ]")
        else:
            back = english if show_sylven else sylven
            self._fc_label.configure(text=back, fg=GOLD)
            self._fc_sub.configure(text=f"({pos})")
        self._fc_progress.configure(
            text=f"Card {self._fc_index + 1} of {len(self._fc_deck)}")

    def _fc_flip(self):
        self._fc_flipped = not self._fc_flipped
        self._fc_render()

    def _fc_next(self):
        self._fc_index = (self._fc_index + 1) % len(self._fc_deck)
        self._fc_flipped = False
        self._fc_render()

    def _fc_prev(self):
        self._fc_index = (self._fc_index - 1) % len(self._fc_deck)
        self._fc_flipped = False
        self._fc_render()

    # ── QUIZ ────────────────────────────────────────────────────────────────
    def _show_quiz(self):
        self._clear()
        self._quiz_direction = tk.StringVar(value="sylven→english")
        self._quiz_filter = tk.StringVar(value="all")

        tk.Label(self.content, text="Multiple Choice Quiz", font=FONT_TITLE,
                 bg=BG, fg=ACCENT).pack(pady=(24, 4))

        opt_frame = tk.Frame(self.content, bg=BG)
        opt_frame.pack(pady=4)
        tk.Label(opt_frame, text="Direction:", font=FONT_SMALL,
                 bg=BG, fg=SUBTEXT).pack(side="left")
        for val, lbl in [("sylven→english", "Sylven → English"),
                          ("english→sylven", "English → Sylven")]:
            tk.Radiobutton(opt_frame, text=lbl, variable=self._quiz_direction,
                           value=val, bg=BG, fg=TEXT, selectcolor=PANEL,
                           font=FONT_SMALL).pack(side="left", padx=8)

        filter_frame = tk.Frame(self.content, bg=BG)
        filter_frame.pack(pady=2)
        tk.Label(filter_frame, text="Filter by:", font=FONT_SMALL,
                 bg=BG, fg=SUBTEXT).pack(side="left")
        for val in ["all", "noun", "verb", "adjective", "pronoun", "number"]:
            tk.Radiobutton(filter_frame, text=val.capitalize(),
                           variable=self._quiz_filter, value=val,
                           bg=BG, fg=TEXT, selectcolor=PANEL,
                           font=FONT_SMALL).pack(side="left", padx=5)

        tk.Button(self.content, text="Start New Question", font=FONT_BODY,
                  bg=ACCENT, fg=BG, bd=0, padx=16, pady=6, cursor="hand2",
                  command=self._quiz_new).pack(pady=10)

        self._quiz_frame = tk.Frame(self.content, bg=BG)
        self._quiz_frame.pack(fill="both", expand=True, padx=40)
        self._quiz_new()

    def _quiz_new(self):
        for w in self._quiz_frame.winfo_children():
            w.destroy()

        pos_filter = self._quiz_filter.get()
        pool = [v for v in VOCABULARY if pos_filter == "all" or v[2] == pos_filter]
        if len(pool) < 4:
            tk.Label(self._quiz_frame, text="Not enough words for this filter.",
                     bg=BG, fg=RED, font=FONT_BODY).pack(pady=20)
            return

        correct = random.choice(pool)
        wrongs = random.sample([v for v in pool if v != correct], 3)
        choices = [correct] + wrongs
        random.shuffle(choices)

        show_sylven = self._quiz_direction.get() == "sylven→english"
        question = correct[0] if show_sylven else correct[1]
        answer = correct[1] if show_sylven else correct[0]

        tk.Label(self._quiz_frame,
                 text=f"What does this mean?\n\n{question}",
                 font=FONT_LARGE, bg=BG, fg=TEXT, wraplength=600,
                 justify="center").pack(pady=(20, 30))

        self._quiz_btns = []
        for choice in choices:
            display = choice[1] if show_sylven else choice[0]
            is_correct = (choice == correct)
            btn = tk.Button(self._quiz_frame, text=display,
                            font=("Helvetica", 12), bg=CARD_BG, fg=TEXT,
                            bd=0, pady=10, padx=20, cursor="hand2",
                            width=36, wraplength=400,
                            activebackground=PANEL,
                            command=lambda d=display, ic=is_correct, a=answer:
                                self._quiz_answer(d, ic, a))
            btn.pack(pady=5)
            self._quiz_btns.append((btn, is_correct, display))

    def _quiz_answer(self, chosen, is_correct, answer):
        # Disable all buttons and highlight
        for btn, ic, display in self._quiz_btns:
            btn.configure(state="disabled")
            if ic:
                btn.configure(bg=GREEN, fg=BG)
            elif display == chosen and not ic:
                btn.configure(bg=RED, fg=BG)

        self._update_score(is_correct)
        msg = "✓ Correct!" if is_correct else f"✗ The answer was: {answer}"
        color = GREEN if is_correct else RED

        tk.Label(self._quiz_frame, text=msg, font=("Helvetica", 13, "bold"),
                 bg=BG, fg=color).pack(pady=8)
        tk.Button(self._quiz_frame, text="Next Question →", font=FONT_BODY,
                  bg=ACCENT, fg=BG, bd=0, padx=14, pady=6, cursor="hand2",
                  command=self._quiz_new).pack(pady=4)

    # ── TRANSLATION PRACTICE ────────────────────────────────────────────────
    def _show_translation(self):
        self._clear()
        self._trans_direction = tk.StringVar(value="sylven→english")

        tk.Label(self.content, text="Translation Practice", font=FONT_TITLE,
                 bg=BG, fg=ACCENT).pack(pady=(24, 4))
        tk.Label(self.content, text="Type your translation and check your answer.",
                 font=FONT_SMALL, bg=BG, fg=SUBTEXT).pack()

        dir_frame = tk.Frame(self.content, bg=BG)
        dir_frame.pack(pady=8)
        for val, lbl in [("sylven→english", "Sylven → English"),
                          ("english→sylven", "English → Sylven")]:
            tk.Radiobutton(dir_frame, text=lbl, variable=self._trans_direction,
                           value=val, bg=BG, fg=TEXT, selectcolor=PANEL,
                           font=FONT_SMALL).pack(side="left", padx=10)

        self._trans_word_var = tk.StringVar()
        self._trans_answer = ""

        word_frame = tk.Frame(self.content, bg=CARD_BG,
                              highlightbackground=BORDER, highlightthickness=1)
        word_frame.pack(pady=14, ipadx=30, ipady=20)
        tk.Label(word_frame, text="Translate:", font=FONT_SMALL,
                 bg=CARD_BG, fg=SUBTEXT).pack()
        self._trans_prompt = tk.Label(word_frame, text="",
                                       font=FONT_LARGE, bg=CARD_BG, fg=GOLD)
        self._trans_prompt.pack(pady=6)
        self._trans_pos_lbl = tk.Label(word_frame, text="", font=FONT_SMALL,
                                        bg=CARD_BG, fg=SUBTEXT)
        self._trans_pos_lbl.pack()

        tk.Label(self.content, text="Your answer:", font=FONT_SMALL,
                 bg=BG, fg=SUBTEXT).pack()
        entry = tk.Entry(self.content, textvariable=self._trans_word_var,
                         font=("Helvetica", 14), bg=PANEL, fg=TEXT,
                         insertbackground=TEXT, bd=0, width=28,
                         highlightbackground=BORDER, highlightthickness=1)
        entry.pack(pady=6, ipady=6)
        entry.bind("<Return>", lambda e: self._trans_check())

        btn_row = tk.Frame(self.content, bg=BG)
        btn_row.pack(pady=6)
        tk.Button(btn_row, text="Check", font=FONT_BODY, bg=ACCENT, fg=BG,
                  bd=0, padx=16, pady=6, cursor="hand2",
                  command=self._trans_check).pack(side="left", padx=6)
        tk.Button(btn_row, text="Skip / New", font=FONT_BODY, bg=PANEL, fg=SUBTEXT,
                  bd=0, padx=16, pady=6, cursor="hand2",
                  command=self._trans_new).pack(side="left", padx=6)

        self._trans_result = tk.Label(self.content, text="", font=("Helvetica", 13, "bold"),
                                       bg=BG, fg=TEXT)
        self._trans_result.pack(pady=8)

        self._trans_new()

    def _trans_new(self):
        word = random.choice(VOCABULARY)
        show_sylven = self._trans_direction.get() == "sylven→english"
        self._trans_prompt.configure(text=word[0] if show_sylven else word[1])
        self._trans_pos_lbl.configure(text=f"({word[2]})")
        self._trans_answer = word[1].lower() if show_sylven else word[0].lower()
        self._trans_word_var.set("")
        self._trans_result.configure(text="")

    def _trans_check(self):
        user = self._trans_word_var.get().strip().lower()
        correct_answers = [a.strip().lower() for a in self._trans_answer.split("/")]
        # Also accept if user input is contained in any answer or vice versa
        is_correct = any(user == a or user in a or a in user for a in correct_answers)
        if is_correct:
            self._trans_result.configure(
                text="✓ Correct!", fg=GREEN)
            self._update_score(True)
            self.after(1200, self._trans_new)
        else:
            self._trans_result.configure(
                text=f"✗ Expected: {self._trans_answer.title()}", fg=RED)
            self._update_score(False)

    # ── SAMPLE SENTENCES ───────────────────────────────────────────────────
    def _show_sentences(self):
        self._clear()
        tk.Label(self.content, text="Sample Sentences", font=FONT_TITLE,
                 bg=BG, fg=ACCENT).pack(pady=(24, 4))
        tk.Label(self.content, text="Cultural phrases and example sentences from the language.",
                 font=FONT_SMALL, bg=BG, fg=SUBTEXT).pack(pady=(0, 16))

        container = tk.Frame(self.content, bg=BG)
        container.pack(fill="both", expand=True, padx=40)

        for sylven, english in SAMPLE_SENTENCES:
            card = tk.Frame(container, bg=CARD_BG,
                            highlightbackground=BORDER, highlightthickness=1)
            card.pack(fill="x", pady=6, ipadx=16, ipady=10)
            tk.Label(card, text=sylven, font=("Georgia", 13, "bold"),
                     bg=CARD_BG, fg=GOLD, anchor="w").pack(anchor="w", padx=10, pady=(8, 2))
            tk.Label(card, text=english, font=FONT_BODY,
                     bg=CARD_BG, fg=TEXT, anchor="w").pack(anchor="w", padx=10, pady=(0, 8))

    # ── GRAMMAR NOTES ──────────────────────────────────────────────────────
    def _show_grammar(self):
        self._clear()
        tk.Label(self.content, text="Grammar Notes", font=FONT_TITLE,
                 bg=BG, fg=ACCENT).pack(pady=(24, 4))

        canvas = tk.Canvas(self.content, bg=BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.content, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        inner = tk.Frame(canvas, bg=BG)
        canvas.create_window((0, 0), window=inner, anchor="nw")

        for title, body in GRAMMAR_NOTES:
            card = tk.Frame(inner, bg=CARD_BG,
                            highlightbackground=BORDER, highlightthickness=1)
            card.pack(fill="x", padx=30, pady=8, ipadx=16, ipady=10)
            tk.Label(card, text=title, font=FONT_HEAD,
                     bg=CARD_BG, fg=ACCENT).pack(anchor="w", padx=10, pady=(8, 2))
            tk.Label(card, text=body, font=FONT_MONO,
                     bg=CARD_BG, fg=TEXT, anchor="w", justify="left",
                     wraplength=680).pack(anchor="w", padx=10, pady=(0, 8))

        inner.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.bind("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

    # ── FULL VOCABULARY LIST ───────────────────────────────────────────────
    def _show_vocab(self):
        self._clear()
        tk.Label(self.content, text="Full Vocabulary", font=FONT_TITLE,
                 bg=BG, fg=ACCENT).pack(pady=(24, 4))

        search_frame = tk.Frame(self.content, bg=BG)
        search_frame.pack(pady=6)
        tk.Label(search_frame, text="🔍", bg=BG, fg=SUBTEXT,
                 font=("Helvetica", 12)).pack(side="left")
        self._search_var = tk.StringVar()
        self._search_var.trace("w", self._vocab_filter)
        search_entry = tk.Entry(search_frame, textvariable=self._search_var,
                                font=FONT_BODY, bg=PANEL, fg=TEXT,
                                insertbackground=TEXT, bd=0, width=30,
                                highlightbackground=BORDER, highlightthickness=1)
        search_entry.pack(side="left", ipady=5, padx=6)

        # Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=CARD_BG, foreground=TEXT,
                         fieldbackground=CARD_BG, rowheight=28,
                         font=("Helvetica", 11))
        style.configure("Treeview.Heading", background=PANEL, foreground=ACCENT,
                         font=("Helvetica", 11, "bold"))
        style.map("Treeview", background=[("selected", BORDER)],
                  foreground=[("selected", ACCENT)])

        frame = tk.Frame(self.content, bg=BG)
        frame.pack(fill="both", expand=True, padx=20, pady=8)

        self._tree = ttk.Treeview(frame, columns=("sylven", "english", "type"),
                                   show="headings", selectmode="browse")
        for col, w, label in [("sylven", 200, "Sylven"), ("english", 300, "English"),
                                ("type", 120, "Part of Speech")]:
            self._tree.heading(col, text=label)
            self._tree.column(col, width=w, anchor="w")

        vsb = ttk.Scrollbar(frame, orient="vertical", command=self._tree.yview)
        self._tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self._tree.pack(fill="both", expand=True)

        self._vocab_all = VOCABULARY
        self._vocab_populate(VOCABULARY)

    def _vocab_populate(self, words):
        self._tree.delete(*self._tree.get_children())
        for sylven, english, pos in words:
            self._tree.insert("", "end", values=(sylven, english, pos))

    def _vocab_filter(self, *_):
        q = self._search_var.get().lower()
        filtered = [v for v in VOCABULARY
                    if q in v[0].lower() or q in v[1].lower() or q in v[2].lower()]
        self._vocab_populate(filtered)


# ── ENTRY POINT ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = SylvenApp()
    app.mainloop()
