// estudiantes_mongo.js
// Comandos para usar en la consola de MongoDB (mongosh)
// Inserción de documentos en la colección "Estudiantes"
use laboratorio5;

db.Estudiantes.drop();

db.Estudiantes.insertMany([
  { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
  { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
  { "nombre": "Luis", "edad": 19, "ciudad": "Cali" }
]);

// Consultas básicas
// 1) Todos los documentos
db.Estudiantes.find().pretty();

// 2) Filtrar por ciudad (ej: Medellín)
db.Estudiantes.find({ ciudad: "Medellín" }).pretty();

// 3) Consultar estudiantes mayores de 20 años
db.Estudiantes.find({ edad: { $gt: 20 } }).pretty();
