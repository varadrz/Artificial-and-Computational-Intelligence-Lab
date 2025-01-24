#Vacuum Cleaner Intelligent Agent Simulation
class VacuumCleanerAgent:
    def __init__(self, environment):
        #Initialize the environment and starting position of the agent
        self.environment = environment
        self.position = [0,0]               #Start at the top-left corner (0,0)
    def perceive_and_act(self):
        #Sense the current state of the environment at the agent's position
        current_state = self.environment[self.position[0]][self.position[1]]

        if current_state == 'Dirty':
            print (f"Position {self.position} is Dirty. Cleaning...")

            #Clean the current position
            self.environment[self.position[0]][self.position[1]] = 'Clean'
        
        else:
            print (f"Position {self.position} is Clean. Moving...")


#Move to the next position (simple strategy: move right, then down)
        if self.position [1] < len(self.environment[0]) - 1:
            #move right if not at the end of the row
            self.position[1] +=1
        elif self.position[0] < len(self.environment) - 1:
            #Move down if at the end of the row
            self.position[1] = 0
            self.position[0] +=1
        else:
            print ("Finished Cleaning the environment")
            return False        #No more positions to move to
        return True



# Define the environment (2D Grid)
# Each cell is either 'Dirty' or 'Clean'
environment = [
    ['Dirty', 'Clean'],
    ['Dirty', 'Dirty']
]


#Display the initial state of the environment
print("initial Environment:")
for row in environment:
    print(row)

#Create an instance of the vaccum cleaner agent
agent = VacuumCleanerAgent(environment)

#Run the agent in a loop until the environment is completely clean
while agent.perceive_and_act():
    #Display the environment after each action
    for row in environment:
        print(row)
    print()

#Display the final state of the environment
print("Final Environment:")
for row in environment:
    print(row)