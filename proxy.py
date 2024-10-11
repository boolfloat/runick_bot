def get_next_proxy_soski():
    proxy_file = 'socks5.txt'
    used_proxies_file = 'used_socks5.txt'
    with open(proxy_file, 'r') as file:
        
        proxies = file.readlines()

    if not proxies:
        print("Нет доступных прокси.")
        return None

    with open(used_proxies_file, 'a') as used_file:
        used_file.write(proxies[0])

    with open(proxy_file, 'w') as file:
        file.writelines(proxies[1:])

    return proxies[0].strip()

def get_next_proxy_http():
    proxy_file = 'http.txt'
    used_proxies_file = 'used_http.txt'
    with open(proxy_file, 'r') as file:
        
        proxies = file.readlines()

    if not proxies:
        print("Нет доступных прокси.")
        return None

    with open(used_proxies_file, 'a') as used_file:
        used_file.write(proxies[0])

    with open(proxy_file, 'w') as file:
        file.writelines(proxies[1:])

    return proxies[0].strip()








# def main():
#     proxy = get_next_proxy()
#     if proxy:
#         print(f"Использую прокси: socks5://{proxy}")
#     else:
#         print("Больше нет доступных прокси.")

# if __name__ == "__main__":
    
#     main()
