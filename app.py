import streamlit as st
import base64

# Page settings
st.set_page_config(
    page_title="AI Study Agent",
    page_icon="🤖",
    layout="wide"
)

# Background image
try:
    with open("study_background.jpg", "rb") as file:
        image = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(
                "data:image/jpeg;base64,{image}"
            );
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        [data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.90);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

except FileNotFoundError:
    st.warning("Background image not found. Check study_background.jpg")


# Sidebar
st.sidebar.title("🤖 AI Study Agent")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "🏠 Home",
        "📚 Study Planner",
        "🧠 AI Tutor",
        "❓ Quiz",
        "📊 Progress",
        "📄 Notes Analyzer"
    ]
)


# Home
if menu == "🏠 Home":

    st.title("🤖 AI Study Agent")
    st.subheader("Your Personal AI Study Assistant")

    st.write(
        "Study smarter, plan better and track your progress."
    )

    st.divider()

    st.header("🚀 Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📚 Study Planner")
        st.write("Create your daily study plan.")

        st.info("🧠 AI Tutor")
        st.write("Ask questions and learn concepts.")

        st.info("❓ Quiz")
        st.write("Test your knowledge.")

    with col2:
        st.info("📊 Progress Tracker")
        st.write("Track your study progress.")

        st.info("📄 Notes Analyzer")
        st.write("Upload and analyze your notes.")

    st.success("🎯 Start studying and achieve your goals!")


# Study Planner
elif menu == "📚 Study Planner":

    st.title("📚 Study Planner")

    subject = st.text_input("Enter your subject")

    hours = st.number_input(
        "Study hours",
        min_value=1,
        max_value=12,
        value=2
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("Create Study Plan"):

        if subject:

            st.subheader("🗓️ Your Study Plan")

            st.write(f"📖 Subject: {subject}")
            st.write(f"⏰ Study Time: {hours} hours")
            st.write(f"📊 Difficulty: {difficulty}")

            st.write("1️⃣ Learn basic concepts")
            st.write("2️⃣ Study important topics")
            st.write("3️⃣ Practice questions")
            st.write("4️⃣ Revise the topics")

            st.success("✅ Study plan created!")

        else:
            st.warning("Please enter a subject.")


# AI Tutor
elif menu == "🧠 AI Tutor":

    st.title("🧠 AI Tutor")

    question = st.text_area(
        "Ask your question",
        placeholder="Example: What is Python?"
    )

    if st.button("Ask AI"):

        if question:

            q = question.lower()

            if "python" in q:

                st.success(
                    "🐍 Python is a programming language "
                    "used for AI, Data Science and web development."
                )

            elif "ai" in q:

                st.success(
                    "🤖 AI means Artificial Intelligence. "
                    "It enables computers to perform intelligent tasks."
                )

            elif "data science" in q:

                st.success(
                    "📊 Data Science involves collecting, "
                    "analyzing and interpreting data."
                )

            elif "django" in q:

                st.success(
                    "🌐 Django is a Python framework "
                    "used to build web applications."
                )

            else:

                st.info(
                    "💡 Try asking about Python, AI, "
                    "Data Science or Django."
                )

        else:
            st.warning("Please enter your question.")


# Quiz
elif menu == "❓ Quiz":

    st.title("❓ Study Quiz")

    st.subheader("Question 1")

    answer = st.radio(
        "What is Python?",
        [
            "A) Programming Language",
            "B) Operating System",
            "C) Database",
            "D) Web Browser"
        ]
    )

    if st.button("Check Answer"):

        if answer == "A) Programming Language":
            st.success("🎉 Correct Answer!")

        else:
            st.error("❌ Wrong Answer!")
            st.info(
                "Correct answer: A) Programming Language"
            )


# Progress
elif menu == "📊 Progress":

    st.title("📊 My Progress")

    progress = st.slider(
        "Study Progress",
        0,
        100,
        0
    )

    st.progress(progress)

    st.write(
        f"📈 Your Progress: {progress}%"
    )

    if progress == 100:
        st.success("🎉 Study plan completed!")

    elif progress >= 50:
        st.info("👍 Great progress! Keep going!")

    else:
        st.warning("💪 Keep studying!")


# Notes Analyzer
elif menu == "📄 Notes Analyzer":

    st.title("📄 Notes Analyzer")

    uploaded_file = st.file_uploader(
        "Upload your notes",
        type=["txt"]
    )

    if uploaded_file is not None:

        notes = uploaded_file.read().decode("utf-8")

        st.subheader("📖 Your Notes")

        st.write(notes)

        words = notes.split()

        st.subheader("📊 Notes Information")

        st.write(
            f"📝 Total Words: {len(words)}"
        )

        st.success(
            "✅ Notes analyzed successfully!"
        )