import random, pygame

# loading all teams from a text file
def loadTeams():
    with open("Assets/teams.txt", "r") as f:
        lines = f.readlines()

    teams = []
    for line in lines:
        teams.append(line.strip())
    return teams

# Class that handles each match
class Match:
    def __init__(self, window, team1, team2, position, size):
        self.window = window
        self.position = position
        self.size = size

        self.team1 = team1
        self.team2 = team2
        self.winner = ""     
        self.score = {
            "team1":0,
            "team2":0
        }

        self.completed = False

        self.waitTime = 1   

    # Getting a winner for the match
    def DeclareWinner(self):
        if len(self.winner)!=0:
            return

        team1 = random.randint(0, 100)
        score = random.randint(1, 7)
        score2 = random.randint(0, score-1)

        if team1>random.randint(0, 100):
            self.winner = self.team1
            self.score["team1"] = score
            self.score["team2"] = score2
        else:
            self.winner = self.team2
            self.score["team1"] = score2
            self.score["team2"] = score

    # So goofy
    def DrawCard(self):
        size = self.size

        text = self.team1
        text2 = self.team2

        x = self.position[0]
        y = self.position[1]

        rect1 = pygame.Rect(x , y, size[0],  size[1])
        scorerect1 = pygame.Rect(x+15 , y+size[1]/2-5, size[0]-30,  size[1]-size[1]/2)
        rect2 =  pygame.Rect(x+size[0]+20, y, size[0],  size[1])
        scorerect2 = pygame.Rect(x+size[0]+20+15 , y+size[1]/2-5, size[0]-30,  size[1]-size[1]/2)


        pygame.draw.rect(self.window.screen, (23,23,23), rect1)
        pygame.draw.rect(self.window.screen, (23,23,23), rect2)
        pygame.draw.rect(self.window.screen, (0,0,0), scorerect1)
        pygame.draw.rect(self.window.screen, (0,0,0), scorerect2)

        if self.completed:
            self.window.Text(str(self.score["team1"]), scorerect1.center, (255,255,255), 15)
            self.window.Text(str(self.score["team2"]), scorerect2.center, (255,255,255), 15)
            
            if self.winner == self.team1:
                text += " >"
            else:
                text2 += " >"

        self.window.Text(text, (rect1.centerx ,rect1.y+10), (255,255,255), 15)
        self.window.Text("V.S", ((x+size[0]+10), rect1.centery), (0,0,0), 15)
        self.window.Text(text2, (rect2.centerx ,rect2.y+10), (255,255,255), 15)




    def Simulate(self):
        self.DeclareWinner()
        self.waitTime-=0.01

        if self.waitTime < 0:
            self.completed = True

# Simulating entire thing
class Tournament:
    def __init__(self, window, teams:list):
        self.window = window
        self.teams = []
        self.round = 1
        self.current = 0
        self.size = (75, 50)

        # Generating teams that qualified
        count = 0

        for i in range(len(teams)):
            if 70>(i*random.uniform(0, 1)):
                self.teams.append(teams[i])
                count+=1

            
            if count==16:
                break
        
        self.matches = []
        self.oldMatches = []

        # Creating round of 16
        matches = self.teams

        x = 10+self.size[0]+(100*(self.round-1))
        y = (self.window.size.y-(self.size[1]+20)*8/self.round)/2+20

        while len(matches)>0:
            team1 = matches[random.randint(0, len(matches)-1)]
            matches.remove(team1)
            team2 =  matches[random.randint(0, len(matches)-1)]
            matches.remove(team2)

            self.matches.append(Match(self.window, team1, team2, (x, y), self.size))
            y+=self.size[1]+20


    def nextBracket(self):
        self.round+=1   

        for m in self.matches:
            self.oldMatches.append(m)
        
        matches = []
        x = self.matches[0].position[0]+self.size[0]+150
        y = (self.window.size.y-(self.size[1]+20)*8/self.round)/2+20

        for i in range(0, len(self.matches)-1, 2):
            m = Match(self.window, self.matches[i].winner, self.matches[i+1].winner, (x,y), self.size)
            matches.append(m)
            y += self.size[1]+20
        
        self.matches = matches
    
    def Draw(self):
        for match in self.oldMatches:
            match.DrawCard()

        for match in self.matches:
            match.DrawCard()


    def Update(self):
        self.matches[self.current].Simulate()

        if self.matches[self.current].completed:
            self.current+=1
        
        if self.current>len(self.matches)-1:
            self.current = 0

            if self.round < 4:
                self.nextBracket()
            else:
                self.window.Text(f"{self.matches[0].winner} has won the world cup!", (self.window.size.x/2, self.window.size.y-20))

        self.Draw()
        


