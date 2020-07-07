import string
# - Stupid Addition -------------------------------------------------------------------

def Stupid_Addition(inp1, inp2):
        if type(inp1) == str and type(inp2) == str:
            i1 = int(inp1)
            i2 = int(inp2)
            return i1 + i2

        if type(inp1) == int and type(inp2) == int:
            return f"'{inp1}{inp2}'"

print(Stupid_Addition(1, 6))

        
# - Unpacking dictionaries -------------------------------------------------------------------

dic1 = {"name1": "mary", "name2": "may", "name3": "like"}
dic2 = {"name1": "Eda", "name2": "bit", "name3": "love"}
dic3 = {"name1": "pidgey", "name2": "ratata", "name3": "have a"}

template = "I {name3} {name1}, I don't {name3} {name2}."

print (template.format(**dic1) )# ➞ "I like Mary, I don't like May."
print (template.format(**dic2) )# ➞ "I love Eda, I don't love Bit."
print (template.format(**dic3) )# ➞ "I have a Pidgey, I don't have a Rattata."

# - Capital Split  -------------------------------------------------------------------

def capital_split(txt):
    text = []
    for elem in txt:
        elem2 = elem
        if elem in string.ascii_uppercase:
            elem2 = f" {elem.lower()}"

        text.append(elem2)
    return "".join(text)

print(capital_split("iLoveMyTeapot")) 