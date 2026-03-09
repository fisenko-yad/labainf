disk_size_mb = 1.44
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

disk_size_kb = disk_size_mb * 1024
disk_size_bytes = disk_size_kb * 1024

chars_per_book = pages * lines_per_page * chars_per_line
book_size_bytes = chars_per_book * bytes_per_char

books_count = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_count)
