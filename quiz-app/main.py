import streamlit as st 
import random 
import time 


st.title("📝 Quiz Application")
st.title("HAND HYGEIN")


questions = [
    {
        "question": "1: What is the primary purpose of hand hygiene in healthcare?",
        "options": ["A: To prevent patient falls","To prevent medication errors","B: To prevent transmission of microorganisms","C: To improve patient satisfaction"],
        "answer": "To prevent transmission of microorganisms",
    },
    {
        "question": "2: When should healthcare workers perform hand hygiene?",
        "options": ["A: Only after patient contact","B: Only before patient contact","C: Before and after patient contact","D: Only when hands are visibly soiled"],
        "answer": "Before and after patient contact",
    },
    {
        "question": "3: What is the most effective method of hand hygiene?",
        "options": ["A: Washing hands with soap and water","B: Using hand sanitizer","C: Wearing gloves","D: Using antiseptic wipes"],
        "answer": "Washing hands with soap and water (when hands are visibly soiled) or B) Using hand sanitizer (when hands are not visibly soiled)",
    },
    {
        "question": "4: How long should healthcare workers wash their hands?",
        "options": ["A: 10 seconds","B: 20-30 seconds","C: 40 seconds","D: 1 minute"
],
        "answer": "20-30 seconds",
    },
    {
        "question":"5 What is the correct technique for handwashing?",
        "options": ["A: Rubbing hands together quickly","B: Using hot water only","C: Lathering soap and rubbing all surfaces","D: Rinsing hands quickly"],
        "answer": "Karachi",
    },
    {
        "question":"6: When should healthcare workers use hand sanitizer?",
        "options":["A: When hands are visibly soiled","B: When hands are not visibly soiled","C: After removing gloves","D: Before donning gloves"],
        "answer":"When hands are not visibly soiled"
        
    },
    {
     "question":"7: What is the minimum alcohol concentration required for hand sanitizer to be effective?",
     "options":["A: 40%","B: 50%","C: 60%","D: 70%"],
     "answer":"60%"  
    },
      {
     "question":"8: Can hand sanitizer be used on hands that are visibly soiled?",
     "options":["A: Yes","B: No","C: Only if hands are washed first","D: Only if hands are rinsed first"],
     "answer":"No"  
    },
        {
     "question":"9: How often should healthcare workers perform hand hygiene?",
     "options":["A: Only when entering a patient room","B: Only when exiting a patient room","C: Frequently throughout the day","D: Only when performing invasive procedures"],
     "answer":"Frequently throughout the day"  
    },
          {
     "question":"10. What is the role of hand hygiene in preventing healthcare-associated infections?",
     "options":["A: It has no impact","B: It reduces the risk of transmission","C: It eliminates the risk of transmission","D: It increases the risk of transmission"],
     "answer":"B: It reduces the risk of transmission"  
    },
            {
     "question":"11. When should healthcare workers wear gloves?",
     "options":["A: Only when performing invasive procedures","B: Only when contact with bodily fluids is anticipated","C: For all patient interactions","D: Never"],
     "answer":"B)Only when contact with bodily fluids is anticipated"  
    },
              {
     "question":"12. Can hand hygiene prevent the transmission of antibiotic-resistant organisms?",
     "options":["A) Yes","B) No","C) Only if hands are washed with soap and water","D) Only if hands are sanitized with alcohol-based hand rub"],
     "answer":"A) Yes"  
    },
                {
     "question":"13. How can healthcare workers ensure effective hand hygiene?",
     "options":["A) By following hospital policies","B) By using hand sanitizer frequently","C) By washing hands only when visibly soiled","D) By relying on others to perform hand hygiene"],
     "answer":"A) By following hospital policies"  
    },
                  
   
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
  
    time.sleep(5)

    st.session_state.current_question = random.choice(questions)

    st.rerun()