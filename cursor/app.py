import streamlit as st
import time
from snake_game import SnakeGame, GameRenderer

# Page configuration
st.set_page_config(
    page_title="Snake Game",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .game-container {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .score-display {
        background-color: #2E8B57;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .game-board {
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        line-height: 1.2;
        background-color: white;
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #2E8B57;
    }
    .controls-section {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'game' not in st.session_state:
        st.session_state.game = SnakeGame()
    if 'game_paused' not in st.session_state:
        st.session_state.game_paused = False
    if 'last_update' not in st.session_state:
        st.session_state.last_update = time.time()
    if 'game_speed' not in st.session_state:
        st.session_state.game_speed = 0.3  # seconds between moves

def handle_keyboard_input():
    """Handle keyboard input for game controls"""
    # Direction buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("⬆️ Up", key="up"):
            st.session_state.game.move_snake((0, -1))
    
    with col2:
        col2_1, col2_2, col2_3 = st.columns([1, 1, 1])
        with col2_1:
            if st.button("⬅️ Left", key="left"):
                st.session_state.game.move_snake((-1, 0))
        with col2_2:
            if st.button("⏸️ Pause", key="pause"):
                st.session_state.game_paused = not st.session_state.game_paused
        with col2_3:
            if st.button("➡️ Right", key="right"):
                st.session_state.game.move_snake((1, 0))
    
    with col3:
        if st.button("⬇️ Down", key="down"):
            st.session_state.game.move_snake((0, 1))

def display_game_info():
    """Display game information and controls"""
    game_state = st.session_state.game.get_game_state()
    
    # Game info
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.metric("Score", game_state['score'])
    
    with col2:
        if game_state['game_over']:
            st.error("🎮 Game Over! Click 'New Game' to restart.")
        elif game_state['game_won']:
            st.success("🎉 Congratulations! You won!")
        else:
            status = "⏸️ Paused" if st.session_state.game_paused else "▶️ Playing"
            st.info(f"Status: {status}")
    
    with col3:
        st.metric("Snake Length", len(game_state['snake']))

def main():
    """Main application function"""
    st.markdown('<h1 class="main-header">🐍 Snake Game</h1>', unsafe_allow_html=True)
    
    # Initialize session state
    initialize_session_state()
    
    # Sidebar for game settings
    with st.sidebar:
        st.header("🎮 Game Settings")
        
        # Board size
        board_size = st.selectbox(
            "Board Size",
            ["Small (15x15)", "Medium (20x20)", "Large (25x25)"],
            index=1
        )
        
        size_map = {
            "Small (15x15)": 15,
            "Medium (20x20)": 20,
            "Large (25x25)": 25
        }
        
        # Game speed
        game_speed = st.slider(
            "Game Speed",
            min_value=0.1,
            max_value=1.0,
            value=0.3,
            step=0.1,
            help="Speed of the snake movement"
        )
        
        st.session_state.game_speed = game_speed
        
        # New game button
        if st.button("🔄 New Game", type="primary"):
            st.session_state.game = SnakeGame(size_map[board_size], size_map[board_size])
            st.session_state.game_paused = False
            st.rerun()
        
        st.markdown("---")
        st.markdown("### 🎯 How to Play")
        st.markdown("""
        1. Use the direction buttons to control the snake
        2. Eat the 🍎 to grow and increase your score
        3. Avoid hitting the walls or yourself
        4. Try to fill the entire board to win!
        """)
        
        st.markdown("### 🏆 High Score")
        if 'high_score' not in st.session_state:
            st.session_state.high_score = 0
        
        st.metric("Best Score", st.session_state.high_score)
    
    # Main game area
    with st.container():
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        # Display game info
        display_game_info()
        
        # Game board
        game_state = st.session_state.game.get_game_state()
        board_display = GameRenderer.render_board(game_state)
        
        st.markdown('<div class="game-board">', unsafe_allow_html=True)
        st.text(board_display)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Game controls
        st.markdown('<div class="controls-section">', unsafe_allow_html=True)
        st.markdown("### 🎮 Controls")
        handle_keyboard_input()
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Auto-move logic
    if not game_state['game_over'] and not game_state['game_won'] and not st.session_state.game_paused:
        current_time = time.time()
        if current_time - st.session_state.last_update >= st.session_state.game_speed:
            st.session_state.game.move_snake()
            st.session_state.last_update = current_time
            
            # Update high score
            if game_state['score'] > st.session_state.high_score:
                st.session_state.high_score = game_state['score']
            
            st.rerun()

if __name__ == "__main__":
    main() 