import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Cuestionario: Introducción a Java",
    page_icon="☕",
    layout="centered"
)

st.title("☕ Actividad Interactiva: Introducción a Java")
st.write("Responde a las siguientes 10 preguntas. Recibirás retroalimentación inmediata al marcar cada respuesta.")

# Estructura de datos de las preguntas
preguntas = [
    # --- PREGUNTAS TEÓRICAS (1 - 7) ---
    {
        "id": 1,
        "enunciado": "1. ¿Qué significa el acrónimo WORA en el contexto de Java?",
        "opciones": [
            "Write Once, Run Anywhere",
            "Write Option, Run Always",
            "Web Object Relational Architecture",
            "Windows Operating System Requirement"
        ],
        "correcta": 0,
        "explicacion": "Significa 'Write Once, Run Anywhere' (Escribe una vez, ejecuta en cualquier parte), haciendo referencia a la portabilidad de la JVM.",
        "es_codigo": False
    },
    {
        "id": 2,
        "enunciado": "2. ¿Qué componente se encarga de ejecutar el Bytecode de Java en cualquier sistema operativo?",
        "opciones": [
            "JDK (Java Development Kit)",
            "JVM (Java Virtual Machine)",
            "JRE (Java Runtime Environment)",
            "JCP (Java Community Process)"
        ],
        "correcta": 1,
        "explicacion": "La JVM (Máquina Virtual de Java) interpreta o compila el Bytecode (.class) al código máquina específico de cada sistema operativo.",
        "es_codigo": False
    },
    {
        "id": 3,
        "enunciado": "3. ¿Quién es considerado el padre del lenguaje de programación Java?",
        "opciones": [
            "Dennis Ritchie",
            "James Gosling",
            "Bjarne Stroustrup",
            "Guido van Rossum"
        ],
        "correcta": 1,
        "explicacion": "James Gosling lideró el equipo del Green Project en Sun Microsystems que dio origen a Java en 1995.",
        "es_codigo": False
    },
    {
        "id": 4,
        "enunciado": "4. ¿Cuál de los siguientes NO es un tipo de dato primitivo en Java?",
        "opciones": [
            "int",
            "boolean",
            "String",
            "double"
        ],
        "correcta": 2,
        "explicacion": "String es una Clase (tipo de dato no primitivo o por referencia). Los 8 primitivos son: byte, short, int, long, float, double, char y boolean.",
        "es_codigo": False
    },
    {
        "id": 5,
        "enunciado": "5. ¿Qué palabra reservada se utiliza para definir una constante en Java?",
        "opciones": [
            "const",
            "static",
            "final",
            "immutable"
        ],
        "correcta": 2,
        "explicacion": "La palabra clave 'final' evita que el valor de una variable sea modificado tras su asignación inicial.",
        "es_codigo": False
    },
    {
        "id": 6,
        "enunciado": "6. ¿Qué operador evalúa si dos condiciones son verdaderas con evaluación de cortocircuito?",
        "opciones": [
            "&",
            "&&",
            "|",
            "||"
        ],
        "correcta": 1,
        "explicacion": "El operador '&&' (AND lógico) realiza evaluación de cortocircuito: si la primera condición es falsa, no evalúa la segunda.",
        "es_codigo": False
    },
    {
        "id": 7,
        "enunciado": "7. ¿Para qué se utiliza la clase Scanner en Java?",
        "opciones": [
            "Para compilar código fuente",
            "Para limpiar la memoria no utilizada",
            "Para leer entradas de datos desde la consola",
            "Para renderizar interfaces gráficas"
        ],
        "correcta": 2,
        "explicacion": "Scanner (java.util.Scanner) permite capturar la entrada de datos del usuario por teclado a través de System.in.",
        "es_codigo": False
    },
    # --- PREGUNTAS DE ENCONTRAR EL ERROR (8 - 10) ---
    {
        "id": 8,
        "enunciado": "8. Encuentra el error en el siguiente código de Java:",
        "codigo": """public class Ejemplo {
    public static void main(String[] args) {
        float pi = 3.1416;
        System.out.println(pi);
    }
}""",
        "opciones": [
            "El método main no puede ser static",
            "Falta la letra 'f' al final del literal decimal (3.1416f)",
            "System.out.println no acepta variables de tipo float",
            "La clase debe llamarse Main"
        ],
        "correcta": 1,
        "explicacion": "En Java, los literales decimales son 'double' por defecto. Para asignarlos a un 'float' se requiere el sufijo 'f' (ej. 3.1416f) o hacer un casting explícito.",
        "es_codigo": True
    },
    {
        "id": 9,
        "enunciado": "9. Encuentra el error en el siguiente código de constantes:",
        "codigo": """public class Constantes {
    public static void main(String[] args) {
        final int LIMITE = 100;
        LIMITE = 200;
        System.out.println(LIMITE);
    }
}""",
        "opciones": [
            "No se puede reasignar un valor a una variable declarada como 'final'",
            "Las constantes deben declararse fuera de la clase",
            "Falta importar la librería de constantes",
            "El nombre LIMITE debe estar en minúsculas"
        ],
        "correcta": 0,
        "explicacion": "Una variable con el modificador 'final' es una constante y su valor no puede cambiarse una vez asignado.",
        "es_codigo": True
    },
    {
        "id": 10,
        "enunciado": "10. Encuentra el error en la firma del método main:",
        "codigo": """public class HolaMundo {
    public void main(String args) {
        System.out.println("¡Hola!");
    }
}""",
        "opciones": [
            "Falta el punto y coma después de System.out.println",
            "Falta la palabra reservada 'static' y 'args' debe ser un arreglo (String[] args)",
            "El mensaje debe ir entre comillas simples",
            "La palabra 'public' no se puede usar en métodos main"
        ],
        "correcta": 1,
        "explicacion": "El punto de entrada de la JVM requiere obligatoriamente que la firma sea 'public static void main(String[] args)'.",
        "es_codigo": True
    }
]

# Inicializar estado para guardar respuestas del usuario
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

# Renderizar cada pregunta dentro de un contenedor (tarjeta)
for idx, p in enumerate(preguntas):
    with st.container():
        st.subheader(p["enunciado"])
        
        # Si contiene bloque de código, se muestra con formato resaltado
        if p["es_codigo"]:
            st.code(p["codigo"], language="java")
            
        opcion_seleccionada = st.radio(
            "Selecciona tu respuesta:",
            p["opciones"],
            key=f"p_{p['id']}",
            index=None
        )
        
        # Botón para comprobar respuesta individual
        if st.button(f"Comprobar pregunta {p['id']}", key=f"btn_{p['id']}"):
            if opcion_seleccionada is None:
                st.warning("⚠️ Por favor, selecciona una opción antes de comprobar.")
            else:
                indice_seleccionado = p["opciones"].index(opcion_seleccionada)
                es_correcta = indice_seleccionado == p["correcta"]
                st.session_state.respuestas[p["id"]] = es_correcta
                
                if es_correcta:
                    st.success(f"✅ **¡VERDADERO! Respuesta correcta.**\n\n{p['explicacion']}")
                else:
                    respuesta_correcta_texto = p["opciones"][p["correcta"]]
                    st.error(f"❌ **FALSO.**\n\n**La respuesta correcta es:** {respuesta_correcta_texto}\n\n**Explicación:** {p['explicacion']}")
        
        st.divider()

# Sección final con puntuación acumulada
if len(st.session_state.respuestas) > 0:
    correctas = sum(st.session_state.respuestas.values())
    total_respondidas = len(st.session_state.respuestas)
    st.info(f"📊 **Resultado actual:** Hash respondido {total_respondidas} de 10 preguntas. Respuestas correctas: {correctas}/{total_respondidas}")

