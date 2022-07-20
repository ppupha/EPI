from models.life_cycle_ctrl import LifeCycleWindow
from models.decomposition_ctrl import DecompositionWindow
from PyQt5.QtWidgets import QMainWindow
import models.mainwindow as mwd
from cocomo import *
import matplotlib.pyplot as plt
import multiprocessing as mp


class CocomoMainwindow(QMainWindow):
    def __init__(self):
        super(CocomoMainwindow, self).__init__()
        self.ui = mwd.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_combo_boxes()
        self.on_kloc_changed()
        self.ui.run_btn.clicked.connect(self.run)
        self.ui.kloc_spinBox.valueChanged.connect(self.on_kloc_changed)

    def run(self):
        kloc = self.ui.kloc_spinBox.value()
        factors_idxs = self.__get_factors_idxs()
        lang_idx = self.ui.lang_comboBox.currentIndex()
        mode_idx = self.ui.model_comboBox.currentIndex()
        month_cost = self.ui.month_cost_spinBox.value()
        lc, dc, labor, time, money = Cocomo.run(factors_idxs, kloc, lang_idx, mode_idx, month_cost)
        lcw = LifeCycleWindow(self, lc, money)
        lcw.show()
        dcmp = DecompositionWindow(self, dc, money)
        dcmp.show()
        plot_proc = mp.Process(target=draw_graph, args=(lc,))
        plot_proc.start()

    def __get_factors_idxs(self) -> []:
        idxs = [
            self.ui.rely_comboBox.currentIndex(),
            self.ui.data_comboBox.currentIndex(),
            self.ui.cplx_comboBox.currentIndex(),
            self.ui.time_comboBox.currentIndex(),
            self.ui.stop_comboBox.currentIndex(),
            self.ui.virt_comboBox.currentIndex(),
            self.ui.turn_comboBox.currentIndex(),
            self.ui.acap_comboBox.currentIndex(),
            self.ui.aexp_comboBox.currentIndex(),
            self.ui.pcap_comboBox.currentIndex(),
            self.ui.vexp_comboBox.currentIndex(),
            self.ui.lexp_comboBox.currentIndex(),
            self.ui.modp_comboBox.currentIndex(),
            self.ui.tool_comboBox.currentIndex(),
            self.ui.sced_comboBox.currentIndex()
        ]
        return idxs

    def on_kloc_changed(self):
        kloc = self.ui.kloc_spinBox.value()
        mode = CocomoMode.get_mode(kloc)
        self.ui.model_comboBox.setCurrentText(mode.name)

    def setup_combo_boxes(self):
        for mode in Cocomo.Modes:
            self.ui.model_comboBox.addItem(mode.name)
        for lang in Cocomo.PL:
            self.ui.lang_comboBox.addItem(lang.name)

        for rely in RELY.drivers:
            self.ui.rely_comboBox.addItem(rely.name)

        for data in DATA.drivers:
            self.ui.data_comboBox.addItem(data.name)

        for cplx in CPLX.drivers:
            self.ui.cplx_comboBox.addItem(cplx.name)

        for time in TIME.drivers:
            self.ui.time_comboBox.addItem(time.name)

        for stor in STOR.drivers:
            self.ui.stop_comboBox.addItem(stor.name)

        for virt in VIRT.drivers:
            self.ui.virt_comboBox.addItem(virt.name)

        for turn in TURN.drivers:
            self.ui.turn_comboBox.addItem(turn.name)

        for acap in ACAP.drivers:
            self.ui.acap_comboBox.addItem(acap.name)

        for aexp in AEXP.drivers:
            self.ui.aexp_comboBox.addItem(aexp.name)

        for pcap in PCAP.drivers:
            self.ui.pcap_comboBox.addItem(pcap.name)

        for vexp in VEXP.drivers:
            self.ui.vexp_comboBox.addItem(vexp.name)

        for lexp in LEXP.drivers:
            self.ui.lexp_comboBox.addItem(lexp.name)

        for modp in MODP.drivers:
            self.ui.modp_comboBox.addItem(modp.name)

        for tool in TOOL.drivers:
            self.ui.tool_comboBox.addItem(tool.name)

        for sced in SCED.drivers:
            self.ui.sced_comboBox.addItem(sced.name)


def draw_graph(lc):
    month_life_cycle = [round(i) for i in lc.time]
    workers = []
    n = len(month_life_cycle)
    for i in range(n):
        cur_workers = []
        for j in range(month_life_cycle[i]):
            val = round(round(lc.work[i]) / month_life_cycle[i])
            cur_workers.append(val)
        if sum(cur_workers) != round(lc.work[i]):
            cur_workers = fix_cur_work(lc.work[i], cur_workers)
            # cur_workers[len(cur_workers) - 1] += round(lc.work[i] - sum(cur_workers))
        workers += cur_workers
    if sum(workers) != round(lc.total_work):
        workers[len(workers) - 1] += round(lc.total_work) - sum(workers)

    plt.rcParams.update({'font.size': 7})
    months = [i for i in range(1, lc.total_time + 1)]
    plt.bar(months, workers)
    plt.xlabel("Время, месяцы")
    plt.ylabel("Количество работников")
    #ax.set_facecolor('seashell')
    #fig.set_facecolor('floralwhite')
    plt.xticks(months, months)
    plt.tight_layout()
    plt.grid(True)
    for x, y in zip(months, workers):
        plt.text(x, y, '%d' % y, ha='center', va='bottom', )
    plt.show()


def fix_cur_work(total_work, workers):
    diff = round(total_work) - sum(workers)
    step = 1
    if diff < 0:
        step = -1
    i = len(workers) - 1
    while diff != 0:
        print(f"i = {i}, diff = {step}")
        workers[i] = workers[i] + step
        diff += -step
        i -= 1
        if i < 0:
            i = 0
    return workers
