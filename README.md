# Factory-Project
# 🏭 **FactoryProject**

Aplicación web desarrollada con **Django** bajo el patrón **MVT (Model–View–Template)**, diseñada para gestionar las operaciones de una **fábrica**.
Actualmente, el alcance del sistema se centra en la aplicación **Planificación**.

---

## 🚀 **Características Principales**

* Arquitectura **MVT** completamente implementada.
* Panel de administración de Django configurado para manejar entidades clave.
* Formularios funcionales para **crear, listar y buscar** información.
* Interfaz responsive basada en **Bootstrap** (en progreso).

---

## 🧩 **Estructura del Proyecto**

### **Modelos definidos en `models.py`**

| Clase      | Descripción                                                            |
| :--------- | :--------------------------------------------------------------------- |
| `Proyecto` | Representa un proyecto planificado dentro de la fábrica.               |
| `Cliente`  | Define los datos de los clientes asociados a los proyectos.            |
| `Vendedor` | Contiene la información de los vendedores que gestionan los proyectos. |

---

### **Templates y URLs**

| Template          | Descripción                                                                        | URL            |
| :---------------- | :--------------------------------------------------------------------------------- | :------------- |
| 🏠 **Index**      | Template base desde el cual se extienden los demás templates.                      | `/`            |
| 📋 **Proyectos**  | Lista los proyectos ingresados y permite realizar búsquedas por nombre de cliente. | `/proyectos/`  |
| 👥 **Clientes**   | Muestra los clientes registrados en el sistema.                                    | `/clientes/`   |
| 💼 **Vendedores** | Visualiza los vendedores activos en el sistema.                                    | `/vendedores/` |

---

## 🧾 **Formularios**

| Formulario               | Función                                         | Acceso                                        |
| :----------------------- | :---------------------------------------------- | :-------------------------------------------- |
| 🔍 **Buscar Proyecto**   | Permite buscar proyectos por nombre de cliente. | `/proyectos/`                                 |
| ➕ **Crear Proyecto**     | Formulario para registrar un nuevo proyecto.    | Botón en `/proyectos/` o `/proyectos/crear`   |
| 🧱 **Crear Cliente**     | Alta de nuevos clientes en el sistema.          | Botón en `/clientes/` o `/clientes/crear`     |
| 🧑‍💼 **Crear Vendedor** | Alta de nuevos vendedores en el sistema.        | Botón en `/vendedores/` o `/vendedores/crear` |

---

## 🛠️ **Tecnologías Utilizadas**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-0C4B33?logo=django)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)

---

## 💡 **Próximas Mejoras**

* [ ] Agregar autenticación de usuarios.
* [ ] Mejorar el diseño visual de los templates con Bootstrap.
* [ ] Implementar validaciones avanzadas en formularios.
* [ ] Agregar reportes descargables en PDF o Excel.

---

## 📂 **Estructura del Proyecto (Vista Simplificada)**

```
FactoryProject/
│
├── planificacion/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── planificacion
│           ├── index.html
│           ├── proyectos.html
│           ├── clientes.html
│           └── vendedores.html
│
├── Fabrica/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

## 👨‍💻 **Autor**

**Elias Milano**
📍 Montevideo, Uruguay
💼 Ingeniero de Producción y Desarrollador FullStack


