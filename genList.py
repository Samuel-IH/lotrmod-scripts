import os

potencies = [0, 1, 2, 3, 4]
containers = [
    ("lotr:item.mug", 0),
    ("lotr:item.ceramicMug", 100),
    ("lotr:item.gobletGold", 200),
    ("lotr:item.gobletSilver", 300),
    ("lotr:item.gobletCopper", 400),
    ("lotr:item.gobletWood", 500),
    ("lotr:item.skullCup", 600),
    ("lotr:item.wineGlass", 700),
    ("minecraft:glass_bottle", 800),
    ("lotr:item.waterskin", 900),
    ("lotr:item.aleHorn", 1000),
    ("lotr:item.aleHornGold", 1100),
]
prefix = "lotr:item.mug"
drinks = [
    ("DwarvenTonic", 4396),
    ("Ale", 4224),
    ("Miruvor", 4227),
    ("OrcDraught", 4228),
    ("Mead", 4298),
    ("RedWine", 4373),
    ("Cider", 4387),
    ("Perry", 4388),
    ("CherryLiqueur", 4389),
    ("Rum", 4390),
    ("AthelasBrew", 4391),
    ("Vodka", 4434),
    ("MapleBeer", 4492),
    ("Araq", 4511),
    ("CarrotWine", 4544),
    ("BananaBeer", 4545),
    ("MelonLiqueur", 4546),
    ("CactusLiqueur", 4600),
    ("TorogDraught", 4620),
    ("LemonLiqueur", 4679),
    ("LimeLiqueur", 4686),
    ("TauredainCocoa", 4721),
    ("CornLiquor", 4753),
    ("WhiteWine", 4818),
    ("MorgulDraught", 4848),
    ("PlumKvass", 4858),
    ("TermiteTequila", 4904),
    ("SourMilk", 4915),
    ("PomegranateWine", 4918)
]

output_zen = ""

for drink in drinks:
    for potency in potencies:
        for container in containers:
            output_zen += f"\ngenFor({drink[1]}, <{container[0]}>, <{prefix}{drink[0]}:{container[1]}>, {potency});"

# get path to this script
output_file = os.path.dirname(
    os.path.realpath(__file__)) + "/drink_extensions.zs"
input_code = open(output_file, "r").read()
output_code = input_code.split(
    "//AUTOGENERATED CODE")[0] + "//AUTOGENERATED CODE" + output_zen + "\n"
open(output_file, "w").write(output_code)