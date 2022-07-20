from PyQt5.QtWidgets import QDialog
import models.life_cycle as lc


class LifeCycleWindow(QDialog):
    def __init__(self, parent, lc_data, money):
        super(LifeCycleWindow, self).__init__(parent)
        self.lc_data = lc_data
        self.ui = lc.Ui_Dialog()
        self.ui.setupUi(self)
        self.money = money
        self.show_lc_data()

    def show_lc_data(self):
        self.ui.budj_label.setText(str(self.money))

        labor_labels = [
            self.ui.labor_1_label,
            self.ui.labor_2_label,
            self.ui.labor_3_label,
            self.ui.labor_4_label,
            self.ui.labor_5_label,
        ]
        time_labels = [
            self.ui.time_1_label,
            self.ui.time_2_label,
            self.ui.time_3_label,
            self.ui.time_4_label,
            self.ui.time_5_label,
        ]
        n = len(self.lc_data.work)

        for i in range(n):
            text = f"{self.lc_data.work_perc[i]}/{round(self.lc_data.work[i], 3)}"
            labor_labels[i].setText(text)
            text = f"{self.lc_data.time_perc[i]}/{round(self.lc_data.time[i], 3)}"
            time_labels[i].setText(text)

        text = f"{round(self.lc_data.work_total_perc, 3)}/{round(self.lc_data.total_work, 3)}"
        self.ui.labor_6_label.setText(text)

        text = f"{round(self.lc_data.time_total_percent, 3)}/{round(self.lc_data.total_time, 3)}"
        self.ui.time_6_label.setText(text)
