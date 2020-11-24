input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    max2 = students.length
    index = randint(0, students.length - 1)
    name = students[index]
    students.removeAt(index)
    basic.showString("" + name)
})
let name = ""
let index = 0
let max2 = 0
let students : string[] = []
students = ["Ahmad", "Mohannad", "Jwan", "Alexander", "Hilmir", "Arvid", "Foteini", "Oscar", "Anton", "Pontus", "Roder", "Albin", "Vilhelm", "Leo", "Adam", "Kevin", "Max", "Sakariya", "Dylan", "Leo", "Tryggve", "Albin", "Nikolai", "Aziz", "Muhammad", "Maryam", "Simon", "Emil"]
