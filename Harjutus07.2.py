#03.12 Joonas



mootmised = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]

print(f"Mõõdetav kuu: {mootmised[0]}")
print(f"Viimane mõõdetav tulemus: {mootmised[-1]}kraadi")
print(f"Kõik tempid: {mootmised[1: ]}")
print(f"Suurim tulemus: {max(mootmised[1: ])}")
print(f"Vähim tulemus: {min(mootmised[1: ])}")
print(f"Keskmine: {sum(mootmised[1: ]) / len(mootmised[1: ])}")
print(f"-20 esineb: {mootmised[1: ].count(-20)} korda")
del mootmised[4]
mootmised.insert(4,16)
mootmised[1:].sorted()
print(mootmised)

