import streamlit as st
import math
import re

# Page configuration
st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for calculator styling
st.markdown("""
<style>
    .calculator-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 2rem auto;
        max-width: 500px;
    }
    .display {
        background-color: #1a1a1a;
        color: #00ff00;
        padding: 1.5rem;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        font-size: 2rem;
        text-align: right;
        margin-bottom: 1rem;
        border: 2px solid #333;
        min-height: 80px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    .button-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.5rem;
    }
    .calc-button {
        background: linear-gradient(145deg, #e6e6e6, #ffffff);
        border: none;
        border-radius: 10px;
        padding: 1rem;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 5px 5px 10px #d1d1d1, -5px -5px 10px #ffffff;
    }
    .calc-button:hover {
        transform: translateY(-2px);
        box-shadow: 7px 7px 15px #d1d1d1, -7px -7px 15px #ffffff;
    }
    .operator {
        background: linear-gradient(145deg, #ff9500, #ff8000);
        color: white;
    }
    .equals {
        background: linear-gradient(145deg, #007aff, #0056cc);
        color: white;
    }
    .clear {
        background: linear-gradient(145deg, #ff3b30, #cc2e25);
        color: white;
    }
    .function {
        background: linear-gradient(145deg, #34c759, #28a745);
        color: white;
    }
    .main-header {
        text-align: center;
        color: #333;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .history-section {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

class Calculator:
    def __init__(self):
        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        self.should_reset = False
        self.history = []
    
    def add_to_input(self, value):
        if self.should_reset:
            self.current_input = ""
            self.should_reset = False
        self.current_input += str(value)
    
    def clear(self):
        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        self.should_reset = False
    
    def delete_last(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
    
    def set_operation(self, op):
        if self.current_input:
            if self.previous_input and self.operation:
                self.calculate()
            self.previous_input = self.current_input
            self.operation = op
            self.current_input = ""
    
    def calculate(self):
        if not self.previous_input or not self.current_input or not self.operation:
            return
        
        try:
            prev = float(self.previous_input)
            current = float(self.current_input)
            
            if self.operation == "+":
                result = prev + current
            elif self.operation == "-":
                result = prev - current
            elif self.operation == "×":
                result = prev * current
            elif self.operation == "÷":
                if current == 0:
                    result = "Error: Division by zero"
                else:
                    result = prev / current
            elif self.operation == "^":
                result = prev ** current
            else:
                result = current
            
            # Add to history
            expression = f"{self.previous_input} {self.operation} {self.current_input}"
            self.history.append(f"{expression} = {result}")
            
            self.current_input = str(result)
            self.previous_input = ""
            self.operation = None
            self.should_reset = True
            
        except Exception as e:
            self.current_input = "Error"
            self.should_reset = True
    
    def scientific_function(self, func):
        if not self.current_input:
            return
        
        try:
            value = float(self.current_input)
            
            if func == "sin":
                result = math.sin(math.radians(value))
            elif func == "cos":
                result = math.cos(math.radians(value))
            elif func == "tan":
                result = math.tan(math.radians(value))
            elif func == "log":
                result = math.log10(value) if value > 0 else "Error"
            elif func == "ln":
                result = math.log(value) if value > 0 else "Error"
            elif func == "sqrt":
                result = math.sqrt(value) if value >= 0 else "Error"
            elif func == "square":
                result = value ** 2
            elif func == "factorial":
                if value == int(value) and value >= 0:
                    result = math.factorial(int(value))
                else:
                    result = "Error"
            elif func == "1/x":
                result = 1 / value if value != 0 else "Error"
            else:
                result = value
            
            if result != "Error":
                self.history.append(f"{func}({value}) = {result}")
            
            self.current_input = str(result)
            self.should_reset = True
            
        except Exception as e:
            self.current_input = "Error"
            self.should_reset = True

def initialize_calculator():
    """Initialize calculator in session state"""
    if 'calculator' not in st.session_state:
        st.session_state.calculator = Calculator()

def create_calculator_interface():
    """Create the main calculator interface"""
    calc = st.session_state.calculator
    
    st.markdown('<h1 class="main-header">🧮 Calculator</h1>', unsafe_allow_html=True)
    
    # Calculator container
    st.markdown('<div class="calculator-container">', unsafe_allow_html=True)
    
    # Display
    display_text = calc.current_input if calc.current_input else "0"
    st.markdown(f'<div class="display">{display_text}</div>', unsafe_allow_html=True)
    
    # Scientific functions row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("sin", key="sin", use_container_width=True):
            calc.scientific_function("sin")
    with col2:
        if st.button("cos", key="cos", use_container_width=True):
            calc.scientific_function("cos")
    with col3:
        if st.button("tan", key="tan", use_container_width=True):
            calc.scientific_function("tan")
    with col4:
        if st.button("log", key="log", use_container_width=True):
            calc.scientific_function("log")
    
    # More scientific functions
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("ln", key="ln", use_container_width=True):
            calc.scientific_function("ln")
    with col2:
        if st.button("√", key="sqrt", use_container_width=True):
            calc.scientific_function("sqrt")
    with col3:
        if st.button("x²", key="square", use_container_width=True):
            calc.scientific_function("square")
    with col4:
        if st.button("x!", key="factorial", use_container_width=True):
            calc.scientific_function("factorial")
    
    # Clear and delete row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("C", key="clear", use_container_width=True):
            calc.clear()
    with col2:
        if st.button("⌫", key="delete", use_container_width=True):
            calc.delete_last()
    with col3:
        if st.button("1/x", key="reciprocal", use_container_width=True):
            calc.scientific_function("1/x")
    with col4:
        if st.button("^", key="power", use_container_width=True):
            calc.set_operation("^")
    
    # Number pad and operations
    # Row 1: 7, 8, 9, ÷
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("7", key="7", use_container_width=True):
            calc.add_to_input("7")
    with col2:
        if st.button("8", key="8", use_container_width=True):
            calc.add_to_input("8")
    with col3:
        if st.button("9", key="9", use_container_width=True):
            calc.add_to_input("9")
    with col4:
        if st.button("÷", key="divide", use_container_width=True):
            calc.set_operation("÷")
    
    # Row 2: 4, 5, 6, ×
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("4", key="4", use_container_width=True):
            calc.add_to_input("4")
    with col2:
        if st.button("5", key="5", use_container_width=True):
            calc.add_to_input("5")
    with col3:
        if st.button("6", key="6", use_container_width=True):
            calc.add_to_input("6")
    with col4:
        if st.button("×", key="multiply", use_container_width=True):
            calc.set_operation("×")
    
    # Row 3: 1, 2, 3, -
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("1", key="1", use_container_width=True):
            calc.add_to_input("1")
    with col2:
        if st.button("2", key="2", use_container_width=True):
            calc.add_to_input("2")
    with col3:
        if st.button("3", key="3", use_container_width=True):
            calc.add_to_input("3")
    with col4:
        if st.button("-", key="subtract", use_container_width=True):
            calc.set_operation("-")
    
    # Row 4: 0, ., =, +
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("0", key="0", use_container_width=True):
            calc.add_to_input("0")
    with col2:
        if st.button(".", key="decimal", use_container_width=True):
            if "." not in calc.current_input:
                calc.add_to_input(".")
    with col3:
        if st.button("=", key="equals", use_container_width=True):
            calc.calculate()
    with col4:
        if st.button("+", key="add", use_container_width=True):
            calc.set_operation("+")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # History section
    if calc.history:
        st.markdown('<div class="history-section">', unsafe_allow_html=True)
        st.markdown("### 📝 Calculation History")
        for i, entry in enumerate(reversed(calc.history[-10:])):  # Show last 10 entries
            st.text(f"{len(calc.history) - i}: {entry}")
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application function"""
    initialize_calculator()
    create_calculator_interface()
    
    # Sidebar with additional features
    with st.sidebar:
        st.header("🔧 Calculator Features")
        
        st.markdown("### 📊 Functions Available")
        st.markdown("""
        - **Basic Operations**: +, -, ×, ÷
        - **Scientific Functions**: sin, cos, tan, log, ln
        - **Advanced**: √, x², x!, 1/x, x^y
        - **Memory**: Calculation history
        """)
        
        st.markdown("### 🎯 How to Use")
        st.markdown("""
        1. Click numbers to input values
        2. Use operators for calculations
        3. Press = to see results
        4. Use scientific functions for advanced math
        5. View history for previous calculations
        """)
        
        # Clear history button
        if st.button("🗑️ Clear History"):
            st.session_state.calculator.history = []
            st.rerun()

if __name__ == "__main__":
    main() 