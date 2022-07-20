import math

from matplotlib import pyplot

standart_eaf = {
    'RELY': 1,  # требуемая надежность 0.75-1.4
    'DATA': 1,  # Размер быза даннных 0.94-1.16
    'CPLX': 1,  # Сложность продукта 0.70-1.65
    'TIME': 1,  # Ограничение времени выполнения 1-1.65
    'STOR': 1,  # Ограничение объема основной памяти 1-1.56
    'VIRT': 1,  # Изменчивость виртуальноймашины 0.87-1.3
    'TURN': 1,  # ВРемя реакции компьютера 0.8-1.3
    'ACAP': 1,  # Способности аналитика 1.46-0.71
    'AEXP': 1,  # Знание приложений 1.29-0.82
    'PCAP': 1,  # Способности программиста 1.42-0.7
    'VEXP': 1,  # Знание виртуальной машины 1.21 - 0.9
    'LEXP': 1,  # Знание языка программирования  1.14-0.95
    'MODP': 1,  # Использование современных методов 1.24-0.8
    'TOOL': 1,  # Использование программных инструментов 1.24-0.83
    'SCED': 1,  # Требуемые сроки разработки 1.23-1.1
}

base_code_value = 25  # 000

def get_salary():
    salaries = {
        "Programmer": 50000,
        "Analytic" : 70000,
        "Manager" : 60000,
        "Tester" : 45000
    }
    return salaries

def get_standart_eaf():
    return standart_eaf.copy()


def normal_variant(eaf, size):
    work = 3.2 * eaf * (size ** 1.05)
    time = 2.5 * (work ** 0.38)
    return {
        'work': work,
        'time': time
    }


def inter_variant(eaf, size):
    work = 3.0 * eaf * (size ** 1.12)
    time = 2.5 * (work ** 0.35)
    return {
        'work': work,
        'time': time
    }


def inbuild_variant(eaf, size):
    work = 2.8 * eaf * (size ** 1.2)
    time = 2.5 * (work ** 0.32)
    return {
        'work': work,
        'time': time
    }


def calc_eaf(eaf_list):
    eaf = 1
    for i in eaf_list.keys():
        eaf *= eaf_list[i]
    return eaf


def GraphExperiment(eaf, mode,  attr_values_arr, attr_name_arr):

    code_size = 100
    model_work = []
    model_time = []
    count_attr = len(attr_name_arr)
    count_value = len(attr_values_arr[0])
    #for attr in attr_values_arr[0]:
        #eaf[attr_name] = attr
        
    for i in range(count_value):
        for j in range(count_attr):
            name = attr_name_arr[j]
            value = attr_values_arr[j][i]
            eaf[name]= value
        if mode == 'normal':
            result = cocomo(code_size=code_size,
                            eaf_list=eaf,
                            variant_func=normal_variant)
        elif mode == 'inter':
            result = cocomo(code_size=code_size,
                            eaf_list=eaf,
                            variant_func=inter_variant)
        else:
            result = cocomo(code_size=code_size,
                            eaf_list=eaf,
                            variant_func=inbuild_variant)

        model_work.append(result['work'])
        model_time.append(result['time'])
        
    return [model_work, model_time]


def graphs(): 
    
    #cplx_values = [0.7, 1, 1.3]
    sced_values = [1.23, 1.08, 1.0, 1.04, 1.1]
    modp_values = [1.24, 1.1, 1.0, 0.91, 0.82, ]
    tool_values = [1.23, 1.0, 0.9, 0.88, 0.83, ]
    modes = ['normal', 'inter', 'inbuild']

    #or sced in sced_values:
    for _ in range(1, 2):
        for mode in modes:
            figure, ax = pyplot.subplots(figsize=(15, 10))
            pyplot.subplots_adjust(hspace=0.5)
            pyplot.grid()
            
            eaf = get_standart_eaf()
            #eaf['SCED'] = sced
            modp_result = GraphExperiment(eaf, mode, [modp_values, ], ['MODP', ])
            
            eaf = get_standart_eaf()
            #eaf['SCED'] = sced
            tool_result = GraphExperiment(eaf, mode, [tool_values, ], ['TOOL', ])
            
            eaf = get_standart_eaf()
            #eaf['SCED'] = sced
            modp_sced_result = GraphExperiment(eaf, mode, [modp_values, sced_values ], ['MODP', 'SCED', ])
            
            eaf = get_standart_eaf()
            #eaf['SCED'] = sced
            tool_sced_result = GraphExperiment(eaf, mode, [tool_values, sced_values], ['TOOL', 'SCED',])
            
            pyplot.subplot(121)
            pyplot.title("Трудозатраты Режим: " + mode)# + " ( SCED=" + str(sced) + ")")
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], modp_result[0], label='MODP')
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], tool_result[0], label='TOOL')
            
            pyplot.ylabel("PM")
            pyplot.legend()

            pyplot.subplot(122)
            pyplot.title("Время Режим: " + mode)# + " ( SCED=" + str(sced) + ")")
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], modp_result[1], label='MODP')
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], tool_result[1], label='TOOL')
            
            pyplot.ylabel("TM")
            pyplot.legend()
            
            pyplot.subplot(121)
            pyplot.title("Трудозатраты Режим: " + mode)# + " ( SCED=" + str(sced) + ")")
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], modp_sced_result[0], label='MODP, SCED')
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], tool_sced_result[0], label='TOOL, SCED')
            
            pyplot.ylabel("PM")
            pyplot.legend()

            pyplot.subplot(122)
            pyplot.title("Время Режим: " + mode)# + " ( SCED=" + str(sced) + ")")
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], modp_sced_result[1], label='MODP, SCED')
            pyplot.plot(['оч. низкий', 'низкий', 'номинальный', 'высокий', 'оч. высокий'], tool_sced_result[1], label='TOOL, SCED')
            
            pyplot.ylabel("TM")
            pyplot.legend()
            
            pyplot.show()


def cocomo(code_size, eaf_list, variant_func):
    eaf = calc_eaf(eaf_list)
    return variant_func(eaf, code_size)


def simple_expirement(eaf, code_size, mode, basic_salary):
    code_size /=1000
    result = {}
    if mode == 'normal':
        result = cocomo(code_size=code_size,
                        eaf_list=eaf,
                        variant_func=normal_variant)
    elif mode == 'inter':
        result = cocomo(code_size=code_size,
                        eaf_list=eaf,
                        variant_func=inter_variant)
    else:
        result = cocomo(code_size=code_size,
                        eaf_list=eaf,
                        variant_func=inbuild_variant)

    traditional_result = result

    plan_work = result['work'] * 0.08
    plan_time = result['time'] * 0.36
    plan_workers = math.ceil(plan_work / plan_time)

    design_work = result['work'] * 0.18
    design_time = result['time'] * 0.36
    design_workers = math.ceil(design_work / design_time)

    detail_work = result['work'] * 0.25
    detail_time = result['time'] * 0.18
    detail_workers = math.ceil(detail_work / detail_time)

    coding_work = result['work'] * 0.26
    coding_time = result['time'] * 0.18
    coding_workers = math.ceil(coding_work / coding_time)

    integration_work = result['work'] * 0.31
    integration_time = result['time'] * 0.28
    integration_workers = math.ceil(integration_work / integration_time)

    all_works_traditional = [
        plan_work,
        design_work,
        detail_work,
        coding_work,
        integration_work,
    ]

    all_times_traditional = [
        plan_time,
        design_time,
        detail_time,
        coding_time,
        integration_time,
    ]

    workers = [
        plan_workers,
        design_workers,
        detail_workers,
        coding_workers,
        integration_workers,
    ]

    result['work'] += plan_work

    analyz = result['work'] * 0.04
    design = result['work'] * 0.12
    coding = result['work'] * 0.44
    planning = result['work'] * 0.06
    verification = result['work'] * 0.14
    office = result['work'] * 0.07
    quality = result['work'] * 0.07
    manuals = result['work'] * 0.06

    all_works = [
        analyz,
        design,
        coding,
        planning,
        verification,
        office,
        quality,
        manuals
    ]

    sum_work = sum(all_works)

    Xdata = []
    Ydata = []

    summa = 0
    for i in range(len(all_times_traditional)):
        time = summa
        while (time < summa + all_times_traditional[i]):
            Xdata.append(time)
            Ydata.append(workers[i])
            time += 0.01
        summa += all_times_traditional[i]

    pyplot.title('Работники')
    pyplot.grid(True)
    pyplot.plot(Xdata, Ydata)
    pyplot.xlabel("Месяцы")
    pyplot.ylabel("Количество работников")
    pyplot.show()

    budget_list = []
    salary = {
        "Programmer": basic_salary,
        "Analytic": basic_salary * 1.3,
        "Manager": basic_salary * 1.3,
        "Tester": basic_salary * 0.7,
    }

    times = all_times_traditional


    # budget += ((salary['Manager'] + salary['Analytic']) / 2) * workers_by_time * time_plan_requirements
    budget_list += [(((salary['Manager'] + salary['Analytic']) / 2) * workers[0] * times[0])]
    budget_list += [(((salary['Programmer'] + salary['Analytic']) / 2) * workers[1] * times[1])]
    budget_list += [(((salary['Programmer'] + salary['Analytic']) / 2) * workers[2] * times[2])]
    budget_list += [(((salary['Programmer'] + salary['Tester']) / 2) * workers[3] * times[3])]
    budget_list += [(((salary['Programmer'] + salary['Tester']) / 2) * workers[4] * times[4])]
    print(budget_list)
    sum_budget = 0
    for i in range(len(budget_list)):
        sum_budget += budget_list[i]

    return {
        'work': traditional_result['work'],
        'time': traditional_result['time'],
        'works_t': all_works_traditional,
        'times_t': all_times_traditional,
        'workers': workers,
        'works': all_works,
        'budget': sum_budget,
    }