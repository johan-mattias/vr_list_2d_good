def on_button_pressed_a():
    global max2, index, name
    max2 = len(students)
    index = randint(0, len(students) - 1)
    name = students[index]
    students.remove_at(index)
    basic.show_string("" + (name))
input.on_button_pressed(Button.A, on_button_pressed_a)

name = ""
index = 0
max2 = 0
students: List[str] = []
students = [
"Ahmad",
"Mohannad",
"Jwan",
"Alexander",
"Hilmir",
"Arvid",
"Foteini",
"Oscar",
"Anton",
"Pontus",
"Roder",
"Albin",
"Vilhelm",
"Leo",
"Adam",
"Kevin",
"Max",
"Sakariya",
"Dylan",
"Leo",
"Tryggve",
"Albin",
"Nikolai",
"Aziz",
"Muhammad",
"Maryam",
"Simon",
"Emil",
]