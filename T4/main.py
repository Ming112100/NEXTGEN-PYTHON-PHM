import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView, QTableWidgetItem, QLineEdit, QInputDialog
from PyQt6 import uic
import json, re
class SigninWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('s_in.ui', self)
        self.label_7.mousePressEvent = self.show_register  
        self.pushButton.clicked.connect(self.signin)
        self.lineEdit.returnPressed.connect(self.focus_password)
        self.lineEdit_2.returnPressed.connect(self.signin)
        self.ShowPassword.toggled.connect(self.show_password)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
    def show_password(self, checked):
        if checked:
            self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
    def focus_password(self):
        self.lineEdit_2.setFocus()
    def mousePressEvent(self, event):
        self.lineEdit.clearFocus()
        self.lineEdit_2.clearFocus()
        super().mousePressEvent(event)
    def show_register(self, event):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()
    import json
    def signin(self):
        username_or_email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username_or_email == "" or password == "":
            self.show_message("Error", "Username or password can't be empty.")
            return
        if username_or_email == "Administrator" and password == "admin123":
            self.show_message("Success", "Login successful as Admin!")
            self.show_home("Administrator")
            return
        try:
            with open('in4.json', 'r', encoding='utf-8') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}
        for username, info in users.items():
            if (username_or_email == username or username_or_email == info['email']) and info['password'] == password:
                self.show_message("Success", f"Welcome {username}!")
                self.show_home(username)
                return
        self.show_message("Error", "Invalid username or password.")
    def show_message(self, title, message):
        QMessageBox.information(self, title, message, QMessageBox.StandardButton.Ok)
    def show_home(self, username=None):
        if username == "Administrator":
            current_user_role = "Administrator"
        else:
            try:
                with open('in4.json', 'r', encoding='utf-8') as f:
                    users = json.load(f)
                current_user_role = users.get(username, {}).get("role", "Staff")
            except (FileNotFoundError, json.JSONDecodeError):
                current_user_role = "Staff"
        self.home_window = HomeWindow(username, current_user_role)
        self.home_window.show()
        self.close()
class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('s_up.ui', self)
        self.label_7.mousePressEvent = self.show_signin
        self.pushButton.clicked.connect(self.signup)
        self.ShowPassword.toggled.connect(self.show_password)
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
    def show_password(self, checked):
        if checked:
            self.Password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.Password.setEchoMode(QLineEdit.EchoMode.Password)
    def show_signin(self, event):
        self.signin_window = SigninWindow()
        self.signin_window.show()
        self.close()
    def valid_email(self,email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)
    def signup(self):
        username = self.Username.text()
        password = self.Password.text()
        email = self.Email.text()
        if not username or not password or not email:
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        with open("DATA.json", "r", encoding="utf-8") as f:
            employees = json.load(f)
        emails_in_data = [emp["Email address"] for emp in employees]
        try:
            with open("in4.json", "r", encoding="utf-8") as f:
                accounts = json.load(f)
        except:
            accounts = {}
        if username in accounts:
            QMessageBox.warning(self, "Error", "Username already exists!")
            return
        user_role = None
        for emp in employees:
            if emp["Email address"] == email:
                user_role = emp.get("role", "Staff")
                break
        accounts[username] = {
        "password": password,
        "email": email,
        "role": user_role
    }
        with open("in4.json", "w", encoding="utf-8") as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)
        QMessageBox.information(self, "Success","Account created successfully!")
        self.show_signin(None)
salary_map = {
    "Kế toán trưởng": "10,000,000 VNĐ",
    "Kế toán": "8,000,000 VNĐ", 
    "Quản lý": "12,000,000 VNĐ",
    "Thực tập sinh": "3,000,000 VNĐ",
    "Chuyên viên nhân sự": "10,000,000 VNĐ",
    "Nhân viên nhân sự": "7,000,000 VNĐ",
    "Nhà phát triển phần mềm": "9,500,000 VNĐ",
    "Chuyên viên phân tích dữ liệu": "15,500,000 VNĐ",
    "Nhân viên phân tích dữ liệu": "10,000,000 VNĐ",
    "Chuyên viên marketing": "9,500,000 VNĐ",
    "Nhân viên marketing": "8,000,000 VNĐ",
}
class HomeWindow(QMainWindow):
    def __init__(self, username, current_user_role):
        super().__init__()
        uic.loadUi('home.ui', self)
        self.load_data()
        self.username = username
        self.Name.setText(username)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.insert.mousePressEvent = self.insert_staff
        self.calc.mousePressEvent = self.calculator
        self.search.mousePressEvent = self.searching
        self.current_user_role = current_user_role
        self.tableWidget.cellDoubleClicked.connect(self.edit_or_delete_employee)
        self.employee_id = 1
        self.salary_map = {
            "Kế toán trưởng": "10,000,000 VNĐ",
            "Kế toán": "8,000,000 VNĐ", 
            "Quản lý": "12,000,000 VNĐ",
            "Thực tập sinh": "3,000,000 VNĐ",
            "Chuyên viên nhân sự": "10,000,000 VNĐ",
            "Nhân viên nhân sự": "7,000,000 VNĐ",
            "Nhà phát triển phần mềm": "9,500,000 VNĐ",
            "Chuyên viên phân tích dữ liệu": "15,500,000 VNĐ",
            "Nhân viên phân tích dữ liệu": "10,000,000 VNĐ",
            "Chuyên viên marketing": "9,500,000 VNĐ",
            "Nhân viên marketing": "8,000,000 VNĐ",
        }
        self.tableWidget.installEventFilter(self)
        self.editing_row = None
    def insert_staff(self, event):
        self.insert_staff = InsertStaff(self, self.username, self.current_user_role)
        self.insert_staff.show()
        self.close()
    def calculator(self, event):
        self.calculator_window = Calculator(self.username, self.current_user_role)
        self.calculator_window.show()
        self.close()
    def searching(self, event):
        self.search_window = SearchWindow(self, self.username, self.current_user_role)
        self.search_window.show()
        self.close()
    def add_employee(self):
        name = self.Name.text()
        email = self.Email.text()
        position = self.Pos.currentText()
        b_numbers = self.BNumbers.text()
        p_numbers = self.PNumbers.text()
        birth = self.Birth.text()
        gender = self.Gender.currentText()
        salary = self.salary_map.get(position)
        data = [name, birth, gender, email, p_numbers, position, salary, b_numbers]
        self.home_window.add_to_table(data, position)
        self.close()
        self.home_window.show()
    def create_ID(self, position, data):
        prefix_map = {
            "Nhà phát triển phần mềm": "D",
            "Kế toán trưởng": "A",
            "Kế toán": "A",
            "Quản lý": "M",
            "Thực tập sinh": "I",
            "Nhân viên nhân sự": "HR",
            "Chuyên viên nhân sự": "HR",
            "Chuyên viên phân tích dữ liệu": "BA",
            "Nhân viên phân tích dữ liệu": "BA",
            "Chuyên viên marketing": "MKT",
            "Nhân viên marketing": "MKT",
        }
        prefix = prefix_map.get(position, "X")
        count = 0
        for emp in data:
            if isinstance(emp, dict):
                emp_id = emp.get("Employee's ID", "")
                if emp_id.startswith("#" + prefix):
                    count += 1
        new_id = f"#{prefix}{count+1:03d}"
        return new_id
    def add_to_table(self, data, position):
        try:
            with open("DATA.json", "r", encoding="utf-8") as f:
                all_data = json.load(f)
        except:
            all_data = []
        emp_id = self.create_ID(position, all_data)
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(emp_id))
        for col, value in enumerate(data, start=1):
            self.tableWidget.setItem(row, col, QTableWidgetItem(value))
    def load_data(self, filename="DATA.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return
        self.tableWidget.setRowCount(0)
        for entry in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(entry.get("Employee's ID", "")))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(entry.get("Name", "")))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(entry.get("Date of birth", "")))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(entry.get("Gender", "")))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(entry.get("Email address", "")))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(entry.get("Phone numbers", "")))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(entry.get("Position", "")))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(entry.get("Basic salary", "")))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(entry.get("Bank account numbers", "")))
    def get_role(self):
        name = self.Name.text()
        try:
            with open("DATA.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            for entry in data:
                if entry.get("Name", "") == name:
                    position = entry.get("Position", "")
                    if position == "Quản lý":
                        return "Manager"
                    elif position in ["Chuyên viên nhân sự", "Nhân viên nhân sự"]:
                        return "HR"
                    else:
                        return "Staff"
        except:
            pass
        return "Staff"
    def edit_or_delete_employee(self, row, column):
        name = self.tableWidget.item(row, 1).text() if self.tableWidget.item(row, 1) else "Unknown"
        msg = QMessageBox(self)
        msg.setWindowTitle("Chỉnh sửa hoặc Xóa")
        msg.setText(f"Bạn muốn sửa hay xóa nhân viên '{name}'?")
        edit_btn = msg.addButton("Sửa", QMessageBox.ButtonRole.AcceptRole)
        delete_btn = msg.addButton("Xóa", QMessageBox.ButtonRole.DestructiveRole)
        cancel_btn = msg.addButton("Hủy", QMessageBox.ButtonRole.RejectRole)
        msg.exec()
        clicked = msg.clickedButton()
        if clicked == edit_btn:
            self.edit_employee(row)
        elif clicked == delete_btn:
            confirm = QMessageBox.question(
                self,
                "Xác nhận xóa",
                f"Bạn có chắc chắn muốn xóa nhân viên '{name}' không?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if confirm == QMessageBox.StandardButton.Yes:
                self.delete_employee(row)
    def delete_employee(self, row):
        self.tableWidget.removeRow(row)
        data = []
        row_count = self.tableWidget.rowCount()
        col_count = self.tableWidget.columnCount()
        for r in range(row_count):
            row_data = {}
            for c in range(col_count):
                item = self.tableWidget.item(r, c)
                header = self.tableWidget.horizontalHeaderItem(c).text()
                row_data[header] = item.text() if item else ""
            data.append(row_data)
        with open("DATA.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        QMessageBox.information(self, "Deleted", "Nhân viên đã được xóa thành công!")
    def edit_employee(self, row):
        self.tableWidget.setCurrentCell(row, 0)
        self.tableWidget.selectRow(row)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item:
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        self.editing_row = row
        # Đổi màu dòng đang chỉnh sửa (tùy chọn)
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item:
                item.setBackground(Qt.GlobalColor.yellow)

    def eventFilter(self, source, event):
        if source == self.tableWidget and event.type() == event.Type.KeyPress:
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                if self.editing_row is not None:
                    self.finish_edit()
                    return True
        return super().eventFilter(source, event)

    def finish_edit(self):
        row = self.editing_row
        if row is None:
            return
        # Ép commit giá trị đang sửa
        self.tableWidget.clearFocus()
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                item.setBackground(Qt.GlobalColor.white)
        self.save_to_json("DATA.json")
        QMessageBox.information(self, "Đã lưu", "Thông tin đã được lưu thành công.")
        self.editing_row = None
    def save_to_json(self, filename):
        data = []
        row_count = self.tableWidget.rowCount()
        col_count = self.tableWidget.columnCount()
        for row in range(row_count):
            row_data = {}
            for col in range(col_count):
                item = self.tableWidget.item(row, col)
                header = self.tableWidget.horizontalHeaderItem(col).text()
                row_data[header] = item.text() if item else ""
            data.append(row_data)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
class InsertStaff(QMainWindow):
    def __init__(self, home_window, username, current_user_role):
        super().__init__()
        uic.loadUi('mem_add.ui', self)
        self.home_window = home_window
        self.username = username
        self.current_user_role = current_user_role
        self.Name_2.setText(username)
        self.home.mousePressEvent = self.show_home
        self.calc.mousePressEvent = self.calculator
        self.search.mousePressEvent = self.searching
        self.Add.clicked.connect(self.add)
        self.Gender.setCurrentText("Nam")

    def show_message(self, title, message):
        QMessageBox.information(self, title, message, QMessageBox.StandardButton.Ok)

    def show_home(self, event):
        self.home_window.show()
        self.close()

    def calculator(self, event):
        self.calculator_window = Calculator(self.username, self.current_user_role)
        self.calculator_window.show()
        self.close()

    def searching(self, event):
        self.search_window = SearchWindow(self.home_window, self.username, self.current_user_role)
        self.search_window.show()
        self.close()

    def add(self):
        if not self.check():
            return
        name = self.Name.text()
        email = self.Email.text()
        position = self.Pos.text()
        b_numbers = self.BNumbers.text()
        p_numbers = self.PNumbers.text()
        birth = self.Birth.text()
        gender = self.Gender.currentText()

        if not all([name, email, position, b_numbers, p_numbers, birth, gender]):
            QMessageBox.warning(self, "Error", "Please fill in all fields!")
            return
        valid_positions = [
            "Kế toán", "Kế toán trưởng", "Nhà phát triển phần mềm", "Quản lý",
            "Chuyên viên nhân sự", "Nhân viên nhân sự", 
            "Chuyên viên phân tích dữ liệu", "Chuyên viên marketing", "Nhân viên marketing"
        ]

        if not (position in valid_positions or position.startswith("Thực tập sinh")):
            QMessageBox.warning(self, "Error", "Invalid position!")
            return

        if position.startswith("Thực tập sinh"):
            salary = salary_map.get("Thực tập sinh")
        else:
            salary = salary_map.get(position)

        data = [name, birth, gender, email, p_numbers, position, salary, b_numbers]
        self.home_window.add_to_table(data, position)
        self.save_to_json("DATA.json")
        self.close()
        self.home_window.show()

    def check(self):
        if self.current_user_role not in ["Administrator", "Manager", "HR"]:
            QMessageBox.warning(self, "Error", "You do not have permission to add this staff.")
            return False
        return True

    def save_to_json(self, filename):
        data = []
        row_count = self.home_window.tableWidget.rowCount()
        col_count = self.home_window.tableWidget.columnCount()
        for row in range(row_count):
            row_data = {}
            for col in range(col_count):
                item = self.home_window.tableWidget.item(row, col)
                header = self.home_window.tableWidget.horizontalHeaderItem(col).text()
                row_data[header] = item.text() if item else ""
            data.append(row_data)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
class Calculator(QMainWindow):
    def __init__(self, username, current_user_role):
        super().__init__()
        uic.loadUi('calculator.ui', self)
        self.username = username
        self.Name.setText(username)
        self.home.mousePressEvent = self.show_home
        self.insert.mousePressEvent = self.insert_staff
        self.search.mousePressEvent = self.searching
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.current_user_role = current_user_role
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                self.employees = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.employees = []
        self.comboBox.clear()
        for emp in self.employees:
            self.comboBox.addItem(f"{emp['Name']} ({emp["Employee's ID"]})")
        self.comboBox.currentIndexChanged.connect(self.selected_employee)
    def show_home(self, event):
        self.home_window = HomeWindow(self.username, self.current_user_role)
        self.home_window.show()
        self.close()
    def insert_staff(self, event):
        self.insert_staff = InsertStaff(self, self.username, self.current_user_role)
        self.insert_staff.show()
        self.close()
    def searching(self, event):
        self.search_window = SearchWindow(self, self.username, self.current_user_role)
        self.search_window.show()
        self.close()
    def selected_employee(self, index):
        if index < 0 or index >= len(self.employees):
            return
        text = self.comboBox.currentText()
        match = re.search(r"\(#(\w+)\)", text)
        if not match:
            return
        emp_id = match.group(1)
        emp_info = next((e for e in self.employees if e["Employee's ID"] == emp_id), None)
        if emp_info:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(len(emp_info))
            for col, (key, val) in enumerate(emp_info.items()):
                self.tableWidget.setHorizontalHeaderItem(col, QTableWidgetItem(key.capitalize()))
                self.tableWidget.setItem(0, col, QTableWidgetItem(str(val)))
class SearchWindow(QMainWindow):
    def __init__(self, home_window, username, current_user_role=None):
        super().__init__()
        uic.loadUi('search.ui', self)
        self.load_data()
        self.home_window = home_window
        self.username = username
        self.current_user_role = current_user_role
        self.name.setText(username)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.home.mousePressEvent = self.show_home
        self.calc.mousePressEvent = self.calculator
        self.insert.mousePressEvent = self.insert_staff
        self.Name.textChanged.connect(self.sort_employees)
        self.Pos.textChanged.connect(self.sort_employees)
        self.Gender.currentIndexChanged.connect(self.sort_employees)
    def insert_staff(self, event):
        self.insert_staff = InsertStaff(self, self.username, self.current_user_role)
        self.insert_staff.show()
        self.close()
    def show_home(self, event):
        self.home_window.show()
        self.close()
    def calculator(self, event):
        self.calculator_window = Calculator(self.username, self.current_user_role)
        self.calculator_window.show()
        self.close()
    def load_data(self):
        try:
            with open("DATA.json", "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except Exception:
            self.data = []
        self.display_all_employees()
    def display_all_employees(self):
        self.tableWidget.setRowCount(0)
        for entry in self.data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(entry.get("Employee's ID", "")))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(entry.get("Name", "")))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(entry.get("Date of birth", "")))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(entry.get("Gender", "")))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(entry.get("Email address", "")))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(entry.get("Phone numbers", "")))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(entry.get("Position", "")))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(entry.get("Basic salary", "")))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(entry.get("Bank account numbers", "")))
    def reset_search(self):
        self.Name.clear()
        self.Pos.clear()
        self.Gender.setCurrentIndex(0)
        self.display_all_employees()
    def sort_employees(self):
        name_text = self.Name.text().lower().strip()
        pos_text = self.Pos.text().lower().strip()
        gender_text = self.Gender.currentText().strip()
        filtered = []
        for emp in self.data:
            name_match = name_text in emp.get("Name", "").lower()
            pos_match = pos_text in emp.get("Position", "").lower()
            gender_match = (gender_text == "" or gender_text == "--Tất cả--" or emp.get("Gender", "") == gender_text)
            if name_match and pos_match and gender_match:
                filtered.append(emp)
        if not name_text and not pos_text and (gender_text == "" or gender_text == "--Tất cả--"):
            self.display_all_employees()
            return
        self.tableWidget.setRowCount(0)
        for entry in filtered:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(entry.get("Employee's ID", "")))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(entry.get("Name", "")))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(entry.get("Date of birth", "")))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(entry.get("Gender", "")))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(entry.get("Email address", "")))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(entry.get("Phone numbers", "")))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(entry.get("Position", "")))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(entry.get("Basic salary", "")))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(entry.get("Bank account numbers", "")))
def main():
    app = QApplication(sys.argv)
    window = SigninWindow()
    window.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
