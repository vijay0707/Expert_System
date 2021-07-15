from medical_expert_system import preprocess, Greetings
import os

Greet = Greetings()

def engine():
    while(1):
        Greet.reset()  # Prepare the engine for the execution.
        Greet.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        if input() == "no":
            print("Thank you for consulting")
            os._exit()
                #print(engine.facts)

def main():
    preprocess()
    engine()




# if __name__ == "__main__":
# 	main()