# import pygame
# import time
#
# pygame.init()
# pygame.joystick.init()
#
# print(pygame.joystick.get_count())
# _joystick = pygame.joystick.Joystick(0)
# _joystick.init()
#
# ValueTransitoire = 0
# FinalValueJOY1Horizon = 0
# FinalValueJoy1Vertical = 0
#
# OldStringManette = ""
# NewStringManette = ""
#
# while 1:
#     for event in pygame.event.get():
#
# #Bouton
#         if event.type == pygame.JOYBUTTONDOWN:
#             if event.button == 4:
#                 print("Bouton Start")
#             elif event.button == 5:
#                 print("Bouton Back")
#             elif event.button == 8:
#                 print("Bouton LB")
#             elif event.button == 9:
#                 print("Bouton RB")
#             elif event.button == 10:
#                 print("Bouton Xbox")
#             elif event.button == 11:
#                 print("Bouton A")
#             elif event.button == 12:
#                 print("Bouton B")
#             elif event.button == 13:
#                 print("Bouton X")
#             elif event.button == 14:
#                 print("Bouton Y")
#
# #Joystick
#
#         elif event.type == pygame.JOYAXISMOTION:
#             if (ValueTransitoire - event.value) > 0.1 or (ValueTransitoire - event.value) < 0.1:
#             #Joystisck 1 : en haut à gauche
#                 if event.axis == 0:
#                     ValueTransitoire = event.value*10
#                     ValueTransitoire2 = int(ValueTransitoire)
#                     FinalValueJOY1Horizon = float(ValueTransitoire2/10)
#
#                 elif event.axis == 1:
#                     ValueTransitoire = event.value * 10
#                     ValueTransitoire2 = int(ValueTransitoire)
#                     FinalValueJoy1Vertical = float(ValueTransitoire2 / 10)
#             NewStringManette = ("JOY_{}_{}".format(FinalValueJOY1Horizon, FinalValueJoy1Vertical))
#
#             # Si la valeur de la string est la même que la précédente on ne la renvoie pas
#             if NewStringManette != OldStringManette:
#                 print(NewStringManette)
#                 OldStringManette = NewStringManette
#
#             #LT - 4 & RT - 5
#             if event.axis == 4:
#                 ValueTransitoire = event.value * 10
#                 ValueTransitoire2 = int(ValueTransitoire)
#                 FinalValueLT = float(ValueTransitoire2 / 10)
#                 print("LT_{}" .format(FinalValueLT))
#             elif event.axis == 5:
#                 ValueTransitoire = event.value * 10
#                 ValueTransitoire2 = int(ValueTransitoire)
#                 FinalValueRT = float(ValueTransitoire2 / 10)
#                 print("RT_{}".format(FinalValueRT))