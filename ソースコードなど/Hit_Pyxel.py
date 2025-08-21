import pyxel
import Start_Pyxel_Game

class Temp_Player:
    def __init__(self):
        self.player_x = 0
        self.player_y = 0
        self.player_hp = 1

class Temp_Enemy:
    def __init__(self):
        self.Enemy_x = 0
        self.Enemy_y = 0
        self.deff = 1
        Enemy_hp = 1

class Hit:
    def __init__(self,atk,enemy = Temp_Enemy(),player = Temp_Player()):
        #無敵時間計測
        self.Invinciblity_Time = 360
        self.Invinciblity_Frames = (-1) * self.Invinciblity_Time
        self.enemy = enemy
        self.atk = atk

    def Attack_To_Enemy(self):
        Distan_x = self.enemy.Enemy_x - self.atk.arrow_x
        Distan_y = self.enemy.Enemy_y - self.atk.arrow_y
        damage = 0
        for index_y,atk_y in enumerate(self.atk.Damage):
            for index_x,atk_point in enumerate(atk_y):
                if pyxel.frame_count - self.Invinciblity_Frames > self.Invinciblity_Time:
                    atk_point_y = self.atk.arrow_y + index_y
                    atk_point_x = self.atk.arrow_x + index_x
                    hit_point_x = atk_point_x - self.enemy.Enemy_x
                    hit_point_y = atk_point_y - self.enemy.Enemy_y
                    if (hit_point_x < 0) or (hit_point_y < 0):
                        break
                    try:
                        damage += round(atk_point * self.enemy.Damage[hit_point_y][
                            hit_point_x] / self.enemy.deff)
                    except:
                        pass
        if not (damage == 0):
            self.enemy.Enemy_hp -= damage
            self.atk.is_Hit = True

    def Attack_Player(self):
        pass



if __name__ == "__main__":
    Start_Pyxel_Game.App_pyxel_init().run()