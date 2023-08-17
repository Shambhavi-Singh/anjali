import PySimpleGUI as sg

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import env, rrt, rrt_connect, dynamic_rrt, rrt_star, rrt_star_smart, informed_rrt_star, utils
from rrt import Node


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

figure_w, figure_h = 640, 480  

terrains_dict = {"Chaos Terrain":1, "Mesas Terrain":2, "Cliffs Terrain":3, "Craters Terrain":4, "Glacier Terrain":5, "Sand Dunes Terrain":6, "Gullies Terrain":7, "Medusae Fossae Terrain":8, "Scalloped Terrain":9, "Mud Volcanic Terrain":10, "Random 1":11, "Random 2":12, "Random 3":13}
algorithms = ["RRT", "RRT Connect", "Dynamic RRT", "RRT*", "Informed RRT*", "RRT* Smart"] 
iters_default = {"RRT":10000, "RRT Connect":5000, "Dynamic RRT":5000, "RRT*":1000, "Informed RRT*":1000, "RRT* Smart":1000}

NAME_SIZE = 19
def name(name):
    dots = NAME_SIZE-len(name)-1
    return sg.Text(name + ' '*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0))

sg.theme("TealMono")

leftcol = [
            [name("Select Algorithm:"), sg.Drop(algorithms, key="-Algo-", default_value="RRT", enable_events=True)],
            [name("Select Terrain:"), sg.Drop(list(terrains_dict.keys()), key="-Env-", default_value="Chaos Terrain", enable_events=True)],
            [name("Start coordinate:"), sg.Spin([i for i in range(1,50)], initial_value=2, key="startx"), sg.Text('x'), sg.Spin([i for i in range(1,30)], initial_value=2, key="starty"), sg.Text('y')],
            [name("Goal coordinate:"), sg.Spin([i for i in range(1,50)], initial_value=49, key="goalx"), sg.Text('x'),sg.Spin([i for i in range(1,30)], initial_value=24, key="goaly"), sg.Text('y')],
            [name("Enter value of n:"), sg.Input(key="-n-", size=10, default_text=iters_default["RRT"])],
            [sg.Check("Analysis", key="-analyze-")],
            [name("No. of iterations:"), sg.Spin([i for i in range(1,201)], initial_value=1, key="-iterations-")],
            [sg.Button("Run", size=(10, 1)), sg.Button("Exit", size=(10, 1))],
            [sg.Text("─"*44)],
            [sg.Output(size=(42, 25))]
        ]

rightcol = [[sg.Image("./rrt_2D/terrains/Chaos Terrain.png", key="-marsimg-", size=(400, 300)), sg.Image("./rrt_2D/terrains/Envs/Chaos Terrain.png", key="-marsenv-", size=(400, 300))],
            [sg.Text("─"*81)],
            [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')]
            ]


layout = [[sg.Column(leftcol), sg.VerticalSeparator(pad=None), sg.Column(rightcol, element_justification='c')]]

window = sg.Window("Rover Navigation System", layout, resizable=True, finalize=True, element_justification="center", font="Courier 12")
window.maximize()
canvas_elem = window['-CANVAS-']
figure_agg = None
fig = None


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "-Env-":
        window["-marsimg-"].update("./rrt_2D/terrains/"+values["-Env-"]+".png")
        window["-marsenv-"].update("./rrt_2D/terrains/Envs/"+values["-Env-"]+".png")

    if event == "-Algo-":
        window["-n-"].update(iters_default[values["-Algo-"]])

    if event == "Run":
        terrain = int(terrains_dict[values["-Env-"]])
        env.terrain = terrain
        util = utils.Utils()
        start = (values["startx"], values["starty"])
        goal = (values["goalx"], values["goaly"])
        n = int(values["-n-"]) if values["-n-"].isdigit() else iters_default[values["-Algo-"]]
        if util.is_inside_obs(Node(start)) or util.is_inside_obs(Node(goal)):
            if util.is_inside_obs(Node(start)):
                print("Invalid start node")
            if util.is_inside_obs(Node(goal)):
                print("Invalid goal node")
        else:
            analysis = values["-analyze-"]
            iterations = values["-iterations-"]
            if values["-Algo-"] == "RRT":
                fig = rrt.main(start, goal, terrain, analysis, iterations, n)
            elif values["-Algo-"] == "RRT Connect":
                fig = rrt_connect.main(start, goal, terrain, analysis, iterations, n)
            elif values["-Algo-"] == "Dynamic RRT":
                fig = dynamic_rrt.main(start, goal, terrain, analysis, iterations, n)
            elif values["-Algo-"] == "RRT*":
                fig = rrt_star.main(start, goal, terrain, analysis, iterations, n)
            elif values["-Algo-"] == "Informed RRT*":
                fig = informed_rrt_star.main(start, goal, terrain, analysis, iterations, n)
            elif values["-Algo-"] == "RRT* Smart":
                fig = rrt_star_smart.main(start, goal, terrain, analysis, iterations, n)
            print('-'*40)
        if figure_agg:
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            delete_figure_agg(figure_agg)
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)


window.close()


