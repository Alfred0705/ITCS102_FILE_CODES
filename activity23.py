#3d dimentional list
#lol
yasuo =["lone adventurer", "wind_strike"]
akali =["rouge assasin", "shuriken"]
zed = ["master of the shadow", "shadow_clone"]
#dota
pudge = ["long range hook", "meat_hook"]
invoker = ["too many buttons", "serenadota"]
sniper = ["a long ranger shooter", "snipe"]
#god of war
kratos = ["the god of war", ""]
zues = ["god of olympus", ""]
posideon = ["brother of zues", ""]
#mobile legends 
gusion = ["magic assasin", "twin blades"]
fanny = ["agile assasin in land of dawn", "steel cable"]
alucard = ["first gen character", "fission wave"]
#wild rift
xayah = ["beast human", "double daggers"]
garen = ["the might of demacia", "demacia justice"]
lux = ["sister of garen", "final spark"]
#old
lol = ["yasuo", "akali", "zed"]
dota = ["pudge", "invoker", "sniper"]
god_of_war = ["kratos", "zues", "posideon"]
#new
mobile_legend = ["gusion", "fanny", "alucard"]
wild_rift = ["xayah", "garen", "lux"]
hok = ["wukong", "agudo", "yang_jian"]

old = ["lol", "dota", "god_of_war" ]
new = ["mobile_legends" , "wild rift", "hok"]

games = {"old games" : old, "new games": new}

print("=== 1. Going down one level at a time ===")
print(games["old"]["lol"]["yasuo"][1])

print()
print("=== 2. loop level 1: categories ===")
for category in games:
    print(category)

print()
print("=== 3. Loop level 1-2: categories and titles ===")
for category, titles in games.item():
    print(category)
    for title in titles:
        print(" -", title)

print()
print("=== 4. loop all levels ===")
for category, title in games.item():
    print(category)
    for title in titles.item():
        print(" " + title)
        for name. info in hero.item():
            print("   " + name)
            print("    Description:", info[0])
            print("    Power:", info[1])

print()
print("=== 5. Count every heroes ===")s
count = 0
for titles in games.value():
    for hero in title.value():
        for name in hero:
            count = count + 1
print("Total heroes:", count)

print()
print("=== 6. Search for a hero ===")
search = "yasuo"
found = False
for category , title in games.item():
    for title, hero in titles.item():
        if search in hero:
            print(search, "is from", title , "(" + category + ")")
            print("power:", hero[search][1])
            found = True
if found == False:
    print(search, "not found.")






