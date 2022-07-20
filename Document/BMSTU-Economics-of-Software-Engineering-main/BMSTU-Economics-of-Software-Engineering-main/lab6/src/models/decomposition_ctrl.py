from PyQt5.QtWidgets import QDialog
import models.decomposition as dcmp


class DecompositionWindow(QDialog):
    def __init__(self, parent, dc_data, money):
        super(DecompositionWindow, self).__init__(parent)
        self.dc_data = dc_data
        self.ui = dcmp.Ui_Dialog()
        self.ui.setupUi(self)
        self.money = money
        self.show_dec_data()

    def show_dec_data(self):
        self.ui.budj_label.setText(str(self.money))
        budj_labels = [
            self.ui.budg_1_label,
            self.ui.budg_2_label,
            self.ui.budg_3_label,
            self.ui.budg_4_label,
            self.ui.budg_5_label,
            self.ui.budg_6_label,
            self.ui.budg_7_label,
            self.ui.budg_8_label
        ]
        months_labels = [
            self.ui.month_1_label,
            self.ui.month_2_label,
            self.ui.month_3_label,
            self.ui.month_4_label,
            self.ui.month_5_label,
            self.ui.month_6_label,
            self.ui.month_7_label,
            self.ui.month_8_label,
        ]

        n = len(self.dc_data.budj_perc)
        for i in range(n):
            budj_labels[i].setText(str(round(self.dc_data.budj_perc[i], 3)))
            months_labels[i].setText(str(round(self.dc_data.time[i], 3)))

        self.ui.budg_9_label.setText(str(round(self.dc_data.budj_total_perc, 3)))
        self.ui.month_9_label.setText(str(round(self.dc_data.total_time, 3)))
