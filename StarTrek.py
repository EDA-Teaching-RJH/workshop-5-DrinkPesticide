import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
			"shields": 100, 
			"weapons": 100, 
			"engines": 100, 
			"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

planets = {
	# dictionary of places for missions to be located on 
	"Bajor": {
		"Characters": {
			"Barriel": "Command"
			"Odo": "Operations"
			"Obrien": "Sciences"
			"Dax": "Sciences"
		}
		"Locations": {}
		"Items": {}
		"Enemies": {}
	}
	"Cardassia": {
		"Characters": {}
		"Locations": {}
		"Items": {}
		"Enemies": {}
	}
	"Romulus": {
		"Characters": {}
		"Locations": {}
		"Items": {}
		"Enemies": {}
	}
	"Earth": {
		"Characters": {
			"Sisko": "Command"
			"Odo": "Operations"
			"Obrien": "Sciences"
			"Dax": "Sciences"}
		"Locations": {}
		"Items": {}
		"Enemies": {}
	}
	"Qo'noS": {
		"Characters": {
			"Sisko": "Command"
			"Odo": "Operations"
			"Obrien": "Sciences"
			"Dax": "Sciences"
		}
		"Locations": {}
		"Items": {}
		"Enemies": {}
	}
	"Deep Space Nine": {
		"Characters": {
			"Sisko": "Command"
			"Odo": "Operations"
			"Obrien": "Sciences"
			"Dax": "Sciences"
		}
		"Locations": {}
		"Items": {}
		"Enemies": {}
	}
	}
def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

	if action == "1": 
		score += run_mission() 
	elif action == "2": 
		repair_system() 
	elif action == "3": 
		add_crew_member() 
	elif action == "4": 
		print(f"Simulation ended. Final score: {score}")
	else: 
		print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
# TODO: Implement function to display ship status, resources, and crew 
	for i in ship["systems"]:
		if ship["systems"][i] >= 1:
			print(f"{i} system integrity at {ship["systems"][i]}.")
		else: 
			print(f"{i} system integrity has failed.")

def get_user_action():
# TODO: Implement function to get and return user's chosen action 
	action = input("Please enter an action number from among the list:\n(1.) Deploy to mission. \n(2.) Spend a day repairing key ship systems. \n(3.) Deploy shuttle to recruit a crew member from a nearby system. \n(4.) End simulation and recieve score.")
	if (1 <= action >= 4):
		return action
	else:
		asfadf
def set_nearest_planet():
	asdfdsa	

def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 

def repair_system(): 
# TODO: Implement system repair functionality
	asdafd

def add_crew_member(): 
# TODO: Implement functionality to add a new crew member 
# player will select crew member from their roster as a shuttle pilot
# random planet will be selected by this function 
	asdfafd

def handle_random_event():
# TODO: Implement random events that can occur during the simulation 
	asdffasdd

def use_resource(resource, amount): 
# TODO: Implement resource usage logic 
	asdfdfa

def replenish_resources(): 
# TODO: Implement resource replenishment logic 
	sdfafadadfs

main()
