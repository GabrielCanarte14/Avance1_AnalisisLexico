import tkinter as tk
from analizer_ruby import analyze_code, symbol_table, hashes_table, update_errors, errors_list
from main import lexer

# Crear la ventana principal de la aplicación
window = tk.Tk()
window.title("Analizador de Ruby")
window.geometry("850x650")

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

    symbol_table_text.insert(tk.END, "Tabla de Símbolos:\n")
    for key, value in symbol_table.items():
        symbol_table_text.insert(tk.END, f"{key}: {value}\n")

    hashes_table_text.insert(tk.END, "Tabla de Hashes:\n")
    for key, value in hashes_table.items():
        hashes_table_text.insert(tk.END, f"{key}: {value}\n")

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
    errors_text.delete("1.0", tk.END)
    errors_list.clear()

# Etiqueta y campo de texto para ingresar el código Ruby
code_label = tk.Label(window, text="Código Ruby:")
code_label.grid(row=0, column=0)

code_entry = tk.Text(window, height=10, width=50)
code_entry.grid(row=1, column=0)

# Etiqueta para mostrar "Tokens"
tokens_label = tk.Label(window, text="Tokens")
tokens_label.grid(row=0, column=1, pady=10)

# Cuadro de texto para mostrar los tokens
token_output = tk.Text(window, height=37, width=50)
token_output.grid(row=1, column=1, padx=10, rowspan=6)  # Cambiado el rowspan a 6 para ocupar más filas

# Botón para analizar el código Ruby
analyze_button = tk.Button(window, text="Analizar", command=analyze_code_gui)
analyze_button.grid(row=2, column=0)

# Cuadro de texto para mostrar la tabla de símbolos
symbol_table_text = tk.Text(window, height=7, width=50)
symbol_table_text.grid(row=3, column=0)
symbol_table_text.insert(tk.END, "Tabla de Símbolos:\n")

# Cuadro de texto para mostrar la tabla de hashes
hashes_table_text = tk.Text(window, height=7, width=50)
hashes_table_text.grid(row=4, column=0)
hashes_table_text.insert(tk.END, "Tabla de Hashes:\n")

# Cuadro de texto para mostrar los errores
errors_text = tk.Text(window, height=10, width=50)
errors_text.grid(row=5, column=0)

# Botón para borrar todos los datos
clear_button = tk.Button(window, text="Borrar Datos", command=clear_data)
clear_button.grid(row=6, column=0)

# Configurar la altura de la fila del cuadro de texto de tokens
window.grid_rowconfigure(1, weight=1)

# Actualizar las tablas al iniciar la aplicación
update_tables()
show_errors()

window.mainloop()
