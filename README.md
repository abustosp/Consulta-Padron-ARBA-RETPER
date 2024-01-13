# Cruce de Base de CUITs con Padrón de ARBA

Script para realizar masivamente los cruces de los CUITs de los contribuyentes con el padrón de ARBA.

---

El licenciamiento es bajo PL (es decir que no se puede distribuir comercialmente, solamente GRATIS). y si se utiliza este el código, su derivado también debe ser distribuido abierta y gratuitamente. 

---


## Ejecución del Programa

1. Instalar el ejecutable (el .exe)

    1. Completar la columna con el CUIT que se desea buscar en el Padrón de ARBA en el Excel `Base-Clientes.xlsx` (en la columna `CUIT`)

    2. Ejectuar el programa

    3. Seleccionar el TXT con el Padrón de ARBA a Consultar

    4. Abrir el archivo procesado `Clientes_Procesado.xlsx`

---

### Opción 2: Ejecutar el Script

Los pasos para ejecutar el Script suele ser el siguiente:

1. Descargarse Python (https://www.python.org/downloads/)

2. Instalar Python (https://www.python.org/downloads/)

3. Descargar/Clonar el Script:
    - Descargar el ZIP o
    - Clonar el repositorio con el comando en la consola/terminal:

    ```
    git clone https://github.com/abustosp/Consulta-Padron-ARBA-RETPER.git
    ```

4. Crearse un entorno virtual. Generalmente se hace con el comando:

    Python en windows:
    ```Python en Windows
    python -m venv NombreDelEntornoVirtualaCrear
    ```
    Python en Linux/Mac:	
    ```Python en Linux
    python3 -m venv NombreDelEntornoVirtualaCrear
    ```

5.  Activar el entorno virtual (depdende del sistema operativo):

    - Windows: 
    ```
    EntornoVirtual\Scripts\activate
    ```

    - Linux: 
    ```
    source EntornoVirtual/bin/activate 
    ```

6. Instalar las dependencias/Librerías del proyecto (generalmente se hace con el comando):

    ```Python	
    pip install -r requirements.txt
    ```

    - Si no se tiene el requirements.txt, se puede instalar cada librería con el comando:

    ```Python
    pip install NombreDeLaLibreria1 NombreDeLaLibreria2==version NombreDeLaLibreria3>=version NombreDeLaLibreriaN<=version
    ```

<br>

(generalmente suelo utilizar las siguientes librerias: pandas, numpy, lxml, customtkinter, matplotlib, seaborn , openpyxl, openai , PIL o pillow) <br><br>

7. Ejecutar el Script (generalmente se hace con el comando):

    ```Python
    python NombreDelScript.py
    ```
    o
    ```Python
    python3 NombreDelScript.py
    ```

---
## Aclaraciones

El uso del Programa/Script se ejecuta bajo la responsabilidad de quien lo utiliza. No me hago responsable de los daños que pueda ocasionar el uso indevido del mismo.

Si lo compartís debes hacelo gratis bajo los lineamientos de PL, adicionalmente podés mencioname también para que mas personas conozcan en el mundo de la programacion/automatización con Python/RPA y/o mostrale mis videos para que vean que cosas pueden hacer.

---

### Links de Interés:

- Link de invitación al grupo de RPA en Discord: https://discord.gg/KVYyryvAcD

- Link de invitación al grupo de RPA en WhatsApp: https://chat.whatsapp.com/IekktfvfTNLCkdIagO6xz3

- Tutorial de Descarga de Bots desde Uipath: https://youtu.be/hD5BH7YzABw

- Tutorial de Instalación y descarga de Repositorios con Git: https://youtu.be/ujk27tRdA80

---

Cualquier cosa pueden contactarme en:

    https://www.linkedin.com/in/agust%C3%ADn-bustos-piasentini-468446122/

    https://www.youtube.com/user/agustinbustosp

    whatsapp al https://wa.me/+5493764224695

---


## 💰 Acepto donaciones para mantener el proyecto libre y gratuito

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/agustinbustosp)

[![Invitame un café en cafecito.app](https://cdn.cafecito.app/imgs/buttons/button_5.svg)](https://cafecito.app/abustos)

 
## 💰 Y También en Pesos Argentinos


[![Mercado Pago](https://img.shields.io/badge/Mercado%20Pago%20100-009ee3?style=for-the-badge&logo=mercadopago&logoColor=white)](https://mpago.la/2JBdGez)

[![Mercado Pago](https://img.shields.io/badge/Mercado%20Pago%20500-009ee3?style=for-the-badge&logo=mercadopago&logoColor=white)](https://mpago.la/2CwfjKE)

[![Mercado Pago](https://img.shields.io/badge/Mercado%20Pago%201.000-009ee3?style=for-the-badge&logo=mercadopago&logoColor=white)](https://mpago.la/21Xvpig)

[![Mercado Pago](https://img.shields.io/badge/Mercado%20Pago%205.000-009ee3?style=for-the-badge&logo=mercadopago&logoColor=white)](https://mpago.la/1s4D4mM)

[![Mercado Pago](https://img.shields.io/badge/Mercado%20Pago%2010.000-009ee3?style=for-the-badge&logo=mercadopago&logoColor=white)](https://mpago.la/1n9cimr)
