import pygame
from configuration import Configuration

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.config = Configuration()
        self.font = pygame.font.Font(None, 36)
        self.update_options()

    def update_options(self):
        language = self.config.get_language()
        if language == "english":
            self.options = ["Play", "Credits", "Configuration", "Quit"]
        else:  # Asumimos que es español
            self.options = ["Jugar", "Créditos", "Configuración", "Salir"]

    def draw_options(self):
        self.screen.fill((0, 0, 0))
        self.option_rects = []  # Reiniciar la lista de rectángulos en cada loop
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            rect = text.get_rect(center=(self.screen.get_width() // 2, 150 + i * 50))
            self.screen.blit(text, rect)
            self.option_rects.append((option.lower(), rect))
        pygame.display.flip()

    def show(self):
        self.draw_options()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for option, rect in self.option_rects:
                        if rect.collidepoint(event.pos):
                            if option == "play" or option == "jugar":
                                return self.show_difficulty_menu()
                            elif option == "configuration" or option == "configuración":
                                self.show_configuration()
                                return  # Salir del loop actual después de mostrar configuración
                            else:
                                return option

    def show_difficulty_menu(self):
        self.screen.fill((0, 0, 0))
        difficulty_options = ["Beginner", "Advanced"] if self.config.get_language() == "english" else ["Principiante", "Avanzado"]
        self.option_rects = []  # Reiniciar la lista de rectángulos para el menú de dificultad
        for i, option in enumerate(difficulty_options):
            text = self.font.render(option, True, (255, 255, 255))
            rect = text.get_rect(center=(self.screen.get_width() // 2, 150 + i * 50))
            self.screen.blit(text, rect)
            self.option_rects.append((option.lower(), rect))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for option, rect in self.option_rects:
                        if rect.collidepoint(event.pos):
                            return self.show_level_menu(option)

    def show_level_menu(self, difficulty):
        self.screen.fill((0, 0, 0))
        level_options = [f"Level {i+1}" for i in range(3)]
        self.option_rects = []  # Reiniciar la lista de rectángulos para el menú de niveles
        for i, level in enumerate(level_options):
            text = self.font.render(level, True, (255, 255, 255))
            rect = text.get_rect(center=(self.screen.get_width() // 2, 150 + i * 50))
            self.screen.blit(text, rect)
            self.option_rects.append((level.lower(), rect))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for level, rect in self.option_rects:
                        if rect.collidepoint(event.pos):
                            return difficulty, level
