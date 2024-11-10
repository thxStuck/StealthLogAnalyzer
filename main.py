import os
import subprocess
import logging
from collections import Counter
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def extract_data_from_rar(rar_path):
    extracted_data = {}
    seven_zip_path = r'C:\Program Files\7-Zip\7z.exe'  # Укажите путь к 7z.exe

    if not os.path.exists(seven_zip_path):
        logging.error(f'7z.exe не найден по пути: {seven_zip_path}')
        return extracted_data

    try:
        subprocess.run([seven_zip_path, 'x', rar_path, '-oextracted', '-y'], check=True)
        logging.info(f'Файлы извлечены в папку "extracted".')

        folders = os.listdir("extracted")
        logging.info(f'Найдено {len(folders)} папок в "extracted".')

        for folder in folders:
            folder_path = os.path.join("extracted", folder)
            if os.path.isdir(folder_path):
                ip_address = folder.split(']')[1]
                region = folder.split(']')[0][1:]

                extracted_data[ip_address] = {
                    'region': region,
                    'os_version': None,
                    'browser_data': [],
                    'passwords': [],
                    'log_date': None,
                    'log_time': None
                }

                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    try:
                        if file_name == "System.txt":
                            with open(file_path, 'r') as f:
                                for line in f:
                                    if "OS Version:" in line:
                                        extracted_data[ip_address]['os_version'] = line.split(': ')[1].strip()
                                    if "Local Date:" in line:
                                        extracted_data[ip_address]['log_date'] = line.split(': ')[1].strip()
                                    if "Time:" in line:
                                        extracted_data[ip_address]['log_time'] = line.split(': ')[1].strip()

                        elif file_name == "All Passwords.txt":
                            with open(file_path, 'r') as f:
                                data = f.read()
                                extracted_data[ip_address]['passwords'] = extract_passwords(data)
                                extracted_data[ip_address]['browser_data'] = extract_browsers(data)

                    except Exception as e:
                        logging.error(f'Ошибка при обработке файла {file_name}: {e}')

    except subprocess.CalledProcessError as e:
        logging.error(f'Ошибка при извлечении RAR-файла: {e}')

    return extracted_data

def extract_passwords(data):
    passwords = []
    for line in data.splitlines():
        if "USER:" in line and "PASS:" in line:
            user = line.split("USER: ")[1].split("\n")[0].strip()
            password = line.split("PASS: ")[1].strip()
            passwords.append((user, password))
            logging.info(f'Найден пароль: USER={user}, PASSWORD={password}')
    return passwords

def extract_browsers(data):
    browsers = []
    current_browser = None
    for line in data.splitlines():
        if line.startswith("SOFT:"):
            current_browser = line.split("SOFT: ")[1].split(" (")[0].strip()  
            logging.info(f'Найден браузер: {current_browser}')
        elif "USER:" in line and current_browser:
            browsers.append(current_browser)  
    return browsers

def get_most_popular_password(passwords):
    if not passwords:
        return 'None'
    password_list = [pwd[1] for pwd in passwords]
    password_counts = Counter(password_list)
    most_common = password_counts.most_common()
    if most_common:
        return most_common[0][0]
    else:
        return password_list[0] if password_list else 'None'  


def save_to_sql_file(data, filename='logs_analysis.sql'):
    with open(filename, 'w') as f:
        f.write('CREATE TABLE logs (\n')
        f.write('    region TEXT,\n')
        f.write('    ip TEXT,\n')
        f.write('    most_popular_browser TEXT,\n')
        f.write('    most_popular_password TEXT,\n')
        f.write('    os_version TEXT,\n')
        f.write('    log_date TEXT,\n')
        f.write('    log_time TEXT\n')
        f.write(');\n\n')
        for ip, details in data.items():
            most_popular_browser = Counter(details['browser_data']).most_common(1)
            most_popular_browser = most_popular_browser[0][0] if most_popular_browser else 'Unknown'
            most_popular_password = get_most_popular_password(details['passwords'])
            f.write(f"INSERT INTO logs (region, ip, most_popular_browser, most_popular_password, os_version, log_date, log_time) VALUES (")
            f.write(f"'{details['region']}', '{ip}', '{most_popular_browser}', '{most_popular_password}', ")
            f.write(f"'{details['os_version'] if details['os_version'] else 'None'}', ")
            f.write(f"'{details['log_date'] if details['log_date'] else 'None'}', ")
            f.write(f"'{details['log_time'] if details['log_time'] else 'None'}');\n")

def main():
    rar_path = 'task4.rar'  # Укажите путь к вашему архиву
    extracted_data = extract_data_from_rar(rar_path)
    save_to_sql_file(extracted_data)

if __name__ == "__main__":
    main()
