import pygame
import sys
import math


def end():
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Crows Win", True, yellow)
    screen.blit(text_surface, (width // 2 - 100, height // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Display the message for 3 seconds
    pygame.quit()
    sys.exit()


def kill():
    font = pygame.font.Font(None, 36)
    text_surface = font.render("No of crows killed" + str(count), True, yellow)
    screen.blit(text_surface, (300, 450))
    pygame.display.flip()
    pygame.time.wait(1000)


pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kaooa Game")

white = (220, 220, 220)
black = (255, 242, 204)
yellow = (220, 20, 60)
indigo = (0, 0, 139)
blue = (0, 0, 0)

center_x, center_y = 300, 300
radius_outer = 200
radius_inner = 100
num_points = 10
angle_increment = 2 * math.pi / num_points

star_vertices = []
for i in range(num_points):
    radius = radius_outer if i % 2 == 0 else radius_inner
    angle = i * angle_increment
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    star_vertices.append((x, y))

max_x = max(vertex[0] for vertex in star_vertices)

circle_distance = 40

disc_positions = [(max_x + circle_distance + 10, 150 + i * circle_distance) for i in range(8)]
disc = [(None) for i in range(8)]
ver = [(None) for i in range(10)]
killed = [(None) for i in range(8)]

selected_corner = None
selected_circle = None

current_color = indigo
count = 0
total = 0

while True:
    if current_color == indigo:
        font = pygame.font.Font(None, 36)
        text_surface = font.render("player 1", True, yellow)
        screen.blit(text_surface, (300, 550))
        pygame.display.flip()
    else:
        font = pygame.font.Font(None, 36)
        text_surface = font.render("player 2", True, yellow)
        screen.blit(text_surface, (300, 550))
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            for i, vertex in enumerate(star_vertices):
                dist_squared = (vertex[0] - mouse_x) ** 2 + (vertex[1] - mouse_y) ** 2
                if dist_squared <= 25:
                    selected_corner = i
                    if selected_circle is not None:

                        if disc[selected_circle] is None:
                            disc_positions[selected_circle] = vertex
                            disc[selected_circle] = i
                            ver[i] = selected_circle
                            selected_circle = None
                            total += 1
                            current_color = yellow if current_color == indigo else indigo
                        elif disc[selected_circle] == 0 and (
                           ver[1] is not None and 
                           ver[3] is not None and 
                           ver[9] is not None and 
                           ver[7] is not None):
                           end()

                        elif disc[selected_circle] == 1 and (
                            ver[0] is not None and 
                            ver[2] is not None and 
                            ver[9] is not None and 
                            ver[8] is not None and 
                            ver[3] is not None and 
                            ver[4] is not None):
                            end()
                        elif disc[selected_circle] == 2 and (
                            ver[1] is not None and 
                            ver[3] is not None and 
                            ver[9] is not None and 
                            ver[5] is not None):
                            end()
                        elif disc[selected_circle] == 3 and (
                            ver[2] is not None and 
                            ver[5] is not None and 
                            ver[6] is not None and 
                            ver[4] is not None and 
                            ver[1] is not None and 
                            ver[0] is not None):
                            end()
                        elif disc[selected_circle] == 4 and (
                            ver[3] is not None and 
                            ver[5] is not None and 
                            ver[1] is not None and 
                            ver[7] is not None):
                            end()
                        elif disc[selected_circle] == 5 and (
                            ver[3] is not None and 
                            ver[2] is not None and 
                            ver[6] is not None and 
                            ver[5] is not None and 
                            ver[7] is not None and 
                            ver[8] is not None):
                            end()
                        elif disc[selected_circle] == 6 and (
                            ver[5] is not None and 
                            ver[7] is not None and 
                            ver[3] is not None and 
                            ver[9] is not None):
                            end()
                        elif disc[selected_circle] == 7 and (
                            ver[6] is not None and 
                            ver[8] is not None and 
                            ver[5] is not None and 
                            ver[4] is not None and 
                            ver[9] is not None and 
                            ver[0] is not None):
                            end()
                        elif disc[selected_circle] == 8 and (
                            ver[7] is not None and 
                            ver[9] is not None and 
                            ver[5] is not None and 
                            ver[0]is not None):
                            end()
                        elif disc[selected_circle] == 9 and (
                            ver[0] is not None and 
                            ver[7] is not None and 
                            ver[8] is not None and 
                            ver[1] is not None and 
                            ver[2] is not None and 
                            ver[6] is not None):
                            end()
                        elif (current_color == yellow or (current_color == indigo and total == 8)) and (disc[selected_circle] == 0 and i == 9 and ver[i] is None):
                            ver[disc[selected_circle]]=None
                            disc_positions[selected_circle] = vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            selected_circle = None
                            current_color = yellow if current_color == indigo else indigo
                        elif (current_color == yellow or (current_color == indigo and total == 8)) and(disc[selected_circle] == 9 and i == 0 and ver[i] is None) :
                            ver[disc[selected_circle]]=None
                            disc_positions[selected_circle] = vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            selected_circle = None
                            current_color = yellow if current_color == indigo else indigo
                        elif (current_color == yellow or (current_color == indigo and total == 8)) and(disc[selected_circle]%2 == 1) and (i == disc[selected_circle] + 2 or i == disc[selected_circle] - 2) and ver[i] ==  None:
                            ver[disc[selected_circle]]=None
                            disc_positions[selected_circle] = vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            selected_circle = None
                            current_color = yellow if current_color == indigo else indigo
                        elif (current_color == yellow or (current_color == indigo and total == 8)) and(disc[selected_circle] == 1) and i == 9 and ver[i] is None:
                            ver[disc[selected_circle]]=None
                            disc_positions[selected_circle] = vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            selected_circle = None
                            current_color = yellow if current_color == indigo else indigo
                        elif (current_color == yellow or (current_color == indigo and total == 8)) and disc[selected_circle] == 9 and i == 1 and ver[i] is None :
                            ver[disc[selected_circle]]=None
                            disc_positions[selected_circle] = vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            selected_circle = None
                            current_color = yellow if current_color == indigo else indigo  
                        elif (current_color == yellow or (current_color == indigo and total == 8)) and (ver[i] is None and (i == disc[selected_circle] + 1 or i == disc[selected_circle] - 1)):
                            ver[disc[selected_circle]]=None
                            disc_positions[selected_circle] = vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            selected_circle = None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 0 and ver[1] is not None and i == 3 and ver[i] is None:
                            ver[0]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[1]]=1
                            count+=1
                            disc_positions[ver[1]]=(-max_x + circle_distance + 10, 50 + ver[1]* circle_distance)
                            kill()
                            ver[1]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 0 and ver[9] is not None and i == 7 and ver[i] is None:
                            ver[0]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[9]]=1
                            count+=1
                            disc_positions[ver[9]]=(-max_x + circle_distance + 10, 50 + ver[9]* circle_distance)
                            kill()
                            ver[9]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 1 and ver[3] is not None and i == 4 and ver[i] is None:
                            ver[1]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[3]]=1
                            count+=1
                            disc_positions[ver[3]]=(-max_x + circle_distance + 10, 50 + ver[3]* circle_distance)
                            kill()
                            ver[3]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 1 and ver[9] is not None and i == 8 and ver[i] is None:
                            ver[1]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[9]]=1
                            count+=1
                            disc_positions[ver[9]]=(-max_x + circle_distance + 10, 50 + ver[9]* circle_distance)
                            kill()
                            ver[9]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 2 and ver[3] is not None and i == 5 and ver[i] is None:
                            ver[2]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[3]]=1
                            count+=1
                            disc_positions[ver[3]]=(-max_x + circle_distance + 10, 50 + ver[3]* circle_distance)
                            kill()
                            ver[3]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 2 and ver[1] is not None and i == 9 and ver[i] is None:
                            ver[2]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[1]]=1
                            count+=1
                            disc_positions[ver[1]]=(-max_x + circle_distance + 10, 50 + ver[1]* circle_distance)
                            kill()
                            ver[1]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 3 and ver[5] is not None and i == 6 and ver[i] is None:
                            ver[3]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[5]]=1
                            count+=1
                            disc_positions[ver[5]]=(-max_x + circle_distance + 10, 50 + ver[5]* circle_distance)
                            kill()
                            ver[5]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 3 and ver[1] is not None and i == 0 and ver[i] is None:
                            ver[3]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[1]]=1
                            count+=1
                            disc_positions[ver[1]]=(-max_x + circle_distance + 10, 50 + ver[1]* circle_distance)
                            kill()
                            ver[1]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 4 and ver[3] is not None and i == 1 and ver[i] is None:
                            ver[4]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[3]]=1
                            count+=1
                            disc_positions[ver[3]]=(-max_x + circle_distance + 10, 50 + ver[3]* circle_distance)
                            kill()
                            ver[3]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 4 and ver[5] is not None and i == 7 and ver[i] is None:
                            ver[4]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[5]]=1
                            count+=1
                            disc_positions[ver[5]]=(-max_x + circle_distance + 10, 50 + ver[5]* circle_distance)
                            kill()
                            ver[5]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 5 and ver[3] is not None and i == 8 and ver[i] is None:
                            ver[5]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[3]]=1
                            count+=1
                            disc_positions[ver[3]]=(-max_x + circle_distance + 10, 50 + ver[3]* circle_distance)
                            kill()
                            ver[3]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 5 and ver[6] is not None and i == 2 and ver[i] is None:
                            ver[5]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[6]]=1
                            count+=1
                            disc_positions[ver[6]]=(-max_x + circle_distance + 10, 50 + ver[6]* circle_distance)
                            kill()
                            ver[6]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 6 and ver[5] is not None and i == 9 and ver[i] is None:
                            ver[6]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[5]]=1
                            count+=1
                            disc_positions[ver[5]]=(-max_x + circle_distance + 10, 50 + ver[5]* circle_distance)
                            kill()
                            ver[5]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 6 and ver[3] is not None and i == 3 and ver[i] is None:
                            ver[6]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[3]]=1
                            count+=1
                            disc_positions[ver[3]]=(-max_x + circle_distance + 10, 50 + ver[3]* circle_distance)
                            kill()
                            ver[3]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 7 and ver[8] is not None and i == 0 and ver[i] is None:
                            ver[7]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[8]]=1
                            count+=1
                            disc_positions[ver[8]]=(-max_x + circle_distance + 10, 50 + ver[8]* circle_distance)
                            kill()
                            ver[8]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 7 and ver[6] is not None and i == 2 and ver[i] is None:
                            ver[7]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[6]]=1
                            count+=1
                            disc_positions[ver[6]]=(-max_x + circle_distance + 10, 50 + ver[6]* circle_distance)
                            kill()
                            ver[6]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 8 and ver[7] is not None and i == 1 and ver[i] is None:
                            ver[8]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            killed[ver[7]]=1
                            count+=1
                            disc_positions[ver[7]]=(-max_x + circle_distance + 10, 50 + ver[7]* circle_distance)
                            kill()
                            ver[7]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 8 and ver[5] is not None and i == 9 and ver[i] is None:
                            ver[8]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[5]]=1
                            count+=1
                            disc_positions[ver[5]]=(-max_x + circle_distance + 10, 50 + ver[5]* circle_distance)
                            kill()
                            ver[5]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 9 and ver[0] is not None and i == 3 and ver[i] is None:
                            ver[9]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[0]]=1
                            count+=1
                            disc_positions[ver[0]]=(-max_x + circle_distance + 10, 50 + ver[0]* circle_distance)
                            kill()
                            ver[0]=None
                            current_color = yellow if current_color == indigo else indigo
                        elif current_color == yellow and   disc[selected_circle] == 9 and ver[8] is not None and i == 1 and ver[i] is None:
                            ver[9]=None
                            disc_positions[selected_circle]=vertex
                            disc[selected_circle]=i
                            ver[i]=selected_circle
                            killed[ver[8]]=1
                            count+=1
                            disc_positions[ver[8]]=(-max_x + circle_distance + 10, 50 + ver[8]* circle_distance)
                            kill()
                            ver[8]=None
                            current_color = yellow if current_color == indigo else indigo

            for i, position in enumerate(disc_positions):
                dist_squared = (position[0] - mouse_x) ** 2 + (position[1] - mouse_y) ** 2
                if dist_squared <= 25:
                    selected_circle = i

    screen.fill(black)

    for vertex in star_vertices:
        pygame.draw.circle(screen, white, (int(vertex[0]), int(vertex[1])), 10)

    for i, position in enumerate(disc_positions):
        pygame.draw.circle(screen, current_color, (int(position[0]), int(position[1])), 20)

    for i, position in enumerate(killed):
        if position == 1:
            pygame.draw.circle(screen, yellow, (int(disc_positions[i][0]), int(disc_positions[i][1])), 20)

    pygame.display.flip()
