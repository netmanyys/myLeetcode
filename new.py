import pygame

if current_state == "WELCOME":
    if event.key == pygame.K_RETURN:
        current_state = "PLAYING"
        start_time = time.time()
    elif event.key == pygame.K_TAB:  # Add this condition to handle tab key
        current_state = "PLAYING"
        start_time = time.time()
            