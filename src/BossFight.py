##Grayson Carter
import random
import os
class BossFight:

  def __init__(self):
    self.bossattack = False
    self.bossfight = True
    self.bossalive = True
    self.playeralive = True
    self.bossblock = False
    self.bosskick = False
    self.attack = False
    self.block = False
    self.kick = False
    self.magic = False
    self.boss = False
    self.player = False
    self.magicuser = False
    self.mana = 0
    if self.magicuser == True:
      self.mana = 100
    self.bossdamage = 10
    self.playerdamage = 20
    self.bosshealth = 150
    self.playerhealth = 100
    self.move = random.randint(1, 3)
    if self.boss == False:
      self.bossattack = False
      self.bossblock = False
      self.bosskick = False
    if self.player == False:
      self.attack = False
      self.block = False
      self.kick = False

  def BossMove(self):
    self.player = False
    self.boss = True
    self.move = random.randint(1, 3)
    if self.move == 1:
      self.bossattack = True
      self.bossblock = False
      self.bosskick = False
      print("the boss is about to attack")
    elif self.move == 2:
      self.bossblock = True
      self.bossattack = False
      self.bosskick = False
      print("the boss is about to block")
    elif self.move == 3:
      self.bosskick = True
      self.bossattack = False
      self.bossblock = False
      print("the boss is about to kick")

  def PlayerMove(self):
    if (self.magicuser == False):
      self.boss = False
      self.player = True
      move = input("Would you like to 1.attack, 2.block, or 3.kick (Break Blocks)?")
      if move == "1":
        self.attack = True
        self.block = False
        self.kick = False
      elif move == "2":
        self.block = True
        self.attack = False
        self.kick = False
      elif move == "3":
        self.kick = True
        self.attack = False
        self.block = False
    elif (self.magicuser == True):
        self.boss = False
        self.player = True
        move = input("Would you like to 1.attack, 2.block, 3.kick (Break Blocks), or 4.magic?")
        if move == "1":
          self.attack = True
          self.block = False
          self.kick = False
          self.magic = False
        elif move == "2":
          self.block = True
          self.attack = False
          self.kick = False
          self.magic = False
        elif move == "3":
          self.kick = True
          self.attack = False
          self.block = False
          self.magic = False
        elif move == "4":
          self.kick = False
          self.attack = False
          self.block = False
          self.magic = True
          

  def BossDamage(self):
    if (self.bossalive):
      if self.attack == True:
        if self.bossblock == True:
          self.bosshealth = self.bosshealth
          print("Your attack was BLOCKED")
        elif (self.bossblock == False):
          self.bosshealth = self.bosshealth - self.playerdamage
      elif self.kick == True:
        if self.bossblock == True:
          self.bosshealth = self.bosshealth - self.playerdamage
        elif self.bossblock == False:
          self.bosshealth = self.bosshealth
          print("Your attack MISSED")
      elif(self.magic == True):
        if self.mana <0:
          print("you do not have enough mana to use magic")
        if self.mana >=0:
          self.mana = self.mana - 10
          if self.bossblock == True:
            bosshealth = self.bosshealth - (self.playerdamage/2)
            print("You managed to break the boss's block, but only did half damage")
          elif self.bossblock == False:
            self.bosshealth = self.bosshealth - self.playerdamage
            print("You hit the boss with magic")
          if(self.bossattack == True):
            print("You and the boss both punched each-other")
            print("You could either increase your mana use to damage the boss or you could not.")
            manaincrease = input("1. Increase, 2. Don't")
            if manaincrease == "1":
              print("You used 10 extra mana to damage the boss")
              self.bosshealth = self.bosshealth - self.playerdamage
            elif manaincrease == "2":
              print("you decided to preserve your mana")
              self.bosshealth = self.bosshealth
            if(self.bosskick == True):
              print("You see the boss's foot heading towards your face")
              print("Do you continue your attack or block the kick?")
              kickmagic = input("1. Attack, 2. Block")
              if kickmagic == "1":
                self.bosshealth = self.bosshealth - self.playerdamage
                print("You hit the boss with your attack")
              elif kickmagic == "2":
                print("You stopped the bosses kick")
                self.bosskick = False
      if (self.bosshealth <= 0):
        self.bosshealth = 0
        self.bossalive = False

  def PlayerDamage(self):
    if self.bossattack == True:
      if (self.block == True):
        print("Your block was successful")
      elif (self.block == False):
        print("The boss hit you")
        print("you lost ", self.bossdamage, " health")
        self.playerhealth = self.playerhealth - self.bossdamage
    elif self.bossblock:
      self.playerhealth = self.playerhealth
    elif self.bosskick:
      if self.block:
        print("You got kicked")
        print("you lost ", self.bossdamage, " health")
        self.playerhealth = self.playerhealth - self.bossdamage
      elif not self.block:
        print("You managed to dodge the kick")
      elif self.block:
        self.playerhealth = self.playerhealth - self.bossdamage
        print("The boss kicked you")

  def WheelChair(self):
    self.bosshealth = 100
    self.playerhealth = 100
    self.player = False
    self.boss = True

  def Monkeys(self):
    self.bosshealth = 200
    self.playerhealth = 100
    self.player = False
    self.boss = True

  def OldMan(self):
    self.bosshealth = 500
    self.playerhealth = 100
    self.bossdamage = 25
    self.player = False
    self.boss = False

  def Wizard(self):
    self.bosshealth = 1000
    self.playerhealth = 100
    self.bossdamage = 25
    self.player = False
    self.boss = False

  def BossFight(self):
    if self.playeralive and self.bossalive:
      while self.playeralive and self.bossalive:
        print("your health: ", self.playerhealth)
        print("Your mana: ", self.mana)
        print("boss health: ", self.bosshealth)
        self.BossMove()
        self.PlayerMove()
        self.BossDamage()
        self.PlayerDamage()
        os.system('clear||cls')
        print(self.bossalive)
        if not self.playeralive:
          print("you died")
          exit(0)
        if not self.bossalive:
          break
        if self.playeralive == False:
          exit(0)
