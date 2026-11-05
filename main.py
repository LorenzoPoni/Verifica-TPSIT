def registra_robot(self, robot_prodotti: list[Robot], newRobot: Robot) -> None:
    for(robot in robot_prodotti):
        if(newRobot.codice == robot.codice)
            raise.ValueError("Robot già presente")
    
    robot_prodotti.append(newRobot)

def cerca_robot(self, robot_prodotti: list[Robot], codice: str) -> Robot:
    for(robot in robot_prodotti):
        if(robot.codice == codice):
            return robot

    return

def riepologo_robot(self, nome_azienda: str, robot_prodotti: list [Robot]) -> None:
    for(robot in robot_prodotti):
        print(robot.codice, robot.modello, robot.stato, robot.peso_componenti(self))

if __name__ == "__main__":
    lista_robot = [Robot]
    robot1 = Robot("AB", "ZX", "Cucina", 10.0, "OK")
    registra_robot(self, lista_robot, robot1)