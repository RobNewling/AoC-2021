def main():
    print('Loading Depth Measurements from Input file')
    depth_measurements = load_input_file('Input\input.txt')
    print(f'Loaded {len(depth_measurements)} measurements')

    print('Counting increases')
    total_count, total_decrease, num = count_increases(depth_measurements)

    print(f'Total increase count: {total_count}')
    print(f'Total decrease count: {total_decrease}')
    print(num)
    print(total_count+total_decrease)


def load_input_file(file):
    with open(file) as f:
        original = f.readlines()
        cleaned = [s.strip() for s in original]
        return list(map(int, cleaned))


def count_increases(depth_measurements):
    prev_measurement = None
    increase_count = 0
    decrease_count = 0
    num = 0
    for measurement in depth_measurements:
        num += 1
        print_out = [measurement]
        if prev_measurement is None:
            prev_measurement = measurement
            continue

        if measurement > prev_measurement:
            print_out.append('(increased)')
            increase_count += 1
        elif measurement == prev_measurement:
            print_out.append('(no change)')
        else:
            decrease_count += 1
            print_out.append('(decreased)')
            print(f'{prev_measurement},{measurement}')

        prev_measurement = measurement
        print(' '.join(str(s) for s in print_out))

    return increase_count, decrease_count, num


if __name__ == "__main__":
    main()
