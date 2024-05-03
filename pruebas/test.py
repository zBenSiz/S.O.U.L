import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as time
import wikipedia
import pyjokes
import random
import threading

class Backend:
    def __init__(self):
        self.name = 'soul'
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.español_mes = {
            'January': 'Enero',
            'February': 'Febrero',
            'March': 'Marzo',
            'April': 'Abril',
            'May': 'Mayo',
            'June': 'Junio',
            'July': 'Julio',
            'August': 'Agosto',
            'September': 'Septiembre',
            'October': 'Octubre',
            'November': 'Noviembre',
            'December': 'Diciembre'
        }
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', 150)
        voice_engine = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voice_engine[0].id)
        wikipedia.set_lang('es')
        self.saludo_inicial = False

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        recognizer = ""
        try:
            with sr.Microphone() as source:
                print('Escuchando...')
                voice = self.listener.listen(source)
                recognizer = self.listener.recognize_google(voice, language='es-MX')
                recognizer = recognizer.lower()

                if self.name in recognizer:
                    recognizer = recognizer.replace(self.name, '')
                print("Recognizer:", recognizer)
        except Exception as e:
            print('Algo ha salido mal:', str(e))
        return recognizer

    def run(self):
        global saludo_inicial
        
        if not self.saludo_inicial:
            self.saludo_inicial = True
            select = self.random_choice()
            self.talk(select)

        recognizer = self.listen()

        print(recognizer)
        if 'cómo estás' in recognizer:
            respuestas = ['Bien, ¿y tú?', 'Excelente, ¿cómo estás tú?', 'Muy bien, gracias por preguntar. ¿Y tú cómo has estado?', 'Estoy bien, ¿y tú cómo estás?']
            respuesta = random.choice(respuestas)
            self.talk(respuesta)

        if 'estoy bien' in recognizer:
            respuestas = ['Me alegro, espero sigas así', 'Excelente', 'Muy bien, estoy contento por ti', 'y espero estés mejor con mi servicio']
            respuesta = random.choice(respuestas)
            self.talk(respuesta)

        if 'estoy mal' in recognizer:
            respuestas = ['Lo lamento, siempre recuerda que puedes contar con tus seres queridos', 'lo lamento mucho, espeor mi servicio pueda ayudarte', 'si necesitas algun consejo de vida, pidemelo', 'En serio espero puedas estar mejor y que vuelvas a estar bien']
            respuesta = random.choice(respuestas)
            self.talk(respuesta)

        if 'qué haremos hoy' in recognizer:
            respuestas = ['Vamos a destruir la universidad ya todos los presentes. JAJAJA, es broma, todavía no tengo la capacidad. Mejor mostremos de que soy capaz de hacer para ayudar']
            respuesta = random.choice(respuestas)
            self.talk(respuesta)

        # REPRODUCE UN VIDEO EN YOUTUBE
        if 'reproduce' in recognizer:
            music = recognizer.replace('reproduce', '')
            self.talk('reproduciendo' + music)
            pywhatkit.playonyt(music)

        # INDICA LA HORA ACTUAL
        elif 'hora' in recognizer:
            hora = time.datetime.now().strftime('%I:%M %p')
            self.talk('Son las '+hora)

        # INDICA EL DÍA MES Y AÑO
        elif 'fecha' in recognizer:
            fecha = time.datetime.now().strftime('%d-%h-%Y')
            self.talk('La fecha es: ' + str(fecha))

        # INDICA EL DÍA
        elif 'día' in recognizer:
            dia = time.datetime.now().strftime('%d')
            self.talk('Hoy es el día ' + str(dia))

        # INDICA EL MES
        elif 'mes' in recognizer:
            español_mes_mes = time.datetime.now().strftime('%B')
            self.talk('Estamos en el mes de ' + str(self.español_mes))

        # INDICA EL AÑO
        elif 'año' in recognizer:
            year = time.datetime.now().strftime('%Y')
            self.talk('Estamos en el ' + str(year))

        # BUSCA EN WIKIPEDIA
        elif 'busca en wikipedia' in recognizer:
            consulta = recognizer.replace('busca en wikipedia', '')
            self.talk('buscando en wikipedia' + consulta)
            resultado = wikipedia.summary(consulta, sentences=3)
            self.talk(resultado)

        # BUSCA EN GOOGLE
        elif 'busca en google' in recognizer:
            consulta = recognizer.replace('busca en google', '')
            self.talk('Buscando en google' + consulta)
            pywhatkit.search(consulta)

        # CHISTES
        elif 'chiste' in recognizer:
            try:
                chiste = pyjokes.get_joke(language='es')
                self.talk(chiste)
            except Exception as e:
                print('Error al obtener el chiste:', str(e))
                self.talk("Lo siento, no pude encontrar ningún chiste en este momento.")

        # DATOS CURIOSOS
        elif 'dato curioso' in recognizer:
            try:
                resumen_aleatorio = wikipedia.random(pages=1)
                resultado = wikipedia.summary(resumen_aleatorio, sentences=2)
                self.talk("Aquí tienes un dato curioso: " + resultado)
            except wikipedia.exceptions.DisambiguationError as e:
                print('Error de desambiguación al buscar datos curiosos:', str(e))
                self.talk("Lo siento, no pude encontrar ningún dato curioso en este momento.")
            except wikipedia.exceptions.PageError as e:
                print('Error de página al buscar datos curiosos:', str(e))
                self.talk("Lo siento, no pude encontrar ningún dato curioso en este momento.")

        elif 'consejo' in recognizer or 'consejo de vida' in recognizer:
            consejos = [
                "La paciencia es una virtud. Tómate el tiempo necesario para alcanzar tus metas.",
                "Mantén una actitud positiva incluso en tiempos difíciles. La actitud lo es todo.",
                "Aprende a escuchar tanto como hablas. A menudo, las personas tienen mucho que enseñarnos.",
                "Recuerda que el fracaso es solo una oportunidad para empezar de nuevo, pero con más experiencia.",
                "No te compares con los demás. Cada persona tiene su propio camino y ritmo de progreso.",
                "Cuida tu salud física y mental. Es la base de una vida plena y feliz.",
                "Aprende a perdonar. El perdón libera tu mente y tu corazón de la carga del rencor.",
                "Sé amable con los demás. Un pequeño gesto de amabilidad puede marcar la diferencia en el día de alguien.",
                "No tengas miedo de pedir ayuda cuando la necesites. Nadie puede hacerlo todo por sí solo.",
                "Enfrenta tus miedos en lugar de huir de ellos. El crecimiento personal ocurre fuera de tu zona de confort.",
                "Cultiva relaciones significativas. Las conexiones humanas son una fuente invaluable de apoyo y felicidad.",
                "No dejes que el pasado defina tu futuro. Cada día es una nueva oportunidad para escribir tu propia historia.",
                "Acepta que no puedes controlar todo. Aprende a dejar ir lo que no está en tus manos.",
                "Practica la gratitud diariamente. Reconocer lo que tienes te ayuda a mantener una perspectiva positiva.",
                "No subestimes el poder de tus palabras. Pueden construir o destruir, así que elige sabiamente cómo las usas.",
                "Vive en el momento presente. El pasado ya pasó y el futuro aún no ha llegado.",
                "Aprovecha las oportunidades que se te presentan. A veces, las mejores cosas de la vida llegan cuando menos las esperas.",
                "Sé fiel a ti mismo. No te pierdas tratando de complacer a los demás.",
                "Practica el autocuidado regularmente. No puedes cuidar de los demás si no te cuidas a ti mismo primero.",
                "Rodeate de personas que te inspiren y te hagan crecer. Tu entorno puede influir en tu éxito y felicidad.",
                "Aprende de tus errores. Son lecciones valiosas disfrazadas de experiencias difíciles.",
                "Celebra tus logros, grandes y pequeños. Cada paso hacia adelante merece ser reconocido y celebrado.",
                "Sé compasivo contigo mismo. Eres humano y estás en constante evolución.",
                "Desarrolla hábitos saludables. Tu cuerpo y tu mente te lo agradecerán a largo plazo.",
                "Deja de preocuparte por cosas que no puedes controlar. Enfoca tu energía en lo que sí puedes cambiar.",
                "Haz lo que te apasiona. La vida es demasiado corta para conformarse con algo que no te hace feliz.",
                "Aprende a decir 'no' cuando sea necesario. Establecer límites saludables es esencial para tu bienestar.",
                "Trata a los demás con respeto y cortesía. Pequeños actos de amabilidad pueden hacer una gran diferencia.",
                "No te tomes la vida demasiado en serio. A veces, necesitas reírte de ti mismo y de las situaciones difíciles.",
                "Mantén una mente abierta. Estar dispuesto a considerar nuevas ideas y perspectivas te permite crecer.",
                "Aprende a decir 'lo siento' cuando te equivoques. Reconocer tus errores muestra humildad y madurez.",
                "Celebra la diversidad. El mundo es un lugar más rico y vibrante debido a nuestras diferencias.",
                "Busca la belleza en las pequeñas cosas de la vida. A menudo, son las cosas simples las que traen la mayor alegría.",
                "Haz una pausa y respira profundamente cuando te sientas abrumado. A veces, todo lo que necesitas es un momento de calma.",
                "Aprende a ser paciente contigo mismo. El crecimiento personal lleva tiempo y esfuerzo.",
                "Establece metas claras y alcanzables. Tener un objetivo te ayuda a mantenerte enfocado y motivado.",
                "Aprende a administrar tu tiempo de manera efectiva. Prioriza las tareas importantes y delega cuando sea necesario.",
                "Haz tiempo para la meditación y la reflexión. La quietud mental es importante para tu bienestar emocional."
            ]
            # Se elige un consejo aleatorio de la lista
            consejo = random.choice(consejos)
            self.talk(consejo)

    def random_choice(self):
        lista = ['Hola, estoy acá para ayudarte, ¿Qué necesitas?',"Hola, como te encuentras?","hoy es un gran día, dime que necesitas", "un saludo, te extrañaba", "Estaba en medio de algo, que quieres?", "me desagrada tu precensia, pero soy un fantasma y no tengo nada que hacer, solo dime que quieres", "Hoy te veo bien, ¿algo interesante que quieras? tengo datos curiosos", "Te veo con mala cara, ¿necesitas un chiste?"]
        seleccion = random.choice(lista)
        return seleccion

    def on_button_click(self):
        threading.Thread(target=self.run).start()
