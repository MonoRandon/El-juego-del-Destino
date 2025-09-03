from flask import Flask, render_template, request
import random

app = Flask(__name__)

COLOR_DESCRIPTIONS = {
    "verde": "Tu preferencia por el color green revela tu afinidad con la <b>misterio y descubrimiento</b>.",
    "rojo": "Tu preferencia por el color red revela tu afinidad con la <b>pasión y energía</b>.",
    "azul": "Tu preferencia por el color blue revela tu afinidad con la <b>calma y sabiduría</b>.",
    "morado": "Tu preferencia por el color purple revela tu afinidad con la <b>creatividad y espiritualidad</b>.",
    "amarillo": "Tu preferencia por el color yellow revela tu afinidad con la <b>alegría y optimismo</b>."
}
ANIMAL_DESCRIPTIONS = {
    "gato": "Tu conexión con el <b>gato</b> simboliza tu naturaleza de <b>independencia y misterio</b>.",
    "perro": "Tu conexión con el <b>perro</b> simboliza tu lealtad y amistad.",
    "águila": "Tu conexión con el <b>águila</b> simboliza tu visión y libertad.",
    "león": "Tu conexión con el <b>león</b> simboliza tu coraje y liderazgo.",
    "delfín": "Tu conexión con el <b>delfín</b> simboliza tu inteligencia y alegría."
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        color = request.form['color'].lower()
        animal = request.form['animal'].lower()
        numero_suerte = random.randint(1, 99)
        color_desc = COLOR_DESCRIPTIONS.get(color, "Tu color favorito revela tu personalidad única.")
        animal_desc = ANIMAL_DESCRIPTIONS.get(animal, "Tu animal favorito revela tu espíritu especial.")
        edad_msg = f"A tus <b>{edad} años</b>, estás en un momento favorable para aprovechar nuevas oportunidades."

        # Mensajes personalizados según color y animal
        destiny_message = "Tu destino está lleno de sorpresas."
        if color == "verde":
            destiny_message = "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría."
        elif color == "rojo":
            destiny_message = "Se acerca una etapa de pasión y energía. Aprovecha cada momento para brillar."
        elif color == "azul":
            destiny_message = "La calma y la sabiduría te guiarán hacia grandes logros."
        elif color == "morado":
            destiny_message = "Tu creatividad abrirá puertas inesperadas en tu vida."
        elif color == "amarillo":
            destiny_message = "La alegría y el optimismo te rodearán, atrayendo buenas noticias."

        # Mensaje extra según animal
        if animal == "gato":
            destiny_message += " Confía en tu intuición y busca momentos de misterio."
        elif animal == "perro":
            destiny_message += " La lealtad y la amistad serán clave en tu camino."
        elif animal == "águila":
            destiny_message += " Tu visión te llevará lejos, mantente atento a nuevas oportunidades."
        elif animal == "león":
            destiny_message += " El coraje y el liderazgo te harán destacar."
        elif animal == "delfín":
            destiny_message += " La inteligencia y la alegría te acompañarán en cada paso."

        # Determinar el color real para mostrar en el círculo
        color_map = {
            "verde": "#22c55e",
            "rojo": "#ef4444",
            "azul": "#3b82f6",
            "morado": "#a78bfa",
            "amarillo": "#facc15"
        }
        color_display = color_map.get(color, "#fff")

        # Mensajes creativos para animal favorito
        animal_messages = {
            "gato": "Como un gato, tu destino será explorar nuevos misterios y encontrar tesoros ocultos en los lugares menos esperados.",
            "perro": "La lealtad y el entusiasmo de un perro te abrirán puertas a amistades duraderas y aventuras inolvidables.",
            "águila": "Tu visión de águila te permitirá ver oportunidades donde otros solo ven obstáculos. Vuela alto y conquista tus sueños.",
            "león": "El coraje y la nobleza del león te guiarán a liderar con fuerza y sabiduría. Prepárate para rugir en tu vida.",
            "delfín": "La alegría y la inteligencia del delfín te llevarán a conectar con personas especiales y disfrutar cada momento como una fiesta en el mar."
        }
        animal_desc = animal_messages.get(animal, "Tu animal favorito revela que tu espíritu es único y sorprendente. ¡Deja que te guíe!")

        return render_template('futuro.html', nombre=nombre, destiny_message=destiny_message, color=color_display, color_desc=color_desc, animal=animal, animal_desc=animal_desc, numero_suerte=numero_suerte, edad_msg=edad_msg)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
