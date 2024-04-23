listNames = ["Daniela", "Arturo", "Rodolfo", "Danilo"]

print(listNames[0:3])
# output ['Daniela', 'Arturo', 'Rodolfo']

listNames.append("Marlene")
print(listNames)  # output ['Daniela', 'Arturo', 'Rodolfo', 'Danilo', 'Marlene']

listNames.sort()
print(listNames)  # output ['Arturo', 'Daniela', 'Danilo', 'Marlene', 'Rodolfo']
