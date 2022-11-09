def task4(array, file):
    array_len = len(array)
    file.write("\nList diagram\n")
    file.write("-" * 20)
    sorted_array = sorted(array)

    prev_n = int(sorted_array[0]/10)

    print(sorted_array)
    file.write(f"\n{prev_n}\t|")
    for i in range(array_len):
        if int(prev_n) == int(sorted_array[i] / 10):
            file.write(f"{sorted_array[i] % 10} ")
        else:
            prev_n = int(sorted_array[i] / 10)
            file.write(f"\n{prev_n}\t|")
            file.write(f"{sorted_array[i] % 10} ")




    file.write("\n")
    file.write("-" * 20)