import tkinter as tk
from analizer_ruby import analyze_code, symbol_table, hashes_table

# Crear la ventana principal de la aplicación
window = tk.Tk()
window.title("Analizador de Ruby")
window.geometry("420x800")

# Función para analizar el código Ruby ingresado por el usuario
def analyze_code_gui():
    code = code_entry.get("1.0", tk.END).strip()
    analyze_code(code)
    update_tables()
    update_errors()

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

# Función para actualizar el cuadro de texto de errores
def update_errors():
    errors_text.delete("1.0", tk.END)

    errors_text.insert(tk.END, "Errores:\n")
    # lógica para obtener y mostrar los errores sintácticos

# Función para borrar todos los datos de las tablas y los errores
def clear_data():
    symbol_table.clear()
    hashes_table.clear()
    symbol_table_text.delete("1.0", tk.END)
    hashes_table_text.delete("1.0", tk.END)
    errors_text.delete("1.0", tk.END)

# Etiqueta y campo de texto para ingresar el código Ruby
code_label = tk.Label(window, text="Código Ruby:")
code_label.pack()

code_entry = tk.Text(window, height=10, width=50)
code_entry.pack()

# Botón para analizar el código Ruby
analyze_button = tk.Button(window, text="Analizar", command=analyze_code_gui)
analyze_button.pack()

# Cuadro de texto para mostrar la tabla de símbolos
symbol_table_text = tk.Text(window, height=10, width=50)
symbol_table_text.pack()
symbol_table_text.insert(tk.END, "Tabla de Símbolos:\n")

# Cuadro de texto para mostrar la tabla de hashes
hashes_table_text = tk.Text(window, height=10, width=50)
hashes_table_text.pack()
hashes_table_text.insert(tk.END, "Tabla de Hashes:\n")

# Cuadro de texto para mostrar los errores
errors_text = tk.Text(window, height=10, width=50)
errors_text.pack()
errors_text.insert(tk.END, "Errores:\n")

# Botón para borrar todos los datos
clear_button = tk.Button(window, text="Borrar Datos", command=clear_data)
clear_button.pack()

# Actualizar las tablas al iniciar la aplicación
update_tables()

window.mainloop()
