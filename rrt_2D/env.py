terrain = 6

terrains_dict = {1:"Chaos Terrain", 2:"Mesas Terrain", 3:"Cliffs Terrain", 4:"Craters Terrain", 5:"Glacier Terrain", 6:"Sand Dunes Terrain", 7:"Gullies Terrain", 8:"Medusae Fossae Terrain", 9:"Scalloped Terrain", 10:"Mud Volcanic Terrain", 11: "Random 1", 12:"Random 2", 13: "Random 3"}
class Env:
    
    def __init__(self):
        self.x_range = (0, 50)
        self.y_range = (0, 30)
        if terrain == 1: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars1()
        elif terrain == 2: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars2()
        elif terrain == 3: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars3()
        elif terrain == 4: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars4()
        elif terrain == 5: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars5()
        elif terrain == 6: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars6()
        elif terrain == 7: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars7()
        elif terrain == 8: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars8()
        elif terrain == 9: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars9()
        elif terrain == 10: 
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.mars10()
        elif terrain == 11:
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.terrain1()
        elif terrain == 12:
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.terrain2()
        elif terrain == 13:
            self.obs_boundary, self.obs_rectangle, self.obs_circle, self.img_url = self.terrain3()

    @staticmethod
    def terrain1():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [35, 3, 9, 4],
            [5, 20, 2, 7],
            [35, 15, 3, 5],
            [13, 6, 3, 9],
            [22, 24, 11, 2]
        ]

        obs_cir = [
            [7, 9, 3],
            [26, 17, 4],
            [40, 25, 3],
            [24, 7, 3],
            [15, 22, 3],
            [45, 17, 2]
        ]
        img_url = "./terrains/random1.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url

    @staticmethod
    def terrain2():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [5, 8, 4, 8],
            [6, 20, 10, 3],
            [23, 10, 4, 12],
            [14, 4, 9, 3],
            [33, 10, 8, 3],
            [40, 18, 3, 10]
        ]

        obs_cir = [
            [17, 14, 4],
            [33, 22, 4],
            [33, 5, 3],
            [45, 7, 3],
            [22, 26, 2]
            
        ]
        img_url = "./terrains/random1.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url


    @staticmethod
    def terrain3():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [8, 4, 3, 7],
            [20, 13, 15, 4],
            [42, 5, 3, 8],
            [20, 20, 4, 7],
            [18, 4, 10, 4]
        ]

        obs_cir = [
            [8, 22, 4],
            [15, 15, 3],
            [33, 25, 3],
            [42, 20, 3],
            [35, 7, 3]
        ]
        img_url = "./terrains/random1.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url


    @staticmethod
    def mars1():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [1, 18, 4, 12],
            [5, 28, 8, 2],
            [17, 10, 10, 7],
            [19, 17, 11, 4],
            [27, 15, 4, 2],
            [20, 24, 7, 6],
            [28, 26, 8, 4],
        ]

        obs_cir = [
            [7, 4, 1],
            [13, 3, 1],
            [10, 10, 3],
            [5, 15, 2],
            [14, 24, 1],
            [32, 10, 5],
            [35, 18, 1],
            [40, 22, 2],
            [38, 5, 1]
        ]
        img_url = "./terrains/mars1.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url


    @staticmethod
    def mars2():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [7, 5, 7, 20],
            [42, 1, 5, 12],
            [28, 24, 7, 5],   
        ]

        obs_cir = [
            [4, 23, 2],
            [18, 27, 3],
            [26, 12, 7],
            [40, 18, 3]
        ]
        img_url = "./terrains/mars2.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url
    

    @staticmethod
    def mars3():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [2, 25, 7, 5],
            [25, 1, 5, 8],
            [32, 5, 3, 4]
        ]

        obs_cir = [
            [12, 10, 6],
            [40, 5, 4],
            [29, 21, 9]
        ]
        img_url = "./terrains/mars3.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url
    

    @staticmethod
    def mars4():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            
        ]

        obs_cir = [
            [10, 15, 7],
            [35, 16, 9],
            [21, 10, 2],
            [16, 5, 1],
            [18, 5, 1],
            [16, 25, 2],
            [45, 11, 1]
        ]
        img_url = "./terrains/mars4.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url
    

    @staticmethod
    def mars5():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [8, 5, 3, 6],
            [10, 15, 6, 12],
            [16, 2, 3, 5],
            [25, 4, 16, 10],
            [28, 14, 11, 5],
            [32, 19, 6, 5],
            [21, 22, 4, 8],
            [25, 27, 6, 3]
        ]

        obs_cir = [
            
        ]
        img_url = "./terrains/mars5.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url


    @staticmethod
    def mars6():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
        ]

        obs_cir = [
            [6, 8, 3],
            [8, 17, 2],
            [17, 17, 4],
            [12, 25, 3],
            [27, 23, 5],
            [37, 26, 3],
            [20, 5, 1],
            [28, 7, 5],
            [35, 13, 3],
            [43, 16, 3]
        ]
        img_url = "./terrains/mars5.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url
    

    @staticmethod
    def mars7():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [10, 5, 20, 10],
            [13, 15, 14, 7],
            [33, 8, 5, 16]
        ]

        obs_cir = [
            
        ]
        img_url = "./terrains/mars5.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url
    
    
    @staticmethod
    def mars8():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [5, 8, 8, 12],
            [8, 23, 4, 7],
            [26, 12, 7, 6],
            [20, 18, 13, 12],
            [38, 1, 6, 9]
        ]

        obs_cir = [
            
        ]
        img_url = "./terrains/mars5.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url
    
    
    @staticmethod
    def mars9():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
            [28, 24, 12, 6],
            [40, 6, 4, 8]
        ]

        obs_cir = [
            [6, 10, 4],
            [5, 20, 2],
            [8, 18, 1],
            [30, 6, 1],
            [25, 27, 3],
            [42, 17, 3],
            [25, 15, 3]
        ]
        img_url = "./terrains/mars5.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url
    
    
    @staticmethod
    def mars10():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30,]
        ]

        obs_rectangle = [
        ]

        obs_cir = [
            [8, 6, 2],
            [10, 13, 3],
            [6, 24, 2],
            [23, 13, 2],
            [30, 20, 6],
            [35, 7, 4],
            [42, 22, 2]
        ]
        img_url = "./terrains/mars5.jpg"
        return obs_boundary, obs_rectangle, obs_cir, img_url