import random
import time
from typing import List, Tuple, Optional
import streamlit as st

class SnakeGame:
    def __init__(self, width: int = 20, height: int = 20):
        self.width = width
        self.height = height
        self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.snake = [(self.width // 2, self.height // 2)]  # Start at center
        self.direction = (1, 0)  # Start moving right
        self.food = self._generate_food()
        self.score = 0
        self.game_over = False
        self.game_won = False
    
    def _generate_food(self) -> Tuple[int, int]:
        """Generate food at a random position"""
        while True:
            food = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food not in self.snake:
                return food
    
    def move_snake(self, direction: Optional[Tuple[int, int]] = None):
        """Move the snake in the given direction"""
        if self.game_over or self.game_won:
            return
        
        if direction is not None:
            # Prevent moving in opposite direction
            if (direction[0] != -self.direction[0] or direction[1] != -self.direction[1]):
                self.direction = direction
        
        # Calculate new head position
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # Check for wall collision
        if (new_head[0] < 0 or new_head[0] >= self.width or 
            new_head[1] < 0 or new_head[1] >= self.height):
            self.game_over = True
            return
        
        # Check for self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check for food collision
        if new_head == self.food:
            self.score += 1
            self.food = self._generate_food()
            
            # Check if snake fills the entire board
            if len(self.snake) == self.width * self.height:
                self.game_won = True
        else:
            # Remove tail if no food was eaten
            self.snake.pop()
    
    def get_game_state(self):
        """Return current game state for display"""
        return {
            'snake': self.snake,
            'food': self.food,
            'score': self.score,
            'game_over': self.game_over,
            'game_won': self.game_won,
            'width': self.width,
            'height': self.height
        }
    
    def is_valid_direction(self, direction: Tuple[int, int]) -> bool:
        """Check if the direction is valid (not opposite to current direction)"""
        return not (direction[0] == -self.direction[0] and direction[1] == -self.direction[1])

class GameRenderer:
    """Handles rendering the game board"""
    
    @staticmethod
    def render_board(game_state: dict) -> str:
        """Render the game board as a string representation"""
        width = game_state['width']
        height = game_state['height']
        snake = game_state['snake']
        food = game_state['food']
        
        # Create empty board
        board = [['⬜' for _ in range(width)] for _ in range(height)]
        
        # Place snake
        for i, segment in enumerate(snake):
            if i == 0:  # Head
                board[segment[1]][segment[0]] = '🐍'
            else:  # Body
                board[segment[1]][segment[0]] = '🟢'
        
        # Place food
        board[food[1]][food[0]] = '🍎'
        
        # Convert to string
        board_str = '\n'.join([''.join(row) for row in board])
        return board_str
    
    @staticmethod
    def render_controls():
        """Render game controls"""
        st.markdown("""
        ### Controls:
        - **W/↑**: Move Up
        - **S/↓**: Move Down  
        - **A/←**: Move Left
        - **D/→**: Move Right
        - **Space**: Pause/Resume
        """) 