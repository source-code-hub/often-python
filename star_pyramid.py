import faker


def print_pyramid(depth):
    for i in range(1, depth+1):
        print(' ' * (depth-i), '*' * (2*i-1))


def print_pyramid_r(depth):
    for i in range(depth, 0, -1):
        print(' ' * (depth-i), '*' * (2*i-1))


def print_table(data, header=None):
    max_len = []
    for c in range(len(data[0])):
        m_len = 0
        for r in range(len(data)):
            m_len = max(m_len, len(str(data[r][c])))
        max_len.append(m_len)

    print("+" + "+".join(["-" * cl for cl in max_len]) + "+")
    for r in range(len(data)):
        print("|"+"|".join([str(c).ljust(max_len[i]) for i, c in enumerate(data[r])])+'|')
        print("+" + "+".join(["-"*cl for cl in max_len])+"+")


if __name__ == '__main__':
    print_pyramid(5)
    print_pyramid_r(5)
    f = faker.Faker()
    profiles = []
    for _ in range(20):
        profiles.append([v for k, v in f.profile().items()][:3])
    print_table(profiles)