import xbox

#Init

joy = xbox.Joystick()

#Appuis sur bouton

if joy.A() :
    print ("Bouton A")
elif  joy.b() :
    print ("Bouton B")
elif
    x_axis = joy.leftX()
    y_axis = joy.leftY()



    #On éteint l'IHM

    joy.close()