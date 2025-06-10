# Practicas_ROS2
Compendio de practicas de la documentacion de ROS2 Humble
Comandos para ROS2 Humble

el directorio que contiene el paquete debe tener el sufijo _ws para reconocerse con WorkSpace

en ese ws debe tener un directorio src que tenga todo lo que tendra el paquete
una vez se tiene lo que contendra el paquete se ejecuta el comando:

colcon build

dentro de un espacio de trabajo se pueden tener multiples paquetes en el directorio src

comando para crar un paquete
ros2 pkg create 
--build-type < este argumento tiene unicamente dos opciones ament_cmake y ament_python >
--description < Esta parte unicamente crea la descripcion del paquete que se creara > 
--maintainer-name < Nombre de quien mantiene el nodo > 
--maintainer-email < correo de quien mantiene > 
--license < licencia bajo la que se maneja el paquete > 
--node-name < nombre que tendra el nodo > 
armAX_pkg < nombre del paquete >


en la raiz del ws se tiene que correr el comando 
colcon build para construir el paquete


