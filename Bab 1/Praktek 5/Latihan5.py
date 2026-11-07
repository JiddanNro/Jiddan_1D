"""To-do list demonstrating Qt.green for completed tasks."""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
	QApplication,
	QLineEdit,
	QListWidget,
	QListWidgetItem,
	QPushButton,
	QVBoxLayout,
	QWidget,
)


class TodoApp(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("To-Do List")
		self.setGeometry(300, 300, 400, 400)

		layout = QVBoxLayout()
		self.task_input = QLineEdit()
		self.task_input.setPlaceholderText("Tugas baru...")
		self.add_btn = QPushButton("Tambah")
		self.task_list = QListWidget()
		self.complete_btn = QPushButton("Tandai Selesai")
		self.delete_btn = QPushButton("Hapus")

		layout.addWidget(self.task_input)
		layout.addWidget(self.add_btn)
		layout.addWidget(self.task_list)
		layout.addWidget(self.complete_btn)
		layout.addWidget(self.delete_btn)
		self.setLayout(layout)

		self.add_btn.clicked.connect(self.add_task)
		self.complete_btn.clicked.connect(self.complete_task)
		self.delete_btn.clicked.connect(self.delete_task)

	def add_task(self):
		task = self.task_input.text().strip()
		if task:
			self.task_list.addItem(QListWidgetItem(task))
			self.task_input.clear()

	def complete_task(self):
		"""Mark the selected task as complete using green text."""
		current_item = self.task_list.currentItem()
		if current_item:
			current_item.setForeground(Qt.green)
			current_text = current_item.text()
			if not current_text.startswith("✓ "):
				current_item.setText(f"✓ {current_text}")

	def delete_task(self):
		current_row = self.task_list.currentRow()
		if current_row >= 0:
			self.task_list.takeItem(current_row)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = TodoApp()
	window.show()
	sys.exit(app.exec_())
