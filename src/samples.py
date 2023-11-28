sample_ac = '''
| Información | Datos |
| --- | --- |
| Nombre | lorem ipsum |
| Apellido | lorem ipsum |
| Fecha de nacimiento | lorem ipsum |
| Lugar de nacimiento | lorem ipsum |
| Nacionalidad | lorem ipsum |
| Estado civil | lorem ipsum |
| Domicilio | lorem ipsum |
| Teléfono | lorem ipsum |
| Correo electrónico | lorem ipsum |
'''.strip()

sample_bc = '''
| Información | Datos |
| --- | --- |
| Nombre | lorem ipsum |
| Apellido | lorem ipsum |
| Fecha de nacimiento | lorem ipsum |
| Lugar de nacimiento | lorem ipsum |
| Nacionalidad | lorem ipsum |
| Estado civil | lorem ipsum |
| Domicilio | lorem ipsum |
| Teléfono | lorem ipsum |
| Correo electrónico | lorem ipsum |
'''.strip()

sample_pe = '''
| Información | Datos |
| --- | --- |
| Nombre | lorem ipsum |
| Apellido | lorem ipsum |
| Fecha de nacimiento | lorem ipsum |
| Lugar de nacimiento | lorem ipsum |
| Nacionalidad | lorem ipsum |
| Estado civil | lorem ipsum |
| Domicilio | lorem ipsum |
| Teléfono | lorem ipsum |
| Correo electrónico | lorem ipsum |
'''.strip()



enterprises = '''
| Fecha      | Nombre           | Email                                   | Acta  | Balance | Poder | Revision                      |
| ---------- | ---------------- | --------------------------------------- | ----- | ------- | ----- | ----------------------------- |
| 17/11/2023 | Juan López 	    | juan.lopez@veritran.com	              |  <span>--</span>  |   <span>--</span>	|  <span>--</span>   | <a href="/review/0">Link</a>  |
| 17/11/2023 | María Rodríguez 	| maria.rodriguez@techsoluciones.net	  |  OK   |   OK    |  OK   | <a href="/review/1">Link</a>  |
| 18/11/2023 | Alejandro Pérez 	| alejandro.perez@innovatech.io 	      |  OK   |   OK    |  OK   | <a href="/review/2">Link</a>  |
| 18/11/2023 | Laura González 	| laura.gonzalez@digitalworlds.org	      |  OK   |   OK    |  OK   | <a href="/review/3">Link</a>  |
| 18/11/2023 | Carlos Martínez 	| carlos.martinez@cybersecureco.com	      |  OK   |   OK    |  OK   | <a href="/review/4">Link</a>  |
| 18/11/2023 | Ana Fernández 	| ana.fernandez@implementationmasters.com |  OK   |   OK    |  OK   | <a href="/review/5">Link</a>  |
| 18/11/2023 | Javier Ramírez 	| javier.ramirez@consultech.biz	          |  OK   |   OK    |  OK   | <a href="/review/6">Link</a>  |
| 20/11/2023 | Isabel Sánchez 	| isabel.sanchez@sysadminpros.com	      |  OK   |   OK    |  OK   | <a href="/review/7">Link</a>  |
| 20/11/2023 | Manuel Torres 	| manuel.torres@appdevsolutions.net	      |  OK   |   OK    |  OK   | <a href="/review/8">Link</a>  |
| 20/11/2023 | Patricia Díaz 	| patricia.diaz@qualitytechsolutions.org  |  OK   |   OK    |  OK   | <a href="/review/9">Link</a>  |
| 20/11/2023 | Andrés Castro 	| andres.castro@solutionsarchitects.io	  |  OK   |   OK    |  OK   | <a href="/review/10">Link</a> |
| 20/11/2023 | Gabriela Ruiz 	| gabriela.ruiz@processanalysts.net	      |  OK   |   OK    |  OK   | <a href="/review/11">Link</a> |
| 20/11/2023 | Pedro Ortega 	| pedro.ortega@supportchief.com	          |  OK   |   OK    |  OK   | <a href="/review/12">Link</a> |
| 20/11/2023 | Carolina Mendoza | carolina.mendoza@automationexperts.biz  |  OK   |   OK    |  OK   | <a href="/review/13">Link</a> |
'''.strip()

enterprises_back = '''
| Fecha      | Nombre           | Email                                   | Acta  | Balance | Poder | Revision                      |
| ---------- | ---------------- | --------------------------------------- | ----- | ------- | ----- | ----------------------------- |
| 17/11/2023 | Juan López 	    | juan.lopez@veritran.com	              |  OK   |   OK	|  OK   | <a href="/review/0">Link</a>  |
| 17/11/2023 | María Rodríguez 	| maria.rodriguez@techsoluciones.net	  |  OK   |   OK    |  OK   | <a href="/review/1">Link</a>  |
| 18/11/2023 | Alejandro Pérez 	| alejandro.perez@innovatech.io 	      |  OK   |   OK    |  OK   | <a href="/review/2">Link</a>  |
| 18/11/2023 | Laura González 	| laura.gonzalez@digitalworlds.org	      |  OK   |   OK    |  OK   | <a href="/review/3">Link</a>  |
| 18/11/2023 | Carlos Martínez 	| carlos.martinez@cybersecureco.com	      |  OK   |   OK    |  OK   | <a href="/review/4">Link</a>  |
| 18/11/2023 | Ana Fernández 	| ana.fernandez@implementationmasters.com |  OK   |   OK    |  OK   | <a href="/review/5">Link</a>  |
| 18/11/2023 | Javier Ramírez 	| javier.ramirez@consultech.biz	          |  OK   |   OK    |  OK   | <a href="/review/6">Link</a>  |
| 20/11/2023 | Isabel Sánchez 	| isabel.sanchez@sysadminpros.com	      |  OK   |   OK    |  OK   | <a href="/review/7">Link</a>  |
| 20/11/2023 | Manuel Torres 	| manuel.torres@appdevsolutions.net	      |  OK   |   OK    |  OK   | <a href="/review/8">Link</a>  |
| 20/11/2023 | Patricia Díaz 	| patricia.diaz@qualitytechsolutions.org  |  OK   |   OK    |  OK   | <a href="/review/9">Link</a>  |
| 20/11/2023 | Andrés Castro 	| andres.castro@solutionsarchitects.io	  |  OK   |   OK    |  OK   | <a href="/review/10">Link</a> |
| 20/11/2023 | Gabriela Ruiz 	| gabriela.ruiz@processanalysts.net	      |  OK   |   OK    |  OK   | <a href="/review/11">Link</a> |
| 20/11/2023 | Pedro Ortega 	| pedro.ortega@supportchief.com	          |  OK   |   OK    |  OK   | <a href="/review/12">Link</a> |
| 20/11/2023 | Carolina Mendoza | carolina.mendoza@automationexperts.biz  |  OK   |   OK    |  OK   | <a href="/review/13">Link</a> |
'''.strip()

tb_review = '''
| Documento | Analizar | Aceptar | Rechazar |
| --------- | -------- | ------- | -------- |
| Acta Constitutiva | <button class="btn-system analizar acta">Analizar</button> | <button class="btn-system aceptar acta">Aceptar</button> | <button class="btn-system rechazar acta">Rechazar</button> |
| Poder Especial | <button class="btn-system analizar poder">Analizar</button> | <button class="btn-system aceptar poder">Aceptar</button> | <button class="btn-system rechazar poder">Rechazar</button> |
'''.strip()

# | Balance Contable | <button class="btn-system analizar balance">Analizar</button> | <button class="btn-system aceptar balance">Aceptar</button> | <button class="btn-system rechazar balance">Rechazar</button> |


tb_result_ac = '''
<table><tbody><tr><th>Información</th><th>Datos</th></tr><tr><td>Número de Instrumento</td><td>8,721</td></tr><tr><td>Fecha de emisión</td><td>19 de Diciembre del 2005</td></tr><tr><td>Número de Notaria</td><td>110</td></tr><tr><td>Plaza del Notario</td><td>Monterrey, N. L.</td></tr><tr><td>Escribano interviniente</td><td>Licenciado JESUS HECTOR VILLARREAL ELIZONDO</td></tr><tr><td>Datos de Inscripción</td><td>FOLIO MERCANTIL ELECTRONICO No. 96853</td></tr><tr><td>Denominación social</td><td>BASE INTERNACIONAL CASA DE BOLSA, SOCIEDAD ANÓNIMA DE CAPITAL VARIABLE</td></tr><tr><td>Tipo de Sociedad Mercantil</td><td>Sociedad Anónima de Capital Variable</td></tr><tr><td>Acto</td><td>Constitución de sociedad</td></tr><tr><td>Limitaciones o Prohibiciones</td><td>No especificado</td></tr><tr><td>¿Tiene La Sociedad Facultades para Contratar Créditos?</td><td>Sí</td></tr><tr><td>¿Tiene La Sociedad Facultades para Otorgar Garantías Propias?</td><td>Sí</td></tr><tr><td>¿Tiene La Sociedad Facultades para Otorgar Garantías A Terceros?</td><td>No especificado</td></tr><tr><td>¿Tiene La Sociedad Facultades para Ser Obligado Solidario?</td><td>No especificado</td></tr><tr><td>Fecha Folio ID o Fecha constitución de sociedad</td><td>14-02-2006</td></tr><tr><td><strong>Accionistas</strong></td><td></td></tr><tr><td>Nombre</td><td>C.P. LORENZO BARRERA SEGOVIA</td></tr><tr><td>Persona Física o Jurídica</td><td>Física</td></tr><tr><td>Nacionalidad</td><td>Mexicana</td></tr><tr><td>Fecha de Nacimiento</td><td>No especificado</td></tr><tr><td>Registro Federal de Contribuyentes (RFC)</td><td>BASL-581226-KQA</td></tr><tr><td>Valor Capital Mínimo Fijo (pesos)</td><td>$29,643,640.00</td></tr><tr><td>Número de Acciones Capital Fijo</td><td>No especificado</td></tr><tr><td>Valor Capital Variable (pesos)</td><td>No especificado</td></tr><tr><td>Número de Acciones Capital Variable</td><td>No especificado</td></tr><tr><td>Valor Capital Total Fijo + Variable</td><td>$57,007,000.00</td></tr><tr><td>Número de Acciones Total Fijo + Variable</td><td>No especificado</td></tr><tr><td>Participación Accionaria</td><td>52%</td></tr><tr><td>Nombre</td><td>DR. ALFONSO BARRERA ZERTUCHE</td></tr><tr><td>Persona Física o Jurídica</td><td>Física</td></tr><tr><td>Nacionalidad</td><td>Mexicana</td></tr><tr><td>Fecha de Nacimiento</td><td>No especificado</td></tr><tr><td>Registro Federal de Contribuyentes (RFC)</td><td>BAZA-260303</td></tr><tr><td>Valor Capital Mínimo Fijo (pesos)</td><td>$570,070.00</td></tr><tr><td>Número de Acciones Capital Fijo</td><td>No especificado</td></tr><tr><td>Valor Capital Variable (pesos)</td><td>No especificado</td></tr><tr><td>Número de Acciones Capital Variable</td><td>No especificado</td></tr><tr><td>Valor Capital Total Fijo + Variable</td><td>$57,007,000.00</td></tr><tr><td>Número de Acciones Total Fijo + Variable</td><td>No especificado</td></tr><tr><td>Participación Accionaria</td><td>1%</td></tr><tr><td>Nombre</td><td>ING. ALVARO BARRERA SEGOVIA</td></tr><tr><td>Persona Física o Jurídica</td><td>Física</td></tr><tr><td>Nacionalidad</td><td>Mexicana</td></tr><tr><td>Fecha de Nacimiento</td><td>No especificado</td></tr><tr><td>Registro Federal de Contribuyentes (RFC)</td><td>BASA-611030-PX1</td></tr><tr><td>Valor Capital Mínimo Fijo (pesos)</td><td>$14,251,750.00</td></tr><tr><td>Número de Acciones Capital Fijo</td><td>No especificado</td></tr><tr><td>Valor Capital Variable (pesos)</td><td>No especificado</td></tr><tr><td>Número de Acciones Capital Variable</td><td>No especificado</td></tr><tr><td>Valor Capital Total Fijo + Variable</td><td>$57,007,000.00</td></tr><tr><td>Número de Acciones Total Fijo + Variable</td><td>No especificado</td></tr><tr><td>Participación Accionaria</td><td>25%</td></tr><tr><td>Nombre</td><td>LIC. GABRIELA JOSEFINA JAIME DÍAZ</td></tr><tr><td>Persona Física o Jurídica</td><td>Física</td></tr><tr><td>Nacionalidad</td><td>Mexicana</td></tr><tr><td>Fecha de Nacimiento</td><td>No especificado</td></tr><tr><td>Registro Federal de Contribuyentes (RFC)</td><td>JADG-610625-RR8</td></tr><tr><td>Valor Capital Mínimo Fijo (pesos)</td><td>$11,401,400.00</td></tr><tr><td>Número de Acciones Capital Fijo</td><td>No especificado</td></tr><tr><td>Valor Capital Variable (pesos)</td><td>No especificado</td></tr><tr><td>Número de Acciones Capital Variable</td><td>No especificado</td></tr><tr><td>Valor Capital Total Fijo + Variable</td><td>$57,007,000.00</td></tr><tr><td>Número de Acciones Total Fijo + Variable</td><td>No especificado</td></tr><tr><td>Participación Accionaria</td><td>20%</td></tr><tr><td>Nombre</td><td>SR. ROGELIO JAIME TREVIÑO</td></tr><tr><td>Persona Física o Jurídica</td><td>Física</td></tr><tr><td>Nacionalidad</td><td>Mexicana</td></tr><tr><td>Fecha de Nacimiento</td><td>No especificado</td></tr><tr><td>Registro Federal de Contribuyentes (RFC)</td><td>JATR-370727</td></tr><tr><td>Valor Capital Mínimo Fijo (pesos)</td><td>$570,070.00</td></tr><tr><td>Número de Acciones Capital Fijo</td><td>No especificado</td></tr><tr><td>Valor Capital Variable (pesos)</td><td>No especificado</td></tr><tr><td>Número de Acciones Capital Variable</td><td>No especificado</td></tr><tr><td>Valor Capital Total Fijo + Variable</td><td>$57,007,000.00</td></tr><tr><td>Número de Acciones Total Fijo + Variable</td><td>No especificado</td></tr><tr><td>Participación Accionaria</td><td>1%</td></tr><tr><td>Nombre</td><td>SR. FRANCISCO JAVIER VALDÉS FARIAS</td></tr><tr><td>Persona Física o Jurídica</td><td>Física</td></tr><tr><td>Nacionalidad</td><td>Mexicana</td></tr><tr><td>Fecha de Nacimiento</td><td>No especificado</td></tr><tr><td>Registro Federal de Contribuyentes (RFC)</td><td>VAFF-410108-B96</td></tr><tr><td>Valor Capital Mínimo Fijo (pesos)</td><td>$570,070.00</td></tr><tr><td>Número de Acciones Capital Fijo</td><td>No especificado</td></tr><tr><td>Valor Capital Variable (pesos)</td><td>No especificado</td></tr><tr><td>Número de Acciones Capital Variable</td><td>No especificado</td></tr><tr><td>Valor Capital Total Fijo + Variable</td><td>$57,007,000.00</td></tr><tr><td>Número de Acciones Total Fijo + Variable</td><td>No especificado</td></tr><tr><td>Participación Accionaria</td><td>1%</td></tr><tr><td><strong>Comisario(s)</strong></td><td></td></tr><tr><td>Nombre</td><td>JOSÉ AQUILES ELIZONDO GARZA</td></tr><tr><td><strong>Consejo</strong></td><td></td></tr><tr><td>Nombre</td><td>C.P. LORENZO BARRERA SEGOVIA</td></tr><tr><td>Cargo</td><td>Presidente</td></tr><tr><td>Nombre</td><td>Ing. Álvaro Barrera Segovia</td></tr><tr><td>Cargo</td><td>Secretario</td></tr><tr><td>Nombre</td><td>Lic. Rene Javier Hinojosa Garcia</td></tr><tr><td>Cargo</td><td>Consejero Independiente</td></tr><tr><td>Nombre</td><td>Lic. Horacio Mauricio Marchand Flores</td></tr><tr><td>Cargo</td><td>Consejero Independiente</td></tr><tr><td><strong>Apoderados</strong></td><td></td></tr><tr><td>Nombre</td><td>LORENZO BARRERA SEGOVIA</td></tr><tr><td>Ejercicio</td><td>General para Pleitos y Cobranzas y Actos de Administración y Administración Laboral</td></tr><tr><td>¿Poder Para Actos de Administración?</td><td>Sí</td></tr><tr><td>¿Poder Para Actos de Dominio?</td><td>Sí</td></tr><tr><td>¿Poder Especial Para Cuentas Bancarias?</td><td>Sí</td></tr><tr><td>¿Poder Para Títulos Y Operaciones de Crédito?</td><td>Sí</td></tr><tr><td>¿Poder Para Delegar?</td><td>Sí</td></tr><tr><td>Limitante</td><td>No especificado</td></tr><tr><td>Nombre</td><td>MIGUEL FERNANDO MARTINEZ GONZALEZ</td></tr><tr><td>Ejercicio</td><td>Especial</td></tr><tr><td>¿Poder Para Actos de Administración?</td><td>Sí</td></tr><tr><td>¿Poder Para Actos de Dominio?</td><td>No especificado</td></tr><tr><td>¿Poder Especial Para Cuentas Bancarias?</td><td>No especificado</td></tr><tr><td>¿Poder Para Títulos Y Operaciones de Crédito?</td><td>No especificado</td></tr><tr><td>¿Poder Para Delegar?</td><td>No especificado</td></tr><tr><td>Limitante</td><td>No especificado</td></tr><tr><td>Nombre</td><td>WILMER ANGELES CASTILLO</td></tr><tr><td>Ejercicio</td><td>Especial</td></tr><tr><td>¿Poder Para Actos de Administración?</td><td>Sí</td></tr><tr><td>¿Poder Para Actos de Dominio?</td><td>No especificado</td></tr><tr><td>¿Poder Especial Para Cuentas Bancarias?</td><td>No especificado</td></tr><tr><td>¿Poder Para Títulos Y Operaciones de Crédito?</td><td>No especificado</td></tr><tr><td>¿Poder Para Delegar?</td><td>No especificado</td></tr><tr><td>Limitante</td><td>No especificado</td></tr></tbody></table>
'''.strip()

tb_result_poder = '''
<table>
<thead>
<tr>
<th>Información</th>
<th>Datos</th>
</tr>
</thead>
<tbody>
<tr>
<td>Denominación social de la sociedad que otorga el poder</td>
<td>ON TIME MOBILE TECHNOLOGIES, SOCIEDAD ANÓNIMA DE CAPITAL VARIABLE</td>
</tr>
<tr>
<td>Representante de la sociedad</td>
<td>Marcelo Clemente González</td>
</tr>
<tr>
<td>número o constancia de inscripción del poder en un Registro Oficial</td>
<td></td>
</tr>
<tr>
<td>Número de Instrumento</td>
<td>67,089</td>
</tr>
<tr>
<td>Fecha de emisión del instrumento</td>
<td>26 de junio de 2019</td>
</tr>
<tr>
<td>Escribano interviniente</td>
<td>Uriel Oliva Sanchez</td>
</tr>
<tr>
<td>Nombre y Número de Notaria</td>
<td>Notaría número 215 de la Ciudad de México</td>
</tr>
<tr>
<td>Nombre y Apellido del firmante</td>
<td>Marcelo Clemente González</td>
</tr>
<tr>
<td>Carácter o rol del firmante</td>
<td>Representante de la sociedad</td>
</tr>
<tr>
<td>Artículo o cláusula de otorgamiento</td>
<td>Artículo 2,554 del Código Civil para la Ciudad de México</td>
</tr>
<tr>
<td>Nombre del Apoderado 1</td>
<td>Fabián Andrés Berdiales</td>
</tr>
<tr>
<td>Resumen de facultad A)</td>
<td>Poder general para pleitos y cobranzas</td>
</tr>
<tr>
<td>Resumen de facultad B)</td>
<td>Poder general para actos de administración</td>
</tr>
<tr>
<td>Resumen de facultad C)</td>
<td>Poder general para emitir, girar, endosar, aceptar, avalar, descontar y suscribir toda clase de títulos de crédito</td>
</tr>
<tr>
<td>Resumen de facultad D)</td>
<td>Poder para abrir y cerrar cuentas bancarias en nombre y por cuenta de la sociedad</td>
</tr>
<tr>
<td>Resumen de facultad E)</td>
<td>Poder para actos de administración en materia laboral</td>
</tr>
<tr>
<td>Resumen de facultad F)</td>
<td>Facultad para designar al Director General, a los Gerentes, Sub-Gerentes y demás factores o empleados de la sociedad</td>
</tr>
<tr>
<td>Persona Física o Jurídica</td>
<td>Persona Física</td>
</tr>
<tr>
<td>Número de Inscripción del RFC del Apoderado</td>
<td></td>
</tr>
<tr>
<td>Nacionalidad</td>
<td>Argentino</td>
</tr>
<tr>
<td>Rol del Apoderado</td>
<td>Apoderado</td>
</tr>
<tr>
<td>¿Tiene Poderes para Actos de Administración?</td>
<td>Sí</td>
</tr>
<tr>
<td>¿Tiene Poder para Actos de Dominio?</td>
<td>No</td>
</tr>
<tr>
<td>¿Tiene Poder para Títulos y Operaciones de Crédito?</td>
<td>Sí</td>
</tr>
<tr>
<td>¿Tiene Poder para delegar?</td>
<td></td>
</tr>
<tr>
<td>¿Tiene Poder especial para Cuentas Bancarias?</td>
<td>Sí</td>
</tr>
<tr>
<td>Fecha de Vigencia del Poder</td>
<td></td>
</tr>
<tr>
<td>Nombre del Apoderado 2</td>
<td>Nabil Attar</td>
</tr>
<tr>
<td>Resumen de facultad A)</td>
<td>Poder general para pleitos y cobranzas</td>
</tr>
<tr>
<td>Resumen de facultad B)</td>
<td>Poder general para actos de administración</td>
</tr>
<tr>
<td>Resumen de facultad C)</td>
<td>Poder general para actos de dominio</td>
</tr>
<tr>
<td>Resumen de facultad D)</td>
<td>Poder general para emitir, girar, endosar, aceptar, avalar, descontar y suscribir toda clase de títulos de crédito</td>
</tr>
<tr>
<td>Resumen de facultad E)</td>
<td>Poder para abrir y cerrar cuentas bancarias en nombre y por cuenta de la sociedad</td>
</tr>
<tr>
<td>Resumen de facultad F)</td>
<td>Poder para actos de administración en materia laboral</td>
</tr>
<tr>
<td>Persona Física o Jurídica</td>
<td></td>
</tr>
<tr>
<td>Número de Inscripción del RFC del Apoderado</td>
<td></td>
</tr>
<tr>
<td>Nacionalidad</td>
<td></td>
</tr>
<tr>
<td>Rol del Apoderado</td>
<td>Apoderado</td>
</tr>
<tr>
<td>¿Tiene Poderes para Actos de Administración?</td>
<td>Sí</td>
</tr>
<tr>
<td>¿Tiene Poder para Actos de Dominio?</td>
<td>Sí</td>
</tr>
<tr>
<td>¿Tiene Poder para Títulos y Operaciones de Crédito?</td>
<td>Sí</td>
</tr>
<tr>
<td>¿Tiene Poder para delegar?</td>
<td></td>
</tr>
<tr>
<td>¿Tiene Poder especial para Cuentas Bancarias?</td>
<td>Sí</td>
</tr>
<tr>
<td>Fecha de Vigencia del Poder</td>
<td></td>
</tr>
<tr>
<td>Nombre del Apoderado 3</td>
<td></td>
</tr>
<tr>
<td>Resumen de facultad A)</td>
<td></td>
</tr>
<tr>
<td>Resumen de facultad B)</td>
<td></td>
</tr>
<tr>
<td>Resumen de facultad C)</td>
<td></td>
</tr>
<tr>
<td>Resumen de facultad D)</td>
<td></td>
</tr>
<tr>
<td>Resumen de facultad E)</td>
<td></td>
</tr>
<tr>
<td>Resumen de facultad F)</td>
<td></td>
</tr>
<tr>
<td>Persona Física o Jurídica</td>
<td></td>
</tr>
<tr>
<td>Número de Inscripción del RFC del Apoderado</td>
<td></td>
</tr>
<tr>
<td>Nacionalidad</td>
<td></td>
</tr>
<tr>
<td>Rol del Apoderado</td>
<td></td>
</tr>
<tr>
<td>¿Tiene Poderes para Actos de Administración?</td>
<td></td>
</tr>
<tr>
<td>¿Tiene Poder para Actos de Dominio?</td>
<td></td>
</tr>
<tr>
<td>¿Tiene Poder para Títulos y Operaciones de Crédito?</td>
<td></td>
</tr>
<tr>
<td>¿Tiene Poder para delegar?</td>
<td></td>
</tr>
<tr>
<td>¿Tiene Poder especial para Cuentas Bancarias?</td>
<td></td>
</tr>
<tr>
<td>Fecha de Vigencia del Poder</td>
<td></td>
</tr>
<tr>
<td>¿Dónde podrán ejercitarse las facultades?</td>
<td>En el sector público (dependencias de gobierno) así como privado, incluyendose entre estos, la Secretaría de Hacienda y Crédito Público y su Servicio de Administración Tributaria, el Instituto Mexicano del Seguro Social y cualquier dependencia que pertenezca a éste y el Instituto Nacional de Migración</td>
</tr>
<tr>
<td>¿De qué manera actúan los apoderados? (Individual, conjunta, indistinta)</td>
<td>Conjunta o separadamente</td>
</tr>
</tbody>
</table>
'''
