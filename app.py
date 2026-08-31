import pandas as pd
import streamlit as st

# ============================================================
# CHANDLER PARK ACADEMY — DAY TWO (55 MINUTES)
# "Getting to Know You" — Data Reveal + Shape Survey Stations
# Standalone version (no _common.py / launcher dependency)
# ============================================================

NAVY = "#1F3864"
GOLD = "#B08D57"
CREAM = "#F2EFE9"


def inject_css():
    st.markdown(
        f"""
        <style>
        .stApp {{ background-color: #FFFFFF; }}
        .block-container {{ padding-top: 2rem; padding-bottom: 3rem; max-width: 1100px; }}

        .cpa-banner {{
            background-color: {NAVY};
            color: white;
            padding: 1.1rem 1.8rem;
            border-radius: 10px;
            margin-bottom: 1.6rem;
        }}
        .cpa-banner h1 {{ margin: 0; font-size: 1.6rem; letter-spacing: 0.5px; }}
        .cpa-banner p {{ margin: 0.2rem 0 0 0; opacity: 0.85; font-size: 0.95rem; }}

        .pace-badge {{
            display: inline-block;
            background-color: {GOLD};
            color: white;
            padding: 0.25rem 0.9rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }}

        .big-title {{ color: {NAVY}; font-size: 2.1rem; font-weight: 800; margin-bottom: 0.3rem; }}
        .sub-title {{ color: {GOLD}; font-size: 1.15rem; font-weight: 700; margin-bottom: 1.2rem; }}

        .station-card {{
            background-color: {CREAM};
            border-left: 7px solid {GOLD};
            border-radius: 8px;
            padding: 1.3rem 1.5rem;
            margin-bottom: 1rem;
            height: 100%;
        }}
        .station-card h3 {{ color: {NAVY}; margin-top: 0; }}

        .step-row {{ display: flex; align-items: flex-start; margin-bottom: 1rem; }}
        .step-num {{
            background-color: {NAVY};
            color: white;
            border-radius: 50%;
            min-width: 2.1rem;
            height: 2.1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            margin-right: 0.9rem;
            flex-shrink: 0;
            margin-top: 0.1rem;
        }}
        .step-text {{ font-size: 1.05rem; line-height: 1.5; padding-top: 0.15rem; }}

        .quote-box {{
            background-color: {CREAM};
            border-left: 7px solid {NAVY};
            border-radius: 8px;
            padding: 1.3rem 1.6rem;
            font-size: 1.15rem;
            font-style: italic;
            color: {NAVY};
            margin-bottom: 1.2rem;
        }}

        .ican-box {{
            background-color: white;
            border: 2px solid {GOLD};
            border-radius: 8px;
            padding: 1rem 1.3rem;
            margin-bottom: 0.8rem;
            font-size: 1.05rem;
        }}
        .ican-tag {{
            display: inline-block;
            background-color: {NAVY};
            color: white;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.6rem;
            border-radius: 6px;
            margin-right: 0.6rem;
        }}

        .reflect-box {{
            background-color: {NAVY};
            color: white;
            border-radius: 10px;
            padding: 1.6rem 1.8rem;
            font-size: 1.2rem;
            line-height: 1.6;
            margin-top: 1rem;
        }}

        .warn-box {{
            background-color: #FFF4E5;
            border-left: 7px solid {GOLD};
            border-radius: 8px;
            padding: 1rem 1.3rem;
            margin-top: 0.8rem;
            font-weight: 600;
            color: #7a5a1e;
        }}

        .day-card {{
            background-color: {CREAM};
            border: 2px solid {GOLD};
            border-radius: 12px;
            padding: 1.4rem 1.5rem 0.6rem 1.5rem;
            margin-bottom: 1rem;
        }}
        .day-card h3 {{ color: {NAVY}; margin: 0 0 0.3rem 0; }}
        .day-card p {{ min-height: 3rem; }}
        .status-pill {{
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.6rem;
            border-radius: 999px;
            margin-bottom: 0.6rem;
        }}
        .status-ready {{ background-color: #DCEFDC; color: #206020; }}
        .status-soon {{ background-color: #EEEEEE; color: #777777; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def banner(subtitle="Grade 6 Mathematics"):
    st.markdown(
        f"""
        <div class="cpa-banner">
            <h1>CHANDLER PARK ACADEMY</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )



st.set_page_config(page_title="Day 2 — Getting to Know You: Shape Survey Stations", page_icon="🔷", layout="wide")
inject_css()

# ---- Larger-text / read-aloud overrides for this lesson ----
st.markdown(
    f"""
    <style>
    .block-container {{ max-width: 1500px !important; padding-top: 1.5rem; }}
    .big-title {{ font-size: 4.2rem !important; line-height: 1.15 !important; margin-bottom: 0.6rem !important; }}
    .sub-title {{ font-size: 2.3rem !important; margin-bottom: 1.6rem !important; }}
    .station-card {{ padding: 2rem 2.2rem !important; }}
    .station-card h3 {{ font-size: 2rem !important; margin-bottom: 0.6rem !important; }}
    .station-card p, .station-card {{ font-size: 1.7rem !important; line-height: 1.5 !important; }}
    .station-card b {{ font-size: 1.8rem !important; }}
    .step-row {{ margin-bottom: 1.6rem !important; }}
    .step-num {{ min-width: 3.2rem !important; height: 3.2rem !important; font-size: 1.6rem !important; }}
    .step-text {{ font-size: 1.9rem !important; line-height: 1.5 !important; }}
    div[data-testid="stMarkdownContainer"] p {{ font-size: 1.7rem; line-height: 1.55; }}
    div[data-testid="stMarkdownContainer"] li {{ font-size: 1.7rem; line-height: 1.55; }}
    .pace-badge {{ font-size: 1.4rem !important; padding: 0.4rem 1.3rem !important; margin-bottom: 1.4rem !important; }}
    .shape-tag {{ font-size: 1.6rem !important; padding: 0.35rem 1.3rem !important; margin-bottom: 0.8rem !important; }}
    .q-line {{ font-size: 1.8rem !important; padding: 0.65rem 0 !important; border-bottom: 2px dashed #ccc !important; }}
    .ican-box {{ font-size: 1.7rem !important; padding: 1.5rem 1.8rem !important; }}
    .ican-tag {{ font-size: 1.1rem !important; padding: 0.25rem 0.9rem !important; }}
    .reflect-box {{ font-size: 2rem !important; padding: 2.2rem 2.4rem !important; line-height: 1.5 !important; }}
    .warn-box {{ font-size: 1.6rem !important; padding: 1.5rem 1.8rem !important; }}
    .readaloud-box {{
        background-color: #FFFFFF;
        border: 4px solid {NAVY};
        border-radius: 12px;
        padding: 2rem 2.3rem;
        margin: 1.2rem 0 1.8rem 0;
        font-size: 2rem !important;
        line-height: 1.55 !important;
    }}
    .readaloud-label {{
        display: inline-block;
        background-color: {NAVY};
        color: white;
        font-weight: 800;
        font-size: 1.3rem;
        padding: 0.35rem 1.1rem;
        border-radius: 999px;
        margin-bottom: 0.9rem;
    }}
    .cpa-banner h1 {{ font-size: 2.4rem !important; }}
    .cpa-banner p {{ font-size: 1.4rem !important; }}
    section[data-testid="stSidebar"] button {{ font-size: 1.15rem !important; }}
    .letter-tile {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 3.2rem;
        height: 3.6rem;
        margin: 0.15rem;
        background-color: {NAVY};
        color: white;
        font-size: 2.1rem;
        font-weight: 800;
        border-radius: 8px;
        border-bottom: 5px solid {GOLD};
    }}
    .letter-row {{ margin: 1rem 0 1.4rem 0; }}
    </style>
    """,
    unsafe_allow_html=True,
)

banner("Grade 6 Mathematics | Day Two | 55-Minute Period")


def read_aloud(text):
    st.markdown(
        f"""
        <div class="readaloud-box">
        <span class="readaloud-label">🔊 READ ALOUD</span><br>
        "{text}"
        </div>
        """,
        unsafe_allow_html=True,
    )


def spell_word(word):
    tiles = "".join(f'<span class="letter-tile">{ch}</span>' for ch in word.upper())
    st.markdown(f'<div class="letter-row">{tiles}</div>', unsafe_allow_html=True)


SLIDES = [
    "Welcome Back!",
    "Let's Look at Our Data",
    "What This Data Means",
    "Let's Talk About Confounding",
    "Today: Getting to Know You",
    "Station 1: Hexagon",
    "Station 2: Pentagon",
    "Station 3: Parallelogram",
    "Station 4: Trapezoid",
    "Station 5: STOP & Grow",
    "How to Build Your Shape",
    "Turn It In",
    "Where Your Answers Go",
    "Standards Covered",
    "What You Just Did",
]

if "day2_slide" not in st.session_state:
    st.session_state.day2_slide = 0


def go_to(i):
    st.session_state.day2_slide = i


def go_next():
    st.session_state.day2_slide = min(st.session_state.day2_slide + 1, len(SLIDES) - 1)


def go_prev():
    st.session_state.day2_slide = max(st.session_state.day2_slide - 1, 0)


with st.sidebar:
    st.markdown(f"<h3 style='color:{NAVY};'>Day 2 Roadmap</h3>", unsafe_allow_html=True)
    st.caption("55-minute period — Shape Survey Stations")
    for i, label in enumerate(SLIDES):
        prefix = "▶ " if i == st.session_state.day2_slide else "　"
        st.button(f"{prefix}{i + 1}. {label}", key=f"d2nav_{i}", on_click=go_to, args=(i,), use_container_width=True)
    st.markdown("---")
    st.progress((st.session_state.day2_slide + 1) / len(SLIDES))
    st.caption(f"Slide {st.session_state.day2_slide + 1} of {len(SLIDES)}")

slide = st.session_state.day2_slide

# ============================================================
if slide == 0:
    st.markdown('<span class="pace-badge">0-4 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Welcome Back!</div>', unsafe_allow_html=True)
    read_aloud(
        "Yesterday was a W class. Several of you gave me a pound on your way out the door, and "
        "one of you called it a W class. I heard you. Today, I want to show you exactly why it "
        "was a W - with real numbers from your own work."
    )
    st.write("Take your seat. Today we start by looking at some real data from yesterday.")

# ============================================================
elif slide == 1:
    st.markdown('<span class="pace-badge">4-12 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Let\'s Look at Our Data</div>', unsafe_allow_html=True)
    read_aloud(
        "Out of everyone in this class, forty-two students turned in work yesterday. I hung twelve "
        "of those on our wall because they were exceptional. Let's use math to talk about what that "
        "actually means."
    )

    c1, c2 = st.columns([2, 3])
    with c1:
        st.markdown('<div class="shape-tag">THE NUMBERS</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="station-card">
            <b>Total students:</b> 42<br>
            <b>Work hung as exceptional:</b> 12<br>
            <b>Fraction:</b> 12/42 = 2/7<br>
            <b>Percent:</b> about 28.6%
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        chart_df = pd.DataFrame(
            {"Group": ["Exceptional Work", "Everyone Else"], "Students": [12, 30]}
        ).set_index("Group")
        st.bar_chart(chart_df, color=GOLD, height=420)

    st.write("Turn and talk: about how many students out of every 10 in our class had work hung up?")

# ============================================================
elif slide == 2:
    st.markdown('<span class="pace-badge">12-18 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">What This Data Means</div>', unsafe_allow_html=True)
    read_aloud(
        "Here's the important part: twelve of you are hanging on that wall today. Thirty of you "
        "are not - yet. That word 'yet' matters. Proficiency is not a fixed judgment about who you "
        "are. It is a measurement of where you are right now, on your way to where you're going."
    )
    st.markdown(
        """
        <div class="station-card">
        <h3>🌱 Growth Mindset Moment</h3>
        <p>Being exceptional on Day One doesn't mean you're "done" - and not being on the wall yet
        doesn't mean you can't be. Every single one of you will get more chances this year to build,
        revise, and improve your work.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
elif slide == 3:
    st.markdown('<span class="pace-badge">Bonus</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Let\'s Talk About Confounding</div>', unsafe_allow_html=True)
    read_aloud(
        "A little while ago, when I asked some of you keep-or-rid questions - like your favorite "
        "fruit, or an animal - I had everyone close their eyes before answering. Some of you "
        "probably wondered why."
    )

    st.markdown('<div class="sub-title">Let\'s spell it out together:</div>', unsafe_allow_html=True)
    spell_word("CONFOUNDING")

    st.markdown(
        """
        <div class="station-card">
        <h3>🧠 What Is a Confounding Variable?</h3>
        <p>A confounding variable is something outside the real question that sneaks in and changes
        your answer - without you even noticing. If you can see your neighbor's answer before you
        give yours, their answer can confound - or mix up - your own true answer.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    read_aloud(
        "Closing your eyes removed that confounding variable - peeking, copying, or just being "
        "influenced by what your neighbor picked. That way, your answer was pure. It was actually "
        "yours."
    )

    read_aloud(
        "Here's the real question I want you thinking about for the rest of this year: when it's "
        "time for real math work - a quiz, an independent practice page, a test - will you give "
        "that same pure effort? The kind where your answer is really yours, built from your own "
        "thinking? Or will you get confounded - influenced by what a friend is doing, what answer "
        "someone whispers, or what you think everyone else picked? The eyes-closed activity wasn't "
        "really about fruit or animals. It was practice for something bigger: trusting your own "
        "thinking, even when you can't see what everyone else is doing."
    )

    st.markdown(
        """
        <div class="warn-box">💬 Turn and talk: Can you think of a time in class when you were
        confounded by someone else's answer, on purpose or by accident? What could you do
        differently next time?</div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
elif slide == 4:
    st.markdown('<span class="pace-badge">18-22 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Today: Getting to Know You</div>', unsafe_allow_html=True)
    read_aloud(
        "Today we build a shape - your own choice of one of five - and turn it into a survey about "
        "you. Instead of writing your answers in words, you're going to draw them."
    )
    st.markdown(
        """
        **Today you will:**
        - Use **graph paper, a pencil, and a ruler** to build one grade-6 geometric shape.
        - **Section** your shape into equal, symmetrical, or sequential parts, depending on the shape.
        - Answer a survey question in each section - **by drawing a picture**, not writing words.
        """
    )
    st.write("There are 5 shape stations today. Your table will be assigned one.")

# ============================================================
def shape_station(tag, title, sections, theme, questions, build_note):
    st.markdown(f'<span class="shape-tag">{tag}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="big-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title">{theme}</div>', unsafe_allow_html=True)
    st.write(f"Divide your {title.lower()} into **{sections} sections**. In each section, draw your answer:")
    for i, q in enumerate(questions, start=1):
        st.markdown(f'<div class="q-line"><b>{i}.</b> {q}</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="warn-box">📐 Build note: {build_note}</div>
        """,
        unsafe_allow_html=True,
    )


if slide == 5:
    st.markdown('<span class="pace-badge">Station</span>', unsafe_allow_html=True)
    shape_station(
        "STATION 1",
        "Hexagon",
        6,
        "All About My Faves",
        [
            "Your favorite color",
            "Your favorite music artist or song",
            "Your favorite food",
            "An invention you love - real, or one you wish existed",
            "A favorite place you've been",
            "Your favorite way to spend a weekend",
        ],
        "A hexagon has 6 sides. Draw it on your graph paper, then divide it into 6 roughly equal wedges from the center - like slicing a pizza.",
    )

elif slide == 6:
    st.markdown('<span class="pace-badge">Station</span>', unsafe_allow_html=True)
    shape_station(
        "STATION 2",
        "Pentagon",
        5,
        "My Family & Home",
        [
            "How many siblings you have",
            "Which number you are among your siblings (oldest, youngest, middle, only child)",
            "A pet you have, or wish you had",
            "Someone in your family you look up to",
            "A tradition your family celebrates",
        ],
        "A pentagon has 5 sides. Divide it into 5 sections from a center point, like the Pent Structure we've used before.",
    )

elif slide == 7:
    st.markdown('<span class="pace-badge">Station</span>', unsafe_allow_html=True)
    shape_station(
        "STATION 3",
        "Parallelogram",
        4,
        "Who I Am Becoming",
        [
            "A skill you want to get better at this year",
            "A hobby or activity you love",
            "A subject you're curious about",
            "Something you're proud of",
        ],
        "This is the same shape we've been building all week for area - a parallelogram, divided into 4 equal sections with two straight lines through the middle.",
    )

elif slide == 8:
    st.markdown('<span class="pace-badge">Station</span>', unsafe_allow_html=True)
    shape_station(
        "STATION 4",
        "Trapezoid",
        3,
        "Quick Takes",
        [
            "One word that describes you",
            "Morning person or night person?",
            "A book, show, or game you can't stop thinking about",
        ],
        "Draw a trapezoid, then split it into 3 sections in a row, left to right - one straight cut on each side.",
    )

elif slide == 9:
    st.markdown('<span class="pace-badge">Station</span>', unsafe_allow_html=True)
    shape_station(
        "STATION 5 — GROWTH MINDSET",
        "Octagon: STOP & Grow",
        8,
        "A Positive Mindset Survey",
        [
            "Draw a time you tried something hard.",
            "Draw how your face looks when you make a mistake and keep trying.",
            "Draw a goal you're working toward this year.",
            "Draw someone who encourages you.",
            "Draw what the word \"yet\" means to you.",
            "Draw a mistake that taught you something.",
            "Draw how you help a friend who feels stuck.",
            "Draw one word for how you want to feel in math class this year.",
        ],
        "An octagon has 8 sides, just like a STOP sign - fitting, since this shape is all about pausing to notice your own growth. Divide it into 8 wedges from the center.",
    )

# ============================================================
elif slide == 10:
    st.markdown('<span class="pace-badge">22-45 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">How to Build Your Shape</div>', unsafe_allow_html=True)
    read_aloud(
        "No matter which shape your table gets, the steps are the same. Let's walk through them "
        "together before you start."
    )
    steps = [
        "Get one sheet of graph paper, a pencil, and a ruler.",
        "Using your ruler, draw your assigned shape as large and accurate as you can.",
        "Divide your shape into its sections - equal, symmetrical, or sequential, depending on the shape - using straight ruler lines.",
        "Read each survey question for your shape, one section at a time.",
        "In that section, draw a picture that answers the question. No words - just your drawing.",
        "When every section has a drawing, you're done!",
    ]
    for i, s in enumerate(steps, start=1):
        st.markdown(
            f"""
            <div class="step-row">
                <div class="step-num">{i}</div>
                <div class="step-text">{s}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
elif slide == 11:
    st.markdown('<span class="pace-badge">45-50 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Turn It In</div>', unsafe_allow_html=True)
    read_aloud(
        "Bring your finished shape to the front and place it in the white box for your class number. "
        "We'll be hanging more exceptional work again very soon."
    )

# ============================================================
elif slide == 12:
    st.markdown('<span class="pace-badge">Bonus</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Where Your Answers Go</div>', unsafe_allow_html=True)
    read_aloud(
        "Here's a secret about today: none of this disappears into a box forever. All year long, "
        "I'm going to use your favorite music artist, your siblings, your invention, your skill you "
        "want to learn - all of it - to build real word problems in our i-Ready lessons. When you "
        "see a problem this year and think, wait, that sounds like me, that's not an accident. "
        "That's your own math class, built out of you."
    )
    st.markdown(
        """
        <div class="station-card">
        <h3>🔁 Survey Answers &#8594; Personalized Word Problems</h3>
        <p>Everything your class draws in the Hexagon, Pentagon, Parallelogram, Trapezoid, and
        Octagon stations becomes real material for future i-Ready word problems - personalized so
        they're actually relevant to the students solving them, not generic names and situations
        from a textbook.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
elif slide == 13:
    st.markdown('<span class="pace-badge">Reference</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Standards Covered Today</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">Mathematics</div>', unsafe_allow_html=True)
    math_standards = [
        ("6.G.A.1", "Find the area of shapes composed of triangles, quadrilaterals, and other polygons (built on the same shapes used at each station)."),
        ("6.G.A.3", "Draw polygons and use coordinates/side lengths to describe them."),
        ("6.G.A.4", "Represent and reason about 2-D figures, including their symmetry and how they can be divided into parts."),
        ("6.SP.B.4", "Display numerical data, used today in the Exceptional Work bar chart."),
        ("6.SP.B.5", "Summarize a data set in relation to its context (the 12-out-of-42 discussion)."),
        ("6.RP.A.3c", "Find a percent of a quantity, used to turn 12 out of 42 into a percent."),
        ("MP4, MP5, MP6", "Model with mathematics, use tools strategically, and attend to precision - the same practices from Day One, applied again today."),
    ]
    for code, desc in math_standards:
        st.markdown(f'<div class="ican-box"><span class="ican-tag">{code}</span>{desc}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">English Language Arts</div>', unsafe_allow_html=True)
    ela_standards = [
        ("SL.6.1", "Engage effectively in a range of collaborative discussions (today's data turn-and-talk)."),
        ("W.6.3", "Develop real experiences using effective description - here, expressed through drawing instead of writing."),
        ("L.6.1", "Use conventions of standard English when labeling and discussing shapes and sections."),
    ]
    for code, desc in ela_standards:
        st.markdown(f'<div class="ican-box"><span class="ican-tag">{code}</span>{desc}</div>', unsafe_allow_html=True)

    st.markdown('<div class="sub-title">Social-Emotional Learning</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="ican-box"><span class="ican-tag">SEL</span>
        The Octagon: STOP & Grow station connects to the CASEL core competencies of
        self-awareness and self-management, and to Carol Dweck's research on growth mindset -
        the idea that abilities can be developed through effort, not just fixed traits.</div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(
        "Note: the survey questions themselves (favorite color, siblings, music, etc.) are "
        "intentionally not tied to a specific math content standard - they are a vehicle for "
        "community-building and ELA/SEL skills, carried inside a math-standard-aligned shape."
    )

# ============================================================
elif slide == 14:
    st.markdown('<span class="pace-badge">50-55 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">What You Just Did</div>', unsafe_allow_html=True)

    icans = [
        ("DATA", "I can use a fraction, decimal, and percent to describe part of a group."),
        ("CONSTRUCTION", "I can construct a grade-6 geometric shape and divide it into equal, symmetrical, or sequential sections."),
        ("REPRESENTATION", "I can represent information about myself using a drawing instead of words."),
        ("MINDSET", "I can describe what a growth mindset looks like, using my own words and pictures."),
    ]
    for tag, text in icans:
        st.markdown(f'<div class="ican-box"><span class="ican-tag">{tag}</span>{text}</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="reflect-box">
        Yesterday, twelve of you were on the wall. Today, every single one of you built something
        real - a shape, a survey, a piece of who you are, made with a ruler and a pencil.
        <br><br>
        <b>Are you starting to believe that this class is going to be a W all year, not just on
        Day One?</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="warn-box">
        📓 Journal It: Copy the four statements above into your math journal, word for word.
        Then, in your workbook, write 2-3 sentences for each one describing exactly what you did
        today to earn it - be specific about the steps you took, not just "I did it."
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")
nav1, nav2, nav3 = st.columns([1, 3, 1])
with nav1:
    st.button("⬅ Back", on_click=go_prev, disabled=(slide == 0), use_container_width=True, key="d2_back")
with nav3:
    st.button("Next ➡", on_click=go_next, disabled=(slide == len(SLIDES) - 1), use_container_width=True, key="d2_next")
