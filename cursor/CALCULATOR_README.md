# 🧮 Calculator Apps with Streamlit

Two comprehensive calculator applications built with Python and Streamlit, featuring modern interfaces and advanced functionality.

## 📱 Available Calculators

### 1. **Advanced Calculator** (`calculator.py`)
A full-featured scientific calculator with comprehensive mathematical functions.

### 2. **Simple Calculator** (`simple_calculator.py`)
A clean, basic calculator perfect for everyday arithmetic operations.

## 🚀 Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the calculators**:
   ```bash
   # Advanced Calculator
   streamlit run calculator.py
   
   # Simple Calculator
   streamlit run simple_calculator.py
   ```

## 🎯 Advanced Calculator Features

### 📊 Mathematical Operations
- **Basic Arithmetic**: Addition (+), Subtraction (-), Multiplication (×), Division (÷)
- **Advanced Operations**: Exponentiation (^), Reciprocal (1/x)
- **Scientific Functions**: 
  - Trigonometric: sin, cos, tan (in degrees)
  - Logarithmic: log (base 10), ln (natural log)
  - Power Functions: square (x²), square root (√)
  - Special Functions: factorial (x!)

### 🎨 Interface Features
- **Modern Design**: Gradient backgrounds and neumorphic buttons
- **LED Display**: Retro-style calculator display with green text
- **Calculation History**: View last 10 calculations
- **Error Handling**: Graceful handling of division by zero and invalid operations
- **Responsive Layout**: Works on different screen sizes

### 🔧 User Interface
- **Button Layout**: Organized in a 4x4 grid with additional function rows
- **Color Coding**: Different colors for numbers, operators, and functions
- **Hover Effects**: Interactive button animations
- **Clear Functions**: Clear all (C) and delete last digit (⌫)

## 📱 Simple Calculator Features

### 🎯 Basic Operations
- **Core Arithmetic**: +, -, ×, ÷
- **Decimal Support**: Full decimal number input
- **Clear Functions**: Clear all and delete last digit
- **Error Handling**: Division by zero protection

### 🎨 Design Features
- **Clean Interface**: Minimalist design with modern styling
- **Color-coded Buttons**: Different colors for different button types
- **Responsive Design**: Adapts to different screen sizes
- **Professional Look**: Gradient backgrounds and shadows

## 🛠️ Technical Implementation

### Advanced Calculator (`calculator.py`)
```python
class Calculator:
    def __init__(self):
        self.current_input = ""
        self.previous_input = ""
        self.operation = None
        self.should_reset = False
        self.history = []
```

**Key Features:**
- Session state management for persistent calculations
- Comprehensive error handling
- Scientific function implementations
- Calculation history tracking

### Simple Calculator (`simple_calculator.py`)
```python
class SimpleCalculator:
    def __init__(self):
        self.current = ""
        self.previous = ""
        self.operation = None
        self.should_reset = False
```

**Key Features:**
- Streamlined interface for basic operations
- Efficient state management
- Clean, focused functionality

## 🎨 Customization Options

### Styling
Both calculators use custom CSS for modern styling:
- **Gradient Backgrounds**: Beautiful color transitions
- **Neumorphic Design**: Soft, modern button styling
- **Responsive Layout**: Adapts to different screen sizes
- **Color Themes**: Consistent color schemes

### Functionality
- **Add New Operations**: Extend the calculator classes
- **Modify Styling**: Update CSS in the `st.markdown()` sections
- **Add Features**: Implement additional mathematical functions

## 📁 Project Structure

```
calculator-apps/
├── calculator.py           # Advanced scientific calculator
├── simple_calculator.py    # Basic arithmetic calculator
├── requirements.txt        # Python dependencies
├── CALCULATOR_README.md   # This documentation
├── README.md              # Snake game documentation
├── snake_game.py          # Snake game logic
├── app.py                 # Snake game Streamlit app
└── demo.py                # Snake game demo script
```

## 🎯 Usage Examples

### Advanced Calculator
1. **Basic Calculation**: `5 + 3 = 8`
2. **Scientific Function**: `sin(30) = 0.5`
3. **Power Operation**: `2 ^ 3 = 8`
4. **Square Root**: `√(16) = 4`

### Simple Calculator
1. **Addition**: `10 + 5 = 15`
2. **Multiplication**: `6 × 7 = 42`
3. **Division**: `20 ÷ 4 = 5`
4. **Subtraction**: `15 - 8 = 7`

## 🔧 Troubleshooting

### Common Issues
- **Import Errors**: Ensure all dependencies are installed
- **Display Issues**: Check browser compatibility
- **Performance**: Use smaller window sizes for better performance

### Browser Compatibility
- **Chrome**: Full support
- **Firefox**: Full support
- **Safari**: Full support
- **Edge**: Full support

## 🎉 Features Summary

### Advanced Calculator
✅ Scientific functions (sin, cos, tan, log, ln)  
✅ Advanced operations (√, x², x!, 1/x, x^y)  
✅ Calculation history  
✅ Error handling  
✅ Modern UI with gradients  
✅ Responsive design  

### Simple Calculator
✅ Basic arithmetic operations  
✅ Clean, minimalist interface  
✅ Decimal number support  
✅ Error handling  
✅ Professional styling  
✅ Mobile-friendly design  

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Choose your calculator**:
   ```bash
   # For advanced features
   streamlit run calculator.py
   
   # For simple calculations
   streamlit run simple_calculator.py
   ```

3. **Start calculating!** 🧮

Both calculators are ready to use and provide excellent user experiences for different mathematical needs! 