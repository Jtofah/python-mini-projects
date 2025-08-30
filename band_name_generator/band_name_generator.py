import random
import time

print("Hello Welcome to the Band Name Generator..")
user_city = input("What is the name of your city: ")
user_genre = input(f"What is your genre: Hiphop/Rock/Metal/Pop/Afrobeats: ").strip().capitalize()


#word Bank based on genre
#Hiphop
hh_adj = ["808", "Trap","GRP","Gremlin","Lethal","Coke","Dope","CP3","¥ve","4th Ave.","$treet","Westside","Bando","Black"]
hh_name = ["Boyz","Squad","Mob","Clan","Tribe","Crew","Family","Gang","Sh00ter$"]

#Rock
rock_adj = ["Rebel", "Scream", "Wild", "Electric", "Dead Core", "Classic", "Rocky", "Fiery", "Athemis", "Dread","Alloy"]
rock_name = ["Phase","Anki","Doom", "and the Cosmos", "Rising", "Forever", "thorn", "Revival", "Syndicate","Colts","Ghoul","Kaiju"]

#Metal
metal_adj = ["Slay","Feral","Black","Death","Scream","Hell's","Metal"]
metal_name = ["Steel", "Spawns", "Chains","Ghouls","Skulls", "Blades", "War", "Beasts", "Void", "Abyss", "Titans","Wolves","Sabbath","Inferno","Cult","Scythe","Reaper"]

#Pop
pop_adj = ["Purple","Five","Velvet","Imagine","Juke","Plane","Pay","Dance","The"]
pop_name = ["Boys","Harmony","Rose","Major","Pluto","Knight","Box","Day","Outs","Parrots","Fare","Ferry","Hearts","Clouds","Republic","Nation"]
pop_other = ["and the Symphony","and the Stags","and the Fairies","+ the Robots","& the wildlings","X Band"]

#Afrobeat
afbeat_othr = ["Afri","Black","Ninja","Joy","Vina","Banjo","Bongo","New","Africa","Simba","Sankofa","Asanti"]
afbeat_name = ["Senku","and the Calabash","Child","Tribe","Spirit","Sun","Band","Seed","Masquerades","Sistas","Bradas","Boiz","Chaskele","Express","Village","Rise","Afronauts","and the Shinobi"]

def band_name_gen():
    if user_genre == "Hiphop":  #when the user input is hiphop
       adj = hh_adj + [user_city]
       noun = hh_name
    elif user_genre == "Rock":    #when the user input is Rock
        adj = rock_adj + [user_city]
        noun = rock_name
    elif user_genre == "Metal":     #when the user input is Metal
        adj = metal_adj + [user_city]
        noun = metal_name
    elif user_genre == "Pop":       #when the user input is Pop
        adj = pop_adj + [user_city]
        noun = pop_name
        lead_singer = input(f"Are you the lead singer (Y/N): ").strip().upper()
        if lead_singer == 'Y':
            singer_name = input(f"What is your first name?: ").strip()
            adj = [singer_name]
            noun = pop_other 
        elif lead_singer == 'N':
            pass
        else:
            print(f"Wrong input!\nProceeding with default name generation...") 
            time.sleep(1)
    elif user_genre == "Afrobeats":     #when the user input is Afrobeats
        adj = afbeat_othr + [user_city]
        noun = afbeat_name
    else:
        return "Genre not Available"
  
  # Simulate generating the band name with a loading animation
    for i in range(101):  # Simulate 0% to 100%
        time.sleep(0.02)  # Delay to simulate processing
        print(f"\rGenerating your band name... [{i}%]", end="", flush=True)
    print("\nBand name generated successfully!\n")  # Move to the next line after loading completes
  
    #generate band name
    first_name = random.choice(adj)
    second_name = random.choice(noun)
    return f"{first_name} {second_name}"

# Generate and print the band name
band_name = band_name_gen()
print(f"Your band name is: {band_name}")
        