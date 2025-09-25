#!/usr/bin/env python3
"""
Demo script to test the Snake game logic
Run this to see the game in action in the console
"""

from snake_game import SnakeGame, GameRenderer
import time
import os

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def demo_game():
    """Run a demo of the snake game"""
    print("🐍 Snake Game Demo")
    print("=" * 50)
    
    # Create game instance
    game = SnakeGame(width=10, height=10)  # Smaller board for demo
    
    # Demo moves
    moves = [
        (1, 0),   # Right
        (1, 0),   # Right
        (0, 1),   # Down
        (0, 1),   # Down
        (-1, 0),  # Left
        (-1, 0),  # Left
        (0, -1),  # Up
        (1, 0),   # Right
        (1, 0),   # Right
        (0, 1),   # Down
    ]
    
    print("Starting demo...")
    print("Game will automatically move the snake through some moves")
    print()
    
    for i, move in enumerate(moves):
        clear_screen()
        print(f"🐍 Snake Game Demo - Move {i+1}")
        print("=" * 50)
        
        # Move the snake
        game.move_snake(move)
        
        # Get game state
        game_state = game.get_game_state()
        
        # Display game info
        print(f"Score: {game_state['score']}")
        print(f"Snake Length: {len(game_state['snake'])}")
        print(f"Game Over: {game_state['game_over']}")
        print()
        
        # Display board
        board = GameRenderer.render_board(game_state)
        print("Game Board:")
        print(board)
        print()
        
        if game_state['game_over']:
            print("🎮 Game Over!")
            break
        elif game_state['game_won']:
            print("🎉 You Won!")
            break
        
        # Wait a bit
        time.sleep(1)
    
    print("Demo completed!")

if __name__ == "__main__":
    demo_game() 