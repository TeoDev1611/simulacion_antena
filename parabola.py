import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Usar backend TkAgg para mayor compatibilidad
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from matplotlib.lines import Line2D  # Para crear leyendas manuales

# Función para crear la parábola y calcular el foco
def parabola(a, x_range):
    y = a * x_range**2
    foco_y = 1 / (4 * a)
    return y, foco_y

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-10, 10)
ax.set_ylim(-2, 10)
ax.set_title("Reflexión de Ondas en una Antena Parabólica")

# Datos de la parábola
x = np.linspace(-10, 10, 400)
ray_x = np.linspace(-8, 8, 10)  # 10 rayos
ray_y_start = np.full_like(ray_x, 8)  # Comienzan desde arriba

# Inicializar la parábola con un valor por defecto de a
a = 0.2
y, foco_y = parabola(a, x)

# Crear la línea de la parábola
parabola_line, = ax.plot(x, y, color='blue')

# Graficar el foco
foco_x = 0
foco = ax.scatter(foco_x, foco_y, color='black')

# Añadir texto para la ecuación de la parábola
equation_text = ax.text(0.05, 0.95, f'y = {a:.2f}x²', transform=ax.transAxes, 
                        fontsize=12, verticalalignment='top', 
                        bbox=dict(facecolor='white', alpha=0.7))

# Añadir texto para el foco
foco_text = ax.text(0.05, 0.89, f'Foco: (0, {foco_y:.2f})', transform=ax.transAxes,
                   fontsize=12, verticalalignment='top',
                   bbox=dict(facecolor='white', alpha=0.7))

# Graficar los rayos (inicialización vacía para animación)
ray_lines_incident = []
ray_lines_reflected = []

for i in range(len(ray_x)):
    incident, = ax.plot([], [], 'r--')  # Rayos incidentes (rojos)
    reflected, = ax.plot([], [], 'g')   # Rayos reflejados (verdes)
    ray_lines_incident.append(incident)
    ray_lines_reflected.append(reflected)

# Función para animar los rayos reflejados
def animate_rays(a):
    # Calcular el foco actualizado
    _, foco_y = parabola(a, x)
    
    for i, ray in enumerate(ray_x):
        # Calcular el punto de impacto en la parábola
        ray_y_end = a * ray**2
        
        # Rayos incidentes (líneas rojas punteadas)
        ray_lines_incident[i].set_data([ray, ray], [ray_y_start[i], ray_y_end])
        
        # Rayos reflejados (líneas verdes)
        ray_lines_reflected[i].set_data([ray, foco_x], [ray_y_end, foco_y])

# Función para actualizar la gráfica cuando cambiamos la curvatura
def update(val):
    global a, foco_y
    a = slider_a.val
    y, foco_y = parabola(a, x)
    parabola_line.set_ydata(y)
    foco.set_offsets([0, foco_y])
    
    # Actualizar ecuación y posición del foco
    equation_text.set_text(f'y = {a:.2f}x²')
    foco_text.set_text(f'Foco: (0, {foco_y:.2f})')
    
    # Ajustar límites del eje Y dinámicamente
    max_y = max(np.max(y), 10)
    ax.set_ylim(-2, max_y)
    
    animate_rays(a)
    fig.canvas.draw_idle()

# Añadir un slider para cambiar la curvatura de la parábola
ax_slider = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider, 'Curvatura (a)', 0.05, 1.0, valinit=a, valstep=0.05)
slider_a.on_changed(update)

# Función para la animación
def animate(i):
    animate_rays(a)
    return ray_lines_incident + ray_lines_reflected

# Inicializar animación
animate_rays(a)

# Crear la animación sin blit para evitar los errores
ani = FuncAnimation(fig, animate, frames=range(200), interval=20, blit=False)

# Mantener una referencia global a la animación
global animation_reference
animation_reference = ani

# Añadir elementos adicionales
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Crear leyenda manualmente
legend_elements = [
    Line2D([0], [0], color='blue', lw=2, label='Antena parabólica'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=8, label='Foco'),
    Line2D([0], [0], color='r', linestyle='--', label='Rayos incidentes'),
    Line2D([0], [0], color='g', label='Rayos reflejados')
]
ax.legend(handles=legend_elements, loc='upper right')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.show()