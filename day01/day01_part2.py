def main():
    print('Loading Depth Measurements from Input file')
    depth_measurements = load_input_file('input.txt')
    print(f'Loaded {len(depth_measurements)} measurements')

    print('Counting increases')
    total_count = count_three_measurement_window(depth_measurements)

    print(f'Total increase count: {total_count}')


def load_input_file(file):
    with open(file) as f:
        original = f.readlines()
        cleaned = [s.strip() for s in original]
        return list(map(int, cleaned))



def count_three_measurement_window(depth_measurements):
    increase_count = 0
    prev_window = None
    for i in range(0, len(depth_measurements)-2):
        print(f'{depth_measurements[i:i + 3]}')
        window = sum(depth_measurements[i:i + 3])
        if prev_window is None:
            prev_window = window
            continue

        if window > prev_window:
            increase_count += 1
        prev_window = window

    return increase_count


if __name__ == "__main__":
    main()
