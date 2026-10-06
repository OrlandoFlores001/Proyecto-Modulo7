# 💳 Alke Wallet - Proyecto Módulo 7 (Django & MySQL)

¡Bienvenido a **Alke Wallet**! Una aplicación web de gestión financiera y billetera digital desarrollada con el marco de trabajo **Django** y conectada a una base de datos **MySQL**. El proyecto cuenta con una interfaz adaptativa con estilo visual "Morado Estelar".

---

## 🚀 Características Principales

* **Autenticación y Seguridad:** Sistema de inicio de sesión (`login`/`logout`) protegido con `LoginRequiredMixin` y tokens de seguridad `CSRF` en todos los formularios.
* **Gestión CRUD Completa:**
  * **Crear:** Registro de clientes con generación automática de su número de cuenta (`AW-XXXXXX`) y saldo inicial en cero.
  * **Leer:** Tarjetas de clientes con badges dinámicos de saldo e información de contacto.
  * **Editar:** Modificación de datos del cliente con validación backend para números telefónicos (solo dígitos y máximo 9 caracteres).
  * **Eliminar:** Confirmación antes de borrar clientes de la base de datos.
* **Consultas SQL Personalizadas:** Implementación de la vista de reporte mediante `Transaccion.objects.raw()` ejecutando sentencias `JOIN` para relacionar movimientos de dinero con cuentas.
* **Modelos Relacionados:** Relaciones `OneToOneField` (`Cliente` $\leftrightarrow$ `Cuenta`), `ForeignKey` (`Cuenta` $\leftrightarrow$ `Transaccion`) y `ManyToManyField` (`Cuenta` $\leftrightarrow$ `Etiqueta`).
* **Diseño Morado Estelar:** Estilos CSS personalizados responsivos con gradientes cósmicos, efectos de cristal y microinteracciones.

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python, Django
* **Base de Datos:** MySQL
* **Frontend:** HTML, CSS, Bootstrap, FontAwesome y Bootstrap Icons

---

## ⚙️ Instrucciones de Instalación y Ejecución

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/alke_wallet.git](https://github.com/TU_USUARIO/alke_wallet.git)
cd alke_wallet