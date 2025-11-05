# Factory-Project
# 🏭 **FactoryProject**

Aplicación web desarrollada con **Django** bajo el patrón **MVT (Model–View–Template)**, diseñada para gestionar las operaciones de una **fábrica**.
Actualmente, el alcance del sistema se centra en las aplicaciones **Planificación** y **Producción** para la gestión de datos, y en la aplicación **Cuentas** para la gestión de cuentas de usuarios.

**Video de demostración**: descargar video desde https://drive.google.com/file/d/1zPshIE4JATy1leSb9ZnTprlVUBhDww0_/view?usp=sharing

---

## 🚀 **Características Principales**

* Arquitectura **MVT** completamente implementada. 
* **Vistas estilo función** implementadas en las aplicaciones Cuentas y Planificación.
* **Vistas basadas en clases** implementadas en la aplicación Producción.
* Panel de administración de Django configurado para manejar entidades clave.
* Formularios funcionales para **crear, listar y buscar** información.
* **CRUD** implementado en las vistas de Planificación y Producción
* Interfaz responsive basada en **Bootstrap** (en progreso).

---

## 🧩 **Estructura del Proyecto**

### **Modelos definidos**

| Clase        | Descripción                                                                         |
| :----------- | :-----------------------------------------------------------------------------------|
| `Proyecto`   | Es el modelo principal. Representa un proyecto planificado dentro de la fábrica.    |
| `Producción` | Representa los datos asociados a la gestión de producción de un proyecto.           |
| `Cliente`    | Define los datos de los clientes asociados a los proyectos.                         |
| `Vendedor`   | Contiene la información de los vendedores que gestionan los proyectos.              |
| `Cuentas`    | Modelo para la gestión de cuentas de usuarios de la aplicación                      |

---

### **Templates y URLs principales**

| Template          | Descripción                                                                        | URL                 |
| :---------------- | :--------------------------------------------------------------------------------- | :------------------ |
| 🏠 **Index**      | Template base desde el cual se extienden los demás templates.                      | `/`                 |
| 📋 **Proyectos**  | Lista los proyectos ingresados y permite realizar búsquedas por nombre de cliente. | `/proyectos/`       |
| 💼 **Producción** | Presenta los datos de producción asociados a los proyectos registrados en sistema. | `/produccion/list/` |
| 👥 **Clientes**   | Muestra los clientes registrados en el sistema.                                    | `/clientes/`        |
| 💼 **Vendedores** | Visualiza los vendedores activos en el sistema.                                    | `/vendedores/`      |
| 💼 **Cuentas**    | Presenta los datos de perfil del usuario con sesión activa.                        | `/cuentas/profile/` |

---

## 🧾 **Formularios**

| Formulario                    | Función                                          | Acceso                                         |
| :---------------------------- | :----------------------------------------------- | :--------------------------------------------- |
| 🔍 **Buscar Proyecto**        | Permite buscar proyectos por nombre de cliente.  | `/proyectos/`                                  |
| ➕ **Crear/Editar Proyecto**  | Form para registrar/editar un nuevo proyecto.    | Botón en `/proyectos/` o `/proyectos/crear`    |
| 🧱 **Crear Cliente**          | Alta de nuevos clientes en el sistema.           | Botón en `/clientes/` o `/clientes/crear`      |
| 🧑‍💼 **Crear Vendedor**         | Alta de nuevos vendedores en el sistema.         | Botón en `/vendedores/` o `/vendedores/crear`  |
| 🔍 **Buscar Producción**      | Permite buscar producción por número de proyecto.| `/producción/list/`                            |
| ➕ **Crear/Editar Producción**| Registrar/editar una nueva producción.           | Botón en `/produccion/list` o `/produccion/nuevo/`|
| 🧑‍💼 **Crear/Editar Usuario**   | Registrar/editar un nuevo usuario.               | Botón en `/cuentas/profile/` o `/registro`     |

---

## 🛠️ **Tecnologías Utilizadas**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-0C4B33?logo=django)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)

---

## 💡 **Próximas Mejoras**

* [ ] Mejorar el diseño visual de los templates con Bootstrap.
* [ ] Implementar validaciones avanzadas en formularios.
* [ ] Agregar reportes descargables en PDF o Excel.

---

## 📂 **Estructura del Proyecto (Vista Simplificada)**

```
FactoryProject/
│
├── Main/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── Main
│           └── index.html
│
├── cuentas/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── cuentas
│           ├── login.html
│           ├── logout.html
│           ├── registro.html
│           ├── perfil_detalle.html
│           ├── perfil_editar.html
│           ├── cambiar_contrasena.html
│           └── about_me.html
│
├── planificacion/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── planificacion
│           ├── planificacion.html
│           ├── proyectos.html
│           ├── crear_proyecto.html
│           ├── proyectos_detail.html
│           ├── proyectos_edit.html
│           ├── proyectos_confirm_delete.html
│           ├── clientes.html
│           ├── crear_clientes.html
│           ├── vendedores.html
│           └── crear_vendedores.html
│
├── produccion/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── produccion
│           ├── produccion.html
│           ├── produccion_list.html
│           ├── produccion_form.html
│           ├── produccion_detail.html
│           └── produccion_confirm_delete.html
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


