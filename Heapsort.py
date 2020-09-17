class Heapsort():

    def __init__(self, arr=[]):
        self.arr = arr
        self.length = len(arr)
        self.heap_size = len(arr)

    def left(self, int): return 2*int + 1
    def right(self, int): return 2*int + 2

    def max_heapify(self, int):
        l = self.left(int)
        r = self.right(int)
        if l < self.heap_size and self.arr[l] > self.arr[int]:
            largest = l
        else:
            largest = int
        if r < self.heap_size and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != int:
            temp = self.arr[int]
            self.arr[int] = self.arr[largest]
            self.arr[largest] = temp
            return self.max_heapify(largest)

    def build_max_heap(self):
        for i in range((self.length-1)//2, -1, -1):
            self.max_heapify(i)

    def sort(self):
        self.build_max_heap()
        print(self.arr)
        for i in range(self.length-1, 0, -1):
            temp = self.arr[0]
            self.arr[0] = self.arr[i]
            self.arr[i] = temp
            self.heap_size = self.heap_size - 1
            self.max_heapify(0)
