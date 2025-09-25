import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮",
    layout="centered"
)

# Custom CSS for simple calculator
st.markdown("""
<style>
    .simple-calc {
        background: linear-gradient(145deg, #f0f0f0, #ffffff);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        max-width: 400px;
        margin: 0 auto;
    }
    .calc-display {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 1.5rem;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        font-size: 2.5rem;
        text-align: right;
        margin-bottom: 1.5rem;
        border: 2px solid #34495e;
        min-height: 80px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        overflow: hidden;
    }
    .calc-button {
        background: linear-gradient(145deg, #e6e6e6, #ffffff);
        border: none;
        border-radius: 12px;
        padding: 1.2rem 0.8rem;
        font-size: 1.3rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.2s ease;
        box-shadow: 5px 5px 10px #d1d1d1, -5px -5px 10px #ffffff;
        margin: 0.2rem;
        min-height: 60px;
    }
    .calc-button:hover {
        transform: translateY(-2px);
        box-shadow: 7px 7px 15px #d1d1d1, -7px -7px 15px #ffffff;
    }
    .number-btn {
        background: linear-gradient(145deg, #3498db, #2980b9);
        color: white;
    }
    .operator-btn {
        background: linear-gradient(145deg, #e74c3c, #c0392b);
        color: white;
    }
    .equals-btn {
        background: linear-gradient(145deg, #27ae60, #229954);
        color: white;
    }
    .clear-btn {
        background: linear-gradient(145deg, #f39c12, #e67e22);
        color: white;
    }
    .main-title {
        text-align: center;
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

class SimpleCalculator:
    def __init__(self):
        self.current = ""
        self.previous = ""
        self.operation = None
        self.should_reset = False
    
    def add_digit(self, digit):
        if self.should_reset:
            self.current = ""
            self.should_reset = False
        self.current += str(digit)
    
    def add_decimal(self):
        if "." not in self.current:
            self.current += "."
    
    def clear(self):
        self.current = ""
        self.previous = ""
        self.operation = None
        self.should_reset = False
    
    def delete(self):
        if self.current:
            self.current = self.current[:-1]
    
    def set_operation(self, op):
        if self.current:
            if self.previous and self.operation:
                self.calculate()
            self.previous = self.current
            self.operation = op
            self.current = ""
    
    def calculate(self):
        if not self.previous or not self.current or not self.operation:
            return
        
        try:
            prev = float(self.previous)
            curr = float(self.current)
            
            if self.operation == "+":
                result = prev + curr
            elif self.operation == "-":
                result = prev - curr
            elif self.operation == "×":
                result = prev * curr
            elif self.operation == "÷":
                if curr == 0:
                    result = "Error"
                else:
                    result = prev / curr
            else:
                result = curr
            
            self.current = str(result)
            self.previous = ""
            self.operation = None
            self.should_reset = True
            
        except:
            self.current = "Error"
            self.should_reset = True
    
    def get_display(self):
        if self.current:
            return self.current
        elif self.previous:
            return self.previous
        else:
            return "0"

def create_simple_calculator():
    """Create the simple calculator interface"""
    
    # Initialize calculator in session state
    if 'simple_calc' not in st.session_state:
        st.session_state.simple_calc = SimpleCalculator()
    
    calc = st.session_state.simple_calc
    
    st.markdown('<h1 class="main-title">🧮 Simple Calculator</h1>', unsafe_allow_html=True)
    
    # Calculator container
    st.markdown('<div class="simple-calc">', unsafe_allow_html=True)
    
    # Display
    display_text = calc.get_display()
    st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)
    
    # Buttons grid
    # Row 1: Clear, Delete, %, ÷
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("C", key="clear", use_container_width=True):
            calc.clear()
    with col2:
        if st.button("⌫", key="delete", use_container_width=True):
            calc.delete()
    with col3:
        if st.button("%", key="percent", use_container_width=True):
            # Percent functionality
            pass
    with col4:
        if st.button("÷", key="divide", use_container_width=True):
            calc.set_operation("÷")
    
    # Row 2: 7, 8, 9, ×
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("7", key="7", use_container_width=True):
            calc.add_digit("7")
    with col2:
        if st.button("8", key="8", use_container_width=True):
            calc.add_digit("8")
    with col3:
        if st.button("9", key="9", use_container_width=True):
            calc.add_digit("9")
    with col4:
        if st.button("×", key="multiply", use_container_width=True):
            calc.set_operation("×")
    
    # Row 3: 4, 5, 6, -
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("4", key="4", use_container_width=True):
            calc.add_digit("4")
    with col2:
        if st.button("5", key="5", use_container_width=True):
            calc.add_digit("5")
    with col3:
        if st.button("6", key="6", use_container_width=True):
            calc.add_digit("6")
    with col4:
        if st.button("-", key="subtract", use_container_width=True):
            calc.set_operation("-")
    
    # Row 4: 1, 2, 3, +
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("1", key="1", use_container_width=True):
            calc.add_digit("1")
    with col2:
        if st.button("2", key="2", use_container_width=True):
            calc.add_digit("2")
    with col3:
        if st.button("3", key="3", use_container_width=True):
            calc.add_digit("3")
    with col4:
        if st.button("+", key="add", use_container_width=True):
            calc.set_operation("+")
    
    # Row 5: 0, ., = (span 2 columns)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("0", key="0", use_container_width=True):
            calc.add_digit("0")
    with col2:
        if st.button(".", key="decimal", use_container_width=True):
            calc.add_decimal()
    with col3:
        if st.button("=", key="equals", use_container_width=True):
            calc.calculate()
    with col4:
        # Empty space or additional function
        pass
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Instructions
    st.markdown("---")
    st.markdown("### 📝 Instructions")
    st.markdown("""
    - Click numbers to input values
    - Use operators (+, -, ×, ÷) for calculations
    - Press = to see the result
    - Use C to clear and ⌫ to delete last digit
    """)

def main():
    """Main function"""
    create_simple_calculator()
    
    # Sidebar with calculator info
    with st.sidebar:
        st.header("📱 Calculator Info")
        st.markdown("""
        ### Features:
        - Basic arithmetic operations
        - Clean, modern interface
        - Responsive design
        - Error handling
        """)
        
        st.markdown("### Operations:")
        st.markdown("""
        - **Addition**: +
        - **Subtraction**: -
        - **Multiplication**: ×
        - **Division**: ÷
        """)

if __name__ == "__main__":
    main() 