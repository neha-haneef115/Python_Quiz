import streamlit as st
import random

questions = [
    {
        "question": "Which of the following statements will create a list of squares from 1 to 10?",
        "options": [
            "[x * x for x in range(1, 11)]",
            "[x ** 2 for x in range(0, 10)]",
            "range(x * x, 10)",
            "list(x**2 for x in range(1,10))"
        ],
        "answer": 0
    },
    {
        "question": "What will be the output of: print('a' * 3 + 'b' * 2)?",
        "options": ["aaabb", "aaabbb", "ab", "a3b2"],
        "answer": 0
    },
    {
        "question": "What is the result of: [1, 2] + [3, 4]?",
        "options": ["[1, 2, 3, 4]", "[4, 6]", "[1, 2, [3, 4]]", "Error"],
        "answer": 0
    },
    {
        "question": "Which method can convert a string to lowercase?",
        "options": ["lowercase()", "strtolower()", "lower()", "tolower()"],
        "answer": 2
    },
    {
        "question": "What does this return: type([])?",
        "options": ["<class 'list'>", "list", "array", "<list>"],
        "answer": 0
    },
    {
        "question": "What will the output be? bool([])",
        "options": ["True", "False", "None", "Error"],
        "answer": 1
    },
    {
        "question": "What is the result of: 5 // 2?",
        "options": ["2", "2.5", "3", "Error"],
        "answer": 0
    },
    {
        "question": "Which one is a valid Python set?",
        "options": [
            "[1, 2, 3]",
            "{1, 2, 3}",
            "(1, 2, 3)",
            "<1, 2, 3>"
        ],
        "answer": 1
    },
    {
        "question": "How to get the number of key-value pairs in a dictionary?",
        "options": ["dict.count()", "len(dict)", "dict.length()", "count(dict)"],
        "answer": 1
    },
    {
        "question": "What will be the output: 'Python'[0]?",
        "options": ["P", "Y", "n", "Error"],
        "answer": 0
    },
    {
        "question": "Which loop will execute at least once even if the condition is false?",
        "options": ["while", "for", "do-while (not in Python)", "None"],
        "answer": 3
    },
    {
        "question": "What is the result of this expression: not (True and False)?",
        "options": ["True", "False", "None", "Error"],
        "answer": 0
    },
    {
        "question": "What does the 'pass' statement do?",
        "options": ["Skips execution", "Ends program", "Does nothing", "Returns False"],
        "answer": 2
    },
    {
        "question": "Which of the following is NOT a valid Python data type?",
        "options": ["list", "tuple", "dict", "record"],
        "answer": 3
    },
    {
        "question": "Which function returns a sequence of numbers in Python?",
        "options": ["range()", "enumerate()", "list()", "seq()"],
        "answer": 0
    },
    {
        "question": "Which keyword is used to define an anonymous function?",
        "options": ["lambda", "anonymous", "def", "function"],
        "answer": 0
    },
    {
        "question": "How to handle a division by zero exception?",
        "options": [
            "if divisor == 0 then print error",
            "try: x/0 except ZeroDivisionError: pass",
            "catch(ZeroDivisionError)",
            "None of the above"
        ],
        "answer": 1
    },
    {
        "question": "What is the output of: [i for i in range(5) if i % 2 == 0]?",
        "options": ["[1, 2, 3, 4]", "[0, 2, 4]", "[0, 1, 2, 3, 4]", "[2, 4]"],
        "answer": 1
    },
    {
        "question": "Which statement about tuples is true?",
        "options": [
            "They are mutable",
            "They can contain duplicates",
            "They cannot contain other tuples",
            "They are slower than lists"
        ],
        "answer": 1
    },
    {
        "question": "Which built-in function returns the memory address of an object?",
        "options": ["id()", "address()", "mem()", "ptr()"],
        "answer": 0
    },
    {
        "question": "Which is true about Python functions?",
        "options": [
            "They can return multiple values",
            "They can be passed as arguments",
            "They can be nested",
            "All of the above"
        ],
        "answer": 3
    },
    {
        "question": "Which will raise a syntax error?",
        "options": [
            "x = 10\nif x > 5:\n print(x)",
            "for i in range(5): print(i)",
            "def func(x): return x * 2",
            "x == 5"
        ],
        "answer": 3
    },
    {
        "question": "What is the output of: 3 < 4 and 5 > 6?",
        "options": ["True", "False", "Error", "None"],
        "answer": 1
    },
    {
        "question": "Which operator is used to concatenate two strings?",
        "options": ["+", "&", "*", "."],
        "answer": 0
    },
    {
        "question": "How do you get keys from a dictionary?",
        "options": ["dict.keys()", "dict.values()", "dict.get()", "dict.items()"],
        "answer": 0
    },
    {
        "question": "What is a lambda function?",
        "options": [
            "A function without a name",
            "A recursive function",
            "A deprecated function",
            "None of the above"
        ],
        "answer": 0
    },
    {
        "question": "Which function returns a sorted version of a list?",
        "options": ["sort()", "sorted()", "arrange()", "order()"],
        "answer": 1
    },
    {
        "question": "Which one is an immutable data type?",
        "options": ["list", "dict", "tuple", "set"],
        "answer": 2
    },
    {
        "question": "What happens if you call len() on a number?",
        "options": ["Returns 1", "Raises TypeError", "Returns 0", "Returns length of digits"],
        "answer": 1
    },
    {
        "question": "What does the zip() function do?",
        "options": [
            "Combines multiple iterables element-wise",
            "Compresses strings",
            "Sorts data",
            "None of the above"
        ],
        "answer": 0
    }
]

def main():
    st.set_page_config(
        page_title="Python Concepts Quiz", 
        page_icon="🐍", 
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    st.markdown("""
    <style>
    
    .main {
        padding: 0rem 1rem;
        max-width: 100%;
    }
    
    /* Radio button styling */
    .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
    
    .stRadio label {
        padding: 0.5rem;
        border-radius: 0.3rem;
        margin-bottom: 0.3rem;
        transition: background-color 0.3s;
    }
    
  
    
    
    .subheading {
        text-align: left;
        font-weight: 600;
        font-size: 20px;
        margin-bottom: 30px;
    }
    
   
    @media (prefers-color-scheme: light) {
        .stRadio label:hover {
            background-color: #f7f7f7;
        }
       
        .subheading {
            color: #4B5563;
        }
        .option-container {
            border: 1px solid #e0e0e0;
            background-color: #ffffff;
        }
        .quiz-container {
            background-color: #ffffff;
            color: #31333F;
        }
    }
    
    @media (prefers-color-scheme: dark) {
        .stRadio label:hover {
            background-color: #2d2d2d;
        }
        
        .subheading {
            color: #e0e0e0;
        }
        .option-container {
            border: 1px solid #444444;
            background-color: #1e1e1e;
        }
        .quiz-container {
            background-color: #0e1117;
            color: #ffffff;
        }
      
        .element-container .stTextInput input, 
        .element-container .stTextArea textarea,
        .element-container .stNumberInput input,
        .element-container .stDateInput input {
            background-color: #262730;
            color: #ffffff;
            border-color: #4e4e4e;
        }
        
        .streamlit-expanderHeader {
            background-color: #262730;
            color: #ffffff;
        }
     
        .stAlert {
            border-radius: 4px;
        }
    }
    
   
    @media (max-width: 768px) {
        .main {
            padding: 0rem 0.5rem;
        }
        .stButton button {
            width: 100%;
        }
    }
    
   
    .option-container {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 8px;
    }
    
   
    .stProgress .st-eb {
        background-color: #4CAF50 !important;
    }
    
   
    .quiz-container {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Python Concepts Quiz")
    st.markdown("<div class='subheading'>from step 00_google_colab to step 09_exception_handling</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.quiz_completed = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []
        st.session_state.questions = []
        st.session_state.selected_options = {}
    
    if not st.session_state.quiz_started:
        start_screen()
    elif st.session_state.quiz_completed:
        show_results()
    else:
        display_question()

def start_screen():
    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    st.markdown("### Welcome to the Python Quiz!")
    st.markdown("Test your Python knowledge with this interactive quiz.")
    
    container = st.container()
    
    with container:
        num_questions = st.select_slider(
            "Number of questions:",
            options=[5, 10, 15, 20, 30],
            value=10
        )
        
        st.markdown("### Ready?")
        if st.button("Start Quiz", use_container_width=True, type="primary"):
            if len(questions) < num_questions:
                num_questions = len(questions)
                
            st.session_state.questions = random.sample(questions, num_questions)
            st.session_state.quiz_started = True
            st.session_state.answers = [None] * num_questions
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def display_question():
    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    question_data = st.session_state.questions[st.session_state.current_question]
    total_questions = len(st.session_state.questions)
    
    progress = (st.session_state.current_question) / total_questions
    st.progress(progress)
    
    st.markdown(f"### Question {st.session_state.current_question + 1} of {total_questions}")
    st.markdown(f"**{question_data['question']}**")
    
    
    q_key = f"q{st.session_state.current_question}"
    
    
    if q_key not in st.session_state.selected_options:
        st.session_state.selected_options[q_key] = st.session_state.answers[st.session_state.current_question]
    

    index = None
    if st.session_state.selected_options[q_key] is not None:
        index = question_data["options"].index(st.session_state.selected_options[q_key])
    

    selected_option = st.radio(
        "Select your answer:",
        question_data["options"],
        key=q_key,
        index=index,
        label_visibility="collapsed",
        on_change=option_selected,
        args=(st.session_state.current_question, question_data["options"])
    )
    
    st.markdown("---")
    
    screen_width = 800  
    
  
    if screen_width <= 768: 
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.current_question > 0:
                if st.button("← Previous", use_container_width=True):
                    st.session_state.current_question -= 1
                    st.rerun()
                    
        with col2:
            if st.session_state.current_question < total_questions - 1:
                if st.button("Next →", use_container_width=True):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Submit", use_container_width=True, type="primary"):
                    calculate_score()
                    st.session_state.quiz_completed = True
                    st.rerun()
    else:  
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.session_state.current_question > 0:
                if st.button("← Previous", use_container_width=True):
                    st.session_state.current_question -= 1
                    st.rerun()
                    
        with col3:
            if st.session_state.current_question < total_questions - 1:
                if st.button("Next →", use_container_width=True):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("Submit Quiz", use_container_width=True, type="primary"):
                    calculate_score()
                    st.session_state.quiz_completed = True
                    st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def option_selected(question_index, options):
    
    q_key = f"q{question_index}"
    

    selected_option = st.session_state[q_key]
    

    st.session_state.answers[question_index] = selected_option
    st.session_state.selected_options[q_key] = selected_option
    
    
    if question_index < len(st.session_state.questions) - 1:
        st.session_state.current_question = question_index + 1
        st.rerun()
    elif question_index == len(st.session_state.questions) - 1:
        
        pass

def calculate_score():
    score = 0
    for i, question in enumerate(st.session_state.questions):
        correct_answer = question["options"][question["answer"]]
        if st.session_state.answers[i] == correct_answer:
            score += 1
    st.session_state.score = score

def show_results():
    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    total_questions = len(st.session_state.questions)
    score_percentage = (st.session_state.score / total_questions) * 100
    
    st.markdown("### Quiz Results")
    
    
    screen_width = 800  
    
    if screen_width <= 768:  
        
        st.metric("Score", f"{st.session_state.score}/{total_questions}", f"{score_percentage:.1f}%")
        
        if score_percentage >= 80:
            st.success("Excellent job! You're a Python expert! 🏆")
        elif score_percentage >= 60:
            st.info("Good work! You know Python well! 👍")
        else:
            st.warning("Keep practicing to improve your Python skills! 💪")
            
        st.markdown("### Performance")
        results_chart = {
            "Correct": st.session_state.score,
            "Incorrect": total_questions - st.session_state.score
        }
        st.bar_chart(results_chart)
    else:
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Score", f"{st.session_state.score}/{total_questions}", f"{score_percentage:.1f}%")
            
            if score_percentage >= 80:
                st.success("Excellent job! You're a Python expert! 🏆")
            elif score_percentage >= 60:
                st.info("Good work! You know Python well! 👍")
            else:
                st.warning("Keep practicing to improve your Python skills! 💪")
        
        with col2:
            st.markdown("### Performance")
            results_chart = {
                "Correct": st.session_state.score,
                "Incorrect": total_questions - st.session_state.score
            }
            st.bar_chart(results_chart)
    
    st.markdown("---")
    st.markdown("### Detailed Review")
    
    for i, question in enumerate(st.session_state.questions):
        with st.expander(f"Question {i+1}: {question['question']}"):
            user_answer = st.session_state.answers[i] or "No answer provided"
            correct_answer = question["options"][question["answer"]]
            
            if user_answer == correct_answer:
                st.success(f"Your answer: {user_answer} ✓")
            else:
                st.error(f"Your answer: {user_answer} ✗")
                st.info(f"Correct answer: {correct_answer}")
    
    st.markdown("---")
    if st.button("Take Another Quiz", type="primary", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
