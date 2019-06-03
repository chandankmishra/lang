class ExamRoom:
    def __init__(self, N):
        """
        :type N: int
        """
        self.cur_idx = 0
        self.next_idx = -1
        self.seats = [False] * N
        self.max_dis = [-1] * N
        self.N = N
        self.count = 0

    def seat(self):
        """
        :rtype: int
        """

        if self.count == 0 or self.next_idx == -1:
            self.next_idx = self.N - 1
            self.seats[self.cur_idx] = True
            for i in range(self.N):
                self.max_dis[i] = i
            # print(self.cur_idx, self.next_idx, self.seats, self.max_dis)
            self.count += 1
            return self.cur_idx

        self.seats[self.next_idx] = True

        fill_idx = -1
        for i in range(self.N - 1, -1, -1):
            if self.seats[i] is True:
                fill_idx = i
            if fill_idx != -1:
                self.max_dis[i] = fill_idx - i

        fill_idx = -1
        nidx = 0
        max_distance = 0
        for i in range(self.N):
            if self.seats[i] is True:
                fill_idx = i
            if fill_idx != -1:
                self.max_dis[i] = min(self.max_dis[i], i - fill_idx)
            if self.max_dis[i] > max_distance:
                max_distance = self.max_dis[i]
                nidx = i

        self.cur_idx = self.next_idx
        self.next_idx = nidx
        # print(self.cur_idx, self.next_idx, self.seats, self.max_dis)
        self.count += 1
        return self.cur_idx

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        self.count -= 1
        self.seats[p] = False
        fill_idx = -1
        for i in range(self.N - 1, -1, -1):
            if self.seats[i] is True:
                fill_idx = i
            if fill_idx != -1:
                self.max_dis[i] = fill_idx - i

        fill_idx = -1
        nidx = 0
        max_distance = 0
        for i in range(self.N):
            if self.seats[i] is True:
                fill_idx = i
            if fill_idx != -1:
                self.max_dis[i] = min(self.max_dis[i], i - fill_idx)
            if self.max_dis[i] > max_distance:
                max_distance = self.max_dis[i]
                nidx = i

        self.next_idx = nidx
        self.cur_idx = self.next_idx
        # print(self.cur_idx, self.next_idx, self.seats, self.max_dis)


t = ExamRoom(10)
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
t.leave(0)
t.leave(4)
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
print(t.seat(), end=' ')
t.leave(0)
t.leave(4)
print(t.seat(), end=' ')
print(t.seat(), end=' ')
t.leave(7)
print(t.seat(), end=' ')
t.leave(3)
print(t.seat(), end=' ')
t.leave(3)
print(t.seat(), end=' ')
t.leave(9)
print(t.seat(), end=' ')
t.leave(0)
print(t.seat(), end=' ')
