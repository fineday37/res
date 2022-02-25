import re


def check_ip(one_str):
    list = re.compile('^(([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$')
    if list.match(one_str):
        return True
    else:
        return False


if __name__ == '__main__':
    ip_list = ['', '172.31.137.251', '100.10.0.1000', '127.0.0.1', '22.12.33', '0.0.0.1']
    for one_str in ip_list:
        if check_ip(one_str):
            print('{} 是一个正常的ip'.format(one_str))
        else:
            print('{} 不是一个正常的ip'.format(one_str))

test = re.compile('^(([1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.)$')
tests = test.match('2.').group()
print(tests)

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "a": 4, "c": 3}

for i, j in zip(sorted(dict1.keys()), sorted(dict2.keys())):
    if str(dict1[i]) != str(dict2[j]):
        print(i, dict1[i], j, dict2[j])
