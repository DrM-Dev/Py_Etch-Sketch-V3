#Py-Etch Sketch V3  by  Dr.M-Dev:
#====================================================================================
#====================================================================================
# Imports__________________________
import time
from turtle import Turtle, Screen
# globals__________________________
user_pen_size = 2
drawing_state = "Pen"
is_turning = False
available_colors = ["red",
"green",
"blue",
"yellow",
"orange",
"purple",
"pink",
"brown",
"black",
"white",
"cyan",
"magenta",
"gray" or "grey",
"lightgreen",
"lightblue",
"turquoise",
"skyblue",
"light salmon",
"violet",
"gold"
                    ]

#---------
dim_colors =  ["red", "purple","brown","black","magenta","gray","grey","turquoise","violet"]

light_colors = ["green","blue","yellow","orange","white","cyan","lightgreen","gold" ,"pink","light salmon","skyblue","lightblue"]

#====================================================================================
print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')


print("******** WELCOME TO Py-Etch Sketch V3   -   By: Dr.m DEV *********")
#==========================================================================================================
#______________________________________________________________
background_eraser_color = "white"

#__________________________________Main Objects & Classes
user_pen = Turtle()
my_screen = Screen()
#
user_pen.shape("arrow")
user_pen.shapesize(stretch_wid=0.5,stretch_len=0.5)
#
my_screen.title("Py-Etch Sketch V3  -  Dr.M-Dev")


#__________________________________Functions
def move_forward():
    user_pen.forward(10)

def move_backward():
    user_pen.backward(10)

def turn_right():
    global is_turning
    #----
    if not is_turning:
        is_turning = True
        user_pen.right(10)
    #####
    is_turning = False

def turn_left():
    global is_turning
    # ----
    if not is_turning:
        is_turning = True
        user_pen.left(10)
    #####
    is_turning = False

#----------
def undo():
    user_pen.undo()

def clear():
    my_screen.reset()
    status_typer.penup()
    status_typer.goto(-300, 225)

#----------
def turn_off():
    my_screen.bye()

#____________________________
def switch_color():
    color_picked = False
    color_choice = ""

    while not color_picked:
        color_choice = my_screen.textinput(title="pick a pen color :)", prompt="[just type the name of the color you want!] your choice:")
        #_________________
        for color in available_colors:
            if color_choice == color:
                color_choice = color
                color_picked = True
                break
        #======================
        if not color_picked:
            current_bg = my_screen.bgcolor()
            #----------
            color_picked = True
            my_screen.textinput(title="🚫INVALID INPUT🚫", prompt="Invalid color name (color reset to default)")
            if current_bg in dim_colors:
                color_choice = "white"
            if current_bg in light_colors:
                color_choice = "black"
    #----------------------------------------
    user_pen.pencolor(color_choice)
    drawing()

#_____________________________
def pen_size_plus():
    global user_pen_size
    user_pen_size +=1
    user_pen.pensize(user_pen_size)

def pen_size_minus():
    global user_pen_size
    user_pen_size -= 1
    user_pen.pensize(user_pen_size)

#====================================================================================
#====================================================================================CODE STARTS HERE:
#====================================================================================
def help_screen():
    my_screen.textinput(title="⚠️✍️CONTROLS️", prompt="This is list of controls :)\n"
                                                                       "[you can access this note by pressing [H]\n"
                                                                       "---------------\n"
                                                                       "1-[W,A,S,D]/[Arrows] to Move\n"
                                                                       "2-[R] to Pick Color\n"
                                                                       "3-[P] to Draw\n"
                                                                       "4-[Shift] & [-] or [+]\n"
                                                                       "to Change Pen size\n"
                                                                       "---------------\n"
                                                                       "5-[Q] to change background color\n" 
                                                                       "6-[Z] to Undo\n"
                                                                       "7-[C] to Clear\n"
                                                                       "8-[E] to Erase\n"
                                                                       "9-[Esc] to Exit\n"
                        )

##########COMMANDS
def erasing():
    global drawing_state
    global background_eraser_color
    ########
    drawing_state = "Eraser"
    eraser_size = 50
    ########
    user_pen.color("black")
    user_pen.pencolor(background_eraser_color)
    #
    user_pen.shape("square")
    user_pen.shapesize(stretch_wid=1.6,stretch_len=1.6)
    #
    user_pen.pensize(eraser_size)
    #
    drawing()

def pen():
    global drawing_state
    global user_pen_size
    ########
    drawing_state = "Pen"
    user_pen_size = 2
    ########
    user_pen.color("black")
    user_pen.shape("arrow")
    user_pen.shapesize(stretch_wid=0.5, stretch_len=0.5)
    #
    user_pen.pensize(1)
    #
    drawing()

def drawing():
    my_screen.listen()

    my_screen.onkeypress(key="h", fun=help_screen)
    #_____________________#
    my_screen.onkeypress(key="w", fun=move_forward)
    my_screen.onkeypress(key="s", fun=move_backward)
    my_screen.onkeypress(key="d", fun=turn_right)
    my_screen.onkeypress(key="a", fun=turn_left)
    #
    my_screen.onkeypress(key="Up", fun=move_forward)
    my_screen.onkeypress(key="Down", fun=move_backward)
    my_screen.onkeypress(key="Right", fun=turn_right)
    my_screen.onkeypress(key="Left", fun=turn_left)
    #---------------------
    my_screen.onkey(key="r", fun=switch_color)
    my_screen.onkey(key="q", fun=change_bg)
    #
    my_screen.onkeypress(key="minus", fun=pen_size_minus)
    my_screen.onkeypress(key="plus", fun=pen_size_plus)
    #
    my_screen.onkey(key="p", fun=pen)
    my_screen.onkey(key="e", fun=erasing)
    my_screen.onkeypress(key="z", fun=undo)
    my_screen.onkey(key="c", fun=clear)
    #
    my_screen.onkey(key="Escape", fun=turn_off)
    #_____________________________________________________


#====================================================================================
#====================================================================================
def change_bg():
    global available_colors
    global light_colors
    global dim_colors
    #
    global background_eraser_color
    #
    bg_color_picked = False
    #------------------
    user_bg_choice = my_screen.textinput(title="Change Background", prompt="type the color you want for your background :)")
    # _________________
    for color in available_colors:
        if user_bg_choice == color:
            user_bg_choice = color
            bg_color_picked = True
    #-----------------------------
    if not bg_color_picked:
        user_bg_choice = "white"
        bg_color_picked = True
        my_screen.textinput(title="🚫INVALID INPUT🚫", prompt="Invalid color name (color reset to default)")
        #--------------------------
        status_typer.pencolor("black")
    #=============================================
    if bg_color_picked:
        if user_bg_choice in light_colors:
            for color in light_colors:
                if user_bg_choice == color:
                    status_typer.pencolor("black")
                    # + #
                    my_screen.bgcolor(user_bg_choice)
                    #------

                    background_eraser_color = user_bg_choice #for eraser
                    pen()  # change tool
                    break
            #-------------------------------------
        if user_bg_choice in dim_colors:
            for color in dim_colors:
                if user_bg_choice == color:
                    status_typer.pencolor("white")
                    # + #
                    my_screen.bgcolor(user_bg_choice)
                    # ------

                    background_eraser_color = user_bg_choice  # for eraser
                    pen() #change tool
                    break


#====================================================================================
#====================================================================================
status_typer = Turtle()
#------------------
def status_check():
    global drawing_state
    ##############
    time.sleep(0.1)
    #
    current_pos = user_pen.pos()
    current_color = user_pen.pencolor()
    current_size = user_pen.pensize()
    current_heading = user_pen.heading()
    #X-X-X-X-X-X-X-X-#
    status_typer.penup()
    status_typer.hideturtle()
    #
    #___________________________
    status_typer.clear()
    status_typer.goto(-300,225)
    status_typer.write(f"🎨📟INFO:\n\n\n\n\n", font=("Arial", 10, "bold"))
    status_typer.write(f"Tool:       {drawing_state}\n\n\n\n", font=("Arial", 10, "bold"))
    status_typer.write(f"Position: {current_pos}\n\n\n",font=("Arial", 10, "bold"))
    status_typer.write(f"Heading: {current_heading}\n\n",font=("Arial", 10, "bold"))
    status_typer.write(f"Pensize: {current_size}\n",font=("Arial", 10, "bold"))
    status_typer.write(f"Color:      {current_color}",font=("Arial", 10, "bold"))
    #
    drawing()



#====================================================================================
#====================================================================================
#_________________________________Code_starts_here
help_screen()

still_drawing = True
while still_drawing:
    drawing()
    #--------------
    status_check()



#====================================================================================
#_____________________END CODE
my_screen.exitonclick()
