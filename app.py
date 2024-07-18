import streamlit as st
import pandas as pd
    
final_distribution_df = pd.DataFrame(columns=['Participants', 'Total Amount'])

def participant_input_func():
    global participants_list
    participants_list = []
    participants_input = st.text_input("PARTICIPANTS","")
    if len(participants_input) > 0:
        participants_list.append(participants_input)
        st.write(f"{participants_input} added to the participants list")
    else:
        st.warning("Enter text")
    
    participants_submit_button = st.button("Submit", key='submit_button')
    if participants_submit_button:
        st.write('List Complete',participants_list)

if __name__ == "__main__":
    participant_input_func()
    

