import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_ifuszxx3.json"
lottie_hello = load_lottieurl(lottie_url_hello)

    
css = """

p {
    font-size: 25px;
    line-height: 1.5;
    color: white;
}

.typewriter-text {
  animation: typing 1s steps(30, end) 1s 1 normal both;
  white-space: nowrap;
  overflow: hidden;
  font-size: 20px;
  font-family: "cursive";
  font-style: oblique;
  font-weight: bold;
  color: #a5a6a8;
}

@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

"""

# Set the CSS style
st.write(f'<style>{css}</style>', unsafe_allow_html=True)
text = "Hello, world! This is an example of typing animation using CSS in Streamlit."



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
import time
def app():
    st_lottie(lottie_hello, height="150px",key="hello")
    st.title('Arithmetic Calculator Chatbot') 
    
    # Get the name of the user
    name = st.text_input('What is your name?',placeholder="Enter your name here")
    
    if name:
        # Start the conversation
        
        st.markdown(f'<div class="typewriter-text">Hi {name}, welcome to the Arithmetic Calculator Chatbot!</div>', unsafe_allow_html=True)
        time.sleep(0.5)
    
        st.markdown(f'<div class="typewriter-text">You can perform the arithmetic calculations below!!!</div>', unsafe_allow_html=True)
        
        time.sleep(2.5)
        # Display the available operations
        st.write('\n')        
        # Ask for the first operand
        num1 = st.empty()
        num1_placeholder = num1.text_input(f'{name} please enter the first operand:', value='',placeholder="Enter the first operand")
        
        # Ask for the operator
        operator = st.selectbox(f'{name} please select an operator:', ['+', '-', '*', '/'])
        
        # Ask for the second operand
        num2 = st.empty()
        num2_placeholder = num2.text_input(f'{name} please enter the second operand:', value='',placeholder="Enter the second operand")
        
        # Perform the operation using the calculator function and display the result
        if num1_placeholder and num2_placeholder:
            num1_value = float(num1_placeholder)
            num2_value = float(num2_placeholder)
            
            if num2_value != 0 or operator != '/':
                result = calculator(num1_value, operator, num2_value)
                st.write(f'The result is: {result}')
            else:
                st.write('Error: Division by zero')



       
    
if __name__ == '__main__':
    app()
    

    
    

