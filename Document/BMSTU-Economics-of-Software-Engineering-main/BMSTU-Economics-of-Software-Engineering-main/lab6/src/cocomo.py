class ProgrammingLanguage:
    def __init__(self, name: str, basic_assembler: float):
        self.name = name
        self.basic_assembler = basic_assembler

    def __repr__(self):
        return f"{self.name}_{self.basic_assembler}"


class Driver:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}-{self.value}"


class RELY:
    descr = "Требуемая надежность"
    drivers = (Driver("Очень низкий", 0.75),
               Driver("Низкий", 0.86),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 1.15),
               Driver("Очень высокий", 1.4))


class DATA:
    descr = "Размер базы данных"
    drivers = (Driver("Низкий", 0.94),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 1.08),
               Driver("Очень высокий", 1.16))


class CPLX:
    descr = "Сложность продукта"
    drivers = (Driver("Очень низкий", 0.7),
               Driver("Низкий", 0.85),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 1.15),
               Driver("Очень высокий", 1.3))


class TIME:
    descr = "Ограничение времени выполнения"
    drivers = (Driver("Номинальный", 1.0),
               Driver("Высокий", 1.1),
               Driver("Очень высокий", 1.50))


class STOR:
    descr = "Ограничение объема основной памяти"
    drivers = (Driver("Номинальный", 1.0),
               Driver("Высокий", 1.06),
               Driver("Очень высокий", 1.21))


class VIRT:
    descr = "Изменчивость виртуальной машины"
    drivers = (Driver("Низкий", 0.87),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 1.15),
               Driver("Очень высокий", 1.30))


class TURN:
    descr = "Время реакции компьютера"
    drivers = (Driver("Низкий", 0.87),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 1.07),
               Driver("Очень высокий", 1.15))


class ACAP:
    descr = "Способности аналитика"
    drivers = (Driver("Очень низкий", 1.46),
               Driver("Низкий", 1.19),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 0.86),
               Driver("Очень высокий", 0.71))


class AEXP:
    descr = "Знание приложений"
    drivers = (Driver("Очень низкий", 1.29),
               Driver("Низкий", 1.15),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 0.91),
               Driver("Очень высокий", 0.82))


class PCAP:
    descr = "Способности программиста"
    drivers = (Driver("Очень низкий", 1.42),
               Driver("Низкий", 1.17),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 0.86),
               Driver("Очень высокий", 0.7))


class VEXP:
    descr = "Знание виртуальной машины"
    drivers = (Driver("Очень низкий", 1.21),
               Driver("Низкий", 1.1),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 0.9))


class LEXP:
    descr = "Знание языка программирования"
    drivers = (Driver("Очень низкий", 1.14),
               Driver("Низкий", 1.07),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 0.95))


class MODP:
    descr = "Использование современных методов"
    drivers = (Driver("Очень низкий", 1.24),
               Driver("Низкий", 1.1),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 0.91),
               Driver("Очень высокий", 0.82))


class TOOL:
    descr = "Использование программных инструментов"
    drivers = (Driver("Очень низкий", 1.24),
               Driver("Низкий", 1.1),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 0.91),
               Driver("Очень высокий", 0.82))


class SCED:
    descr = "Требуемые сроки разработки"
    drivers = (Driver("Очень низкий", 1.23),
               Driver("Низкий", 1.08),
               Driver("Номинальный", 1.0),
               Driver("Высокий", 1.04),
               Driver("Очень высокий", 1.1))


class CocomoMode:
    name = None

    def get_labor_costs(self, eaf: float, kloc: float) -> float:
        pass

    def get_time(self, labor_costs: float) -> float:
        pass

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def get_mode(kloc: float):
        if kloc < 50:
            return CocomoNormalMode
        elif 50 <= kloc < 500:
            return CocomoIntermediateMode
        else:
            return CocomoBuiltinMode


class CocomoNormalMode(CocomoMode):
    name = "Обычный"

    def get_labor_costs(self, eaf: float, kloc: float) -> float:
        lc = 3.2 * eaf * pow(kloc, 1.05)
        return lc

    def get_time(self, labor_costs: float) -> float:
        time = 2.5 * pow(labor_costs, 0.38)
        return time

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class CocomoIntermediateMode(CocomoMode):
    name = "Промежуточный"

    def get_labor_costs(self, eaf: float, kloc: float) -> float:
        lc = 3.0 * eaf * pow(kloc, 1.12)
        return lc

    def get_time(self, labor_costs: float) -> float:
        time = 2.5 * pow(labor_costs, 0.35)
        return time

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class CocomoBuiltinMode(CocomoMode):
    name = "Встроенный"

    def get_labor_costs(self, eaf: float, kloc: float) -> float:
        lc = 2.8 * eaf * pow(kloc, 1.2)
        return lc

    def get_time(self, labor_costs: float) -> float:
        time = 2.5 * pow(labor_costs, 0.32)
        return time

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Decomposition:
    budj_perc = [4, 12, 44, 6, 14, 7, 7, 6]
    budj_total_perc = sum(budj_perc)

    def __init__(self, time: float):
        self.total_time = time
        self.time = []
        for bt in self.budj_perc:
            val = (time / self.budj_total_perc) * bt
            self.time.append(val)


class Lifecycle:
    work_perc = [8, 18, 25, 26, 31]
    work_total_perc = sum(work_perc)
    time_perc = [36, 36, 18, 18, 28]
    time_total_percent = sum(time_perc)

    def __init__(self, work, time):
        self.total_work = work
        self.total_time = time
        self.work = []
        for wp in self.work_perc:
            val = round((work / self.work_total_perc) * wp)
            self.work.append(val)
        if sum(self.work) != self.total_work:
            self.work[len(self.work) - 1] += round(self.total_work - sum(self.work))
        self.time = []
        for tp in self.time_perc:
            val = round((time / self.time_total_percent) * tp)
            self.time.append(val)
        if sum(self.time) != self.total_time:
            self.time[len(self.time) - 1] += round(self.total_time - sum(self.time))


class Cocomo:
    Modes = (CocomoNormalMode(),
             CocomoIntermediateMode(),
             CocomoBuiltinMode())
    PL = (ProgrammingLanguage("Ассемблер", 1),
          ProgrammingLanguage("С", 2.5),
          ProgrammingLanguage("Кобол", 3),
          ProgrammingLanguage("Фортран", 3),
          ProgrammingLanguage("Паскаль", 3.5),
          ProgrammingLanguage("С++", 6),
          ProgrammingLanguage("Java", 6),
          ProgrammingLanguage("Ada 95", 6.5),
          ProgrammingLanguage("Access", 8.5),
          ProgrammingLanguage("Delphi Pascal", 11),
          ProgrammingLanguage("CORBA", 16))

    Factors = (RELY, DATA, CPLX,
               TIME, STOR, VIRT, TURN,
               ACAP, AEXP, PCAP, VEXP, LEXP,
               MODP, TOOL, SCED)

    @staticmethod
    def run(factors_idxs: [], kloc: float, lang_idx: int, mode_idx: int, month_cost: int):
        assert len(Cocomo.Factors) == len(factors_idxs)
        kloc = kloc * Cocomo.PL[lang_idx].basic_assembler
        eaf = Cocomo.__eaf(factors_idxs)
        mode = Cocomo.Modes[mode_idx]
        labor_costs = round(mode.get_labor_costs(eaf, kloc))
        time = round(mode.get_time(labor_costs))
        money = time * month_cost
        print("labor costs = {0}".format(labor_costs))
        print("time = {0}".format(time))
        lc = Lifecycle(labor_costs, time)
        dc = Decomposition(time)
        return lc, dc, labor_costs, time, money


    @staticmethod
    def __eaf(factors_idxs: []) -> float:
        eaf = 1.0
        n = len(Cocomo.Factors)
        for i in range(n):
            eaf *= Cocomo.Factors[i].drivers[factors_idxs[i]].value
        return eaf
