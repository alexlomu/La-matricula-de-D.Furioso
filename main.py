from bs4 import BeautifulSoup

# Leer el contenido del archivo 'Inbox'
with open('Inbox', 'r', encoding='utf-8') as file:
    inbox_content = file.read()

# Parsear el contenido del archivo con BeautifulSoup
soup = BeautifulSoup(inbox_content, 'html.parser')

# Encontrar la línea que contiene la matrícula
matricula_line = [line for line in soup.get_text().split('\n') if 'Matricula' in line]

if matricula_line:
    # Extraer la matrícula
    matricula = matricula_line[0].split(':')[-1].strip()

    print("Matrícula:", matricula)
else:
    print("No se encontró la matrícula en el archivo 'Inbox'.")

