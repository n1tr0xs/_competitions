# SOLVED
# fail test 17
def flush_print(*args, **kwargs):
    print(*args, **kwargs, flush=True)


start = 1
end = int(input())
while True:
    if start == end:
        flush_print(f'! {start}')
        exit()
    count = end - start + 1
    k = count // 2
    flush_print('?', k, k)
    flush_print(*range(start, start + k))
    flush_print(*range(start + k + count % 2, end + 1))
    answer = input()
    if answer == '=':
        flush_print('!', k + 1)
        break
    if answer == '<':
        start = start + k + count % 2
    if answer == '>':
        end = start + k - 1
