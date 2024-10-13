from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])


window = QWidget()
window.setWindowTitle("Створіть власного хробака")
window.show()
window.resize(500,500)

layout = QVBoxLayout()


name_input = QLineEdit()
name_input.setPlaceholderText("Введіть ім'я хробака")

size_combo = QComboBox()
size_combo.addItems(["Маленький", "Середній", "Великий"])

form_combo = QComboBox()
form_combo.addItems(["Прямий", "Кучерявий", "Хвилястий"])

create_button = QPushButton("Створити")

worm_display_label = QLabel("Тут буде ваш хробак")



def create_ascii_worm(name, size, form):
    worm_forms = {
        "Прямий": lambda s: "-" * s,
        "Кучерявий": lambda s: "#" * s,
        "Хвилястий": lambda s: "~" * s,
    }
    return f"{name}\n{worm_forms[form](size)}"

def create_worm():
    worm_name = name_input.text().strip()
    worm_size = size_combo.currentText()
    worm_form = form_combo.currentText()

    if not worm_name:
        QMessageBox.warning(window, "Увага", "Введіть ім'я хробака.")
        return

    size_mapping = {"Маленький": 10, "Середній": 15, "Великий": 25}
    size = size_mapping[worm_size]

    ascii_worm = create_ascii_worm(worm_name, size, worm_form)
    worm_display_label.setText(ascii_worm)


create_button.clicked.connect(create_worm)


layout.addWidget(QLabel("Введіть ім'я хробака:"))
layout.addWidget(name_input)
layout.addWidget(QLabel("Оберіть розмір хробака:"))
layout.addWidget(size_combo)
layout.addWidget(QLabel("Оберіть форму:"))
layout.addWidget(form_combo)
layout.addWidget(create_button)
layout.addWidget(worm_display_label)


window.setLayout(layout)
app.exec_()