import scala.io.StdIn.readLine
object AreaTSC {
  def main(args: Array[String]) = {
    //Declaracion de Variables y Otros
      println("Ejercicio 01: Area Triangulo")
    //Datos de entrada
    println("Ingrese Base:")
    val b = readLine().toInt
    println("Ingrese Altura:")
    val h = readLine().toInt
    //Proceso
    val area=(b*h)/2
    //Datos de Salida
    println("El area del triangulo es:"+area)
  }
}