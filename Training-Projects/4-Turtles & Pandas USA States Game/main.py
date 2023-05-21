import turtle
import pandas

class Main:

    def __init__(self):
      self.image = "blank_states_img.gif"
      self.screen = turtle.Screen()
      self.set_background()
      self.data = pandas.read_csv("50_states.csv")
      self.discovered_states_list = []
      self.undiscovered_states_list = self.data["state"].to_list()
      
    def set_background(self):
        self.screen.title("U.S. States Game")
        self.screen.addshape(self.image)
        turtle.shape(self.image)

    def check_answer_left(self, answer_state):
        
        answer_state = answer_state.capitalize()
        print(answer_state)
        
        if answer_state in self.undiscovered_states_list:
            self.discovered_states_list.append(answer_state)
            self.draw_state(answer_state)
        
        elif answer_state in self.discovered_states_list:
            print("Already in the Map!")
            self.get_input_answer_box()

        return(len(self.discovered_states_list))

    def get_input_answer_box(self):
        discovered_states_number = len(self.discovered_states_list)
        if discovered_states_number == 0:
            answer_state = self.screen.textinput(title="Guess the State", prompt="What's another state's name?")
        else:
            answer_state = self.screen.textinput(title=f"{len(self.discovered_states_list)}/50 States", prompt="What's another state's name?")
        return answer_state
    
    def draw_state(self, answer_state):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = self.data[self.data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    def exit_game(self):
        self.screen.exitonclick()


us_states_game = Main()
answer_try = us_states_game.get_input_answer_box()

while us_states_game.check_answer_left(answer_try) < 50 and answer_try.lower() != "exit":
    answer_try = us_states_game.get_input_answer_box()

if us_states_game.check_answer_left(answer_try) == 51:
    print("Won the game!")

us_states_game.exit_game()