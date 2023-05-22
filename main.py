from component import *
from arrange_component import *
from tabulate import tabulate

    
import matplotlib.pyplot as plt

def test_wo_memo(t = 10): 
    result = 0
    for _ in range (10):
        Resistor.calculate_count = 0
        resistors = [Resistor(randint(1,100)) for _ in range (t)]
        target = randint(1,100)
        arrange_circuit(resistors, target)
        result += Resistor.calculate_count
    return result/10

def test_memo(t = 10): 
    result = 0
    for _ in range (10):
        Resistor.calculate_count = 0
        resistors = [Resistor(randint(1,100)) for _ in range (t)]
        target = randint(1,100)
        arrange_circuit_with_memo(resistors, target)
        result += Resistor.calculate_count
    return result/10


def benchmark(n=8):
    x = []
    y_wo_memo = []
    y_memo = []
    for i in range(1, n):
        x.append(i)
        y_wo_memo.append(test_wo_memo(i))
        y_memo.append(test_memo(i))
    
    # Membuat tabel x, y_wo_memo, dan y_memo
    table = [["Ukuran masukan (n)", "Comp w/o memo", "Comp w/memo"]]
    for i in range(len(x)):
        table.append([x[i], y_wo_memo[i], y_memo[i]])
    
    # Menampilkan tabel
    print(tabulate(table, headers="firstrow"))
    
    # Menampilkan grafik
    plt.plot(x, y_memo, label="Dengan memoisasi")
    plt.plot(x, y_wo_memo, label="Tanpa memoisasi")
    
    # Menambahkan judul dan label sumbu
    plt.title("Perbandingan Banyak Operasi dengan dan tanpa Memoisasi")
    plt.xlabel("Ukuran masukan (n)")
    plt.ylabel("Banyak perbandingan")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    benchmark(8)
    # import time
    
    # r1 = Resistor(10)
    # r2 = Resistor(20)
    # r3 = Resistor(30)
    # r4 = Resistor(40)
    # r5 = Resistor(50)
    # r6 = Resistor(60)
    # r7 = Resistor(70)
     
    # list_resistor = [r1, r2, r3, r4, r5, r6, r7]
    # target = 77
    
    # start_time = time.time()
    # result = arrange_circuit_with_memo(list_resistor, target)
    # end_time = time.time()
    # print("Solution: " + str(result))
    # print("Execution time: " + str(end_time - start_time) + "ms")
    




