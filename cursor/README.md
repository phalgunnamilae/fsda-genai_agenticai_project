# 🐍 Snake Game with Streamlit

A classic Snake game built with Python and Streamlit, featuring a beautiful web interface with interactive controls.

## 🎮 Features

- **Classic Snake Gameplay**: Control a snake to eat food and grow longer
- **Beautiful UI**: Modern Streamlit interface with custom styling
- **Interactive Controls**: Button-based controls for easy gameplay
- **Game Settings**: Adjustable board size and game speed
- **Score Tracking**: Real-time score display and high score tracking
- **Pause/Resume**: Pause the game at any time
- **Game States**: Clear indication of game over, win, or playing status
- **Responsive Design**: Works on different screen sizes

## 🚀 Installation

1. **Clone or download the project files**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 How to Play

1. **Start the game**:
   ```bash
   streamlit run app.py
   ```

2. **Game Controls**:
   - Use the direction buttons (⬆️ ⬅️ ➡️ ⬇️) to control the snake
   - Click "⏸️ Pause" to pause/resume the game
   - Click "🔄 New Game" to restart

3. **Game Rules**:
   - Eat the 🍎 to grow and increase your score
   - Avoid hitting the walls or yourself
   - Try to fill the entire board to win!

## 🎛️ Game Settings

- **Board Size**: Choose between Small (15x15), Medium (20x20), or Large (25x25)
- **Game Speed**: Adjust the snake movement speed from 0.1 to 1.0 seconds
- **High Score**: Track your best score across sessions

## 📁 Project Structure

```
snake-game/
├── app.py              # Main Streamlit application
├── snake_game.py       # Core game logic
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🛠️ Technical Details

### Core Components

1. **SnakeGame Class** (`snake_game.py`):
   - Handles game state management
   - Implements snake movement logic
   - Manages collision detection
   - Tracks score and game status

2. **GameRenderer Class** (`snake_game.py`):
   - Renders the game board using emojis
   - Creates visual representation of snake and food

3. **Streamlit App** (`app.py`):
   - Provides the web interface
   - Handles user interactions
   - Manages game session state
   - Implements auto-move functionality

### Game Mechanics

- **Snake Movement**: Continuous movement in current direction
- **Food Generation**: Random placement avoiding snake body
- **Collision Detection**: Wall and self-collision checking
- **Score System**: Increment score when food is eaten
- **Win Condition**: Snake fills entire board

## 🎨 Customization

You can easily customize the game by modifying:

- **Board Size**: Change default dimensions in `SnakeGame.__init__()`
- **Game Speed**: Adjust the default speed in `initialize_session_state()`
- **Visual Elements**: Modify emojis in `GameRenderer.render_board()`
- **Styling**: Update CSS in the `st.markdown()` section

## 🐛 Troubleshooting

- **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
- **Streamlit Issues**: Ensure you're using Streamlit version 1.28.0 or higher
- **Performance**: For better performance, use smaller board sizes on slower devices

## 🎉 Enjoy the Game!

The Snake game is now ready to play! Open your browser and navigate to the URL shown in the terminal after running `streamlit run app.py`.

Happy gaming! 🐍🎮 