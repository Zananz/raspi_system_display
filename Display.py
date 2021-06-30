import pygame
import get_values

pygame.init()

screen = pygame.display.set_mode((400, 300))

run = True

font = pygame.font.SysFont("Arial", 20)

while run:
    
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    screen.fill((0,0,0))
    
    core_temperature = font.render("Core temperature: %s°C"%get_values.core_temperature(), True, (0, 128, 0))
    
    RAM_total, RAM_used, RAM_free = get_values.RAM()
    
    Used_RAM_procent = round(int(RAM_used)*100/int(RAM_total), 1)
    
    RAM_total = font.render       ("Total RAM: %s"% RAM_total, True, (0, 128, 0))
    RAM_used = font.render        ("Used RAM:  %s"% RAM_used, True, (0, 128, 0)) 
    RAM_free = font.render        ("Free RAM:  %s"% RAM_free, True, (0, 128, 0))
    
    Used_RAM_procent = font.render("Free RAM:  %s%%"% Used_RAM_procent, True, (0, 128, 0))
    
    screen.blit(core_temperature,(0,0))
    screen.blit(RAM_total,(0,20))
    screen.blit(RAM_used,(0,40))
    screen.blit(RAM_free,(0,60))
    
    screen.blit(Used_RAM_procent,(0,80))
    
    pygame.display.flip()
    
    pygame.time.wait(500)
    
pygame.quit()

    
    