import streamlit as st
import pandas as pd

# --- Cargar los datos ---
@st.cache_data
def cargar_datos():
    return pd.read_csv("productos_chatbot_final.csv")

df = cargar_datos()
st.write("✅ Datos cargados:")
st.write(df.head())

# --- Inicializar variables en session_state ---
if "tipo_piel" not in st.session_state:
    st.session_state.tipo_piel = None
if "edad_usuario" not in st.session_state:
    st.session_state.edad_usuario = None
if "nombre_usuario" not in st.session_state:
    st.session_state.nombre_usuario = None

# --- Título ---
st.title("🧴 Asistente Virtual de Skincare")

# --- Nombre del usuario ---
nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.session_state.nombre_usuario = nombre

if st.session_state.nombre_usuario:
    st.header(f"🌟 Bienvenida/o, {st.session_state.nombre_usuario}")

    opcion = st.selectbox(
        "Elige una opción:",
        [
            "Selecciona una opción",
            "1. ¿Qué tipo de piel tengo? (Test)",
            "2. Saber más de mi tipo de piel",
            "3. Armar mi rutina de skincare",
            "4. Productos recomendados",
            "5. Problemas comunes",
            "6. Consejos de cuidado",
            "7. Ingredientes importantes",
            "8. Mitos del skincare",
            "9. Ayuda general"
        ]
    )

    # --- Opción 1: Test de tipo de piel ---
    if opcion == "1. ¿Qué tipo de piel tengo? (Test)":
        st.subheader("🧪 TEST: ¿Qué tipo de piel tienes?")

        preguntas = [
            ("¿Cómo luce tu piel al natural?", ["Lisa y con brillo natural, no oleosa.", "Algo opaca y seca.", "Me brilla toda la cara.", "Algunas zonas brillan y otras están secas."]),
            ("¿Cómo son tus poros?", ["Finos y poco visibles.", "Casi imperceptibles.", "Grandes y visibles en todo el rostro.", "Grandes solo en la frente, nariz y mentón."]),
            ("¿Cómo se siente tu piel al tacto?", ["Suave y lisa.", "Áspera o descamada.", "Gruesa, con granitos.", "Una mezcla de seca y grasa."]),
            ("¿Cómo se comporta tu piel durante el día?", ["Brilla ligeramente al final del día.", "Se mantiene opaca casi todo el día.", "Brilla mucho todo el día.", "Brilla en la zona T, pero no en mejillas."]),
            ("¿Tienes granitos o puntos negros?", ["Muy pocos o ninguno.", "Raramente o nunca.", "Frecuentemente.", "Algunas veces, según la zona."]),
            ("¿Cómo ves tu piel según tu edad?", ["Normal, sin muchas imperfecciones.", "Arrugas marcadas, se siente tirante.", "Piel grasa, pocas arrugas.", "Líneas finas y zonas mixtas."])
        ]

        opciones = []
        for idx, (pregunta, respuestas) in enumerate(preguntas):
            respuesta = st.radio(pregunta, respuestas, key=f"preg_{idx}")
            opciones.append(respuesta)

        if st.button("Ver mi tipo de piel"):
            conteo = {"a": 0, "b": 0, "c": 0, "d": 0}
            for r in opciones:
                if "Lisa" in r or "Finos" in r or "Suave" in r or "Brilla ligeramente" in r or "Muy pocos" in r or "Normal" in r:
                    conteo["a"] += 1
                elif "seca" in r or "imperceptibles" in r or "Áspera" in r or "opaca" in r or "Raramente" in r or "Arrugas" in r:
                    conteo["b"] += 1
                elif "brilla toda la cara" in r or "Grandes y visibles" in r or "granitos" in r or "mucho todo el día" in r or "Frecuentemente" in r or "Piel grasa" in r:
                    conteo["c"] += 1
                else:
                    conteo["d"] += 1

            resultado = max(conteo, key=conteo.get)
            tipo_map = {"a": "NORMAL", "b": "SECA", "c": "GRASA", "d": "MIXTA"}
            st.session_state.tipo_piel = tipo_map[resultado]

            edad = st.number_input("🎂 ¿Cuántos años tienes?", min_value=0, max_value=120, step=1)
            if edad < 13:
                st.warning("Esta app está pensada para mayores de 13 años.")
            elif edad <= 18:
                st.session_state.edad_usuario = "adolescente"
            elif edad <= 59:
                st.session_state.edad_usuario = "adulto"
            else:
                st.session_state.edad_usuario = "adulto mayor"

            st.success(f"✅ Tu tipo de piel es: {st.session_state.tipo_piel}")

    # --- Opción 2: Info extendida ---
    elif opcion == "2. Saber más de mi tipo de piel":
        info_piel = {
            "NORMAL": "Piel equilibrada: poros finos, textura suave y saludable.",
            "SECA": "Produce poco sebo, se siente tirante y puede descamarse. Necesita hidratación intensa.",
            "GRASA": "Produce mucho sebo, suele tener brillo y tendencia al acné. Usa productos oil-free.",
            "MIXTA": "Zona T grasa y mejillas secas. Requiere productos diferentes según la zona.",
            "SENSIBLE": "Se irrita fácilmente. Evita fragancias, alcohol y prefiere productos suaves."
        }
        if st.session_state.tipo_piel:
            st.info(info_piel.get(st.session_state.tipo_piel))
        else:
            st.warning("Primero realiza el test para saber tu tipo de piel.")

    # --- Opción 3: Rutina básica ---
    elif opcion == "3. Armar mi rutina de skincare":
        rutinas = {
            "NORMAL": "Limpieza equilibrada, hidratación ligera, protector solar.",
            "SECA": "Limpieza suave, serum hidratante, crema nutritiva, protector solar.",
            "GRASA": "Gel limpiador, tónico equilibrante, hidratante ligera, protector solar matificante.",
            "MIXTA": "Productos ligeros en zona T, hidratación en mejillas.",
            "SENSIBLE": "Productos sin fragancia, calmantes como aloe y manzanilla, protector solar mineral."
        }
        if st.session_state.tipo_piel:
            st.success(rutinas.get(st.session_state.tipo_piel))
        else:
            st.warning("Primero realiza el test para saber tu tipo de piel.")

    # --- Opción 4: Recomendaciones de productos ---
    elif opcion == "4. Productos recomendados":
        if st.session_state.tipo_piel and st.session_state.edad_usuario:
            necesidad = st.text_input("¿Qué necesitas? (acné, hidratación, manchas, etc.)")
            if necesidad:
                resultados = df[
                    df["tipo_piel"].str.lower().str.contains(st.session_state.tipo_piel.lower()) &
                    df["edad"].str.lower().str.contains(st.session_state.edad_usuario.lower()) &
                    df["necesidades"].str.lower().str.contains(necesidad.lower())
                ]
                if not resultados.empty:
                    for _, row in resultados.iterrows():
                        st.markdown(f"### 🧴 {row['nombre']} ({row['marca']})")
                        st.write(f"💸 **Precio:** {row['precio']}")
                        st.write(f"[🔗 Enlace al producto]({row['enlace']})")
                        st.markdown("---")
                else:
                    st.warning("No se encontraron productos con esas características.")
        else:
            st.warning("Primero completa el test para obtener recomendaciones.")

    # --- Opción 5: Problemas comunes ---
    elif opcion == "5. Problemas comunes":
        problemas = {
            "SECA": "Resequedad, descamación, líneas finas.",
            "GRASA": "Acné, puntos negros, poros dilatados.",
            "MIXTA": "Desequilibrio en zonas, acné en zona T.",
            "SENSIBLE": "Enrojecimiento, irritación, alergias.",
            "NORMAL": "Muy pocos problemas visibles, pero requiere cuidado básico."
        }
        if st.session_state.tipo_piel:
            st.info(f"{st.session_state.tipo_piel}: {problemas.get(st.session_state.tipo_piel, 'Sin datos')}")
        else:
            st.warning("Realiza el test primero.")

    # --- Opción 6: Consejos por tipo ---
    elif opcion == "6. Consejos de cuidado":
        st.markdown("""
- **SECA**: Usa limpiadores suaves, evita alcohol, aplica humectantes ricos.
- **GRASA**: Evita aceites pesados, elige productos oil-free.
- **MIXTA**: Usa productos diferentes en cada zona si es necesario.
- **SENSIBLE**: Prioriza ingredientes calmantes, sin perfume.
- **NORMAL**: Mantén una rutina básica equilibrada.
        """)

    # --- Opción 7: Ingredientes clave ---
    elif opcion == "7. Ingredientes importantes":
        st.markdown("""
- **Ácido hialurónico**: Hidratación profunda.
- **Niacinamida**: Control de grasa, mejora textura.
- **Retinol**: Antiarrugas, renovación celular.
- **Vitamina C**: Ilumina, reduce manchas.
        """)

    # --- Opción 8: Mitos comunes ---
    elif opcion == "8. Mitos del skincare":
        st.markdown("""
- ❌ El limón aclara la piel – Puede causar quemaduras.
- ❌ Si arde, está funcionando – No, probablemente es irritante.
- ❌ Solo las mujeres deben cuidarse la piel – ¡Todos debemos hacerlo!
        """)

    # --- Opción 9: Ayuda general ---
    elif opcion == "9. Ayuda general":
        st.markdown("""
🆘 **¿No sabes por dónde empezar?**

1. Realiza el test para conocer tu tipo de piel.
2. Aprende más sobre tu tipo (opción 2).
3. Arma tu rutina (opción 3).
4. Busca productos (opción 4).
5. Explora mitos, ingredientes y consejos.

💡 Y si tienes dudas reales, consulta a un dermatólogo/a.
        """)
