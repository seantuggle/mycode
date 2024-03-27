#!/usr/bin/env python3

def main():
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ")
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ")
    value = marvelchars.get(char_name, {}).get(char_stat, "Unknown")
    print(f"{char_name}'s {char_stat} is: {value.title()}")

marvelchars = {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    },
    "Iron Man": {
        "real name": "Tony Stark",
        "powers": "genius intellect, powered armor",
        "archenemy": "Mandarin"
    },
    "Thor": {
        "real name": "Thor Odinson",
        "powers": "godly strength, control over lightning",
        "archenemy": "Loki"
    },
    "Black Widow": {
        "real name": "Natasha Romanoff",
        "powers": "master assassin, martial artist",
        "archenemy": "Taskmaster"
    },
    "Captain America": {
        "real name": "Steve Rogers",
        "powers": "superhuman strength, agility, endurance",
        "archenemy": "Red Skull"
    },
    "Spider-Man": {
        "real name": "Peter Parker",
        "powers": "wall-crawling, super strength, spider-sense",
        "archenemy": "Green Goblin"
    },
    "Black Panther": {
        "real name": "T'Challa",
        "powers": "enhanced strength, agility, senses",
        "archenemy": "Killmonger"
    },
    "Doctor Strange": {
        "real name": "Stephen Strange",
        "powers": "sorcery, mystical arts",
        "archenemy": "Dormammu"
    },
    "Wolverine": {
        "real name": "Logan",
        "powers": "regenerative healing, adamantium claws",
        "archenemy": "Sabretooth"
    },
    "Deadpool": {
        "real name": "Wade Wilson",
        "powers": "accelerated healing factor, expert marksman, master martial artist, fourth-wall awareness",
        "archenemy": "Ajax (Francis)"
    },
    "Storm": {
        "real name": "Ororo Munroe",
        "powers": "weather manipulation, flight, control over lightning and winds",
        "archenemy": "Shadow King"
    },
    "Black Bolt": {
        "real name": "Blackagar Boltagon",
        "powers": "hypersonic voice capable of massive destruction, flight, energy manipulation",
        "archenemy": "Maximus the Mad"
    },
    "Captain Marvel": {
        "real name": "Carol Danvers",
        "powers": "superhuman strength, flight, energy projection, cosmic awareness",
        "archenemy": "Yon-Rogg"
    },
    "Groot": {
        "real name": "Groot",
        "powers": "super strength, regeneration, ability to control plant life",
        "archenemy": "Ronan the Accuser"
    },
    "Jean Grey": {
        "real name": "Jean Grey",
        "powers": "telepathy, telekinesis, phoenix force manipulation",
        "archenemy": "Magneto"
    },
    "Daredevil": {
        "real name": "Matt Murdock",
        "powers": "enhanced senses, radar sense, expert martial artist",
        "archenemy": "Bullseye"
    },
    "Venom": {
        "real name": "Eddie Brock",
        "powers": "symbiote grants superhuman strength, agility, shapeshifting, and web-slinging",
        "archenemy": "Carnage"
    },
    "Magneto": {
        "real name": "Max Eisenhardt (Erik Lehnsherr)",
        "powers": "control over magnetism, manipulation of metal objects",
        "archenemy": "Professor X"
    },
    "Black Cat": {
        "real name": "Felicia Hardy",
        "powers": "master thief, expert martial artist, probability manipulation",
        "archenemy": "Spider-Man"
    },
    "Quicksilver": {
        "real name": "Pietro Maximoff",
        "powers": "superhuman speed",
        "archenemy": "Magneto"
    },
    "War Machine": {
        "real name": "James Rhodes",
        "powers": "powered armor suit, weapons arsenal",
        "archenemy": "Iron Monger"
    },
    "Falcon": {
        "real name": "Sam Wilson",
        "powers": "flight, avian telepathy",
        "archenemy": "Red Skull"
    },
    "Winter Soldier": {
        "real name": "Bucky Barnes",
        "powers": "superhuman strength, agility, expert marksman",
        "archenemy": "Captain America (formerly)"
    },
    "Ant-Man": {
        "real name": "Scott Lang",
        "powers": "size manipulation, insect communication",
        "archenemy": "Yellowjacket"
    },
    "Wasp": {
        "real name": "Hope van Dyne",
        "powers": "size manipulation, bio-electric energy blasts",
        "archenemy": "Egghead"
    }
}

if __name__ == "__main__":
    main()

