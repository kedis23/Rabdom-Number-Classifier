from random import randint


class RandomNumberClassifier:
    def __init__(self, nums=None):
        if nums is None:
            nums = [[], [], [], [], []]
        self.cat1 = nums[0]
        self.cat2 = nums[1]
        self.cat3 = nums[2]
        self.cat4 = nums[3]
        self.cat5 = nums[4]

    def print(self):
        print(f"cat1: 1-20 = {self.cat1}\nTotal numbers: {len(self.cat1)} \n"
              f"cat2: 21-40 = {self.cat2}\nTotal numbers: {len(self.cat2)} \n"
              f"cat3: 41-60 = {self.cat3}\nTotal numbers: {len(self.cat3)} \n"
              f"cat4: 61-80 = {self.cat4}\nTotal numbers: {len(self.cat4)} \n"
              f"cat5: 81-100 = {self.cat5}\nTotal numbers: {len(self.cat5)} \n")

    def rand_gen(self) -> list:
        num = self.get_amount()
        nums = [[], [], [], [], []]
        for i in range(num):
            value = randint(1, 100)
            if value <= 20:
                nums[0].append(value)
            if value >= 21 and value <= 40:
                nums[1].append(value)
            if value >= 41 and value <= 60:
                nums[2].append(value)
            if value >= 61 and value <= 80:
                nums[3].append(value)
            if value >= 81 and value <= 100:
                nums[4].append(value)
        return nums


    def get_amount(self) -> int:
        while True:
            amount = input("Enter amount: ")
            try:
                val = int(amount)
                if val < 101:
                    break
                else:
                    print("Amount can't be over 100, try again")
            except ValueError:
                print("Amount must be a number, try again")
        return val





if __name__ == '__main__':
    nums = RandomNumberClassifier().rand_gen()
    p = RandomNumberClassifier(nums)
    p.print()
