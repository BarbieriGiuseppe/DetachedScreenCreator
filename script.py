import subprocess
import time

def create_screens_with_detach(num_screens):
    screen_names = ["uno", "due", "tre", "qua", "cin", "sei", "set", "ott", "nov", "diec"]
    
    for i in range(num_screens):
        screen_name = screen_names[i]
        
        # Creazione della sessione screen
        create_command = f"screen -S {screen_name}"
        subprocess.run(create_command, shell=True)
        print(f"Created screen: {screen_name}")
        
        # Invio del comando "screen -d" all'interno della sessione appena creata
        detach_command = f"screen -S {screen_name} -d"
        subprocess.run(detach_command, shell=True)
        print(f"Detached from screen: {screen_name}")
        
        time.sleep(1)  # Attendi un secondo per evitare sovrapposizioni di nomi

if __name__ == "__main__":
    num_screens = 10
    create_screens_with_detach(num_screens)
