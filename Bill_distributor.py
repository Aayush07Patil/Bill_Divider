import streamlit as st
import pandas as pd

if 'participants_list' not in st.session_state:
    st.session_state['participants_list'] = []
if 'items_list' not in st.session_state:
    st.session_state['items_list'] = []

def input_participants():
    participants_input = st.text_input("Enter Participant Name")
    if st.button("Add Participant"):
        if participants_input:
            st.session_state['participants_list'].append(participants_input)
            st.write(f"{participants_input} added to the participants list")
        else:
            st.warning("Enter a name")
    if st.button("Submit Participants"):
        st.session_state['participants_complete'] = True

def input_items():
    item_name = st.text_input("Enter Item Name")
    item_value = st.number_input("Enter Item Value", min_value=0.0, format="%.2f")
    participants_in_item = st.multiselect("Select Participants for this Item", st.session_state['participants_list'])

    if st.button("Add Item"):
        if item_name and item_value > 0 and participants_in_item:
            st.session_state['items_list'].append({
                'item_name': item_name,
                'item_value': item_value,
                'participants': participants_in_item
            })
            st.write(f"Item '{item_name}' with value {item_value} added for participants {participants_in_item}")
        else:
            st.warning("Enter item details and select participants")
    if st.button("Submit Items"):
        st.session_state['items_complete'] = True

def calculate_shares():
    final_distribution = {participant: 0.0 for participant in st.session_state['participants_list']}
    
    for item in st.session_state['items_list']:
        split_value = item['item_value'] / len(item['participants'])
        for participant in item['participants']:
            final_distribution[participant] += split_value

    final_distribution_df = pd.DataFrame(list(final_distribution.items()), columns=['Participant', 'Total Amount Due'])
    st.write(final_distribution_df)
            
if __name__ == "__main__":
    input_participants()
    input_items()
    calculate_shares()