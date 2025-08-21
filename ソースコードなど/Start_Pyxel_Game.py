import Pyxel_Game
import pyxel
import Pyxel_Seting
import os
SCREEN_WIDTH = 160
SCREEN_HIGHT = 120
class App_pyxel_init:
    def __init__(self):
        f=open("save.txt")
        fl1=f.readlines()
        f.close()
        fl2=fl1[3].split('=')
        framelate=int(fl2[1].strip())
        pyxel.init(SCREEN_WIDTH, SCREEN_HIGHT, title="魔女",fps=framelate)

    def run(self):
        App_Start().run()

class App_Start:
    def __init__(self,Mode = [False,False]):
        self.Start = False
        self.Set = False
        self.Start_Display = False
        self.Preparation = [True,True]
        self.Open_Time = 1
        pyxel.load("Title.pyxres")
        pyxel.sound(0).set("c3d4e4f4", "S", "5", "N", 20)
        pyxel.sound(1).set("e4e3", "S", "5", "N", 5)
        self.JP_Font = pyxel.Font(os.path.join("Language", "umplus_j10r.bdf"))
        self.Mode = Mode
        self.Select_Command = 0
        self.Any_Command = 3


    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        # ノーダメージチャレンジモードのフラグ
        No_Hit1 = pyxel.btn(pyxel.KEY_D) and pyxel.btnp(pyxel.KEY_N)
        No_Hit2 = pyxel.btnp(pyxel.KEY_D) and pyxel.btn(pyxel.KEY_N)
        # リバースモード
        Reverse1 = pyxel.btn(pyxel.KEY_R) and pyxel.btnp(pyxel.KEY_T)
        Reverse2 = pyxel.btnp(pyxel.KEY_R) and pyxel.btn(pyxel.KEY_T)
        #選択したか確認
        is_Select = pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_SHIFT)
        is_Wait_Time = not (self.Start or self.Set)
        if  pyxel.btnp(pyxel.KEY_DOWN) and is_Wait_Time:
            pyxel.play(0,1)
            self.Select_Command = (self.Select_Command / 8 + 1 ) % self.Any_Command  * 8

        if pyxel.btnp(pyxel.KEY_UP) and is_Wait_Time:
            pyxel.play(0,1)
            self.Select_Command = (self.Select_Command / 8 - 1 ) % self.Any_Command * 8

        if No_Hit1 or No_Hit2:
            self.Mode[0] = True
        if Reverse1 or Reverse2:
            self.Mode[1] = True

        if is_Select and is_Wait_Time:
            if self.Select_Command == 0:
                self.Start = True
                pyxel.play(0, 0)
                self.Open_Time = pyxel.frame_count
            elif self.Select_Command == 8:
                pyxel.quit()
            elif self.Select_Command == 16:
                self.Set = True
                pyxel.play(0, 0)
                self.Open_Time = pyxel.frame_count
        can_Open = pyxel.frame_count - self.Open_Time > 20
        if can_Open and self.Start:
            self.Start_Display = True
            Play_Game = Pyxel_Game.App(SCREEN_WIDTH ,SCREEN_HIGHT ,self.JP_Font ,self.Mode)
            Play_Game.run()

        if can_Open and self.Set:
            self.Start_Display = True
            Pyxel_Seting.Seting_App(self.Mode, SCREEN_WIDTH, SCREEN_HIGHT).run()

        elif ((pyxel.frame_count - self.Open_Time ) % 5 == 0) and self.Start:
            self.Preparation[0] = not(self.Preparation[0])
        elif ((pyxel.frame_count - self.Open_Time ) % 5 == 0) and self.Set:
            self.Preparation[1] = not(self.Preparation[1])

    def draw(self):
        if not(self.Start_Display):
            pyxel.cls(pyxel.COLOR_WHITE)
            pyxel.blt(0, 0, 0, 8, 8, SCREEN_WIDTH, SCREEN_HIGHT, pyxel.COLOR_WHITE)
            pyxel.blt(SCREEN_WIDTH // 2 - 28, SCREEN_HIGHT // 2 - 12 + self.Select_Command , 0, 0, 8, 8, 8, pyxel.COLOR_BLACK)
            pyxel.text(SCREEN_WIDTH // 2 - 18, SCREEN_HIGHT // 2 - 4, 'E N D', pyxel.COLOR_WHITE)
            if self.Preparation[0]:
                pyxel.text(SCREEN_WIDTH // 2 - 18, SCREEN_HIGHT // 2 - 12, 'START', pyxel.COLOR_WHITE)
            if self.Preparation[1]:
                pyxel.text(SCREEN_WIDTH // 2 - 18, SCREEN_HIGHT // 2 + 4 , 'S E T', pyxel.COLOR_WHITE)


if __name__ == '__main__':
    App_pyxel_init().run()