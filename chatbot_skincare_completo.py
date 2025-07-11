
# --- Sección: Importaciones necesarias ---
import pandas as pd

# --- Sección: Carga de datos ---
df = pd.read_csv("productos_chatbot_final.csv")

# --- Sección: Variables globales ---
tipo_piel_usuario = None
edad_usuario = None

# --- Sección: Función de menú principal ---
def mostrar_menu(nombre):
    print(f"\n🌟 Bienvenido/a, {nombre}, a tu asistente de skincare 🌟")
    print("Elige una opción:")
    print("1. ¿Qué tipo de piel tengo? (Test)")
    print("2. Quiero saber más de mi tipo de piel")
    print("3. ¿Cómo armo mi rutina de skincare según mi tipo de piel?")
    print("4. ¿Qué productos me recomiendas?")
    print("5. Problemas comunes según tu tipo de piel")
    print("6. Consejos para el cuidado de piel según tu tipo de piel")
    print("7. Ingredientes que deberías conocer")
    print("8. Mitos comunes del skincare")
    print("9. No sé... ¡Ayuda!")
    print("10. Salir")

# --- Sección: Test para determinar tipo de piel ---
def test_tipo_piel():
    global tipo_piel_usuario, edad_usuario
    print("\n🧪 TEST: ¿Qué tipo de piel tienes?")
    print("Contesta cada pregunta marcando a, b, c o d según lo que más se parezca a ti.")

    preguntas = [
        {
            "pregunta": "1. ¿Cómo luce tu piel al natural?",
            "opciones": {
                "a": "Lisa y con brillo natural, no oleosa.",
                "b": "Algo opaca y seca.",
                "c": "Me brilla toda la cara.",
                "d": "Algunas zonas están brillosas y otras secas."
            }
        },
        {
            "pregunta": "2. ¿Cómo son tus poros?",
            "opciones": {
                "a": "Finos y poco visibles.",
                "b": "Casi imperceptibles.",
                "c": "Grandes y visibles en todo el rostro.",
                "d": "Grandes solo en la frente, nariz y mentón."
            }
        },
        {
            "pregunta": "3. Al tocar tu piel, ¿cómo se siente?",
            "opciones": {
                "a": "Suave y lisa.",
                "b": "Áspera, a veces descamada.",
                "c": "Gruesa, con granitos.",
                "d": "Una mezcla de seca y grasa según la zona."
            }
        },
        {
            "pregunta": "4. ¿Cómo se comporta tu piel durante el día?",
            "opciones": {
                "a": "Brilla ligeramente al final del día.",
                "b": "Se mantiene opaca casi todo el día.",
                "c": "Brilla mucho todo el día.",
                "d": "Brilla en la zona T, pero no en las mejillas."
            }
        },
        {
            "pregunta": "5. ¿Sueles tener granitos o puntos negros?",
            "opciones": {
                "a": "Muy pocos o ninguno.",
                "b": "Raramente o nunca.",
                "c": "Frecuentemente.",
                "d": "Algunas veces, según la zona."
            }
        },
        {
            "pregunta": "6. Para tu edad, ¿cómo ves tu piel?",
            "opciones": {
                "a": "Normal, sin muchas imperfecciones.",
                "b": "Arrugas marcadas, se siente tirante.",
                "c": "Pocas arrugas, pero piel grasa.",
                "d": "Algunas líneas finas y zonas mixtas."
            }
        }
    ]

    puntajes = {"a": 0, "b": 0, "c": 0, "d": 0}
    tipo_piel = {
        "a": "NORMAL",
        "b": "SECA",
        "c": "GRASA",
        "d": "MIXTA"
    }

    for q in preguntas:
        print(f"\n{q['pregunta']}")
        for letra, texto in q['opciones'].items():
            print(f"  {letra}) {texto}")
        while True:
            r = input("Elige a, b, c o d: ").lower()
            if r in ["a", "b", "c", "d"]:
                puntajes[r] += 1
                break
            else:
                print("❌ Entrada inválida. Por favor escribe a, b, c o d.")

    resultado = max(puntajes, key=puntajes.get)
    tipo_piel_usuario = tipo_piel[resultado]

    # Guardar edad
    while True:
        try:
            edad = int(input("\n🎂 ¿Cuántos años tienes?: "))
            if edad < 13:
                print("⚠️ Esta app está diseñada para mayores de 13 años.")
                return
            elif edad <= 18:
                edad_usuario = "adolescente"
            elif edad <= 59:
                edad_usuario = "adulto"
            else:
                edad_usuario = "adulto mayor"
            break
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")

    print("\n🔍 Resultado del test:")
    print(f"✅ Según tus respuestas, tu tipo de piel es: **{tipo_piel_usuario}**.")
    input("Presiona Enter para volver al menú.")

# --- Sección: Información extendida ---
info_piel = {
    "NORMAL": "Piel equilibrada: poros finos, textura suave y saludable.",
    "SECA": "Produce poco sebo, se siente tirante y puede descamarse. Necesita hidratación intensa.",
    "GRASA": "Produce mucho sebo, suele tener brillo y tendencia al acné. Usa productos oil-free.",
    "MIXTA": "Zona T grasa y mejillas secas. Requiere productos diferentes según la zona.",
    "SENSIBLE": "Se irrita fácilmente. Evita fragancias, alcohol y prefiere productos suaves."
}

def info_según_resultado(tipo):
    print(f"\n📘 Más sobre tu tipo de piel ({tipo}):")
    print(info_piel.get(tipo, "No se encontró información para este tipo."))
    input("\nPresiona Enter para volver al menú.")

def rutina_por_tipo(tipo):
    print("\n🧴 Rutina básica según tu tipo de piel:")
    rutinas = {
        "SECA": "Limpieza suave, serum hidratante, crema nutritiva, protector solar.",
        "GRASA": "Gel limpiador, tónico equilibrante, hidratante ligera, protector solar matificante.",
        "MIXTA": "Productos ligeros en zona T, hidratación en mejillas.",
        "SENSIBLE": "Productos sin fragancia, calmantes como aloe y manzanilla, protector solar mineral.",
        "NORMAL": "Limpieza equilibrada, hidratación ligera, protector solar."
    }
    print(rutinas.get(tipo, "No hay rutina definida para este tipo de piel."))
    input("Presiona Enter para volver al menú.")

def recomendar_productos():
    global tipo_piel_usuario, edad_usuario
    if not tipo_piel_usuario or not edad_usuario:
        print("\n⚠️ Para recibir recomendaciones completas, primero realiza el test.")
        input("Presiona Enter para volver al menú.")
        return

    necesidad = input("💡 ¿Qué necesitas? (acné, hidratación, manchas, arrugas, etc.): ").lower()

    resultados = df[
        df['tipo_piel'].str.lower().str.contains(tipo_piel_usuario.lower()) &
        df['edad'].str.lower().str.contains(edad_usuario.lower()) &
        df['necesidades'].str.lower().str.contains(necesidad)
    ]

    if not resultados.empty:
        print("\n🔍 Recomendaciones:\n")
        for i, row in resultados.iterrows():
            print(f"🧴 Producto: {row['nombre']} ({row['marca']})")
            print(f"💸 Precio: {row['precio']}")
            print(f"🔗 Enlace: {row['enlace']}")
            print("-" * 40)
    else:
        print("😕 No se encontraron productos con esas características.")
    input("Presiona Enter para volver al menú.")

def problemas_comunes(tipo):
    print("\n📌 Problemas comunes según tipo de piel:")
    info = {
        "SECA": "resequedad, descamación, líneas finas.",
        "GRASA": "acné, puntos negros, poros dilatados.",
        "MIXTA": "desequilibrio en zonas, acné en zona T.",
        "SENSIBLE": "enrojecimiento, irritación, alergias."
    }
    print(f"- {tipo}: {info.get(tipo, 'No disponible')}")
    input("Presiona Enter para volver al menú.")

def consejos_por_tipo():
    print("\n🧠 Consejos según tipo de piel:")
    print("- SECA: Usa limpiadores suaves, evita alcohol, aplica humectantes ricos.")
    print("- GRASA: Evita aceites pesados, elige productos oil-free.")
    print("- MIXTA: Usa productos diferentes en cada zona si es necesario.")
    print("- SENSIBLE: Prioriza ingredientes calmantes, sin perfume.")
    input("Presiona Enter para volver al menú.")

def ingredientes_clave():
    print("\n🧪 Ingredientes importantes:")
    print("- Ácido hialurónico: Hidratación profunda.")
    print("- Niacinamida: Control de grasa, mejora textura.")
    print("- Retinol: Antiarrugas, renovación celular.")
    print("- Vitamina C: Ilumina, reduce manchas.")
    input("Presiona Enter para volver al menú.")

def mitos_skincare():
    print("\n🚫 Mitos comunes del skincare:")
    print("❌ El limón aclara la piel – Puede causar quemaduras.")
    print("❌ Si arde, es porque está funcionando – No, probablemente es irritante.")
    print("❌ Solo las mujeres deben cuidarse la piel – ¡Todos debemos hacerlo!")
    input("Presiona Enter para volver al menú.")

def ayuda():
    print("\n🆘 AYUDA GENERAL")
    print("-" * 50)
    print("¿No sabes por dónde empezar? ¡No te preocupes, te ayudo! 💖\n")
    print("👉 Aquí tienes algunas sugerencias:")
    print("1️⃣ Si no sabes tu tipo de piel, empieza por la opción 1: '¿Qué tipo de piel tengo?'.")
    print("2️⃣ Luego puedes usar la opción 2 para aprender más sobre ese tipo de piel.")
    print("3️⃣ Con eso claro, usa la opción 3 para armar tu rutina.")
    print("4️⃣ ¿Quieres productos específicos? La opción 4 es para ti.")
    print("5️⃣ ¿Te interesa aprender más? Explora las opciones 5 a 8.")
    print("\n📌 Consejo: todo lo que elijas está pensado para ayudarte a conocerte y cuidarte mejor.")
    print("🧴 Si tienes dudas reales sobre tu piel, lo mejor es consultar a un dermatólogo/a.")
    input("\nPresiona Enter para volver al menú.")

def chatbot():
    print("👋 ¡Hola! Soy tu asistente virtual de skincare.")
    nombre = input("¿Cómo te llamas? ")

    while True:
        mostrar_menu(nombre)
        opcion = input("Escribe el número de la opción que quieres: ")

        if opcion == "1":
            test_tipo_piel()
        elif opcion == "2":
            if tipo_piel_usuario:
                info_según_resultado(tipo_piel_usuario)
            else:
                print("\n📌 Aún no sabemos tu tipo de piel. Realiza el test (opción 1).")
                input("Presiona Enter para volver al menú.")
        elif opcion == "3":
            if tipo_piel_usuario:
                rutina_por_tipo(tipo_piel_usuario)
            else:
                print("\n📌 Aún no sabemos tu tipo de piel. Realiza el test (opción 1).")
                input("Presiona Enter para volver al menú.")
        elif opcion == "4":
            recomendar_productos()
        elif opcion == "5":
            if tipo_piel_usuario:
                problemas_comunes(tipo_piel_usuario)
            else:
                print("\n📌 No sabemos tu tipo de piel todavía. Haz primero el test (opción 1).")
                input("Presiona Enter para volver al menú.")
        elif opcion == "6":
            consejos_por_tipo()
        elif opcion == "7":
            ingredientes_clave()
        elif opcion == "8":
            mitos_skincare()
        elif opcion == "9":
            ayuda()
        elif opcion == "10":
            print(f"\n👋 ¡Gracias por usar el asistente, {nombre}! Cuida tu piel 💖")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

# Ejecutar chatbot
chatbot()
