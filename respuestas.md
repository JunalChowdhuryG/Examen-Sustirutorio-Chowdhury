# **Parte Teorica Examen Sustitutorio Chowdhury Gomez Junal**

1. **Por que Git es un DAG y justifica por que no hay ciclos y como esto garantiza la terminacion de algoritmos de busqueda de rutas**

![](img/git_dag.png)
  
Por ejemplo en este grafico es parte del historial de un repositorio de git de mi [Practica Calificada 4](https://github.com/JunalChowdhuryG/Grupo-2-Practica-Calificada-4) cada commit es un nodo y las ramas son los commits que se crean a partir de un commit anterior no hay ciclos porque si no se perderia el historial de los commits ya que esto implica que un commit  puede apuntar a uno de sus ancestros y esto crearia un bucle en el grafo  esto garantiza que no haya ciclos en el grafo lo que significa que no se puede volver a un commmit anterior a menos que se cree un nuevo commit que apunte al ese commit anterior y esto ayuda en la terminacion de algoritmos de busqueda de rutas ya que se puede garantizar que no se volvera a visitar un nodo y no entraria en un bucle infinito ya que estaria visitando el mismo nodo una y otra vez

El documento generado esta en [docs/demo.pdf](docs/demo.pdf)



2. **Mediator vs Adapter**

[Medium: Backpressure Explained](https://medium.com/@jayphelps/backpressure-explained-the-flow-of-data-through-software-2350b3e77ce7)
teniendo en cuenta que back-pressure es  mecanismo que permite a un sistema manetener el control el flujo de datos entre componentes para evitar la sobrecarga y garantiza que los recursos se utilicen de manera eficiente

ya que mediator permite la comunicacion de componenetes sin que estos se conoscan directamente esto reduce el acoplamiento entre ellos y esto en un entorno de microservicion es uti l ya que los servcios se pueden desrrollar de manera independiente y al utilizar el mediator se pueede centralizar la logica de comunicacion y tambien la tranformacion de mensajes esto ayuda en la implementacion de back presure en cambio el adapter si bien es cierto facilicta la tranformacion de mensajes en diferentes fomatos este no considera el problema de acoplamiento de la mismaforma que mediatorr ya que adapter puede introducir dependencias directas entre lso componentes esto  puede dificultar la implementacion osea puede generar una difificultad al implementar la logica back pressure al crear acoplamiento osea uno depende de otro







