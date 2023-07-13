import tkinter as tk
from analizer_ruby import analyze_code, symbol_table, hashes_table, update_errors, errors_list, arrays_table,sets_table,function_table
from main import lexer

# Crear la ventana principal de la aplicación
window = tk.Tk()
window.title("Analizador de Ruby")
window.geometry("1100x700")

# Configurar el layout en forma de grid
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Función para analizar el código Ruby ingresado por el usuario
def analyze_code_gui():
    clear_data()
    code = code_entry.get("1.0", tk.END).strip()
    lexer.input(code)
    token_output.delete("1.0", tk.END)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_output.insert(tk.END, f"Token('{tok.type}', '{tok.value}')\n")
    analyze_code(code)
    update_tables()
    show_errors()

# Función para actualizar los cuadros de texto de las tablas
def update_tables():
    symbol_table_text.delete("1.0", tk.END)
    hashes_table_text.delete("1.0", tk.END)
    array_table_text.delete("1.0", tk.END)
    set_table_text.delete("1.0", tk.END)
    function_table_text.delete("1.0", tk.END)

    symbol_table_text.insert(tk.END, "Tabla de Símbolos:\n")
    for key, value in symbol_table.items():
        symbol_table_text.insert(tk.END, f"{key}: {value}\n")

    hashes_table_text.insert(tk.END, "Tabla de Hashes:\n")
    for key, value in hashes_table.items():
        hashes_table_text.insert(tk.END, f"{key}: {value}\n")

    array_table_text.insert(tk.END, "Tabla de Arrays:\n")
    for key, value in arrays_table.items():
        array_table_text.insert(tk.END, f"{key}: {value}\n")

    set_table_text.insert(tk.END, "Tabla de Sets:\n")
    for key, value in sets_table.items():
        set_table_text.insert(tk.END, f"{key}: {value}\n")

    function_table_text.insert(tk.END, "Tabla de Funciones:\n")
    for key, value in function_table.items():
        function_table_text.insert(tk.END, f"{key}: {value}\n")

def show_errors():
    errors_text.delete("1.0", tk.END)
    errors_text.insert(tk.END, "Errores:\n")
    for error in errors_list:
        errors_text.insert(tk.END, error)

# Función para borrar todos los datos de las tablas y los errores
def clear_data():
    symbol_table.clear()
    hashes_table.clear()
    symbol_table_text.delete("1.0", tk.END)
    hashes_table_text.delete("1.0", tk.END)
    array_table_text.delete("1.0", tk.END)
    set_table_text.delete("1.0", tk.END)
    function_table_text.delete("1.0", tk.END)
    errors_text.delete("1.0", tk.END)
    errors_list.clear()

column1_frame = tk.Frame(window)
column1_frame.pack(side="left", fill="y",padx=10)

# Etiqueta y campo de texto para ingresar el código Ruby
code_label = tk.Label(column1_frame, text="Código Ruby:")
code_label.pack()

code_entry = tk.Text(column1_frame, height=25, width=50)
code_entry.pack()

# Botón para analizar el código Ruby
analyze_button = tk.Button(column1_frame, text="Analizar", command=analyze_code_gui)
analyze_button.pack()

# Cuadro de texto para mostrar los errores
errors_text = tk.Text(column1_frame, height=13, width=50)
errors_text.pack()

# Botón para borrar todos los datos
clear_button = tk.Button(column1_frame, text="Borrar Datos", command=clear_data)
clear_button.pack()


# Marco para la segunda columna
column2_frame = tk.Frame(window)
column2_frame.pack(side="left", fill="y", padx=10)

# Etiqueta para mostrar "Tokens"
tokens_label = tk.Label(column2_frame, text="Tokens")
tokens_label.pack()

# Cuadro de texto para mostrar los tokens
token_output = tk.Text(column2_frame, height=40, width=30)
token_output.pack()

# Marco para la tercera columna
column3_frame = tk.Frame(window)
column3_frame.pack(side="left", fill="y" , padx=10)

# Cuadro de texto para mostrar la tabla de símbolos
symbol_table_text = tk.Text(column3_frame, height=8, width=50)
symbol_table_text.pack()
symbol_table_text.insert(tk.END, "Tabla de Símbolos:\n")

# Cuadro de texto para mostrar la tabla de hashes
hashes_table_text = tk.Text(column3_frame, height=8, width=50)
hashes_table_text.pack()
hashes_table_text.insert(tk.END, "Tabla de Hashes:\n")

# Cuadros de texto adicionales
array_table_text = tk.Text(column3_frame, height=8, width=50)
array_table_text.pack()
array_table_text.insert(tk.END, "Tabla de Arrays:\n")

set_table_text = tk.Text(column3_frame, height=8, width=50)
set_table_text.insert(tk.END, "Tabla de Sets:\n")
set_table_text.pack()

function_table_text = tk.Text(column3_frame, height=8, width=50)
function_table_text.pack()
function_table_text.insert(tk.END, "Tabla de Funciones:\n")


# Actualizar las tablas al iniciar la aplicación
update_tables()
show_errors()

window.mainloop()
