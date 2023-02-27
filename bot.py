import streamlit as st

# Define the calculator function
def calculator(num1, operator, num2):
    # Perform the operation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2
    else:
        result = 'Invalid operator'
        
    return result

# Define the Streamlit app
def app():
    st.title('Arithmetic Calculator Chatbot')
    
    # Get the name of the user
    name = st.text_input('What is your name?',placeholder="Enter your name here")
    
    if name:
        # Start the conversation
        st.write(f'Hi {name}, welcome to the Arithmetic Calculator Chatbot!')
        st.write(f'You can perform the arithmetic calculations below!!!')
        # Display the available operations
                
        # Ask for the first operand
        num1 = st.empty()
        num1_placeholder = num1.text_input('Please enter the first operand:', value='')
        
        # Ask for the operator
        operator = st.selectbox('Please select an operator:', ['+', '-', '*', '/'])
        
        # Ask for the second operand
        num2 = st.empty()
        num2_placeholder = num2.text_input('Please enter the second operand:', value='')
        
        # Perform the operation using the calculator function and display the result
        if num1_placeholder and num2_placeholder:
            num1_value = float(num1_placeholder)
            num2_value = float(num2_placeholder)
            
            if num2_value != 0 or operator != '/':
                result = calculator(num1_value, operator, num2_value)
                st.write(f'The result is: {result}')
            else:
                st.write('Error: Division by zero')

# Start the Streamlit app
if __name__ == '__main__':
    app()