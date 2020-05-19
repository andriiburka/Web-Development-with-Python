class Stack(list):
    def stack_reverse(self):
        return self[::-1]


def start(query):
    nums = []
    for _ in range(query):
        cmd = input()
        if cmd.startswith('1'):
            nums.append(cmd.split()[1])
        if nums:
            if cmd.startswith('2'):
                nums.pop()
            elif cmd.startswith('3'):
                print(max(nums))
            elif cmd.startswith('4'):
                print(min(nums))
    print(", ".join(list(map(str, Stack(nums).stack_reverse()))))


if __name__ == '__main__':
    start(query=int(input()))
