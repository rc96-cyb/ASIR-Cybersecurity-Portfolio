# **Generador de usuarios en CSV**

Script en Python que lee una lista de empleados nuevos desde un archivo JSON y genera un CSV con el nombre de usuario, una contraseña inicial aleatoria y el correo corporativo de cada uno.

Estado: Terminado.

## **Requisitos**:
- Python 3.13
- Librería unidecode, que se usa para quitar caracteres especiales de los nombres de usuario:

***`pip install unidecode`***

## **Archivo de entrada**

El repositorio incluye `employees_list.json`, un ejemplo con empleados inventados que se puede usar directamente. Para usar otra lista, mantén este formato (nombre y apellidos en campos separados):

```json
[
  {"nombre": "María José", "apellidos": "García López"},
  {"nombre": "Carlos", "apellidos": "de la Cruz Sánchez"},
  {"nombre": "Irene", "apellidos": "Navarro"}
]
```
## **Ejecución**

Para ejecutarlo en la terminal de Linux o en Windows, simplemente hay que añadir el nombre del archivo json y el nombre del archivo csv que se quiere crear. Importante recordar que el archivo json debe existir en la carpeta antes de ejecutar el script, de lo contrario lanzará un error. 

**Comando en Linux**: ***`./csv_users_generator.py employees_list.json users.csv`***
**Comando en Windows**: ***`python3 csv_users_generator.py employees_list.json users.csv`***

## **Resultado**

Se crea CSV_Files/users.csv. 

Ejemplo del archivo creado users.csv:

```Name,Surname,sAMAccountName,Password,Email```
```laura,martínez ruiz,l.martinezruiz,BbdVXHmJsPt2G7vr,l.martinezruiz@empresa.com```


## **Cómo funciona y decisiones tomadas**

- **Nombre de usuario**: inicial del nombre + . + apellidos, en minúsculas, sin espacios, sin apóstrofos y sin tildes ni ñ. Los guiones se conservan.
- **Duplicados**: si dos personas generan el mismo usuario, a la segunda se le añade un número (p.sanzdiaz, p.sanzdiaz1).
- **Contraseñas**: 16 caracteres (letras y dígitos) generados con el módulo secrets, pensado para uso criptográfico. No se usa random porque sus valores son predecibles.
- **Correo**: usuario + @empresa.com. El dominio se cambia en la variable email_ext del script.
- **Columna sAMAccountName**: sigue el nombre del atributo de Active Directory, para poder usar el CSV como base al crear usuarios en un dominio.


## **Limitaciones**

- No se comprueba el límite de 20 caracteres de sAMAccountName en Active Directory.
- Si el archivo json no está bien estructurado o falta algún dato, lanzará un error.

## **Seguridad**

- Las contraseñas iniciales se guardan en texto plano en el CSV.
*Mitigaciones*: obligar a cambiarla en el primer inicio de sesión y borrar el archivo después de usarlo.