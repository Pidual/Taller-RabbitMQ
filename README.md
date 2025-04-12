# Taller-RabitMQ
(Documento de las preguntas en https://github.com/Pidual/Taller-RabbitMQ/blob/main/Documentacion%20RabbitMQ.pdf)
--David Santiago Cubillos Méndez <br>
--Carlos Hernando Lozano Perez<br>
Diagrama de arquitectura
(haz click para ver en HD en una nueva pestaña)
![SADSADASDSA (1)](https://github.com/user-attachments/assets/145c6bb3-3ccd-4aef-a178-4c7c54127f38)



Para correlo ejecutamos el comando en la ruta que aparece en la iamgen 
docker-compose up --build -d   
![image](https://github.com/user-attachments/assets/d1e56e0a-b015-49c9-b72f-be3e46d5a193)

despues vamos a ver si estan corriendo nuestros contenedores con el comando 
docker-compose ps

![image](https://github.com/user-attachments/assets/6138db2a-02d5-446e-b981-5a6881dfec2a)

en en la ruta 
http://localhost:8080/dashboard/#/

verems que estan corriendo 

![image](https://github.com/user-attachments/assets/d49082ae-2630-4383-b2d0-069abf9e2a22)

![image](https://github.com/user-attachments/assets/01e80205-9b3e-4650-a6c8-bfa5961a1496)

ahora ingresamos en otra ruta a nuestro rabbit 

http://localhost:15672/#/

el usuario es admin y la clave admin

![image](https://github.com/user-attachments/assets/4cc0d5f9-15eb-4664-ab1a-abfe5177f899)

podemos entrar a cualquiera de nuestros clientes 
 http://localhost/cliente/uno   o  http://localhost/cliente/dos  

 Cada vez que se refresque la pagina es una peticcion 
 para saber si esta pues en el terminal ponemos el siguiente comando 

 docker logs tallerrabbitmq-analytics-app-1 -f

como vemos cada vez que se refresque a la izquierda va recibir la petición 

![image](https://github.com/user-attachments/assets/2b1651d1-3f14-4979-a7c3-88716f09604d)


y tambien en la pagina de Rabbit veremos  la grafica del mensaje 

![image](https://github.com/user-attachments/assets/1b3e7c2b-75b2-455c-920a-1dddd45cd6b7)

y adicionalmente en el monitor de ruta 

http://localhost/monitor

veremos la peticiones 

![image](https://github.com/user-attachments/assets/8de6d64d-295c-4c2b-9242-87c52d8eb92e)



 
