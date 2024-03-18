# Pewarna
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

class Node_Scooter:
    def __init__(self, id_scooter, nama_scooter):
        self.id_scooter = id_scooter
        self.nama_scooter = nama_scooter
        self.next = None

    def __str__(self):
        return f"ID: {self.id_scooter}, Nama Part Scooter: {self.nama_scooter}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.histori_data = []

    def ambil_data(self, ambil, data):
        self.histori_data.append((ambil, data))

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    def fibonaci(self):
        current = self.head
        count = 0
        while current:
            current.id_scooter = self.fibonacci(count)
            count += 1
            current = current.next

    def quicksort(self, head):
        if head is None or head.next is None:
            return head

        pivot = head.id_scooter
        left_head = left_tail = Node_Scooter(0, 0)
        equal_head = equal_tail = Node_Scooter(0, 0)
        right_head = right_tail = Node_Scooter(0, 0)

        current = head
        while current is not None:
            if current.id_scooter <  pivot:
                left_tail.next = current
                left_tail = current
            elif current.id_scooter == pivot:
                equal_tail.next = current
                equal_tail = current
            else:
                right_tail.next = current
                right_tail = current
            current = current.next

        left_tail.next = None
        equal_tail.next = None
        right_tail.next = None

        left_head = self.quicksort(left_head.next)
        right_head = self.quicksort(right_head.next)

        if left_head:
            head = left_head
            left_tail.next = equal_head.next
        else:
            head = equal_head.next

        equal_tail.next = right_head

        return head

    def insert_at_end(self, head, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        if head is None:
            return new_node

        current = head
        while current.next is not None:
            current = current.next

        current.next = new_node
        return head

    def menambah_di_awalan(self, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        new_node.next = self.head
        self.head = new_node
        self.ambil_data("menambah_di_awalan", (id_scooter, nama_scooter))

    def menambah_di_akhiran(self, id_scooter, nama_scooter):
        new_node = Node_Scooter(id_scooter, nama_scooter)
        if not self.head:
            self.head = new_node
            self.ambil_data("menambah_di_akhiran", (id_scooter, nama_scooter))
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.ambil_data("menambah_di_akhiran", (id_scooter, nama_scooter))

    def menambah_di_antara_node(self, id_scooter, nama_scooter, posisi):
        if posisi < 0:
            print("posisi pemilihan diantara node kada valid.")
            return
        if posisi == 0:
            self.menambah_di_awalan(id_scooter, nama_scooter)
            return
        new_node = Node_Scooter(id_scooter, nama_scooter)
        current = self.head
        for i in range(posisi - 1):
            if current:
                current = current.next
            else:
                print("posisi pemilihan diantara node kada valid.")
                return
        if not current:
            print("posisi pemilihan diantara node kada valid.")
            return
        new_node.next = current.next
        current.next = new_node
        self.ambil_data("menambah_di_antara_node", (id_scooter, nama_scooter, posisi))

    def menghapus_node(self, id_scooter):
        current = self.head
        if current and current.id_scooter == id_scooter:
            self.head = current.next
            self.ambil_data("menghapus_node", id_scooter)
            return
        while current.next and current.next.id_scooter == id_scooter:
            current.next = current.next.next
            self.ambil_data("menghapus_node", id_scooter)
            return
        print(f"Node dengan id scooter {id_scooter} kdd.")

    def tampilkan_output(self):
        current = self.head
        while current:
            print(BOLD + CYAN +"")
            print(current, end=" -> ")
            current = current.next
        print("None")

    def tampilkan_histori_data(self):
        print(BOLD + YELLOW + "Record Data:" + RESET)
        for ambil, data in self.histori_data:
            print(BOLD + CYAN + "")
            print(f"{ambil}: {data}")

linked_list = LinkedList()
print(BOLD + BLUE +"""
     ======================
     = Nolimitz Maticshop =
     ======================
      """)
try:
    # Untuk menambahkan node di awal, di akhir, dan sesuai posisi yang diinginkan diantara node tersebut
    print(BOLD + GREEN + "====================================================================================================" + RESET)
    print(BOLD + YELLOW + "Node yang sudah tertambah: " + RESET)
    print(BOLD + GREEN + "====================================================================================================" + RESET)
    linked_list.menambah_di_awalan(1, "Pulley")
    linked_list.menambah_di_awalan(4, "ECU")
    linked_list.menambah_di_awalan(6, "Kampas ganda")
    linked_list.menambah_di_awalan(16, "Noken T2")
    linked_list.menambah_di_awalan(18, "Throttle  Position Sensor")
    linked_list.menambah_di_awalan(26, "Filter Udara")
    linked_list.menambah_di_akhiran(9, "Roller")
    linked_list.menambah_di_akhiran(2, "Injector")
    linked_list.menambah_di_akhiran(3, "Busi")
    linked_list.menambah_di_akhiran(12, "Per cvt")
    linked_list.menambah_di_akhiran(30, "Throttle Body")
    linked_list.menambah_di_akhiran(21, "Oli Motul")
    linked_list.menambah_di_akhiran(19, "Knalpot Zrc")
    linked_list.tampilkan_output()
    print(BOLD + GREEN + "====================================================================================================" + RESET)

    # untuk menambah di antara node(4, "mberr", 0)  # sesuai posisi 0 1 2 3 4 seterusnya
    print(BOLD + YELLOW + "Node yang sudah tertambah diantaranya: " + RESET)
    print(BOLD + GREEN + "====================================================================================================" + RESET)
    linked_list.menambah_di_antara_node(23, "Velg Bintang", 0)
    linked_list.tampilkan_output()
    print(BOLD + GREEN + "====================================================================================================" + RESET)

    # Untuk menghapus node
    print(BOLD + YELLOW + "Node yang sudah terhapus: " + RESET)
    print(BOLD + GREEN + "====================================================================================================" + RESET)
    linked_list.menghapus_node(26)  # Contoh penghapusan berdasarkan id
    linked_list.tampilkan_output()
    print(BOLD + GREEN + "====================================================================================================" + RESET)

    # buat sorting
    print(BOLD + YELLOW + "Node yang sudah tersorting: " + RESET)
    print(BOLD + GREEN + "====================================================================================================" + RESET)
    linked_list.head = linked_list.quicksort(linked_list.head)
    linked_list.tampilkan_output()
    print(BOLD + GREEN + "====================================================================================================" + RESET)

    # buat searching pake fibonacci
    print(BOLD + YELLOW + "id node yang sudah terderet oleh fibonacci:" + RESET)
    print(BOLD + GREEN + "====================================================================================================" + RESET)
    linked_list.fibonaci()
    linked_list.head = linked_list.quicksort(linked_list.head)
    linked_list.tampilkan_output()
    print(BOLD + GREEN + "====================================================================================================" + RESET)

    # Disp histori_data
    linked_list.tampilkan_histori_data()
    print(BOLD + GREEN + "====================================================================================================" + RESET)
except TypeError:
    print("MBERR")
