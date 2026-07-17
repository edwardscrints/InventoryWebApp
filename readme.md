# Assisprex - Sistema de Gestión de Inventario

Plataforma integral para la gestión de productos, diseñada con una arquitectura desacoplada (Frontend/Backend) que garantiza alta disponibilidad, trazabilidad de datos y una experiencia de usuario fluida.

## Características Principales

*   **Gestión Completa (CRUD):** Creación, lectura, actualización y eliminación de productos.
*   **Auditoría de Datos (Reto Diferenciador):** Sistema de historial dinámico que registra la creación y los cambios específicos en cada campo del producto (trazabilidad exacta de operaciones).
*   **Gestión de Estados:** Cambio rápido de estado (Activo/Inactivo) directamente desde la interfaz principal con un solo clic.
*   **Eliminación Segura:** Prevención de borrados accidentales mediante validación por modal de doble confirmación.
*   **Base de Datos Autogestionada:** Migración y creación de estructura automatizada mediante SQLAlchemy (ORM).

## Tecnologías Utilizadas
*   **Frontend:** Vue 3, Vite.
*   **Backend:** Python 3.12, FastAPI.
*   **Base de Datos:** PostgreSQL 15 (Desplegado vía Docker).

---

##  Dependencias Principales

### Backend (Python)
Las siguientes librerías deben estar listadas en tu archivo `requirements.txt`:
*   `fastapi`: Framework principal para la construcción de la API REST.
*   `uvicorn`: Servidor ASGI para ejecutar la aplicación FastAPI.
*   `sqlalchemy`: ORM para el mapeo y gestión de la base de datos relacional.
*   `psycopg2` (o `psycopg2-binary`): Driver adaptador para conectar Python con PostgreSQL.
*   `python-dotenv`: Gestor para cargar variables de entorno desde el archivo `.env`.

### Frontend (Vue 3)
Las siguientes librerías se instalaron vía NPM y se encuentran en el `package.json`:
*   `vue`: Framework progresivo de JavaScript.
*   `vue-router`: Enrutador oficial para crear la Single Page Application (SPA).
*   `axios`: Cliente HTTP basado en promesas para consumir la API de FastAPI.

---

##  Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu entorno local antes de iniciar:

*   [Python 3.12+](https://www.python.org/downloads/)
*   [Node.js (v18+) y npm](https://nodejs.org/)
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) (o el motor de Docker activo).

---

##  Instalación y Configuración

Sigue estos pasos en orden para levantar el entorno de desarrollo.

### 1. Despliegue de la Base de Datos (Docker)

Levanta el contenedor de PostgreSQL ejecutando el siguiente comando en tu terminal:

```bash
docker run --name assisprex-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=inventory_db -p 5432:5432 -d postgres:15-alpine
```

### 2. Configuración del Backend (FastAPI)
Abre una nueva terminal en la raíz del proyecto y navega a la carpeta del backend:

```bash
cd backend
Crea y activa un entorno virtual:
```

PowerShell
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate
Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
Configura las variables de entorno:
```

Crea un archivo .env en la raíz de la carpeta backend.

Añade la cadena de conexión basada en el archivo .env.example:

Fragmento de código
DATABASE_URL=postgresql://postgres:admin@localhost:5432/inventory_db
Inicia el servidor Backend:

```bash
uvicorn app.main:app --reload
El backend arrancará en http://127.0.0.1:8000 y SQLAlchemy creará automáticamente las tablas necesarias en PostgreSQL.
```

### 3. Configuración del Frontend (Vue 3)
Abre una nueva terminal en la raíz del proyecto y navega a la carpeta del frontend:

```bash
cd frontend
Instala las dependencias de Node:
```

```bash
npm install
Inicia el servidor de desarrollo:
```

```bash
npm run dev
El frontend arrancará y estará disponible en http://localhost:5173.
```

 Uso de la Aplicación
Una vez que ambos servidores (Vite y Uvicorn) estén corriendo, abre tu navegador y visita http://localhost:5173.

Utiliza el botón "+ Nuevo Producto" para registrar el primer artículo en la base de datos.

Explora las acciones de edición, cambio de estado y revisa el Historial para comprobar la auditoría de los datos.

 ### Autor
Ing. Edward Gabriel Acosta
Backend Developer & Software Integration Engineer
Bogotá, Colombia.