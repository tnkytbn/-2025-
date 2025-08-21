#ナズェミテルンディス!!!
import Start_Pyxel_Game
import random
import pyxel
import math
import Hit_Pyxel
class Arrow:
    def __init__(self,arrow_x,arrow_y,ARROW_DIRECTION , is_Reverse_mode):
        self.is_Hit = False
        self.arrow_x = arrow_x
        self.arrow_y = arrow_y + 12
        self.Damage = [[0 for x in range(16)] for y in range(8)]
        for x in range(16):
            self.Damage[4][x] = 3

        for x in range(10,14):
            self.Damage[3][x] = 2
            self.Damage[5][x] = 2

        for x in range(10,12):
            self.Damage[2][x] = 1
            self.Damage[6][x] = 1

        self.is_Reverse_mode = is_Reverse_mode
        self.ARROW_DIRECTION = ARROW_DIRECTION
        if self.is_Reverse_mode:
            self.ARROW_DIRECTION = (self.ARROW_DIRECTION + 1) % 2
            self.arrow_y -=  20

        if self.ARROW_DIRECTION == 0:
            self.arrow_x += 26
        else:
            self.arrow_x -= 10
        self.arrow_y +=  9

    def update(self,SCREEN_WIDTH):
        if (-15 <= self.arrow_x <= SCREEN_WIDTH):
            self.arrow_x += 5 * (-1) ** self.ARROW_DIRECTION

    def draw(self):
        pyxel.blt(self.arrow_x, self.arrow_y, self.ARROW_DIRECTION, 48, 0, 16, 8, pyxel.COLOR_WHITE)


class Enemy:
    def __init__(self,SCREEN_WIDTH,SCREEN_HIGHT,Status):
        self.Enemy_max_hp,self.ATK ,self.deff = Status
        self.Enemy_max_hp = round(self.Enemy_max_hp * 1000)
        if self.Enemy_max_hp < 100:
            self.Enemy_max_hp = 100
        self.Enemy_hp = self.Enemy_max_hp
        self.Enemy_hp_Text = self.Enemy_hp
        self.Enemy_HP_Bar = 16
        self.Enemy_per = 1000
        self.Enemy_Size_y = 32
        self.Enemy_x = 132
        self.Enemy_y = SCREEN_HIGHT // 2 - 20
        self.phase = 1
        self.chenge_time = 5
        self.hp_Act = False
        self.Wait_New_Form = False
        self.Trans_Form = False
        self.Form = 0
        self.Beat_Direction = False
        self.Beat_Time = 0
        self.Hole_Appear = False
        self.Hole_Disapaer = False
        self.Hole_Del_time = -1
        self.can_Back_By_Beat = False
        balls=[]
        # ビットアート
        self.Damage = [[0 for x in range(24)] for y in range(32)]
        for x in range(14,18):
            self.Damage[3][x] = 1
        for x in range(13,20):
            self.Damage[4][x] = 1
        for x in range(12,21):
            self.Damage[5][x] = 1
        for y in range(6, 11):
            for x in range(11,22):
                self.Damage[y][x] = 1
        for x in range(12,21):
            self.Damage[11][x] = 1
        for x in range(13,20):
            self.Damage[12][x] = 1
        for x in range(14,20):
            self.Damage[13][x] = 1
        #腕
        for y in range(14,16):
            for x in range(6,20):
                self.Damage[y][x] = 1

        for x in range(6,12):
            self.Damage[16][x] = 1
        for x in range(7,10):
            self.Damage[17][x] = 1
        for y in range(16, 21):
            for x in range(13, 21):
                self.Damage[y][x] = 1
        for y in range(21, 23):
            for x in range(13, 20):
                self.Damage[y][x] = 1
        for y in range(23,31):
            for x in range(13,16):
                self.Damage[y][x] = 1
                self.Damage[y][x + 4] = 1
        self.Damage[29][13] = 0
        self.Damage[29][17] = 0

    def Enemy_hp_is_zero(self):
        return self.Enemy_hp <= 0

    def Enemy_Full_Heal(self):
        if self.hp_Act:
            if self.Wait_New_Form:
                if self.Enemy_hp < self.Enemy_max_hp:
                    self.Enemy_Heal()
                else:
                    self.Wait_New_Form = False
                    self.hp_Act = False
            else:
                self.Wait_New_Form = True

    def Enemy_Heal(self):
        self.Enemy_hp += 50

    def beat(self):
        self.Enemy_y += 3
        if self.Enemy_Size_y > 0:
            self.Enemy_Size_y -= 3
        else:
            if self.Hole_Del_time < 0:
                self.Hole_Del_time = pyxel.frame_count
            elif (pyxel.frame_count - self.Hole_Del_time) > 10:
                self.Hole_Appear = False
                self.Hole_Disapaer = True
                self.can_Back_By_Beat = True

    def Beat_Enemy(self):
        if not (self.Beat_Direction):
            pyxel.stop()
            self.Beat_Direction = True
            self.Beat_Direction_time = pyxel.frame_count
        elif ((self.Beat_Direction_time - pyxel.frame_count) % 20 == 0):
            if self.Hole_Appear:
                self.beat()
            elif not (self.Hole_Disapaer):
                self.Hole_Appear = True

    def Enemy_HP_Text(self):
        if self.Enemy_hp < 0:
            self.Enemy_hp = 0
        self.Enemy_hp_Text = self.Enemy_hp
        self.Enemy_HP_Bar = round(self.Enemy_hp * 32 / self.Enemy_max_hp)

    def Phase_Change(self,Player):
        if self.Enemy_hp == 0 and (self.phase == 1):
            if not (self.Trans_Form):
                self.TF_Time = pyxel.frame_count
                self.Trans_Form = True
                self.Damage[14][5] = 1
                self.Damage[15][5] = 1
                self.Damage[0][12] = 1
                self.Damage[0][13] = 1
                self.Damage[0][18] = 1
                self.Damage[0][19] = 1
                self.Damage[1][11] = 1
                self.Damage[1][12] = 1
                self.Damage[1][19] = 1
                self.Damage[1][20] = 1
                self.Damage[2][11] = 1
                self.Damage[2][20] = 1
                self.Damage[3][11] = 1
                self.Damage[3][20] = 1
                self.Damage[3][12] = 1
                self.Damage[3][19] = 1
                self.Damage[4][12] = 1
                for y in range(27,29):
                    self.Damage[y][13] = 0
                    self.Damage[y][17] = 0
                self.Damage[26][17] = 0
                Player.Delete_Arrow()
            elif ((pyxel.frame_count - self.TF_Time) % 60 == 0):
                self.deff *=  1.5
                self.ATK *=  1.5
                self.Enemy_max_hp = round(self.Enemy_max_hp * 1.5)
                self.Enemy_hp = 100
                self.phase = 2
                self.From = 1
                self.Trans_Form = False
                self.hp_Act = True
            elif ((pyxel.frame_count - self.TF_Time) % self.chenge_time == 0):
                self.Form = (self.Form + 1) % 2

    #def atk(self,num):
      #balls.append(ball(num))
    def Delete_Atk_Count(self):
        delete=0
        for ball in self.ball.copy():
            balls.update(self.SCREEN_WIDTH)
            Hit_Pyxel.Hit(arrows, Enemy).Attack_To_Enemy()
            if not (-15 <= ball.x <= self.SCREEN_WIDTH):
                self.balls.remove(ball)
                delete+=1
        return delete


    def Delete_ball(self):
        for ball in self.balls.copy():
            self.arrow.remove(ball)



class Player:
    def __init__(self,SCREEN_WIDTH,SCREEN_HIGHT,Mode):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HIGHT = SCREEN_HIGHT
        self.arrow = []
        self.player_x = SCREEN_WIDTH // 2 - 64
        self.player_y = SCREEN_HIGHT // 2 - 16
        self.wait_time = 10
        self.wait = -1 * self.wait_time
        self.HP_Bar = 16
        self.per = 1000
        self.Mode = Mode
        # ノーダメージチャレンジモード
        if self.Mode[0]:
            self.player_max_hp = 1
            self.player_hp = 1
            self.player_hp_Text = 1
        else:
            self.player_max_hp = 100
            self.player_hp = self.player_max_hp
            self.player_hp_Text = self.player_hp
        # リバースモード
        if self.Mode[1]:
            self.REVERSE_MODE = True
            self.Deg = 540
            self.WITCH_DIRECTION = 1
        else:
            self.WITCH_DIRECTION = 0
            self.Deg = 0

    def move(self):
        # 移動
        # 右
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.Mode[1]:
                if self.player_x + 13 > 0:
                    self.player_x -= 3
            else:
                if self.player_x - 19 < self.SCREEN_HIGHT:
                    self.player_x += 3

        # 左
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.Mode[1]:
                if self.player_x - 19 < self.SCREEN_HIGHT:
                    self.player_x += 3
            else:
                if self.player_x + 13 > 0:
                    self.player_x -= 3
        # 上
        if pyxel.btn(pyxel.KEY_UP):
            if self.Mode[1]:
                if self.player_y + 19 < self.SCREEN_HIGHT:
                    self.player_y += 3
            else:
                if self.player_y + 13 > 0:
                    self.player_y -= 3
        # 下
        if pyxel.btn(pyxel.KEY_DOWN):
            if self.Mode[1]:
                if self.player_y + 13 > 0:
                    self.player_y -= 3
            else:
                if self.player_y + 19 < self.SCREEN_HIGHT:
                    self.player_y += 3

        # 向き(バンクの番号)を切り変える
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if (self.Deg == 180):
                self.WITCH_DIRECTION = 1
            else:
                self.WITCH_DIRECTION = 0

        if pyxel.btnp(pyxel.KEY_LEFT):
            if (self.Deg == 180):
                self.WITCH_DIRECTION = 0
            else:
                self.WITCH_DIRECTION = 1

    def Player_Shot(self,Enemy):
        # 矢を打つ
        if (pyxel.frame_count - self.wait >= self.wait_time) and ( pyxel.btn(pyxel.KEY_Z)or pyxel.btn(pyxel.KEY_SHIFT)) and not (
                Enemy.Trans_Form or Enemy.hp_Act):
            self.wait = pyxel.frame_count
            self.arrow.append(Arrow(self.player_x, self.player_y, self.WITCH_DIRECTION,self.Mode[1]))
        for arrows in self.arrow.copy():
            arrows.update(self.SCREEN_WIDTH)
            Hit_Pyxel.Hit(arrows, Enemy).Attack_To_Enemy()
            if not (-15 <= arrows.arrow_x <= self.SCREEN_WIDTH) or arrows.is_Hit:
                self.arrow.remove(arrows)

    def Player_HP_Text(self):
        if self.player_hp < 0:
            self.player_hp = 0
        self.player_hp_Text = self.player_hp
        self.HP_Bar = round(self.player_hp * 32 / self.player_max_hp)

    def Player_hp_is_zero(self):
        return self.player_hp <= 0

    def Delete_Arrow(self):
        for arrows in self.arrow.copy():
            self.arrow.remove(arrows)


class App:
    def __init__(self,SCREEN_WIDTH,SCREEN_HIGHT,JP_Font ,Mode):
        self.Time_Zero = pyxel.frame_count
        self.Mode = Mode
        f = open("save.txt")
        savetxt = f.readlines()
        f.close()
        save = []
        for s in savetxt:
            try:
                save.append(int(s.split("=")[1]))
            except:
                save.append(float(s.split("=")[1]))
        self.Status = [save[0],save[1],save[2]]
        self.FPS=save[3]
        self.is_No_Hit_mode ,self.is_Reverse_mode = Mode
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HIGHT = SCREEN_HIGHT
        self.Ellen = Enemy(self.SCREEN_WIDTH,self.SCREEN_HIGHT ,self.Status)
        self.karen = Player(self.SCREEN_WIDTH,self.SCREEN_HIGHT,self.Mode)
        self.JP_Font = JP_Font
        pyxel.load("witch.pyxres")
        pyxel.sound(60).set("c3d4e4f4", "S", "5", "N", 20)
        pyxel.sound(61).set("e4e3", "S", "5", "N", 5)
        self.is_Game_Over = False
        self.can_Back = False
        self.Re_Start = False
        self.Select = False
        self.is_Stop_Music = False
        self.Preparation = True
        self.Sound_Wait = 0
        self.Select_Command = 0
        self.Any_Command = 2
        self.How_Long_Atk = 250
        self.Enemy_Attack_Count = 0

    def run(self):
        pyxel.playm(0,loop = True)
        pyxel.run(self.update, self.draw)

    def update(self):
        #Escで終了
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_E):
            self.karen.player_hp -= 10000000000000000000000000

        Restart_Wait = self.can_Back and not(self.Re_Start)
        # スタート画面もしくは終了
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_SHIFT)) and Restart_Wait:
            if self.Select_Command == 0:
                pyxel.play(0, 60)
                self.Re_Start = True
                self.Sound_Wait = pyxel.frame_count
            elif self.Select_Command == 8:
                pyxel.quit()

        #カーソル
        if Restart_Wait:
            if pyxel.btnp(pyxel.KEY_DOWN):
                pyxel.play(0, 61)
                self.Select_Command = (self.Select_Command / 8 + 1) % self.Any_Command * 8

            if pyxel.btnp(pyxel.KEY_UP):
                pyxel.play(0, 61)
                self.Select_Command = (self.Select_Command / 8 - 1) % self.Any_Command * 8

        #点滅させた後スタート画面に戻る処理
        if  self.Re_Start:
            #スタート画面に戻る
            if (pyxel.frame_count - self.Sound_Wait) > 20:
                Start_Pyxel_Game.App_Start(self.Mode).run()
            #表示のフラグ
            elif (pyxel.frame_count - self.Sound_Wait) % 5 == 0:
                self.Preparation = not (self.Preparation)

        if not(self.karen.Player_hp_is_zero() or self.Ellen.Enemy_hp_is_zero()) or self.Ellen.Trans_Form:
            self.karen.move()
            self.karen.Player_Shot(self.Ellen)
            #敵の攻撃抽選
            if not(self.Enemy_Attack_Count>self.How_Long_Atk):
                self.Enemy_Attack_Count=0
                #EneAt=random.randint(0,1)
            #self.Ellen.atk(EneAt)
            #self.Enemy_Attack_Count += self.karen.Delete_Atk_Count()
            # プレイヤーのHP表記
            self.karen.Player_HP_Text()
            # 敵のHP表記
            self.Ellen.Enemy_HP_Text()
            # Phase変化演出
            self.Ellen.Phase_Change(self.karen)
            #敵のHPが回復する演出
            self.Ellen.Enemy_Full_Heal()
        elif not(self.karen.Player_hp_is_zero()):
            self.karen.Delete_Arrow()
            #倒す演出
            self.Ellen.Beat_Enemy()
            self.can_Back = self.Ellen.can_Back_By_Beat
        elif self.karen.Player_hp_is_zero():
            # プレイヤーのHP表記
            self.karen.Player_HP_Text()
            self.karen.Delete_Arrow()
            self.is_Game_Over = True
            if not(self.is_Stop_Music):
                pyxel.stop()
                self.is_Stop_Music = True
            self.can_Back = True


    def draw(self):
        #画面を初期化
        pyxel.cls(pyxel.COLOR_BLACK)

        #夕暮れ
        for x in range(20):
            for y in range(11):
                pyxel.blt(8 * x,  8 * y, 0, 40, 8, 8, 8)

        #野原を表示
        for x in range(20):
            for y in range(5):
                pyxel.blt(8 * x, self.SCREEN_HIGHT - 8 * y, x % 2, 0, 8, 8, 8)

        #木を描写
        for x in range(20):
                pyxel.blt(16 * x, self.SCREEN_HIGHT - 48, 0, 40, 16, 16, 16,pyxel.COLOR_WHITE)

        # 主人公を描写
        pyxel.blt(self.karen.player_x, self.karen.player_y, self.karen.WITCH_DIRECTION, 8, 0, 32, 32, pyxel.COLOR_WHITE, self.karen.Deg)

        # HPを表示
        pyxel.text(4, 4, f'HP:{self.karen.player_hp_Text:>3}/{self.karen.player_max_hp}', pyxel.COLOR_WHITE)
        pyxel.blt(4, 10, 0, 8, 32, 32, 8, pyxel.COLOR_BLACK)
        pyxel.blt(4, 10, 0, 8, 40, self.karen.HP_Bar, 8, pyxel.COLOR_BLACK)

        if not(self.is_Game_Over):
            #自機(当たり判定)を描写
            pyxel.blt(self.karen.player_x + 12, self.karen.player_y + 12, self.karen.WITCH_DIRECTION, 40, 0, 8, 8, pyxel.COLOR_WHITE)
        elif self.is_Game_Over:
            pyxel.text(self.SCREEN_WIDTH // 2 - 35, self.SCREEN_HIGHT // 2 - 12, 'ゲームオーバー', pyxel.COLOR_WHITE, self.JP_Font)
            if self.Preparation:
                pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 , 'TITLE', pyxel.COLOR_WHITE)
            pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 + 8 , 'E N D', pyxel.COLOR_WHITE)
            pyxel.blt(self.SCREEN_WIDTH // 2 - 28, self.SCREEN_HIGHT // 2 + self.Select_Command, 0, 0, 32, 8, 8,
                      pyxel.COLOR_BLACK)

        for arrows in self.karen.arrow:
            arrows.draw()

        #敵の表示
        if self.Ellen.Hole_Appear:
            pyxel.blt(self.Ellen.Enemy_x, 65, 0, 88, 48, 24, 16, pyxel.COLOR_WHITE)

        # 敵の表示
        if (self.Ellen.Enemy_Size_y > 0) or self.Ellen.Trans_Form:
            pyxel.blt(self.Ellen.Enemy_x, self.Ellen.Enemy_y, 0, 64, 32 * self.Ellen.Form, 24, self.Ellen.Enemy_Size_y, pyxel.COLOR_WHITE)
            pyxel.text(self.SCREEN_WIDTH - 50 , 4, f'HP:{self.Ellen.Enemy_hp_Text:>4}/{self.Ellen.Enemy_max_hp}', pyxel.COLOR_WHITE)
            pyxel.blt(self.SCREEN_WIDTH - 35, 10, 0, 8, 32, 32, 8, pyxel.COLOR_BLACK)
            pyxel.blt(self.SCREEN_WIDTH - 35, 10, 0, 8, 40, self.Ellen.Enemy_HP_Bar, 8, pyxel.COLOR_BLACK)
        elif self.Ellen.phase == 2 and not(self.Ellen.Hole_Appear):
            #クリアタイムの処理
            Crear_Sec = (self.Ellen.Beat_Direction_time - self.Time_Zero) / self.FPS
            self.beat_Time_min = math.floor(Crear_Sec / 60)
            self.beat_Time_sec = math.floor(Crear_Sec) % 60
            if self.beat_Time_sec < 10:
                self.beat_Time_sec = "0" + str(self.beat_Time_sec)
            elif Crear_Sec < 6000:
                self.beat_Time_sec = str(self.beat_Time_sec)
            elif Crear_Sec >= 6000:
                self.beat_Time_sec = "59"

            if self.beat_Time_min < 10:
                self.beat_Time_min = "0" + str(self.beat_Time_min)
            elif self.beat_Time_min < 100:
                self.beat_Time_min = str(self.beat_Time_min)
            else:
                self.beat_Time_min = "99"

            self.beat_Time = self.beat_Time_min + ":" + self.beat_Time_sec
            pyxel.text(self.SCREEN_WIDTH // 2 - 34, self.SCREEN_HIGHT // 2 - 12, 'ゲームクリア', pyxel.COLOR_WHITE, self.JP_Font)
            pyxel.text(self.SCREEN_WIDTH // 2 - 24, self.SCREEN_HIGHT // 2, f'Time:{self.beat_Time}', pyxel.COLOR_WHITE)
            if self.Preparation:
                pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 + 6, 'TITLE', pyxel.COLOR_WHITE)
            pyxel.text(self.SCREEN_WIDTH // 2 - 18, self.SCREEN_HIGHT // 2 + 14, 'E N D', pyxel.COLOR_WHITE)
            pyxel.blt(self.SCREEN_WIDTH // 2 - 28, self.SCREEN_HIGHT // 2 + 6 + self.Select_Command, 0, 0, 32, 8, 8,
                      pyxel.COLOR_BLACK)
            if self.Mode[0] and self.Mode[1]:
                pyxel.text(self.SCREEN_WIDTH // 2 + 30, self.SCREEN_HIGHT // 2 + 30, 'マジかよ…', pyxel.COLOR_WHITE,
                           self.JP_Font)

        if self.Mode[0]:
            pyxel.text(4, 20, 'CHALLENGE_MODE', pyxel.COLOR_RED)
        if self.Mode[1]:
            pyxel.text(4, 30, 'REVERSE_MODE', pyxel.COLOR_RED)

if __name__ == "__main__":
    Start_Pyxel_Game.App_pyxel_init().run()