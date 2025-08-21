import os
import pyxel
import Start_Pyxel_Game
class Seting_App:
    def __init__(self ,MODE ,SCREEN_WIDTH ,SCREEN_HIGHT):
        f = open("save.txt")
        savetxt = f.readlines()
        f.close()
        save=[]
        for s in savetxt:
            try:
                save.append(int(s.split("=")[1]))
            except:
                save.append(float(s.split("=")[1]))

        self.Status= save
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HIGHT = SCREEN_HIGHT
        self.Mode = MODE
        self.Back = False
        self.Select_Status = True
        self.Display = True
        self.Back_Wait_Time = -1
        self.Select_Command = 0
        pyxel.load("Title.pyxres")
        pyxel.sound(0).set("c3d4e4f4", "S", "5", "N", 20)
        pyxel.sound(1).set("e4e3", "S", "5", "N", 5)
        self.JP_Font = pyxel.Font(os.path.join("Language", "umplus_j10r.bdf"))
        self.x_Select_Command = 0
        self.y_Select_Command = 0
        self.x_Status_Length = 8
        self.Status_Bar = [Bar(x) for x in self.Status]
        self.Any_x = 5
        self.Any_y = 5
        self.y_Max = (self.Any_y - 1) * 8
        self.Select_Status_Array = [
            [1, 1.5, 2, 2.5, 3],
            [1, 1.5, 2, 2.5, 3],
            [1, 1.5, 2, 2.5, 3],
            [30, 45, 60, 75, 90]
        ]

        # 0:HP,1:ATTACK,2:DEFENSE,3:FPS
        self.temp_y = 0
        self.temp_x = 0
        self.x_Back_Cursor = 0
        self.y_Back_Cursor = 0
        self.Back_Point_x = -32
        self.Back_Point_y = 16

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.y_Max == self.y_Select_Command:
            self.x_Back_Cursor = self.Back_Point_x
            self.y_Back_Cursor = self.Back_Point_y
            self.Select_Status = False
        else:
            self.x_Back_Cursor = 0
            self.y_Back_Cursor = 0
            self.Select_Status = True

        if pyxel.btnp(pyxel.KEY_SHIFT) or pyxel.btnp(pyxel.KEY_SPACE):
            if self.y_Max == self.y_Select_Command:
                self.Back = True

        if self.Back:
            if (self.Back_Wait_Time < 0):
                pyxel.play(0, 0)
                self.Back_Wait_Time = pyxel.frame_count
            elif (pyxel.frame_count - self.Back_Wait_Time) > 20:
                with open("save.txt") as f:
                    rewrite=f.readlines()
                rewrite[0] = "HPrank=" + str(self.Status[0]) +'\n'
                rewrite[1] = "ATKrank=" + str(self.Status[1]) +'\n'
                rewrite[2] = "DEFrank=" + str(self.Status[2]) +'\n'
                rewrite[3] = "FPS=" + str(self.Status[3]) +'\n'
                with open("save.txt",mode='w') as f:
                    f.write(''.join(rewrite))

                Start_Pyxel_Game.App_Start(self.Mode).run()
            elif (pyxel.frame_count - self.Back_Wait_Time) % 5 == 0:
                self.Display = not(self.Display)

        if pyxel.btnp(pyxel.KEY_DOWN) and not(self.Back):
            pyxel.play(0, 1)
            self.y_Select_Command = (self.y_Select_Command / 8 + 1) % self.Any_y * 8
            if self.y_Max == self.y_Select_Command:
                self.x_Select_Command = 0
                self.Select_Status = False

        if pyxel.btnp(pyxel.KEY_UP) and not(self.Back):
            pyxel.play(0, 1)
            self.y_Select_Command = (self.y_Select_Command / 8 - 1) % self.Any_y * 8
            if self.y_Max == self.y_Select_Command:
                self.x_Select_Command = 0
                self.Select_Status = False

        if not(self.y_Max == self.y_Select_Command) and self.Select_Status:
            if pyxel.btnp(pyxel.KEY_RIGHT) and not(self.Back):
                pyxel.play(0, 1)
                self.x_Select_Command = (self.x_Select_Command / self.x_Status_Length + 1) % self.Any_x * self.x_Status_Length
                self.temp_y = int(self.y_Select_Command / 8)
                self.temp_x = int(self.x_Select_Command / self.x_Status_Length)
                self.Status[self.temp_y] = self.Select_Status_Array[self.temp_y][self.temp_x]
                self.Status_Bar[int(self.y_Select_Command / 8)] = self.x_Select_Command + self.x_Status_Length

            if pyxel.btnp(pyxel.KEY_LEFT) and not(self.Back):
                pyxel.play(0, 1)
                self.x_Select_Command = (self.x_Select_Command / self.x_Status_Length - 1) % self.Any_x * self.x_Status_Length
                self.temp_y = int(self.y_Select_Command / 8)
                self.temp_x = int(self.x_Select_Command / self.x_Status_Length)
                self.Status[self.temp_y] = self.Select_Status_Array[self.temp_y][self.temp_x]
                self.Status_Bar[int(self.y_Select_Command / 8)] = self.x_Select_Command + self.x_Status_Length

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        pyxel.blt(self.SCREEN_WIDTH // 2 - 28 + self.x_Back_Cursor,
                  self.SCREEN_HIGHT // 2 - 12 + self.y_Select_Command + self.y_Back_Cursor, 0, 0, 8, 8, 8,
                  pyxel.COLOR_BLACK)
        pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 - 44 + self.y_Max, 'H P:', pyxel.COLOR_WHITE)
        pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 - 36 + self.y_Max, 'ATK:', pyxel.COLOR_WHITE)
        pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 - 28 + self.y_Max, 'DEF:', pyxel.COLOR_WHITE)
        pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 - 20 + self.y_Max, 'FPS:', pyxel.COLOR_WHITE)
        pyxel.blt(self.SCREEN_WIDTH // 2, self.SCREEN_HIGHT // 2 - 44 + self.y_Max, 0, 8, 0,
                  int(self.Status_Bar[0] / 2), 8,
                  pyxel.COLOR_WHITE)
        pyxel.blt(self.SCREEN_WIDTH // 2, self.SCREEN_HIGHT // 2 - 36 + self.y_Max, 0, 8, 0,
                  int(self.Status_Bar[1] / 2), 8,
                  pyxel.COLOR_WHITE)
        pyxel.blt(self.SCREEN_WIDTH // 2, self.SCREEN_HIGHT // 2 - 28 + self.y_Max, 0, 8, 0,
                  int(self.Status_Bar[2] / 2), 8,
                  pyxel.COLOR_WHITE)
        pyxel.blt(self.SCREEN_WIDTH // 2, self.SCREEN_HIGHT // 2 - 20 + self.y_Max, 0, 8, 0,
                  int(self.Status_Bar[3] / 2), 8,
                  pyxel.COLOR_WHITE)
        if self.Display:
            pyxel.text(self.SCREEN_WIDTH // 2 - 18 + self.Back_Point_x,
                       self.SCREEN_HIGHT // 2 - 12 + self.y_Max + self.Back_Point_y, 'BACK', pyxel.COLOR_WHITE)

def Bar(Statu):
    if (Statu == 1) or (Statu == 30):
        return 8
    if (Statu == 1.5) or (Statu == 45):
        return 16
    if (Statu == 2) or (Statu == 60):
        return 24
    if (Statu == 2.5) or (Statu == 75):
        return 32
    if (Statu == 3) or (Statu == 90):
        return 40
    return 0
if __name__ == "__main__":
    Start_Pyxel_Game.App_pyxel_init().run()