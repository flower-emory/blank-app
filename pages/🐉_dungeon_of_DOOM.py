import streamlit as st

rooms = [
    {
        "treasures": ["gold coin", "gem"],
        "monsters": ["goblin"],
        "secrets": ["map to next room"],
    },
    {
        "treasures": ["silver coin"],
        "monsters": ["troll"],
        "secrets": ["look behind the rock"],
    },
    {
        "treasures": ["diamond"],
        "monsters": ["dragon"],
        "secrets": ["use the key to open the door"],
    },
    {
        "treasures": ["ruby"],
        "monsters": ["giant spider"],
        "secrets": ["spiders are afraid of fire"],
    },
    {
        "treasures": ["emerald"],
        "monsters": ["unicorn", "giant eagle"],
        "secrets": ["unicorns are afraid of the dark"],
    },
    {
        "treasures": ["sapphire"],
        "monsters": ["giant squid"],
        "secrets": ["squids are afraid of the light", "the sapphire is actually glass"],
    },
    {
        "treasures": ["opal", "ruby"],
        "monsters": ["giant eagle"],
        "secrets": ["the eagle is actually a hologram"],
    },
]

st.title("Welcome to the dungeon! 👹")

st.write("Print out the first room:")
room = rooms[0]
st.write(room)

st.write("Print out the 3rd room:")
rooms[2]


st.write("Print out the last room:")
rooms[-1]

st.write("Print out the treasures in the 2nd room:")
rooms[1]["treasures"]


st.write("Print out the monsters in the 4th room:")
rooms[3]["monsters"]

st.write("Print out the second secret in the 6th room:")
rooms[5]["secrets"][1]